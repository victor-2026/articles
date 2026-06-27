# Articles

LinkedIn post drafts, wiki knowledge base, and content strategy for AI QA Engineering.

## Structure

```
Articles/
├── AGENTS.md                 # AI rules & boundaries
├── README.md
├── _Тезисы.md                # Content ideas pipeline (human)
├── raw/                      # Source materials — human only, AI read-only
├── wiki/                     # AI-organized knowledge: formats, emoji, strategies
├── linkedin-posts/           # Post drafts organized by project
│   ├── Buzzhive/             # Buzzhive test automation series
│   ├── OrangeHRM/            # OrangeHRM demo project series
│   ├── Webwright/            # Microsoft Webwright experiment series
│   ├── Old/                  # Archive — immutable by AI
│   ├── weekly/               # Weekly performance reports
│   ├── hooks-library.md      # Reusable hooks from top posts
│   ├── performance-log.csv   # Published post metrics
│   └── swe-tester-rewrite.md # Rewrite drafts
├── md2linkedin.py            # Script: .md → LinkedIn format
└── pbcopy-html.swift         # Script: HTML → system clipboard
```

## Pipeline

```
raw/ (source)  →  wiki/ (patterns)  +  linkedin-posts/ (drafts)  →  LinkedIn
```

---

*Pattern: raw → wiki (Karpathy-style)*
*See AGENTS.md for AI boundaries and conventions.*