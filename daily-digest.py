#!/usr/bin/env python3
"""Daily AI-Testing Digest — RSS fetch + keyword scoring + Groq summary."""

import argparse
import json
import os
import re
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import date, datetime
from pathlib import Path
from typing import Any

import xml.etree.ElementTree as ET

import httpx
import feedparser

SCRIPT_DIR = Path(__file__).parent
CONFIG_PATH = SCRIPT_DIR / "digest-config.json"
DIGESTS_DIR = SCRIPT_DIR / "digests"
GOLDEN_PATH = SCRIPT_DIR / "golden-dataset.json"
# used for cron log path
ROOT_DIR = SCRIPT_DIR.parent

# ── Config ──────────────────────────────────────────────────────────────────

def load_config() -> dict:
    with open(CONFIG_PATH) as f:
        return json.load(f)


def groq_api_key() -> str | None:
    key = os.environ.get("GROQ_API_KEY")
    if key:
        return key
    for name in ("1.groq_ke", "1.groq_key"):
        key_file = Path.home() / name
        if key_file.exists():
            return key_file.read_text().strip()
    return None


# ── RSS fetch ───────────────────────────────────────────────────────────────

def _parse_pubdate(published_parsed) -> str | None:
    """Convert feedparser time tuple to ISO datetime string."""
    try:
        return datetime(*published_parsed[:6]).isoformat()
    except Exception:
        return None


def _is_recent(published_str: str, max_days: int) -> bool:
    """Check if a date string is within max_days."""
    for fmt in ("%Y-%m-%dT%H:%M:%S", "%a, %d %b %Y %H:%M:%S %z",
                "%a, %d %b %Y %H:%M:%S %Z", "%Y-%m-%d"):
        try:
            from datetime import timezone
            dt = datetime.strptime(published_str.strip(), fmt)
            if dt.tzinfo is None:
                dt = dt.replace(tzinfo=timezone.utc)
            delta = datetime.now(timezone.utc) - dt
            return delta.days <= max_days
        except ValueError:
            continue
    return True  # if can't parse, keep it


def _parse_rss_xml(xml_text: str) -> list[dict]:
    """Fallback: parse RSS XML with ElementTree when feedparser fails."""
    items: list[dict] = []
    try:
        root = ET.fromstring(xml_text)
        for item_elem in root.iter("item"):
            def _tag(tag):
                el = item_elem.find(tag)
                return el.text if el is not None else ""
            items.append({
                "title": _tag("title"),
                "link": _tag("link"),
                "published": _tag("pubDate"),
                "summary": _clean_html(_tag("description")),
            })
    except Exception:
        pass
    return items


def fetch_feed(source: dict) -> list[dict]:
    """Fetch and parse a single RSS feed. Returns list of items."""
    items: list[dict] = []
    max_age = source.get("max_age_days", 7)
    try:
        resp = httpx.get(source["url"], timeout=source.get("timeout", 15),
                         follow_redirects=True, headers={"User-Agent": "daily-digest/1.0"})
        resp.raise_for_status()
        feed = feedparser.parse(resp.text)
        raw_entries = feed.entries

        # Fallback: if feedparser returned 0 items, try XML parser
        if not raw_entries:
            raw_entries = _parse_rss_xml(resp.text)

        for entry in raw_entries:
            if isinstance(entry, dict):
                # XML fallback items are dicts
                title = entry.get("title", "") or ""
                link = entry.get("link", "") or ""
                published = entry.get("published", "") or ""
                summary = _clean_html(entry.get("summary", "") or entry.get("description", "") or "")
            else:
                # feedparser entries have attributes
                title = entry.get("title", "") or ""
                link = entry.get("link", "") or ""
                published = entry.get("published", "") or ""
                summary = _clean_html(entry.get("summary", "") or entry.get("description", "") or "")
                if hasattr(entry, "published_parsed") and entry.published_parsed:
                    iso = _parse_pubdate(entry.published_parsed)
                    if iso:
                        published = iso

            if max_age > 0 and published:
                if not _is_recent(published, max_age):
                    continue

            items.append({
                "title": title,
                "link": link,
                "published": published,
                "summary": summary,
                "source": source["id"],
                "source_name": source["name"],
            })
    except Exception as e:
        print(f"  [WARN] {source['id']}: {e}", file=sys.stderr)
    return items


