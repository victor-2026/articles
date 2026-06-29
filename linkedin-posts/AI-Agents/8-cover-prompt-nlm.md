# Cover Image Prompt — Article 8

Use this prompt in NotebookLM or any AI image generator to create the article cover.

---

## Article Title
**Skills Are Not npm Packages** — Three-Layer Architecture for Self-Validating Agent Skills

## What to Generate
A dark-themed architecture diagram showing 4 layers stacked vertically with arrows between them.

## Layout (top to bottom)

```
┌──────────────────────────────────────────┐
│  Skills Are Not npm Packages             │
│  Three-Layer Architecture                │
├──────────────────────────────────────────┤
│                                          │
│  ┌────────────────────────────────────┐  │
│  │  CONTEXT LAYER                     │  │
│  │  AGENTS.md · Stop-rules · Boundaries│  │
│  └────────────────────────────────────┘  │
│                  ↓                       │
│  ┌────────────────────────────────────┐  │
│  │  SKILL LAYER                       │  │
│  │  SKILL.md · Self-Evaluation 4 axes │  │
│  └────────────────────────────────────┘  │
│                  ↓                       │
│  ┌────────────────────────────────────┐  │
│  │  VALIDATION LAYER                  │  │
│  │  BDD Harness · Executable Specs    │  │
│  └────────────────────────────────────┘  │
│                  ↓                       │
│  ┌────────────────────────────────────┐  │
│  │  OUTPUT                            │  │
│  │  Test code · Feature files · Rules │  │
│  └────────────────────────────────────┘  │
│                                          │
│  ONE MODEL · No external judge required  │
│                                          │
│  Article 8 · AI Agents series            │
└──────────────────────────────────────────┘
```

## Design Specs

- **Format:** 1920 × 1080 (16:9, LinkedIn cover)
- **Background:** Dark (#0D1117 or similar GitHub-dark)
- **Layer colors:** Blue (Context), Green (Skill), Purple (Validation), Dark Purple (Output)
- **Arrows:** Downward arrows (↓) between layers, accent blue color
- **Side badge:** "ONE MODEL" vertically on the right side
- **Subtitle:** "No external judge required" at bottom
- **Footer:** "Article 8 · AI Agents series · Victor Ematin"
- **Typography:** Clean sans-serif, white text, bold layer titles

## Layer Descriptions

| Layer | Title | Content | Color |
|-------|-------|---------|-------|
| 1 | CONTEXT | AGENTS.md · Stop-rules · Boundaries | Blue |
| 2 | SKILL | SKILL.md · Self-Evaluation (4 axes) | Green |
| 3 | VALIDATION | BDD Harness · Executable Specs | Violet |
| 4 | OUTPUT | Test code · Feature files · Behavior rules | Dark Violet |

## Key Message
Three layers, one model, no external judge. Skills are behavior blueprints, not npm packages.
