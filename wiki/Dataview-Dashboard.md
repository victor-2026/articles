# Dataview Dashboard — LinkedIn Posts

> **Status:** Dataview installed in vault. Posts need frontmatter to be queryable. Sample queries below work after adding frontmatter.

## 1. All posts by date (newest first)

```dataview
TABLE
  format AS "Format",
  series AS "Series",
  impressions AS "👁 Imp",
  engagement AS "💬 %"
FROM "linkedin-posts"
WHERE type = "linkedin-post"
SORT date DESC
```

## 2. Posts by series (count)

```dataview
TABLE length(rows) AS "Count"
FROM "linkedin-posts"
WHERE type = "linkedin-post"
GROUP BY series
SORT length(rows) DESC
```

## 3. Posts by format

```dataview
TABLE length(rows) AS "Count"
FROM "linkedin-posts"
WHERE type = "linkedin-post"
GROUP BY format
```

## 4. High-engagement posts (>1%)

```dataview
TABLE
  date AS "Published",
  impressions AS "👁",
  engagement AS "💬 %"
FROM "linkedin-posts"
WHERE type = "linkedin-post" AND engagement > 1.0
SORT engagement DESC
```

## 5. Pending posts (not published)

```dataview
LIST
FROM "linkedin-posts"
WHERE type = "linkedin-post" AND status != "published"
```

## 6. Tasks (incomplete)

```dataview
TASK
FROM "linkedin-posts"
WHERE !completed
SORT priority ASC

## 7. Wiki articles by topic

```dataview
TABLE
  date AS "Updated",
  tags AS "Tags"
FROM "wiki"
WHERE type = "wiki-article"
SORT date DESC
```

## 8. Weekly reports

```dataview
TABLE
  total-posts AS "Posts",
  best-performer AS "🏆 Top",
  impressions AS "👁 Total"
FROM "linkedin-posts/weekly"
WHERE type = "weekly-report"
SORT date DESC
```

## Setup instructions

1. **Install dataview** in this vault: Settings → Community plugins → Browse → Dataview → Install → Enable
2. **Add frontmatter** to existing posts (see template below)
3. **Refresh** the dashboard to see queries populate

## Frontmatter template for new posts

```yaml
---
type: linkedin-post
title: "Post Title"
date: 2026-06-12
format: post
series: AI-Agents
status: draft | published
impressions: 0
engagement: 0
tags: [qa, ai-agents, kpi]
---

# Post title here
...
```

## Frontmatter batch fix (optional, dangerous)

If you want to add frontmatter to all existing posts at once, run this from a terminal:

```bash
cd /Users/victor/Projects/Articles
for f in linkedin-posts/**/*.md; do
  if ! head -1 "$f" | grep -q "^---$"; then
    # Prepend frontmatter
    { echo "---"; echo "type: linkedin-post"; echo "title: \"$(basename "$f" .md)\""; echo "date: 2026-06-01"; echo "status: published"; echo "---"; echo; cat "$f"; } > "$f.tmp" && mv "$f.tmp" "$f"
  fi
done
```

**⚠️ Test on 1-2 files first** — this bulk-modifies your posts.