def _clean_html(text: str) -> str:
    """Remove HTML tags from text."""
    text = re.sub(r"<[^>]+>", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text[:500]  # keep first 500 chars


def fetch_all(config: dict) -> list[dict]:
    """Fetch all RSS feeds concurrently."""
    all_items: list[dict] = []
    sources = config["sources"]
    timeout = config.get("rss_timeout", 15)

    rss_sources = [s for s in sources if s.get("type") != "manual"]
    manual_sources = [s for s in sources if s.get("type") == "manual"]

    print(f"  Fetching {len(rss_sources)} sources...", file=sys.stderr)

    for ms in manual_sources:
        print(f"    [MANUAL] {ms['id']}: check {ms['url']} manually", file=sys.stderr)

    max_age = config.get("max_age_days", 7)
    with ThreadPoolExecutor(max_workers=max(1, len(rss_sources))) as pool:
        futures = {pool.submit(fetch_feed, {**s, "timeout": timeout, "max_age_days": max_age}): s["id"] for s in rss_sources}
        for future in as_completed(futures):
            sid = futures[future]
            try:
                items = future.result()
                all_items.extend(items)
                print(f"    {sid}: {len(items)} items", file=sys.stderr)
            except Exception as e:
                print(f"    {sid}: ERROR {e}", file=sys.stderr)

    print(f"  Total: {len(all_items)} items from {len(rss_sources)} sources", file=sys.stderr)
    return all_items


# ── Scoring ─────────────────────────────────────────────────────────────────

def score_item(item: dict, config: dict) -> float:
    """Compute relevance score for an item."""
    text = (item.get("title", "") + " " + item.get("summary", "") + " " + item.get("source_name", "")).lower()
    kw = config["keywords"]
    w = config["weights"]

    score = 0.0

    # core keywords × 3.0 (count once, first match)
    for k in kw["core"]:
        if k.lower() in text:
            score += w["core_keyword"]
            break

    # adjacent keywords × 1.0 (accumulate all matches)
    for k in kw["adjacent"]:
        if k.lower() in text:
            score += w["adjacent_keyword"]

    # people match
    for p in config["people"]:
        name = p["name"].lower()
        company = p.get("company", "").lower()
        if name in text or (company and company in text):
            score += w["person_match"]

    # brand match
    for b in config["brands"]:
        if b.lower() in text:
            score += w["brand_match"]

    # multiply by source weight + add source boost
    weight_map = {s["id"]: s["weight"] for s in config["sources"]}
    boost_map = {s["id"]: s.get("boost", 0) for s in config["sources"]}
    return score * weight_map.get(item["source"], 0.5) + boost_map.get(item["source"], 0)


# ── Groq summary ────────────────────────────────────────────────────────────

def groq_summarize(items: list[dict], config: dict, today_str: str) -> str | None:
    """Send top items to Groq LLM and return summarized digest text."""
    api_key = groq_api_key()
    if not api_key:
        return None

    model = config.get("groq_model", "openai/gpt-oss-120b")

    # Build prompt
    news_block = "\n\n".join(
        f"{i+1}. [{item['source']}] {item['title']}\n   {item['link']}\n   {item['summary'][:300]}"
        for i, item in enumerate(items)
    )

    prompt = f"""Напиши дайджест по AI-Testing за {today_str}. Формат:

🔥 [N] **Заголовок** — суть и значимость для QA (1 предложение, не начинай с "это").
📋 [N] Заголовок — суть (коротко).
...

**Итог:** тренд дня, 1 предложение.

Правила (строго):
- [N] = номер новости из списка ниже. Один буллет = одна новость из списка.
- Буллетов НЕ БОЛЬШЕ, чем новостей в списке. Ничего вне списка: ни заголовков, ни фактов.
- Пример хорошего стиля:
🔥 [1] **File Upload Testing Without Dependencies** — решение для загрузки файлов в тестах без локальных путей, устраняет главную боль CI-окружений.

Не используй "это важно, потому что", "это позволяет", "это о том, как". Только суть.

Новости:
{news_block}"""

    try:
        resp = httpx.post(
            "https://api.groq.com/openai/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json",
            },
            json={
                "model": model,
                "messages": [{"role": "user", "content": prompt}],
                "temperature": 0.3,
                "max_tokens": 1500,
            },
            timeout=60,
        )
        resp.raise_for_status()
        data = resp.json()
        return data["choices"][0]["message"]["content"].strip()
    except Exception as e:
        print(f"  [WARN] Groq API error: {e}", file=sys.stderr)
        return None


