#!/usr/bin/env python3
"""Generate W35 weekly charts: daily trend + top posts."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

OUT = "/Users/victor/Projects/Articles/linkedin-posts/weekly"

# Daily trend (Aug 18-24)
days = ["Mon 8/18", "Tue 8/19", "Wed 8/20", "Thu 8/21", "Fri 8/22", "Sat 8/23", "Sun 8/24"]
imp = [6382, 7966, 2463, 1671, 160, 183, 77]
eng = [22, 24, 13, 17, 0, 0, 1]

plt.figure(figsize=(10, 5))
plt.bar(days, imp, color="#0969da", alpha=0.85, label="Impressions")
ax = plt.gca()
ax2 = ax.twinx()
ax2.plot(days, eng, color="#f85149", marker="o", linewidth=2, label="Engagements")
ax2.set_ylabel("Engagements", color="#f85149")
ax2.tick_params(axis="y", labelcolor="#f85149")
ax.set_ylabel("Impressions", color="#0969da")
ax.tick_params(axis="y", labelcolor="#0969da")
ax.set_xticklabels(days, rotation=30, ha="right")
plt.title("W35 Daily Trend (Aug 18-24, 2026)", fontweight="bold")
ax.legend(loc="upper left")
ax2.legend(loc="upper right")
plt.tight_layout()
plt.savefig(f"{OUT}/w35-daily-trend.png", dpi=150, bbox_inches="tight")
plt.close()

# Top posts by impressions
posts = [
    ("Article 12\n(repost)", 17874),
    ("Article 16\npost", 277),
    ("Article 14\npost", 224),
    ("Article 14\ncarousel", 166),
    ("Article 16\ncarousel", 156),
    ("Part That\nLands", 74),
    ("Article 13\ncarousel", 41),
]
labels = [p[0] for p in posts]
vals = [p[1] for p in posts]

plt.figure(figsize=(10, 5))
colors = ["#f85149" if "Article 12" in l else "#0969da" for l in labels]
bars = plt.barh(labels, vals, color=colors, alpha=0.85)
for b, v in zip(bars, vals):
    plt.text(b.get_width() + 200, b.get_y() + b.get_height()/2, f"{v:,}", va="center")
plt.xlabel("Impressions")
plt.title("W35 Top Posts by Impressions (Article 12 = 94.6%)", fontweight="bold")
plt.tight_layout()
plt.savefig(f"{OUT}/w35-top-posts.png", dpi=150, bbox_inches="tight")
plt.close()

print("charts done")
