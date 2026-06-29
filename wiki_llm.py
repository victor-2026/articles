#!/usr/bin/env python3
"""
Articles Wiki LLM - Generate LinkedIn article drafts and ideas from raw materials

Usage:
    python3 wiki_llm.py <topic> [--context 'text']              — Generate draft
    python3 wiki_llm.py <topic> --from-raw [--lang ru|en]       — Generate from raw files
    python3 wiki_llm.py --ask "question"                         — Q&A from wiki
    python3 wiki_llm.py --ideas [--from-raw]                     — Generate post ideas
    python3 wiki_llm.py --ask "question" -m llama-3.3-70b       — Better quality

Models (cost per 1M tokens):
  openai/gpt-oss-120b     $0.15/$0.60 — cheap, good for drafts (DEFAULT)
  llama-3.3-70b-versatile $0.59/$0.79 — best quality
  openai/gpt-oss-20b      $0.075/$0.30 — fastest, cheapest
"""

import os
import sys
import re
from pathlib import Path
from datetime import datetime

GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"
GROQ_MODEL = "openai/gpt-oss-120b"

PROJECT_DIR = Path(__file__).parent
WIKI_DIR = PROJECT_DIR / "wiki"
RAW_DIR = PROJECT_DIR / "raw"
POSTS_DIR = PROJECT_DIR / "linkedin-posts"

SYSTEM_PROMPT = """You are a senior tech writer and QA engineer creating LinkedIn content.
Write in Russian or English based on user preference.
Follow LinkedIn best practices: hook → body → CTA → author line.
Keep posts practical, specific, and actionable.
Avoid generic advice — focus on real experience and data.
Max 500 words."""

SYSTEM_PROMPT_QA = """You are a senior tech writer and QA engineer.
Answer based on the provided wiki context about LinkedIn formats and strategies.
If information is not in context, say so honestly.
Answer concisely (3-5 sentences)."""


def get_groq_key():
    key = os.environ.get("GROQ_API_KEY")
    if key:
        return key
    raise ValueError("GROQ_API_KEY not set. Run: export GROQ_API_KEY=$(cat ~/1.groq_ke)")


def ask_llm(prompt: str, system_prompt: str = SYSTEM_PROMPT, temperature: float = 0.7, model: str = "") -> str:
    import requests
    headers = {"Authorization": f"Bearer {get_groq_key()}", "Content-Type": "application/json"}
    data = {
        "model": model or GROQ_MODEL,
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt}
        ],
        "temperature": temperature,
        "max_tokens": 1200
    }
    resp = requests.post(GROQ_API_URL, headers=headers, json=data, timeout=60)
    resp.raise_for_status()
    return resp.json()["choices"][0]["message"]["content"]


def read_raw_files() -> str:
    """Read all raw files for context"""
    parts = []
    for f in sorted(RAW_DIR.glob("*.md")) + sorted(RAW_DIR.glob("*.txt")):
        try:
            content = f.read_text(encoding="utf-8")[:2000]
            parts.append(f"## {f.name}\n{content}\n")
        except:
            pass
    return "\n\n".join(parts)


def find_relevant_files(query: str, top_n: int = 3) -> list:
    keywords = query.lower().split()
    wiki_files = list(WIKI_DIR.glob("*.md"))
    scores = {}
    for f in wiki_files:
        try:
            content = f.read_text(encoding="utf-8").lower()
            score = sum(1 for kw in keywords if kw in content)
            if score > 0:
                scores[f] = score
        except:
            pass
    sorted_files = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    return [f for f, _ in sorted_files[:top_n]]


def build_context(files: list, max_chars: int = 3000) -> str:
    context_parts = ["# Контекст из Wiki\n"]
    total = 0
    for f in files:
        if total >= max_chars:
            break
        try:
            content = f.read_text(encoding="utf-8")[:max_chars // len(files)]
            context_parts.append(f"## {f.name}\n{content}\n")
            total += len(content)
        except:
            pass
    return "\n\n".join(context_parts)


LOG_FILE = PROJECT_DIR / "wiki_llm.log"


def log_run(mode: str, topic: str, status: str, output: str = ""):
    line = f"[{datetime.now().isoformat()}] {mode} | {topic[:80]} | {status} | {output[:80]}"
    with open(LOG_FILE, "a") as f:
        f.write(line + "\n")


def clean_filename(s: str) -> str:
    s = s.lower().replace(" ", "-")
    s = re.sub(r'[^a-zа-я0-9_-]', '', s)
    return s[:60] + ".md"


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)

    args = sys.argv[1:]

    model = ""
    for flag in ("--model", "-m"):
        if flag in args:
            idx = args.index(flag)
            if idx + 1 < len(args):
                model = args[idx + 1]
            args = [a for a in args if a not in (flag, model)]

    print(f"🤖 Model: {model or GROQ_MODEL}")

    from_raw = "--from-raw" in args
    lang = "en" if "--lang" in args and args[args.index("--lang") + 1] == "en" else "ru"
    args = [a for a in args if a not in ("--from-raw", "--lang", "en", "ru")]
    if from_raw:
        raw_content = read_raw_files()
        if raw_content:
            context_arg = "--context"
            args.extend([context_arg, raw_content])

    if args[0] == "--ask":
        question = " ".join(args[1:]) if len(args) > 1 else ""
        if not question:
            print("❓ Введите вопрос после --ask")
            sys.exit(1)

        relevant = find_relevant_files(question)
        context = ""
        if relevant:
            print(f"📄 Нашёл: {[f.name for f in relevant]}")
            context = build_context(relevant)

        prompt = f"""## Контекст из Wiki
{context}

## Вопрос
{question}

## Инструкция
Ответь кратко (3-5 предложений) используя Wiki контекст."""
        answer = ask_llm(prompt, SYSTEM_PROMPT_QA, temperature=0.3, model=model)
        print(f"\n## Answer\n\n{answer}\n")
        log_run("ask", question, "ok")
        return

    if args[0] == "--ideas":
        raw = raw_content if from_raw else ""
        prompt = f"""Generate 5 LinkedIn post ideas about AI testing, QA automation, or engineering culture.

Context from raw materials:
{raw[:3000] if raw else "No specific context — use general expertise"}

For each idea provide:
- Title
- Hook (1 sentence)
- Target audience
- Why it would perform well

Language: {"Russian" if lang == "ru" else "English"}"""
        ideas = ask_llm(prompt, temperature=0.8, model=model)
        print(f"\n## 💡 Post Ideas\n\n{ideas}\n")
        log_run("ideas", "", "ok")
        return

    topic = " ".join(args)
    context_text = ""
    if "--context" in args:
        idx = args.index("--context")
        if idx + 1 < len(args):
            context_text = args[idx + 1]

    prompt = f"""Write a LinkedIn post about: {topic}

Context: {context_text[:3000] if context_text else "Use your expertise on this topic"}

Format: hook → body with insights → CTA → author line
Language: {"Russian" if lang == "ru" else "English"}

Make it specific, actionable, and based on real experience."""

    print(f"\n# {topic}\n")
    result = ask_llm(prompt, temperature=0.7, model=model)
    print(result)

    POSTS_DIR.mkdir(exist_ok=True)
    fname = clean_filename(topic)
    (POSTS_DIR / fname).write_text(
        f"# {topic}\n\n{result}\n\n---\n*Generated by wiki_llm.py (Groq) — {datetime.today().strftime('%Y-%m-%d')}*\n", encoding="utf-8")
    print(f"\n💾 Saved to: linkedin-posts/{fname}")
    log_run("generate", topic, "ok", f"linkedin-posts/{fname}")


if __name__ == "__main__":
    main()