# ── LLM grounding guard ─────────────────────────────────────────────────────

def ground_summary(llm_text: str | None, n_items: int) -> str | None:
    """Drop LLM bullets that don't reference a real input item.

    Keeps only 🔥/📋 lines carrying a valid [N] marker (1..n_items),
    strips the marker, caps bullets at n_items. Non-bullet lines
    (e.g. Итог) pass through. Returns None if no bullet survived —
    caller falls back to the honest raw format (real items + links).
    Silence beats hallucination: fewer but grounded.
    """
    if not llm_text:
        return None
    kept: list[str] = []
    tail: list[str] = []
    seen: set[int] = set()
    for line in llm_text.splitlines():
        s = line.strip()
        if s.startswith(("🔥", "📋")):
            m = re.match(r"^[🔥📋]\s*\[(\d+)\]\s*(.*)$", s)
            if not m:
                continue  # bullet without source ref → hallucination, drop
            n = int(m.group(1))
            if not (1 <= n <= n_items) or n in seen:
                continue
            seen.add(n)
            kept.append(re.sub(r"\s{2,}", " ",
                               s.replace(f"[{n}]", "", 1)).strip())
        else:
            tail.append(line)
    if not kept:
        print("  [guard] LLM summary had 0 grounded bullets → raw fallback",
              file=sys.stderr)
        return None
    if len(kept) < len([l for l in llm_text.splitlines()
                        if l.strip().startswith(("🔥", "📋"))]):
        print(f"  [guard] dropped ungrounded bullets, kept {len(kept)}/{n_items}",
              file=sys.stderr)
    return "\n".join(kept + tail)


# ── Dedup against recent digests ────────────────────────────────────────────

def load_recent_links(lookback: int = 3, today_str: str = "") -> set[str]:
    """Collect links already covered in recent digest files.

    Skips today's own file so the current digest is not deduped against itself.
    """
    seen: set[str] = set()
    files = sorted(DIGESTS_DIR.glob("*.md"), reverse=True)
    if today_str:
        files = [f for f in files if f.stem != today_str]
    for path in files[:lookback]:
        try:
            text = path.read_text()
        except Exception:
            continue
        # collect markdown links: [title](url)
        for m in re.findall(r"\]\((https?://[^)\s]+)\)", text):
            seen.add(m.rstrip("/"))
        # also bare URLs on their own line
        for m in re.findall(r"^https?://[^\s]+", text, flags=re.MULTILINE):
            seen.add(m.rstrip("/"))
    return seen


def dedup_items(items: list[dict], lookback: int = 3, today_str: str = "") -> tuple[list[dict], int]:
    """Drop items whose link already appeared in recent digests.

    Returns (kept_items, dropped_count). Items without a link are kept.
    """
    seen = load_recent_links(lookback, today_str=today_str)
    kept: list[dict] = []
    dropped = 0
    for it in items:
        link = (it.get("link") or "").rstrip("/")
        if link and link in seen:
            dropped += 1
        else:
            kept.append(it)
    return kept, dropped


# ── Routing (не потерять полезное) ──────────────────────────────────────────

def route_item(item: dict, routes: list[dict]) -> list[str]:
    """Match an item against config routes. Returns list of actions."""
    text = (item.get("title", "") + " " + item.get("summary", "")).lower()
    return [r["action"] for r in routes
            if any(k.lower() in text for k in r.get("match", []))]


def format_routing(scored: list[dict], routes: list[dict]) -> list[str]:
    """Build the «Куда это» checklist. Rule:
    1. Полезно и ново (нет маршрута) → кандидат в wiki-страницу.
    2. Полезно для текущих статей/проектов (есть маршрут) → вписать в конец
       страницы / план обсуждений. Решение за человеком — здесь только напоминалка.
    """
    lines = ["### Куда это (не потерять)", ""]
    for item in scored:
        actions = route_item(item, routes)
        title = item.get("title", "?")[:80]
        if actions:
            for a in actions:
                lines.append(f"- [ ] {title} → {a}")
        else:
            lines.append(f"- [ ] {title} → 🆕 новое: кандидат в wiki-страницу?")
    lines.append("")
    return lines


