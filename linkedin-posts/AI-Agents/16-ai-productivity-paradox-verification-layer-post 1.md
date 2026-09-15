Agents write 7x more code. Releases grew 20%.

GitLab: 78% code faster, 79% admit delivery hasn't sped up.
METR: engineers felt +20% speed. Measured: -19%.

The bottleneck moved from writing to checking - and that's now a QA leadership problem.

The fix I use:
→ AI reviewer + auto-fix loop before a human looks (one agent finds, another repairs)
→ Regression checklists generated from git diff on every PR
→ Mutation testing to catch agent tests that assert a string instead of behavior (34/34 faults caught)
→ Specs as the new code - a bad spec produces wrong code faster

Block's numbers after 3 months of focused champions: AI-authored code +69%, automated PRs 21x. Then the review pipeline broke first - exactly where QA should have been standing.

Where is your team on the 0-5 delegation scale - and what breaks first when you hit 4?

Victor Ematin · AI Quality Engineering Lead · OpenCode Go

#AIEngineering #AIAgents #QualityEngineering #GenAITesting #AIProductivity