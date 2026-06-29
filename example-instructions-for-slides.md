### Recommended Slide Ordering (8 limitation slides \+ bookends)

1. Title Slide  
   *"Webwright Limitations: What Microsoft's Research Reveals"*  
   \[Subtitle\] Practical constraints of autonomous web agents  
   \[Visual\] Your logo \+ subtle background (e.g., terminal/code motif)  
2. Context Slide (1 sentence)  
   *"While Webwright advances web automation, these limitations shape real-world viability—based on Microsoft's findings."*  
   \[Visual\] Simple scale graphic: "Innovation ↔ Practicality"  
3. Limitation Slides (ordered by foundational impact → situational):  
   * Model dependency (Core enabler—if weak, everything fails)  
   * Context limits (Fundamental LLM constraint)  
   * Premature "done" (Critical reliability issue)  
   * Maintenance costs (Ongoing operational burden)  
   * Granularity challenge (Design tension affecting sustainability)  
   * Environment limits (Use-case boundary)  
   * Cost factor (Economic filter for adoption)  
   * Predictability trade-off (Philosophical contrast to traditional)  
4. Call-to-Action Slide  
   *"Match Webwright to your: \[Stability\] × \[Volume\] × \[Maintenance Capacity\]"*  
   \[Visual\] Venn diagram or triple-scale graphic  
   \[Link\] Microsoft announcement (bottom-right corner)  
5. Engagement Slide (Optional but recommended)  
   *"Which limitation impacts your work most? Comment below ↓"*  
   \[Visual\] Poll-style icons or blank space for comments

---

### 🎨 Visual Hierarchy Tips (for your design tool)

* Typography:  
  * Headings: Bold sans-serif (e.g., Inter Bold, 28-32pt)  
  * Body: Regular weight (20-24pt)  
  * Key terms: Bold (not italics—for LinkedIn clarity)  
* Color Use:  
  * 1 primary color (e.g., your brand blue) for headings/icons  
  * 1 accent color (e.g., orange) for ⚠️ warnings  
  * Neutral gray for body text (avoid pure black on white—use \#333)  
* Icon Strategy:  
  * Keep ⚠️ consistent (same size/color)  
  * Consider adding micro-icons per slide (e.g., 💡 for granularity, 💰 for cost)  
  * *Never* overload—1 visual anchor per slide max  
* Spacing:  
  * Minimum 1.5 line height  
  * Ample padding (20% of slide height as margin)  
  * Group related concepts with subtle background tints (5% opacity)

---

### ✏️ Targeted Bullet Refinements (optional tweaks)

Based on your drafts, these micro-adjustments could enhance clarity:

1. Model dependency:  
   *"Performance hinges on the LLM's reasoning depth: GPT-5.4 leads in accuracy, Claude Opus 4.7 in step efficiency, while compact models (e.g., Qwen3.5-9B) often need auxiliary tools (like syntax validators) to handle multi-step web flows reliably."*  
   → *Adds "auxiliary tools" for concreteness*  
2. Cost factor:  
   *"Top models run*   
3. 2.37–  
4. 2.37–*6.09 per task, but amortization kicks in fast: once generated, Webwright's executable scripts run near-zero marginal cost—making it viable for workflows exceeding 50+ monthly executions."*  
   → *Adds practical break-even threshold*  
5. Environment limits:  
   *"On non-semantic sites (e.g., HTML5 games, legacy frames), agents fallback to perception primitives—clicking coordinates or matching visual patterns—which works but sacrifices the 10x speed and resilience of DOM-based interactions."*  
   → *Quantifies the trade-off ("10x speed")*

---

### 🖼️ Picture/Screenshot Concept Clues (describe to your designer or generate yourself)

For each limitation slide, consider these read-only describable concepts:

| Limitation | Suggested Visual Concept | Creation Clue (for your tool) |
| :---- | :---- | :---- |
| Model dependency | Model performance bar chart (accuracy vs. cost) | Draw 3-4 labeled bars: GPT-5.4 (high accuracy, $$$), Claude Opus (medium accuracy, $$$$), Qwen (lower accuracy, $) |
| Context limits | Timeline showing context overflow | Horizontal timeline: 20 steps → \[summary box\] → 20 steps → \[overflow warning icon\] |
| Premature "done" | Before/after terminal state | Split screen: Left=false success (terminal says "done" but cart empty), Right=true success (order confirmed) |
| Maintenance costs | Script library decay over time | Flowchart: Fresh script → \[site update\] → Silent failure → \[validation\] → Update/retire |
| Granularity | Fragmented vs. monolithic script library | Two grids: Left=many tiny boxes (micro), Right=1 huge box covering 90% of area (monolith) |
| Environment limits | Fallback mechanism illustration | Diagram: Semantic path (blocked) → Arrow to fallback path (coordinates/visual matching) |
| Cost factor | Cost amortization curve | Graph: Y-axis=$/task, X-axis=executions. High initial cost dropping to near-zero after N |
| Predictability | Rigid vs. adaptive path | Two paths: Straight line hitting obstacle (traditional), winding path avoiding obstacle (Webwright) |

Execution Tip: Use simple shapes (arrows, boxes, icons) in your design tool—no need for complex illustrations. Even hand-drawn style vectors work well for technical carousels.

---