# ── Output ──────────────────────────────────────────────────────────────────

def format_digest(scored: list[dict], llm_text: str | None, total: int,
                  source_ids: list[str], today_str: str,
                  routes: list[dict] | None = None) -> str:
    """Format the final digest."""
    lines: list[str] = []
    lines.append(f"# Дайджест AI-Testing · {today_str}")
    lines.append("")

    if llm_text:
        lines.append(llm_text)
        lines.append("")
    else:
        # raw format if no LLM
        for i, item in enumerate(scored):
            star = "🔥" if i < 3 else "📋"
            lines.append(f"{star} **[{item['source']}]** {item['title']}")
            lines.append(f"   {item['link']}")
            lines.append(f"   Score: {item['_score']:.2f}")
            lines.append("")

    # Append links after LLM text
    lines.append("### Ссылки")
    lines.append("")
    for i, item in enumerate(scored):
        star = "🔥" if i < 3 else "📋"
        title = item.get("title", "?")
        link = item.get("link", "")
        if link:
            lines.append(f"{star} [{title}]({link})")
        else:
            lines.append(f"{star} {title} (нет ссылки)")

    lines.append("")
    source_list = ", ".join(sorted(set(source_ids)))
    lines.append(f"📊 *Всего отобрано: {len(scored)} из {total} · Источники: {source_list}*")
    if routes:
        lines.append("")
        lines.extend(format_routing(scored, routes))
    return "\n".join(lines)


def fetch_url(url: str) -> dict | None:
    """Fetch a URL and extract readable text. Returns item dict or None."""
    try:
        resp = httpx.get(url, timeout=30, follow_redirects=True,
                         headers={"User-Agent": "Mozilla/5.0 (compatible; daily-digest/1.0)"})
        resp.raise_for_status()
        text = resp.text
        # Try common extractors:
        # 1. Check for meta description
        m = re.search(r'<meta[^>]+name=["\']description["\'][^>]+content=["\']([^"\']+)', text)
        description = m.group(1) if m else ""
        # 2. Check for article/entry content
        body = re.search(r'<article[^>]*>(.*?)</article>', text, re.DOTALL)
        if not body:
            body = re.search(r'<main[^>]*>(.*?)</main>', text, re.DOTALL)
        if not body:
            body = re.search(r'<body[^>]*>(.*?)</body>', text, re.DOTALL)
        content = _clean_html(body.group(1)) if body else _clean_html(text)
        # Get title from <title> tag
        title_m = re.search(r'<title[^>]*>(.*?)</title>', text, re.DOTALL)
        title = _clean_html(title_m.group(1)) if title_m else url

        return {
            "title": title[:200],
            "link": url,
            "published": date.today().isoformat(),
            "summary": content[:1000],
            "source": "url-import",
            "source_name": "Web Import",
            "_score": 999.0,
        }
    except Exception as e:
        print(f"  [WARN] Failed to fetch {url}: {e}", file=sys.stderr)
        return None


ASSISTANT_TEXT = """\
  --import-url URL   Fetch a LinkedIn/any URL, extract text, add to digest
  --manual TEXT      Add a manual news item (free-form text)
"""


def print_digest(digest: str) -> None:
    print(digest)


def save_digest(digest: str, today_str: str) -> Path:
    DIGESTS_DIR.mkdir(parents=True, exist_ok=True)
    path = DIGESTS_DIR / f"{today_str}.md"
    path.write_text(digest)
    return path


# ── Telegram delivery ───────────────────────────────────────────────────────

TG_CHAT_IDS = [117754174]


def tg_token() -> str | None:
    token = os.environ.get("TG_BOT_TOKEN")
    if token:
        return token
    token_file = Path.home() / ".tg_token"
    if token_file.exists():
        return token_file.read_text().strip()
    return None


def tg_send(text: str, parse_mode: str = "Markdown") -> bool:
    token = tg_token()
    if not token:
        print("⚠️ TG_BOT_TOKEN not set (env or ~/.tg_token)", file=sys.stderr)
        return False
    text = text[:3800]
    ok = False
    for mode in (parse_mode, None):
        try:
            resp = httpx.post(
                f"https://api.telegram.org/bot{token}/sendMessage",
                json={"chat_id": TG_CHAT_IDS[0], "text": text,
                      "parse_mode": mode} if mode else
                     {"chat_id": TG_CHAT_IDS[0], "text": text},
                timeout=30,
            )
            ok = resp.status_code == 200
            if ok:
                return True
        except Exception as e:
            print(f"⚠️ TG send failed ({mode}): {e}", file=sys.stderr)
    return ok


