The same model evaluating the same skill is like a student grading their own homework. I proved this with 18 runs across 3 skills — 0% lift.

8 skills. 4 self-evaluation axes. 6 stop-rules. Zero external judges. I built a three-layer architecture that validates AI-generated test code without a second LLM.

I spent a month building 8 skills with a different architecture. Three layers instead of one:

1️⃣ Context Layer — AGENTS.md + stop-rules (what NOT to do)

2️⃣ Skill Layer — domain knowledge + 4-axis self-evaluation

3️⃣ Validation Layer — BDD harness as executable specs

Here's the difference: Gulin treats skills as code-gen packages. I treat them as agent behavior blueprints.

Once the skill is loaded, the agent knows not just what to write, but when to ask for help, how to fail honestly, and how to validate its own output
  

I wrote up the full architecture — including what I learned from people I never met, and what it means for enterprise QA with AI agents.

  

Read the full article 👇

  

Victor Ematin · AI Quality Engineering Lead · OpenCode Go

  

#TestAutomation #AIQA #AgenticTesting #Playwright #OpenCode