# ── Eval mode ───────────────────────────────────────────────────────────────

def eval_threshold(config: dict) -> None:
    """Evaluate scoring against golden dataset and find best threshold."""
    if not GOLDEN_PATH.exists():
        print(f"Golden dataset not found at {GOLDEN_PATH}")
        print("Create it first with labeled items.")
        return

    with open(GOLDEN_PATH) as f:
        golden = json.load(f)

    print(f"Golden dataset: {len(golden)} items\n")

    results = []
    for item in golden:
        item["_score"] = score_item(item, config)

    # Try thresholds
    best_f1 = 0.0
    best_t = 1.5
    print(f"{'Threshold':>10} {'Precision':>10} {'Recall':>10} {'F1':>10} {'TP':>4} {'FP':>4} {'FN':>4}")
    print("-" * 62)

    for t in [round(x * 0.1, 1) for x in range(5, 31)]:  # 0.5 to 3.0 step 0.1
        tp = sum(1 for it in golden if it["_score"] >= t and it.get("relevant", False))
        fp = sum(1 for it in golden if it["_score"] >= t and not it.get("relevant", False))
        fn = sum(1 for it in golden if it["_score"] < t and it.get("relevant", False))

        precision = tp / (tp + fp) if (tp + fp) > 0 else 0.0
        recall = tp / (tp + fn) if (tp + fn) > 0 else 0.0
        f1 = 2 * precision * recall / (precision + recall) if (precision + recall) > 0 else 0.0

        marker = " ◀ BEST" if f1 > best_f1 else ""
        if f1 > best_f1:
            best_f1 = f1
            best_t = t

        if t == 1.5 or f1 > best_f1 - 0.05 or t in [round(x * 0.5, 1) for x in range(2, 7)]:
            print(f"{t:>10.1f} {precision:>10.3f} {recall:>10.3f} {f1:>10.3f} {tp:>4} {fp:>4} {fn:>4}{marker}")

    print(f"\nBest threshold: {best_t:.1f} (F1={best_f1:.3f})")
    print(f"Current threshold in config: {config['threshold']:.1f}")

    # Show misclassifications at current threshold
    current_t = config["threshold"]
    print(f"\nMiscclassifications at threshold {current_t:.1f}:")
    for item in golden:
        pred = item["_score"] >= current_t
        actual = item.get("relevant", False)
        if pred != actual:
            label = "FP" if pred else "FN"
            print(f"  [{label}] score={item['_score']:.2f} {item.get('source','?')}: {item['title'][:80]}")
            if item.get("note"):
                print(f"         Note: {item['note']}")


# ── Cron install ────────────────────────────────────────────────────────────

def install_cron() -> None:
    """Install daily cron job at 9:00."""
    script_path = SCRIPT_DIR / "daily-digest.py"
    cron_line = (f"0 9 * * * TG_BOT_TOKEN=$(cat ~/.tg_token) "
                 f"/Library/Frameworks/Python.framework/Versions/3.12/bin/python3 "
                 f"{script_path} --save --telegram 2>> {DIGESTS_DIR}/cron.log\n")

    existing = ""
    cron_file = Path.home() / ".cron_digest"
    if cron_file.exists():
        existing = cron_file.read_text()

    if cron_line in existing:
        print("Cron job already installed.")
        return

    # Check if crontab has it
    import subprocess
    result = subprocess.run(["crontab", "-l"], capture_output=True, text=True)
    current_crontab = result.stdout if result.returncode == 0 else ""

    if cron_line in current_crontab:
        print("Cron job already in crontab.")
        return

    new_crontab = current_crontab + cron_line
    with open(cron_file, "w") as f:
        f.write(new_crontab)

    subprocess.run(["crontab", str(cron_file)], check=True)
    print(f"Cron job installed: daily at 9:00 → {DIGESTS_DIR}/")


# ── Main ────────────────────────────────────────────────────────────────────

def main() -> None:
    parser = argparse.ArgumentParser(description="Daily AI-Testing Digest")
    parser.add_argument("--no-llm", action="store_true", help="Skip Groq, print raw scores")
    parser.add_argument("--manual", type=str, help='Add manual news item (in quotes)')
    parser.add_argument("--import-url", type=str, help='Fetch URL and add to digest')
    parser.add_argument("--json", action="store_true", help="Output JSON instead of formatted digest")
    parser.add_argument("--no-save", action="store_true", help="Skip saving to digests/")
    parser.add_argument("--save", action="store_true", help="Force save (default: auto-save)")
    parser.add_argument("--eval", action="store_true", help="Evaluate golden dataset and tune threshold")
    parser.add_argument("--telegram", action="store_true", help="Send digest to Telegram after generation")
    parser.add_argument("--install-cron", action="store_true", help="Install daily cron at 9:00")
    args = parser.parse_args()

    config = load_config()
    today_str = date.today().isoformat()

    # Eval mode
    if args.eval:
        eval_threshold(config)
        return

    # Cron mode
    if args.install_cron:
        install_cron()
        return

    # Normal mode: fetch + score + summarize
    all_items = fetch_all(config)

    if not all_items:
        print("Нет новостей (все источники недоступны).")
        sys.exit(1)

    # Score
    for item in all_items:
        item["_score"] = score_item(item, config)

    # Filter by threshold
    threshold = config["threshold"]
    scored = [it for it in all_items if it["_score"] >= threshold]
    scored.sort(key=lambda x: x["_score"], reverse=True)

    # Enforce per-source cap (default: unlimited if not configured)
    max_per_source = config.get("max_per_source", 0)
    if max_per_source > 0:
        per_source: dict[str, int] = {}
        capped: list[dict] = []
        for it in scored:
            src = it["source"]
            if per_source.get(src, 0) < max_per_source:
                per_source[src] = per_source.get(src, 0) + 1
                capped.append(it)
        scored = capped

    # Dedup: drop items whose link already appeared in recent digests
    # (applied BEFORE top_n so the top list refills with fresh items)
    dedup_lookback = config.get("dedup_lookback", 3)
    if dedup_lookback > 0:
        scored, dropped = dedup_items(scored, lookback=dedup_lookback, today_str=today_str)
        if dropped:
            print(f"  [dedup] excluded {dropped} item(s) already in recent digests", file=sys.stderr)

    top_n = config.get("top_n", 10)
    top = scored[:top_n]

    # Add manual item
    if args.manual:
        manual_item = {
            "title": args.manual,
            "link": "",
            "published": today_str,
            "summary": "",
            "source": "manual",
            "source_name": "Manual",
            "_score": 999.0,
        }
        top.insert(0, manual_item)
        scored.insert(0, manual_item)

    # Import URL
    if args.import_url:
        imported = fetch_url(args.import_url)
        if imported:
            top.insert(0, imported)
            scored.insert(0, imported)

    # Groq summary (grounded: bullets must cite input items)
    llm_text = None
    if not args.no_llm and top:
        llm_text = ground_summary(groq_summarize(top, config, today_str), len(top))

    # Output
    source_ids = list({it["source"] for it in all_items})

    if args.json:
        output = {
            "date": today_str,
            "total_raw": len(all_items),
            "total_after_filter": len(scored),
            "sources": source_ids,
            "llm_summary": llm_text,
            "top_items": [
                {
                    "title": it["title"],
                    "link": it["link"],
                    "source": it["source"],
                    "score": round(it["_score"], 2),
                }
                for it in top
            ],
        }
        print(json.dumps(output, ensure_ascii=False, indent=2))
    else:
        digest = format_digest(top, llm_text, len(all_items), source_ids, today_str,
                               routes=config.get("routes", []))
        print_digest(digest)

    # Save
    do_save = args.save or not args.no_save
    if do_save:
        if args.json:
            path = DIGESTS_DIR / f"{today_str}.json"
            path.write_text(json.dumps(output, ensure_ascii=False, indent=2))
        else:
            path = save_digest(digest, today_str)
        print(f"\n💾 Saved: {path}", file=sys.stderr)

    # Telegram delivery
    if args.telegram:
        if args.json:
            tg_send(json.dumps(output, ensure_ascii=False)[:3800])
        else:
            tg_send(digest)
        print("📨 Sent to Telegram", file=sys.stderr)

    # Exit code: 1 if no items passed threshold
    if not top:
        sys.exit(0)


if __name__ == "__main__":
    main()
