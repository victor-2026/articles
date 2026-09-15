- [
    
    ![View Addy Osmani’s  graphic link](https://media.licdn.com/dms/image/v2/D5603AQFo4QAj2ZTUdw/profile-displayphoto-scale_100_100/B56aAchMYkGcAY-/0/1787184860290?e=1790812800&v=beta&t=3fmVXip1Iljd8fLpNLQWjFayWfp_TE55ASsf7QQFnhQ)
    
    
    
    ](https://www.linkedin.com/in/addyosmani?miniProfileUrn=urn%3Ali%3Afsd_profile%3AACoAAAGXfeABZZsHYLPYGlkS7eoFikrNAYkiEHg)
    
    [Addy Osmani • FollowingMember of Technical Staff at Anthropic](https://www.linkedin.com/in/addyosmani?miniProfileUrn=urn%3Ali%3Afsd_profile%3AACoAAAGXfeABZZsHYLPYGlkS7eoFikrNAYkiEHg)14h •
    
    At Anthropic, Claude now writes 80% of our code. Engineers ship 8x more code per quarter. Side effect: Tests grew 10x. CI jobs up 25x in 6 months. Here's what helped us scale:  
      
    [https://lnkd.in/gjs9d8_e](https://lnkd.in/gjs9d8_e)  
      
    Lines of code isn't (of course) a direct measure of value. That's why these numbers matter less as a productivity flex and more as a systems warning. Writing code is no longer the constraint. Claude also reviews and helps approve PRs, so changes get smaller and more frequent.  
      
    Tests grew 10x while headcount barely moved. Result: CI jobs up 25x in 6 months. The quality bar didn't change: named human owner on every PR, required approval, same CI gates. What changed is volume through those gates.  
      
    That's why we had to rebuild test impact analysis. Agents can't just dump diffs. They need a deterministic set of relevant tests so they can self-verify and iterate. A 20-minute lag in that service meant tens of thousands of test updates not applied - missed regressions, flaky blockers, or tests that should have run and didn't.  
      
    Three patches bought us 70 days, then 29, then less than a day. The rewrite took one engineer three weeks. A year ago that would have been closer to a quarter. After cutover, the job-result backlog went flat. So generated code isn't the metric. The metric is whether review, tests, and CI can absorb the new rate of change without letting bad diffs through.  
      
    Codegen just moved the bottleneck downstream.  
      
    [hashtag#ai](https://www.linkedin.com/search/results/all/?keywords=%23ai&origin=HASH_TAG_FROM_FEED) [hashtag#programming](https://www.linkedin.com/search/results/all/?keywords=%23programming&origin=HASH_TAG_FROM_FEED) [hashtag#softwareengineering](https://www.linkedin.com/search/results/all/?keywords=%23softwareengineering&origin=HASH_TAG_FROM_FEED)
    
    …more
    
    Activate to view larger image,
    
    ![diagram](https://media.licdn.com/dms/image/v2/D5622AQFkLBfB_5VcKQ/feedshare-shrink_800/B56aCjhxzlJkAc-/0/1789449936398?e=1790812800&v=beta&t=mKong8beIeZhlZvwtynZH-KhIUVynJYmdlZRoGocESM)
    
    Activate to view larger image,
    
    - ![like](https://static.licdn.com/aero-v1/sc/h/emei2gdl9ikg7penkh9ij9llx)![insightful](https://static.licdn.com/aero-v1/sc/h/3bhtnif60blspoiyhoex4lfx)![love](https://static.licdn.com/aero-v1/sc/h/esahr356vrv0vklww6hcjar1j)1,919
    - - 148 comments
        - 128 reposts
    
    Like
    
    Comment
    
    Repost
    
    Send
    
- ## Feed post number 2
    
    [
    
    ![View Addy Osmani’s  graphic link](https://media.licdn.com/dms/image/v2/D5603AQFo4QAj2ZTUdw/profile-displayphoto-scale_100_100/B56aAchMYkGcAY-/0/1787184860290?e=1790812800&v=beta&t=3fmVXip1Iljd8fLpNLQWjFayWfp_TE55ASsf7QQFnhQ)
    
    
    
    ](https://www.linkedin.com/in/addyosmani?miniProfileUrn=urn%3Ali%3Afsd_profile%3AACoAAAGXfeABZZsHYLPYGlkS7eoFikrNAYkiEHg)
    
    [Addy Osmani • FollowingMember of Technical Staff at Anthropic](https://www.linkedin.com/in/addyosmani?miniProfileUrn=urn%3Ali%3Afsd_profile%3AACoAAAGXfeABZZsHYLPYGlkS7eoFikrNAYkiEHg)1d •
    
    Tip: Claude Code has several skill-cleanup commands. Each answers a different question.  
      
    /skill-doctor → which skills you use  
    /skills, then t → what each costs  
    /doctor → fixes setup + [CLAUDE.md](http://claude.md/) debt  
    /context → what's in the window now  
    /usage → what burns your limits  
      
    1 /skill-doctor: which skills are worth keeping?  
      
    Every skill in the listing costs tokens. This shows what each one costs and how often it has fired, and flags the ones never invoked at all. In an interactive session the report opens in the /plugin manager's Stats tab. With -p it prints as text.  
      
    2 /skills: where you act on that report  
      
    The report tells you what's dead weight. This is where you cut it. Highlight a skill, press Space to cycle its state (on, name-only, user-only, off), Esc to save. It writes skillOverrides into .claude/settings.local.json, so you never have to edit a [SKILL.md](http://skill.md/) someone else maintains.  
      
    3 /doctor: is the setup itself healthy?  
      
    It finds problems and you press f to have Claude fix them, confirming before it changes anything. Covers version and auto-updater state, auth and connectivity, PATH and leftover installs, unparseable settings files, and [CLAUDE.md](http://claude.md/) debt: de-duping your personal file against the project one, splitting an overgrown root file into nested files and skills.  
      
    4 /context: what's in the window right now?  
      
    A snapshot of the live session rather than a standing audit. Worth knowing: the Skills row reports the listing size after the budget is applied, so it matches what the model actually receives, not what's sitting on disk.  
      
    5 /usage: what's burning your limits?  
      
    Session and weekly consumption against your plan. /cost is an alias for it now.  
      
    Hopefully helpful to a few folks :)  
      
    [hashtag#ai](https://www.linkedin.com/search/results/all/?keywords=%23ai&origin=HASH_TAG_FROM_FEED) [hashtag#programming](https://www.linkedin.com/search/results/all/?keywords=%23programming&origin=HASH_TAG_FROM_FEED) [hashtag#softwareengineering](https://www.linkedin.com/search/results/all/?keywords=%23softwareengineering&origin=HASH_TAG_FROM_FEED)
    
    …more
    
    Activate to view larger image,
    
    ![text](https://media.licdn.com/dms/image/v2/D5622AQH85FH2QVaETg/feedshare-shrink_800/B56aChCLyJIIAc-/0/1789408099810?e=1790812800&v=beta&t=kq5o5VvCsRcsqcuaaAGYj5628ti5bPa1NnTEM_JPDpE)
    
    Activate to view larger image,
    
    - ![like](https://static.licdn.com/aero-v1/sc/h/emei2gdl9ikg7penkh9ij9llx)![insightful](https://static.licdn.com/aero-v1/sc/h/3bhtnif60blspoiyhoex4lfx)![love](https://static.licdn.com/aero-v1/sc/h/esahr356vrv0vklww6hcjar1j)725
    - - 37 comments
        - 50 reposts
    
    Like
    
    Comment
    
    Repost
    
    Send
    
- ## Feed post number 3
    
    [](https://www.linkedin.com/in/addyosmani?miniProfileUrn=urn%3Ali%3Afsd_profile%3AACoAAAGXfeABZZsHYLPYGlkS7eoFikrNAYkiEHg)


View Addy Osmani’s graphic link

Addy Osmani

• Following

Member of Technical Staff at Anthropic

14h •

  

At Anthropic, Claude now writes 80% of our code. Engineers ship 8x more code per quarter. Side effect: Tests grew 10x. CI jobs up 25x in 6 months. Here's what helped us scale:

  

https://lnkd.in/gjs9d8_e

  

Lines of code isn't (of course) a direct measure of value. That's why these numbers matter less as a productivity flex and more as a systems warning. Writing code is no longer the constraint. Claude also reviews and helps approve PRs, so changes get smaller and more frequent.

  

Tests grew 10x while headcount barely moved. Result: CI jobs up 25x in 6 months. The quality bar didn't change: named human owner on every PR, required approval, same CI gates. What changed is volume through those gates.

  

That's why we had to rebuild test impact analysis. Agents can't just dump diffs. They need a deterministic set of relevant tests so they can self-verify and iterate. A 20-minute lag in that service meant tens of thousands of test updates not applied - missed regressions, flaky blockers, or tests that should have run and didn't.

  

Three patches bought us 70 days, then 29, then less than a day. The rewrite took one engineer three weeks. A year ago that would have been closer to a quarter. After cutover, the job-result backlog went flat. So generated code isn't the metric. The metric is whether review, tests, and CI can absorb the new rate of change without letting bad diffs through.

  

Codegen just moved the bottleneck downstream.

  

hashtag#ai hashtag#programming hashtag#softwareengineering

…more

Activate to view larger image,

diagram

Activate to view larger image,

likeinsightfullove

1,919

148 comments

128 reposts

  

Like

  

Comment

  

Repost

  

Send

Feed post number 2

View Addy Osmani’s graphic link

Addy Osmani

• Following

Member of Technical Staff at Anthropic

1d •

  

Tip: Claude Code has several skill-cleanup commands. Each answers a different question.

  

/skill-doctor → which skills you use

/skills, then t → what each costs

/doctor → fixes setup + CLAUDE.md debt

/context → what's in the window now

/usage → what burns your limits

  

1 /skill-doctor: which skills are worth keeping?

Every skill in the listing costs tokens. This shows what each one costs and how often it has fired, and flags the ones never invoked at all. In an interactive session the report opens in the /plugin manager's Stats tab. With -p it prints as text.

2 /skills: where you act on that report

The report tells you what's dead weight. This is where you cut it. Highlight a skill, press Space to cycle its state (on, name-only, user-only, off), Esc to save. It writes skillOverrides into .claude/settings.local.json, so you never have to edit a SKILL.md someone else maintains.

3 /doctor: is the setup itself healthy?

It finds problems and you press f to have Claude fix them, confirming before it changes anything. Covers version and auto-updater state, auth and connectivity, PATH and leftover installs, unparseable settings files, and CLAUDE.md debt: de-duping your personal file against the project one, splitting an overgrown root file into nested files and skills.

4 /context: what's in the window right now?

A snapshot of the live session rather than a standing audit. Worth knowing: the Skills row reports the listing size after the budget is applied, so it matches what the model actually receives, not what's sitting on disk.

5 /usage: what's burning your limits?

Session and weekly consumption against your plan. /cost is an alias for it now.

  

Hopefully helpful to a few folks :)

  

hashtag#ai hashtag#programming hashtag#softwareengineering

…more

Activate to view larger image,

text

Activate to view larger image,

likeinsightfullove

725

37 comments

50 reposts

  

Like

  

Comment

  

Repost

  

Send

Feed post number 3

  

  

Comment

  

Repost

  

Send

Feed post number 3

View Addy Osmani’s graphic link

Addy Osmani

• Following

Member of Technical Staff at Anthropic

4d •

  

Excited to announce my next book with O'Reilly: Agentic Engineering!

  

I officially submitted the manuscript a few weeks ago and while the final edition arrives in early 2027, we aren't waiting to share it. We're releasing chapters progressively starting now while my editors and I continue refining the work as practices evolve.

  

Check them out early if you'd like: https://lnkd.in/gymp3B7E

  

For the last six months, I've been writing almost continuously about the changes happening around agentic engineering: loops, goals, context engineering, harnesses, verification, specs, autonomy, software factories and what all of this means for the job of being an engineer.

  

Those posts have sometimes felt like looking at different pieces of the same puzzle. The book gave me the space to put the puzzle together.

  

There's now a much clearer through line in my head for where I think software engineering is going, what changes when agents can take on increasingly large pieces of work and which parts of engineering become more important as a result.

  

One thing writing it has forced me to do is spend a lot more time on the bleeding edge.

Not just trying the latest tools, but actually attempting to work differently. Delegating larger tasks. Building harnesses. Finding the limits of context. Learning what needs to be specified. Figuring out what can safely become autonomous and what absolutely still needs human judgment.

  

My views have changed quite a bit in the process.

And they'll probably keep changing.

  

I like the idea that this book can evolve alongside the field it's trying to describe. By the time the finished book arrives in 2027, I think many workflows that still feel experimental today are going to feel surprisingly ordinary.

  

My hope is that Agentic Engineering helps people get there a little sooner - and more importantly, gives them a framework for navigating everything that comes after.

  

Thank you to everyone at O'Reilly and to the many people who have challenged, sharpened, or contributed to these ideas.

  

I can't wait to share more.

  

hashtag#ai hashtag#programming hashtag#softwareengineering

…more

Activate to view larger image,

View image

Activate to view larger image,

likecelebratelove

5,355

160 comments

91 reposts

  

Like

  

Comment

  

Repost

  

Send

Feed post number 4

View Addy Osmani’s graphic link

Addy Osmani

• Following

Member of Technical Staff at Anthropic

1w •

  

I've joined Anthropic!

  

I'll be working on Claude Code and on making it better for developers who use it. Hit me up with your feedback any time.

  

Had a little fun creating this game with Fable and Three.js :)

  

hashtag#ai hashtag#programming hashtag#softwareengineering

…more

likecelebratelove

14,616

630 comments

60 reposts

  

Like

  

Comment

  

Repost

  

Send

Feed post number 5

View Addy Osmani’s graphic link

Addy Osmani

• Following

Member of Technical Staff at Anthropic

1w •

  

How I do code reviews these days: more code = more selective human review i.e. don't read all the code.

  

1. Every PR gets a multi-agent first pass. It should find bugs, verify them, rank by severity, suggest fixes. Approval stays a human call on anything that matters.

  

2. Low blast radius changes on less sensitive code (there's often a lot!) can skip a deep human review once that review is clean. This helps keep the explosion of PRs manageable.

  

3. Core / sensitive paths still need an owner and human sign-off. That's where you spend time: verification, constraints and earning trust in what the agents can safely cover. You want to keep recoverability.

  

Agents do the first pass and humans cover blast radius.

  

Great question from Gergely Orosz!

  

hashtag#ai hashtag#programming hashtag#softwareengineering

…more

Activate to view larger image,

graphical user interface, text, application, chat or text message

Activate to view larger image,

likeinsightfullove

951

Maksim Koutun and 950 others

164 comments

59 reposts

  

Like

  

Comment

  

Repost

  

Send

Feed post number 6

View Addy Osmani’s graphic link

Addy Osmani

• Following

Member of Technical Staff at Anthropic

1w •

  

The four kinds of loops in loop engineering.

  

I run a few of these every day and what strikes me is how far apart people are on this right now. Some of you are designing full software factories with queues and triggers. Others are still driving every single turn by hand. Both are super reasonable places to be.

  

The taxonomy the Claude Code team published is useful either way and mostly applies even if you're using Codex or another coding harness.

  

A loop is an agent repeating cycles of work until a stop condition is met. There are four kinds, and they form a ladder. Each rung is you handing over one more thing.

  

→ Turn-based. You hand off the check. Every prompt you send is already one: it gathers context, acts, checks its work, repeats. It stops when Claude thinks it's done or needs you. The lever here is verification. Write down how you'd check the work yourself and save it as a skill markdown file, so it can grade itself before handing anything back.

  

→ Goal-based. You hand off the stop condition. "/goal get the homepage Lighthouse score to 90 or above, stop after 5 tries." Each time Claude tries to quit, a separate evaluator model reads your condition and sends it back to work. That's why deterministic criteria beat vibes: tests passed, a score cleared, a p95 under a number.

  

→ Time-based. You hand off the trigger. "/loop 5m check my PR, address review comments, and fix failing CI." /loop runs on your machine, so closing it stops it, while /schedule moves the routine to the cloud. For example, a loop checks the Agent Skills repo for new issues and hands me a summary, instead of me working through the queue by hand.

  

→ Proactive. You hand off the prompt. An event or a schedule starts it, nobody is watching in real time, and the routine runs until you turn it off. Bug triage, migrations, dependency upgrades.

  

If you're near the bottom of the ladder, the thing worth knowing is that more autonomy isn't the upgrade. The check is. Every rung above turn-based inherits whatever verification you wrote, so a loop with a weak check just produces work you can't trust, faster.

  

If you're building toward a factory, the same point runs the other way. These rungs nest rather than replace each other. A proactive routine is a schedule wrapped around a goal wrapped around a check. Get the innermost one wrong and scale multiplies it.

  

Two bits of discipline that apply at every rung. Use a second agent with fresh context for review, because it isn't biased by the first one's reasoning. And watch the meter: plenty of tasks don't need a loop at all, and dynamic workflows can spawn hundreds of agents, so pilot on a slice before a big run.

  

The question is the same wherever you are. Which piece could you hand over next, and can you say precisely what done looks like once you have?

  

#ai #programming #softwareengineering

…more

Your document has finished loading

likeinsightfullove

574

56 comments

47 reposts

  

Like

  

Comment

  

Repost

  

Send

Feed post number 7

View Addy Osmani’s graphic link

Addy Osmani

• Following

Member of Technical Staff at Anthropic

1w •

  

The official documentary for VS Code is out! 🎬

  

Check out the full documentary: https://lnkd.in/gpefQjm4 free to watch on YouTube

  

"The Story of VS Code" beautifully captures what Erich Gamma called an overnight success 10 years in the making. It’s incredible to reflect on this journey - from a small team in Zurich building online tools under the name Monaco to establishing massive open protocols like LSP, to fundamentally changing how we think about code editors in the age of AI and agentic engineering.

  

The evolution of developer tooling has always been a space I care deeply about, and watching this ecosystem grow to support developers wherever they are has been incredibly inspiring. Before we started to switch to agent harnesses, code editors were where we spent all of our time and it's been so interesting to see VS Code evolve to meet the agentic coding moment too.

  

I was so happy to take part in this when filming started a few years ago. A massive congratulations to Stefan Kingham, who directed and produced it, as well as the entire VS Code team and the extended community of contributors for their tremendous work on this release and the editor itself.

  

If you're interested in the history of developer environments, the shift to AI-assisted development or just a great engineering story, I highly recommend giving it a watch.

  

hashtag#programming hashtag#softwareengineering

…more

  

Play

Remaining time

1:28

1x

  

Playback speed

  

Turn closed captions on

  

Unmute

  

Turn fullscreen on

likelovecelebrate

405

23 comments

27 reposts

  

Like

  

Comment

  

Repost

  

Send

Feed post number 8

View Addy Osmani’s graphic link

Addy Osmani

• Following

Member of Technical Staff at Anthropic

1w •

  

"The most important skill in prompting is expertise in the domain you’re prompting for"

  

https://lnkd.in/gPJXQSzt

  

Sometimes the human is the bottleneck. A good reminder LLMs are a force multiplier if you're skilled and to build this domain expertise if you don't have it yet.

  

hashtag#programming hashtag#softwareengineering hashtag#ai

…more

Activate to view larger image,

text

Activate to view larger image,

likeinsightfullove

401

43 comments

32 reposts

  

Like

  

Comment

  

Repost

  

Send

Feed post number 9

Addy’s profile photo

Addy Osmani reposted this

  

View Addy Osmani’s graphic link

Addy Osmani

• Following

Member of Technical Staff at Anthropic

2w •

Here's my agentic code-review skill for Claude Code, Codex & friends

  

I've been iterating on the code review skill in my Agent Skills pack and it transforms the /review process by doing four specific things: 1. reviews on five quality axes, 2. labels findings by severity, 3. orders finding by what changes outcomes and 4. proposes the moves to address the review.

  

Try it out in about 30 seconds: 🔗 https://lnkd.in/gmf3uZ7t

  

npx skills add addyosmani/agent-skills --skill code-review-and-quality

(Want the whole lifecycle pack instead? Spec through ship, just drop the --skill flag).

  

Reviews on five axes: Correctness, readability, architecture, security, and performance. Most automated reviews collapse to "do the tests pass?" Tests are necessary, but they don't catch a leaking module boundary.

  

Labels every finding by severity: "Critical" blocks the merge. No prefix means required. "Nit" and "FYI" are optional. This stops authors from treating every comment as mandatory and burning an afternoon on formatting preferences.

  

Leads with leverage: If there is one structural problem and ten nits, the structural problem is the review. Findings are ordered by what actually changes the outcome.

  

Proposes the move: Saying "This is complex" leaves the author guessing. Saying "Replace this conditional chain with a dispatcher" is a review they can act on.

  

The review is your quality gate. It is worth telling your agent what a good one looks like. Run /review before you merge.

  

If you don't end up using it or there's another code-review skill out there you like better, that's totally cool. I hope this proves useful to someone out there.

  

hashtag#ai hashtag#programming hashtag#softwareengineering

…more

Activate to view larger image,

View image

Activate to view larger image,

likeinsightfulcelebrate

1,480

89 comments

92 reposts

  

Like

  

Comment

  

Repost

  

Send

Feed post number 10

View Addy Osmani’s graphic link

Addy Osmani

• Following

Member of Technical Staff at Anthropic

1w •

  

AI can build the feature, but it won't teach you the lesson unless you force it to.

  

My latest free write-up on expertise: https://lnkd.in/gerVNkGb ✏️

  

Early in my career, I built my engineering intuition by spending thousands of hours debugging failures, reading diffs, and wrestling with abstractions. Today, AI agents can short-circuit that entire journey. You get the completed task, but you miss the reps.

  

If we treat agents/loops/software factories purely as code vending machines, we risk severe skill decay. We might become incredibly fast at prompting, but lose the deep expertise required to actually verify the output when assumptions no longer fit the system.

Verification is the floor. Imagination is the ceiling.

  

To stay sharp and build mastery deliberately, here is how I keep myself in the loop:

Form a hypothesis first: Before prompting, predict what the solution should look like or where an architecture might fail.

  

Anchor on explanation: Instead of just generating net-new features, actively use agents to analyze and explain existing codebases. Forcing the AI to break down complex, pre-existing logic helps build your mental model much faster than just asking it to "write this."

  

Codify the lessons: Don't let your learnings die when the chat window closes. Turn corrected assumptions into linting rules, documentation, or tests in your repo so both you and the next agent can benefit from them.

  

I hope the article is a helpful read and helps unpack how we can keep our mental models sharp while still aggressively leveraging AI.

  

hashtag#ai hashtag#programming hashtag#softwareengineering

…more

Activate to view larger image,

View image

Activate to view larger image,

likeinsightfulcelebrate

369

42 comments

28 reposts

  

Like

  

Comment

  

Repost

  

Send

Feed post number 11

View Addy Osmani’s graphic link

Addy Osmani

• Following

Member of Technical Staff at Anthropic

2w •

  

"Don't paste the AI, please. The world is full of people who don't want to read or think things through. Don't be one of them."

  

https://dontpastetheai.com

  

This resonated. When folks ask for your perspective, they aren't looking for a generic AI summary - they often want your judgment, your context and your hard-earned taste. This is especially true when many of us have access to the same models. Submitting unvetted AI text reduces you to a 'meat proxy' acting as a human middleware layer for an AI harness.

  

Above all, adopt a simple rule of ownership: if your name's on the message, you are responsible for its validity and it should reflect a level of understanding you can defend and feel good about.

  

hashtag#programming hashtag#softwareengineering hashtag#ai

…more

Activate to view larger image,

text, letter

Activate to view larger image,

likelovesupport

886

82 comments

83 reposts

  

Like

  

Comment

  

Repost

  

Send

Feed post number 12

Addy’s profile photo

Addy Osmani reposted this

  

View Addy Osmani’s graphic link

Addy Osmani

• Following

Member of Technical Staff at Anthropic

2w • Edited •

Introducing Clarity - a free Agent skill and Editor for improving the quality of your writing while keeping the human in the loop

  

I'm excited to share Clarity (https://clarity.addy.ie) - an open-source AI agent skill and writing editor to help you draft, rewrite and review prose without losing your authentic voice. It's a one-liner to get started:

  

npx skills add addyosmani/clarity

  

Like many of you, I've found it so easy for writing to drift into robotic, predictable patterns as we try figuring out the best way to incorporate AI as a tool in our workflow. Clarity comes with 18 time-tested writing rules for ensuring your writing is sharp, true to your personal style and actively flags common AI-generated "tells". It's a combination of skill ideas I've been using over the last few months and has been built with evals and quality in mind.

  

Clarity is built around three core commands:

  

Interview: A co-writing feature that helps extract context to build drafts from the ground up.

  

Rewrite: A refinement engine that polishes your existing text while preserving your unique tone.

  

Review: An editor that reviews your work for substance and specifically checks for robotic, AI-sounding phrasing.

  

Because our tools need to live where we actually do our work, I designed Clarity to integrate where you already work, including a browser-based editor, Claude Code and Codex. It also works with most other agents that support agent skills. You can read more about the approach, check out the editor, skill or tutorials on the site.

  

If you are looking for an AI writing partner that prioritizes clear, human substance over fluff, I'd love for you to give it a try. It is fully open-source and ready to use.

  

hashtag#programming hashtag#softwareengineering hashtag#ai

…more

  

Play

Remaining time

1:05

1x

  

Playback speed

  

Turn closed captions on

  

Unmute

  

Turn fullscreen on

likeloveinsightful

941

61 comments

51 reposts

  

Like

  

Comment

  

Repost

  

Send

Feed post number 13

View Addy Osmani’s graphic link

Addy Osmani

• Following

Member of Technical Staff at Anthropic

2w •

  

The cost of AI software development: blank checks or smart routing? How are folks managing their token bills.

  

Databricks just published a breakdown on how companies are managing AI coding costs at scale. Their goal is to give developers frictionless access to AI without the runaway enterprise spend: https://lnkd.in/gzrFaAng ✏️

  

Here is their playbook for managing costs:

  

1️⃣ Ride the "Efficiency frontier": Don't default to the most expensive frontier model for every prompt. Continually evaluate and shift to cheaper or open-source models that meet the quality bar for 90% of everyday coding tasks.

  

2️⃣ Dynamic routing: Don't rely on devs to manually pick the right model. Use a "meta-harness" to automatically route simple tasks to cheap models, saving the expensive heavy-hitters for complex logic.

  

3️⃣ Friction vs. Hard limits: Hard token budgets actually punish your most productive engineers. Instead, give them real-time spend visibility and soft "tripwire" approvals as spend increases.

  

🔥 But over on Hacker News, the developer reality-check told a different story...

  

Devs with "unlimited" AI budgets pushed back, admitting to burning $80+ a day on top-tier models (like Fable/Opus/Sol). Their argument is if spending $80/day gives one developer the output of 3-4 engineers, the ROI is a massive no-brainer. To them, building complex routing infrastructure isn't worth the engineering time.

  

I think there’s still so much to learn here. Check the article out it’s a good read.

  

hashtag#programming hashtag#softwareengineering hashtag#ai

…more

Activate to view larger image,

View image

Activate to view larger image,

likeinsightfullove

136

28 comments

4 reposts

  

Like

  

Comment

  

Repost

  

Send

Feed post number 14

View Addy Osmani’s graphic link

Addy Osmani

• Following

Member of Technical Staff at Anthropic

2w •

  

Find agent failures in seconds with a nice unified view of every LLM call, tool invocation and downstream trace.

  

An AI agent fails in production. The model call looks fine. The API call looks fine. Something in between went wrong - and most tools only see one layer, so you end up stitching trace IDs together by hand while an incident burns.

  

I recorded a short walkthrough of Honeycomb's Agent Timeline + Canvas, which is built for exactly this. It's available for free right now if you want to try it:

  

https://fandf.co/4qkir39

  

It renders a whole multi-agent conversation as one view - model calls, tool calls, agent handoffs - with the failures already marked in red before you go looking. In the video I follow one failing conversation down to the actual root cause: a tool call to create an incident, and underneath it a 502 from the tickets service.

  

Two things stood out. You can also just ask in plain language - I typed "where are the errors coming from" and Honeycomb's Canvas went and investigated on its own, landing on that same 502. And all of it is built on the OpenTelemetry GenAI Semantic Conventions - so you instrument once against an open standard, with no proprietary SDK, and the timeline lights up automatically. Your telemetry stays portable.

  

In partnership with honeycomb.io hashtag#ad

  

hashtag#programming hashtag#softwareengineering

…more

  

Play

Remaining time

2:14

1x

  

Playback speed

  

Turn closed captions on

  

Unmute

  

Turn fullscreen on

likeloveinsightful

118

5 comments

6 reposts

  

Like

  

Comment

  

Repost

  

Send

Feed post number 15

View Addy Osmani’s graphic link

Addy Osmani

• Following

Member of Technical Staff at Anthropic

2w • Edited •

  

Introducing Clarity - a free Agent skill and Editor for improving the quality of your writing while keeping the human in the loop

  

I'm excited to share Clarity (https://clarity.addy.ie) - an open-source AI agent skill and writing editor to help you draft, rewrite and review prose without losing your authentic voice. It's a one-liner to get started:

  

npx skills add addyosmani/clarity

  

Like many of you, I've found it so easy for writing to drift into robotic, predictable patterns as we try figuring out the best way to incorporate AI as a tool in our workflow. Clarity comes with 18 time-tested writing rules for ensuring your writing is sharp, true to your personal style and actively flags common AI-generated "tells". It's a combination of skill ideas I've been using over the last few months and has been built with evals and quality in mind.

  

Clarity is built around three core commands:

  

Interview: A co-writing feature that helps extract context to build drafts from the ground up.

  

Rewrite: A refinement engine that polishes your existing text while preserving your unique tone.

  

Review: An editor that reviews your work for substance and specifically checks for robotic, AI-sounding phrasing.

  

Because our tools need to live where we actually do our work, I designed Clarity to integrate where you already work, including a browser-based editor, Claude Code and Codex. It also works with most other agents that support agent skills. You can read more about the approach, check out the editor, skill or tutorials on the site.

  

If you are looking for an AI writing partner that prioritizes clear, human substance over fluff, I'd love for you to give it a try. It is fully open-source and ready to use.

  

hashtag#programming hashtag#softwareengineering hashtag#ai

…more

  

Play

Remaining time

1:06

1x

  

Playback speed

  

Turn closed captions on

  

Unmute

  

Turn fullscreen on

likeloveinsightful

941

61 comments

51 reposts

  

Like

  

Comment

  

Repost

  

Send

Feed post number 16

View Addy Osmani’s graphic link

Addy Osmani

• Following

Member of Technical Staff at Anthropic

2w •

  

Thoughts on the "end" of programming and what comes after

  

Check out the article: https://lnkd.in/g38ac3Ti

  

Paul Dix just published an interesting read called "The End of Programming" detailing how frontier models and multi-agent orchestration frameworks have fundamentally changing the craft of software development. It compliments some of the thinking on loops, factories and quality constraints a few of us have been writing about this year.

  

My favorite excerpt from the piece captures this transition:

  

"Organizational inertia will likely mean that there’s another decade of humans writing code by hand and having their colleagues review every line of it. Many, if not most, companies will continue to develop software as they have before.

  

But the most productive software creators will be doing it without programming in any traditional sense. They’ll be directing AIs, creating harnesses, and software factories, and QA and verification systems that ship working software faster than we’ve ever seen before."

  

So it's not quite the end, but this deeply resonates with the operational frameworks of loop engineering. The primary bottleneck is no longer code generation but it is going to be codebase-scale verification.

  

As we offload the heavy lifting of writing net-new code to agents, a developer's highest-leverage work shifts to building the tooling necessary to analyze, explain and verify pre-existing codebases so that AI outputs can be integrated safely at scale.

  

hashtag#ai hashtag#programming hashtag#softwareengineering

…more

Activate to view larger image,

table

Activate to view larger image,

likeinsightfullove

359

60 comments

20 reposts

  

Like

  

Comment

  

Repost

  

Send

Feed post number 17

View Addy Osmani’s graphic link

Addy Osmani

• Following

Member of Technical Staff at Anthropic

2w •

  

Agent Skills just crossed 90,000 stars and 600K recent installs!

  

First, a big thank you. If you've checked out Agent Skills and its helped with your agentic engineering workflow in Claude/Codex/Copilot or other tools, I'm happy to hear that. We wanted to help you with a human-in-the-loop skill pack for each part of the SDLC from idea to production. I'm glad it's resonated. If you want to check it out:

  

Run `npx skills add addyosmani/agent-skills` or take a look through: https://lnkd.in/gqFGTYUK ( ⭐ stars always welcome)

  

In the last month, we've improved the underlying skills a lot with regular releases (with evals!), new tutorials, teaching materials, open-source stickers (I've already seen folks in different countries get them printed) and clarity about how to use each skill.

  

Next up, we want to be even more token-efficient. As labs and educators remind folks about the importance of auditing what skills you use and their costs to your context window, we want to ensure we're delivering value with minimal token waste in mind.

  

Thanks for joining us on this journey and looking forward to further improvements!

  

hashtag#programming hashtag#softwareengineering hashtag#ai

…more

Activate to view larger image,

View image

Activate to view larger image,

likelovecelebrate

418

43 comments

10 reposts

  

Like

  

Comment

  

Repost

  

Send

Feed post number 18

View Addy Osmani’s graphic link

Addy Osmani

• Following

Member of Technical Staff at Anthropic

2w •

  

Audit your agent files to keep your agentic coding setup effective - skills, AGENTS.md, MCPs, plugins, the environment - all of it.

  

My latest write-up: https://lnkd.in/gnseEbNp ✏️

  

Your coding agent's configuration has a half-life. Models improve, harnesses add capabilities, and the instructions we wrote for an older version often stay behind, dragging down performance and wasting tokens.

  

As I've spent time exploring the operational limits of multi-agent orchestration frameworks and agentic engineering, a recurring failure mode stands out: configuration rot.

  

We instinctively keep adding skills, add rules to CLAUDE.md or AGENTS.md every time an agent makes a mistake. Over time, these files balloon, adherence drops and we accidentally turn a short decision guide into a sprawling, unmanageable knowledge base.

  

If you are relying on coding agents for daily workflows, check out the write-up on how to maintain rigorous skill hygiene. I personally discovered so many skills and instructions I had completely forgot I added. I've talked to folks who had dozens they've removed after they audited their setups.

  

Every instruction in your environment needs to earn its place again. I put together a practical guide on how to audit your setup and figure out what your coding agent actually still needs.

  

hashtag#programming hashtag#softwareengineering hashtag#ai

…more

Activate to view larger image,

View image

Activate to view larger image,

likeinsightfulcelebrate

392

Maksim Koutun and 391 others

46 comments

35 reposts

  

Like

  

Comment

  

Repost

  

Send

Feed post number 19

View Addy Osmani’s graphic link

Addy Osmani

• Following

Member of Technical Staff at Anthropic

2w •

  

Here's my agentic code-review skill for Claude Code, Codex & friends

  

I've been iterating on the code review skill in my Agent Skills pack and it transforms the /review process by doing four specific things: 1. reviews on five quality axes, 2. labels findings by severity, 3. orders finding by what changes outcomes and 4. proposes the moves to address the review.

  

Try it out in about 30 seconds: 🔗 https://lnkd.in/gmf3uZ7t

  

npx skills add addyosmani/agent-skills --skill code-review-and-quality

(Want the whole lifecycle pack instead? Spec through ship, just drop the --skill flag).

  

Reviews on five axes: Correctness, readability, architecture, security, and performance. Most automated reviews collapse to "do the tests pass?" Tests are necessary, but they don't catch a leaking module boundary.

  

Labels every finding by severity: "Critical" blocks the merge. No prefix means required. "Nit" and "FYI" are optional. This stops authors from treating every comment as mandatory and burning an afternoon on formatting preferences.

  

Leads with leverage: If there is one structural problem and ten nits, the structural problem is the review. Findings are ordered by what actually changes the outcome.

  

Proposes the move: Saying "This is complex" leaves the author guessing. Saying "Replace this conditional chain with a dispatcher" is a review they can act on.

  

The review is your quality gate. It is worth telling your agent what a good one looks like. Run /review before you merge.

  

If you don't end up using it or there's another code-review skill out there you like better, that's totally cool. I hope this proves useful to someone out there.

  

hashtag#ai hashtag#programming hashtag#softwareengineering

…more

Activate to view larger image,

View image

Activate to view larger image,

likeinsightfulcelebrate

1,480

89 comments

92 reposts

  

Like

  

Comment

  

Repost

  

Send

Feed post number 20

View Addy Osmani’s graphic link

Addy Osmani

• Following

Member of Technical Staff at Anthropic

2w •

  

Your AI bill isn't a model problem - it's a caching problem. Here's a way to save on your bill.

  

The fastest way to cut your AI token bill isn't a cheaper model - it's not paying twice for the same answer. Users and agents ask the same things, just phrased differently, and you pay full price to regenerate a response you already have. (Agents make it worse: they can burn roughly 4x the tokens of a normal chat as they loop and re-ask.)

  

Worth a look if token cost is on your radar → https://fandf.co/4wrga7T

  

Redis built a managed fix for exactly this: LangCache. It's a semantic caching layer that sits between your app and the model - it matches a new request to a semantically similar one you've already answered and serves the cached response in milliseconds, calling the LLM only on a real miss. They cite up to 90% lower API costs and multiples-faster responses.

  

It's an old, boring idea - caching - applied to a new and very expensive layer. Because it matches by meaning rather than exact text, "what's your refund policy?" and "how do I get my money back?" resolve to the same cached answer. In high-repetition workloads, a ~70% cache hit rate maps almost directly to ~70% of that spend saved.

  

If you own an AI P&L, this is one of the highest-leverage, least-glamorous levers you have: stop paying twice for the same answer.

  

Sponsored by Redis. hashtag#ad

  

hashtag#ai hashtag#programming hashtag#softwareengineering

…more

  

Play

Remaining time

2:43

1x

  

Playback speed

  

Turn closed captions on

  

Unmute

  

Turn fullscreen on

likeinsightfullove

546

38 comments

40 reposts

  

Like

  

Comment

  

Repost

  

Send

Feed post number 21

View Addy Osmani’s graphic link

Addy Osmani

• Following

Member of Technical Staff at Anthropic

2w •

  

Friction is what builds taste and mastery. The tools that remove it also remove what made us good enough to use them well.

  

Worth reading if you're leading teams or are an early-career engineer: https://lnkd.in/gdM8_8ba by Lars Faye

  

This piece is an interesting read on one of the tensions in our industry right now. As AI tools abstract away the mechanical struggles of coding, they also have this side-effect of removing the where our mental models actually get forced.

  

Expertise isn't just about producing working code. It's the intuition you earn through hours of trying to figure out why a system is broken. It is the architectural "taste" you develop by making bad design choices and feeling their consequences a year later.

  

For engineers entering the industry today, this is the trap: it is increasingly super easy to achieve senior-level looking output without senior-level understanding. But when the abstraction leaks, when the agent gets stuck in a loop, or when the underlying architecture needs to scale, you need that foundational depth to step in and orchestrate a fix.

  

As engineering leaders, our challenge isn't just adopting AI to move faster. It's figuring out how to build intentional friction back into the growth path of our teams. We have to foster environments where developers aren't just accepting generated code, but actively dissecting, verifying and critiquing it.

  

Happy to see folks writing about this!

  

hashtag#ai hashtag#programming hashtag#softwareengineering

…more

Activate to view larger image,

text

Activate to view larger image,

likeloveinsightful

303

50 comments

27 reposts

  

Like

  

Comment

  

Repost

  

Send

Feed post number 22

View Addy Osmani’s graphic link

Addy Osmani

• Following

Member of Technical Staff at Anthropic

3w •

  

Ever wonder why it's so hard to stop scrolling through TikTok, Reels, or Shorts? Your brain's "stop" button literally goes offline.

  

A fascinating new neuroscience study (published in NeuroImage) just revealed exactly what happens to our cognitive control when we fall down the short-form video rabbit hole. It turns out, it's not just a lack of willpower - it's a neurobiological hijacking.

  

Check out the paper: https://lnkd.in/gPPkvS_U

  

Here is what the researchers found:

  

📉 Your self-regulation shuts down: When watching videos you like, two critical brain regions responsible for cognitive control and decision-making - the dACC and the dlPFC - show strong deactivation. Your biological brakes are disabled.

  

🧟 Even bad videos keep you hooked: When a video you dislike pops up, your dACC returns to normal baseline levels, but your dlPFC remains suppressed. Your brain realizes it doesn't like the content, but the higher-level planning required to put the phone down is still offline.

  

🧪 The Glutamate Factor: The researchers found a chemical link to this behavior. People with higher resting levels of glutamate in the dACC experienced less suppression in their cognitive control regions. In short: more baseline glutamate equals a stronger ability to resist the scroll.

  

🔗 A locked-in feedback loop: The connection and communication between the dACC and dlPFC actually increases during video viewing, peaking when watching liked videos. Your brain gets locked into the viewing loop, even while the control centers are powered down.

  

(For context, the primary visual cortex remained consistently active regardless of whether the video was liked or disliked, proving this effect is specific to our cognitive control centers, not just visual processing).

  

The next time you tell yourself you are "just going to watch 5 minutes of Reels" remember that the platform is designed to systematically disable the exact brain regions you need to enforce that 5-minute limit.

…more

Activate to view larger image,

graphical user interface, text, application

Activate to view larger image,

likeinsightfulcelebrate

611

22 comments

91 reposts

  

Like

  

Comment

  

Repost

  

Send

Feed post number 23

View Addy Osmani’s graphic link

Addy Osmani

• Following

Member of Technical Staff at Anthropic

3w •

  

"How do you find the problems to solve as a Staff+ Engineer?"

  

Stare at a blank document until "strategy" happens? Perhaps not... :)

  

Here's a great read on what to do: https://lnkd.in/gg9nWpYc

  

Lalit Maganti recently wrote a fantastic piece on how he finds problems to solve as a Staff Engineer. Making the jump isn't just about solving harder problems. It's about figuring out which ones are worth solving. But how do you find them?

  

Here is the counter-intuitive playbook for finding high-impact work:

  

🧽 Act like a sponge: You don't need speculative brainstorming meetings. Just listen to the ambient noise. What are teams complaining about? What messy workarounds are they building to do their jobs? Take note over time.

  

🛑 Absorb problems: When a user asks for a feature, they are proposing a localized solution. Keep digging into their workflow until you uncover the root constraint. While agents make implementation cheaper, we still want to look for the "right" problems to solve.

  

⏳ Let problems accumulate: This is the hardest one. If you jump on the very first request, you might over-engineer a one-off feature. If you wait and let problems pile up, you'll start to see the "common shape" across multiple teams and can build a systemic, unified solution.

  

Lalit notes his approach relies on having bottom-up autonomy.

  

So, what do you do if you want to operate at a Staff level in a top-down culture?

  

You have to pressure-test the roadmap. Even if you are handed a strict top-down initiative, you can still act like a sponge during the design phase. Interview the downstream teams, validate if the "required" feature actually solves their root issue, and don't be afraid to push back with a more elegant before committing to that direction.

  

hashtag#programming hashtag#softwareengineering hashtag#careers

…more

Activate to view larger image,

text

Activate to view larger image,

likeinsightfullove

945

Valery Leontyev and 944 others

65 comments

71 reposts

  

Like

  

Comment

  

Repost

  

Send

Feed post number 24

Addy’s profile photo

Addy Osmani reposted this

  

View Addy Osmani’s graphic link

Addy Osmani

• Following

Member of Technical Staff at Anthropic

1mo •

Software quality now depends on the constraints you set around your agents.

  

When humans manually wrote most of the code we could look at the code itself for signs of quality. Is it clean? Is it thoughtful? Is it fast? Can another engineer understand it? Does it have tests?

  

Agents can now generate more code than people can read. When code generation scales beyond review, quality - checks for one or more of correctness, maintainability, security, performance etc - increasingly has to live somewhere else.

  

It moves into the harness, environment and operating system around the agent.

  

This can be the tests and deterministic checks that decide what the system is allowed to do (amongst others). Your constraints are what may eventually enable loops of agents to deliver production software reliably. They can include unit tests, property tests, acceptance tests, mutation testing and quality metrics.

  

This back-pressure lets the system resist bad work before it becomes somebody elses problem.

  

Set your constraints. They decide whether the code your agents generate is good enough to ship.

  

hashtag#ai hashtag#programming hashtag#softwareengineering

…more

Activate to view larger image,

diagram, schematic

Activate to view larger image,

likeinsightfullove

1,521

165 comments

130 reposts

  

Like

  

Comment

  

Repost

  

Send

Feed post number 25

Addy’s profile photo

Addy Osmani reposted this

  

  

The Pragmatic Engineer

80,850 followers

3w •

  

Follow

An agent can tell you it's correct, not that it's good. Addy Osmani, author & director of engineering, on finding your edge over AI coding agents:

  

“I always go back to: what is alpha? My definition of alpha is advantage. What is the current thing that models are not very good at doing?

  

For software engineers, we often say that your alpha is in taste. Are we building the right thing? Is the thing that we are building actually good? Sometimes people will say an agent can tell you if it's good. I push back on that. An agent can tell you if a thing looks correct, if it's matching a spec. It doesn't mean it can tell you what's good.

  

Good can mean good from a user experience perspective, could be delightful, could be something that a person will actually want to come back to. And it is still sufficiently nuanced that it's going to take time for models to catch up to a point where they can replace that fully.

  

We tell people that judgment, verification, all of these other aspects continue to be important. But even if you say, maybe a year or two from now, models will catch up. We still need engineers to be answerable for these systems. That doesn't happen overnight. That happens when you understand a system, people trust you and you have that expertise.”

  

Learn more about building Chrome DevTools, AI Engineering and the risks of ‘cognitive surrender,’ with Addy Osmani on The Pragmatic Engineer podcast:

  

• YouTube: https://lnkd.in/eUtYZ2dW

  

• Spotify: https://lnkd.in/eYMH-3dM

  

• Apple: https://lnkd.in/e-mJNYZ3

  

• Summary and transcript: https://lnkd.in/eg8K3C6u

…more

  

Play

Remaining time

1:31

1x

  

Playback speed

  

Unmute

  

Turn fullscreen on

likesupportlove

95

6 comments

7 reposts

  

Like

  

Comment

  

Repost

  

Send

Feed post number 26

View Addy Osmani’s graphic link

Addy Osmani

• Following

Member of Technical Staff at Anthropic

3w •

  

Coming soon: my agent skills for writing while keeping humans more in the loop.

  

A lot of the current work on AI writing seems focused on removing AI tells. Things like "avoid the em dashes", the "its not X its Y", the overly tidy structure and polish. The stuff that gets your spidey senses tingling when you read it.

  

There have been a lot of anti-slop agent skills written that try to help, but I think much of it is about removing these tells rather than improving the quality of writing and bringing the human elements of writing back in the loop.

  

I'm more interested in the opposite problem: how do we keep and encourage what make's a human's writing worth reading in the first place?

  

Things like your personal takes. The observations you've had on topics. The stories only you can tell. The opinions you landed on after trying and failing at something for years. The quirks, anecdotes, jokes and tips that make something feel like only you could have written it.

Yes, this means a little more work from you, but I actually think its worth it.

  

Good writing isn't human because it contains a statistically convincing number of imperfections. It's human because, well...there is a human in it. Funny, right? So my theory is that folks want to solve the "blank page" problem with getting started, feel like writing isn't taking as long as it used to (get some productivity wins) but then benefit from being kept honest about what the piece needs to make it human.

  

My goal here is not to make AI writing harder to detect on checkers like Pangram (I've spent ~100 hours with Pangram 4 this month), it is to help you deliver writing that feels more human because it is more human.

  

The skills are still baking but I'll share them properly once ready :)

  

hashtag#writing hashtag#programming hashtag#ai

…more

Activate to view larger image,

View image

Activate to view larger image,

likeloveinsightful

351

48 comments

4 reposts

  

Like

  

Comment

  

Repost

  

Send

Feed post number 27

Addy’s profile photo

Addy Osmani reposted this

  

  

The Pragmatic Engineer

80,850 followers

3w •

  

Follow

“Don’t just be an engineer”. Addy Osmani, Author & Director of Engineering, on the unbundling of tech careers:

  

“What we are very likely to see happen next with engineering careers, as well as product and other roles, is the unbundling of these careers. So the engineer that also has product sense, the product person that also has engineering sense or UX sense, the UX person that also cares about product.

  

The guidance that I would give people is to think beyond just that narrow lens of engineering. There are many people, especially if you are senior, that have already had to think about these different aspects of success. If you are not someone that has had a chance to think about product or technical evangelism or go-to marketing or any of these other aspects that are generally different puzzle pieces of how businesses are successful, think about the non-engineering things. I think there's a lot of value there.

  

If you can show employers that you are not just a builder, but you're someone that can help them as these roles start to become a little bit fuzzier, I think that you can be successful in these times. Don't just be an engineer.”

  

Find out more on building Chrome DevTools, AI Engineering and the risks of ‘cognitive surrender,’ with Addy Osmani on The Pragmatic Engineer podcast:

  

• YouTube: https://lnkd.in/eUtYZ2dW

  

• Spotify: https://lnkd.in/eYMH-3dM

  

• Apple: https://lnkd.in/e-mJNYZ3

  

• Summary and transcript: https://lnkd.in/eg8K3C6u

…more

  

Play

Remaining time

1:03

1x

  

Playback speed

  

Unmute

  

Turn fullscreen on

likeinsightfulcelebrate

333

10 comments

35 reposts

  

Like

  

Comment

  

Repost

  

Send

Feed post number 28

View Addy Osmani’s graphic link

Addy Osmani

• Following

Member of Technical Staff at Anthropic

3w •

  

"A decade of hard-won lessons from scaling Git at GitHub" - one of the best engineering deep-dives I've read in a while.

  

Check it out: https://lnkd.in/gbqCiu3R

  

Vicent Martí distills a decade of hard-won lessons from scaling Git at GitHub, and unpacks how Cursor is entirely rethinking version control infrastructure with their new system, Origin.

When building and scaling developer tooling, the underlying infrastructure often dictates your ceiling.

  

Git's fundamental design.- specifically its reliance on packfiles and complex DAG walks - makes horizontal scaling incredibly painful over networked filesystems. GitHub solved this elegantly with Spokes and three-phase commit (3PC), ensuring strict consistency.

But what fascinates me most about Cursor’s new architecture, Continuity, is why they had to build it.

  

As we shift deeper into agentic engineering, the operational demands on version control are exploding. Multi-agent workflows spin up millions of ephemeral repositories, generate massive PR volumes, and trigger endless CI runs. Traditional consensus-based systems simply hit a wall with that kind of throughput.

  

To solve this, the team shifted to a stateless, WAL-first design backed by S3. A few brilliant takeaways from the architecture:

  

1. The WAL is the truth: Repositories on disk are just treated as a warm cache. If one goes down, it's effortlessly materialized from the write-ahead log.

  

2. Zero consensus bottlenecks: By removing strict routing tables and primary elections, any server can accept a push, completely bypassing the "tail at scale" latency of 3PC.

  

3. Limitless read scaling: Using optimistic replication via UDP and verifying against S3 allows them to deploy an arbitrary number of replicas for massive monorepos.

  

It is a fun read in distributed systems design demonstrating how AI-native development is forcing us to reinvent the absolute bedrock of our engineering infrastructure.

  

If you care about how tools operate at codebase-scale, this is a must-read.

  

hashtag#ai hashtag#programming hashtag#softwareengineering

…more

Activate to view larger image,

diagram

Activate to view larger image,

likeinsightfullove

728

Maksim Koutun and 727 others

20 comments

35 reposts

  

Like

  

Comment

  

Repost

  

Send

Feed post number 29

View Addy Osmani’s graphic link

Addy Osmani

• Following

Member of Technical Staff at Anthropic

3w •

  

Agents can write the code, but they can't own the outcome.

  

My latest free article: https://lnkd.in/gi6rASC9 ✏️

  

We are moving toward a world of "software factories" - event-driven, repeatable loops where AI agents handle triage, implementation and testing. They are writing more of our code, faster than ever.

  

But fast isn't the same as shippable. The percentage of code physically typed by humans is falling dramatically, but human ownership isn't leaving the software factory. It’s just relocating.

To build an automated system you can actually trust, human judgment needs to shift upstream:

  

- Intent & architecture: Deciding what the system should do and how it should be shaped.

  

- The quality bar: Defining which verification signals (type systems, mutation testing, security scanners) deserve trust.

  

- The final gate: Deciding when the evidence is actually sufficient to ship to production.

We can now fire up dozens of agents in parallel, but our cognitive bandwidth doesn't scale the same way. If you aren't careful, doing parallel work with agents creates massive comprehension debt - you end up approving code you can no longer explain.

  

The best software factories won't be defined by how completely they eliminate human involvement. They’ll be defined by how intelligently they place it. We should remove people from the parts of the loop where machines produce stronger, deterministic signals, and concentrate human attention where context, taste, risk and long-term ownership matter most.

  

When a system fails in production, "the agent wrote it" doesn't cut it. A human still has to own what ultimately ships. Hope the article is helpful!

  

hashtag#ai hashtag#programming hashtag#softwareengineering

…more

Activate to view larger image,

View image

  

See content credentials

Activate to view larger image,

likeinsightfulcelebrate

348

37 comments

32 reposts

  

Like

  

Comment

  

Repost

  

Send

Feed post number 30

View Addy Osmani’s graphic link

Addy Osmani

• Following

Member of Technical Staff at Anthropic

3w •

  

Ever find yourself right-clicking an image to "Save As" only to find the format isn't what you wanted. Here's a Chrome Extension that helps!

  

Check it out: https://lnkd.in/gZweav8x

  

We've all been there - right-clicking to save a simple JPEG or PNG, only to end up with a format that your apps don't support well. It's a modern web problem. Introducing SaveImageAs, a Chrome extension I created to give you back control.

  

With a single right-click on any image, you can choose to save it instantly as JPEG, PNG, or WebP. With a single right-click on any image, you can choose to save it instantly as JPEG, PNG or WebP.

  

Here’s why it’s a game-changer for your workflow:

  

🧠 It finds the BEST version: Most modern websites serve downscaled, re-compressed versions to your browser. SaveImageAs is smarter: it searches the page’s srcset or intelligently strips URL parameters from providers like Cloudinary to find and convert the high-quality original upload if available.

  

🔒 Truly Local & Private: The entire conversion process runs right on your own computer. There are no accounts to create, nothing is uploaded, and no servers are involved. Your privacy is paramount.

  

⚙️ Genuine re-encoding rather than just renaming: Many "converters" are just lazy and change the file extension. SaveImageAs uses a true fetch → decode → raster → re-encode pipeline. It even verifies the resulting byte-level magic numbers to ensure a .webp file is actually WebP data, avoiding Chrome's silent PNG fallback trap.

  

Saves you from the inevitable detour to a web-based file converter or image editor.

Stop letting the web dictate your file formats.

  

I hope that SaveImageAs helps make a difference :)

  

hashtag#programming hashtag#softwareengineering hashtag#webdevelopment

…more

Activate to view larger image,

graphical user interface, application

Activate to view larger image,

likelovecelebrate

346

38 comments

17 reposts

  

Like

  

Comment

  

Repost

  

Send

Feed post number 31

View Addy Osmani’s graphic link

Addy Osmani

• Following

Member of Technical Staff at Anthropic

3w •

  

Much to learn in "Laws of software engineering" by Dr Milan Milanović!

  

I had the distinct privilege of writing the foreword for this fantastic book. For a number of years I've watched teams fall into the same predictable traps and this helps name them.

  

Even as we're pushing the boundaries of AI-native engineering, the forces of human cognition, team dynamics and system complexity haven't been entirely automated away. This book gives you a shared vocabulary (laws) covering decades of hard-earned wisdom.

  

Here are a few of the laws Milan covers that feel particularly important and how I think about them through and AI and agent lens:

  

Tesler's Law (the law of conservation of complexity): Complexity cannot be eliminated, only shifted. As models take over writing syntax, the inherent complexity of software doesn't disappear - it simply shifts to system design and rigorous verification.

  

The law of leaky abstractions: All non-trivial abstractions, to some degree, leak. Relying on an LLM to generate an entire feature is a massive abstraction. When it inevitably produces a subtle runtime bug, you still need engineers with a deep understanding of the underlying stack to step in and fix the leak.

  

Gall's law: A complex system that works is invariably found to have evolved from a simple system that worked. You cannot deploy a sprawling multi-agent orchestration framework from scratch and expect it to succeed without nailing the simple, single-agent loops first.

  

Postel's Law (the robustness principle): Be conservative in what you do, be liberal in what you accept from others. As our infrastructure increasingly relies on agents passing context and fuzzy data back and forth, building resilient interfaces that can handle unpredictable inputs becomes a survival requirement.

  

Whether you're debating architecture trade-offs, scaling an engineering organization, or utilizing tools to analyze and explain pre-existing codebases to your team, these patterns give you the right framing to make deliberate decisions.

  

Grab a copy here and level up your engineering toolkit: https://lnkd.in/gdJjsJfz

  

On a personal note: I still love reading physical books a great deal. I've been giving reading on a new iPad mini a shot but there's something nice about getting "lost" in the focus of a physical book away from a screen that I still enjoy :)

  

hashtag#programming hashtag#softwareengineering hashtag#ai

…more

Activate to view larger image,

graphical user interface, application

Activate to view larger image,

likeloveinsightful

704

Vitaly Sharovatov and 703 others

39 comments

32 reposts

  

Like

  

Comment

  

Repost

  

Send

Feed post number 32

View Addy Osmani’s graphic link

Addy Osmani

• Following

Member of Technical Staff at Anthropic

3w •

  

I had a great conversation in SF with Gergely Orosz! We talked about engineering roles unbundling, DevTools to AI agents, cognitive debt & surrender and more.

View Gergely Orosz’s graphic link

Gergely Orosz

• 2nd

Deepdives on software engineering, tech careers and industry trends. Writing The Pragmatic Engineer, the #1 software engineering newsletter on Substack. Author of The Software Engineer’s Guidebook.

3w •

  

Follow

If you’ve ever opened Chrome DevTools, or optimized a page for Core Web Vitals, you’ve used software built by Addy Osmani. We start from when he built a web browser from scratch, at 16, through his 14 years at Google, to what he sees working (and not working) building software with AI:

  

• YouTube: https://lnkd.in/exitJh6C

• Spotify: https://lnkd.in/eEaxXivq

  

• Apple: https://lnkd.in/eaXmGX3m

  

Brought to you by:

  

• Antithesis – verify your system’s correctness without human review or traditional integration tests – and avoid bugs or outages. Teams like Jane Street, Fly.io, and the etcd community use Antithesis to ship better code, faster. https://lnkd.in/eyWErUbm

  

• Sentry – application monitoring software considered “not bad” by millions of developers. https://lnkd.in/e8VS5YcA

  

• Google Cloud Run – run untrusted agent code without the security anxiety. Cloud Run sandboxes deliver hyper-isolated, ephemeral execution environments that spin up in milliseconds. Check them out: https://lnkd.in/e7urCrPp

  

Here's Addy's advice on where he believes engineers should invest efforts, in the coming years, in his words:

  

“What we are very likely to see happen next with engineering careers (as well as product and other roles) is the unbundling of them, so that an engineer also has product sense, while a product person also has engineering sense, or UX sense.

  

You should think about the non-engineering things if you don’t [usually] have the time to think about product or technical evangelism, or go-to-market approaches, or any other parts of how businesses are successful.

  

If you can show employers that you are not just a builder, but someone that can help them as roles start to become a little bit fuzzier, then I think that you can be successful in these times.

  

Don’t be just an engineer.”

…more

  

Play

Remaining time

0:53

1x

  

Playback speed

  

Turn closed captions on

  

Unmute

  

Turn fullscreen on

likelovecelebrate

280

12 comments

9 reposts

  

Like

  

Comment

  

Repost

  

Send

Feed post number 33

View Addy Osmani’s graphic link

Addy Osmani

• Following

Member of Technical Staff at Anthropic

3w •

  

Agent Skills hit 88K stars! We also just shipped new tutorials with a focus on practical loop engineering, evergreen or existing codebases!

  

Check them out: https://lnkd.in/d-6QbpF9 ✏️

  

Rather than running one-off prompts, effective AI-assisted development comes down to managing the loop. You define the outer goal and harness, while the agent uses structured skills for execution, testing, and verification inside that boundary.

  

The new walkthroughs take you step-by-step through this workflow across greenfield projects, unfamiliar brownfield codebases, and automated background tasks, working identically whether you use Claude Code, Codex or another driver.

  

Along with the new guides, Agent Skills v0.6.7 is now available. We're trying to ship a new release (almost) every Friday to make sure stability and value keep improving.

  

This release brings key harness stability fixes and content upgrades, including a repaired Codex SessionStart hook, pinned plugin manifest versions to prevent drift, native Command Code support, a Phase 0 capability map for multi-spec requests, and pluggable task-tracker targets for teams on Linear or Jira.

  

Do you have feature requests or feedback? If there's anything we could be doing better, we're always happy to hear :)

  

Photo: Graffiti of the "Mission" in San Francisco at 24th Street

…more

Activate to view larger image,

View image

Activate to view larger image,

likecelebratelove

668

61 comments

18 reposts

  

Like

  

Comment

  

Repost

  

Send

Feed post number 34

View Addy Osmani’s graphic link

Addy Osmani

• Following

Member of Technical Staff at Anthropic

4w •

  

Code good enough to ship still needs human taste and ownership. Especially if you're trying to build an AI software factory.

  

A few things that have been working for me:

  

1. Keep human judgment in the loop. That can include upstream where you're dealing with product intent, the design of the system and your quality bar.

  

2. Do review code (lights-on factory) but be intentional with where it’s needed the most. I've found you want to watch out for where automated back-pressure breaks. Or where maintainability trade-offs need to be made.

  

3. Try to push every deterministic signal you can as early and continuously as possible. That can include types, tests, mutation checks, security and architecture rules. This has been working relatively well for me lately.

  

4. Don't fall for the idea that volume of checks alone is going to solve quality. It’'ll likely evolve some trial and error, so be ready to tighten or relax constraints deliberately.

  

The main thing that’s been helpful is aiming to build systems where human taste gets encoded into the environment, you get the machine to provide some evidence of its work and where someone still owns what ultimately goes into production.

  

Working on some more references for how you can do the above yourself.

  

hashtag#ai hashtag#programming hashtag#softwareengineering

…more

Activate to view larger image,

graphical user interface

Activate to view larger image,

likeinsightfullove

381

49 comments

17 reposts

  

Like

  

Comment

  

Repost

  

Send

Feed post number 35

View Addy Osmani’s graphic link

Addy Osmani

• Following

Member of Technical Staff at Anthropic

4w • Edited •

  

Agents at team scale need somewhere to run that you can actually trust.

  

Say you and your team are using AI coding agents - Claude Code, Codex, Cursor, often several at once. On a laptop, that's fine for a quick change. At team scale it's a real problem: each agent has full access to your machine, your keys, your network. No isolation. No audit trail. No central control over models or spend.

  

That's the gap Coder closes. It's a self-hosted platform where your developers and their AI agents work together on your own infrastructure. The agent loop runs in your Coder control plane and workspace - only the model's answer comes over the wire.

  

Check them out: https://fandf.co/4bgdZwf

  

I ran it end to end. On a real app - the RealWorld blog - I delegated one task from a chat: "add an estimated reading time to each article." Coder spun up an isolated workspace on infra I control, the agent read the actual code, wrote a new feature, wired it into the component and template, built the app to verify, and handed back a clean, reviewable diff.

  

Every article now shows "4 min read" - it's pretty real and visible.

  

The part that matters for a team is that the platform teams publish golden templates with the agents baked in - Claude Code, Codex, Cursor - and any model (Anthropic, OpenAI, Bedrock).

  

Every workspace is isolated, and every prompt, tool call, and token is audited, so security can stream it straight to their SIEM. It's the only setup I've seen that self-hosts both the agent AND where the code runs.

  

The agent era isn't only about better models - I think it's about somewhere to run them you can actually trust.

  

Sponsored by Coder. hashtag#ad - worth a look if you're a platform team thinking about agents at scale.

  

hashtag#ai hashtag#programming hashtag#softwareengineering

…more

  

Play

Remaining time

3:32

1x

  

Playback speed

  

Turn closed captions on

  

Unmute

  

Turn fullscreen on

likecelebratelove

144

13 comments

11 reposts

  

Like

  

Comment

  

Repost

  

Send

Feed post number 36

View Addy Osmani’s graphic link

Addy Osmani

• Following

Member of Technical Staff at Anthropic

4w •

  

"Maximizing the value of your Claude Code sessions"

  

Agentic coding tools like Claude Code are incredible, but are you getting the most value out of your tokens? Anthropic's Lydia Hallie just dropped a fantastic guide on how to run efficient Claude Code sessions: https://lnkd.in/gujXdtBJ

  

It turns out that fixing the exact same bug can cost completely different amounts depending on your session hygiene. Head's up: I do anticipate Claude will do more of this for you at some point, but until then:

  

Here is how to optimize your workflow and stop wasting context:

  

1. 🧹 Run /clear between tasks: Don't drag old context into a new problem. You're paying to re-read it on every single turn!

  

2. ⚙️ Set your /model and /effort upfront: Changing these mid-conversation busts your prompt cache, forcing a full-price prefill of your entire session.

  

3. 📎 @-mention files directly: Instead of typing out file paths, tagging them attaches the file to your message immediately, saving Claude a roundtrip "Read" call.

  

4. 🤫 Keep commands quiet: Add quiet flags to noisy terminal commands (like test runners) or run them in a subagent. Massive log outputs get permanently added to your conversation history.

  

5. 🔍 Audit your /context: Run this in a fresh session to see exactly what's loaded from your CLAUDE.md or MCP tools, and trim the excess.

  

6. 📦 /compact before you step away: Prompt caches expire (after an hour on a subscription, or just 5 minutes on an API key). Summarizing your conversation is significantly cheaper while the cache is still warm.

  

The main takeaway? Being efficient with tokens doesn't mean using fewer of them - it means ensuring every token goes toward the problem you're actually trying to solve

  

hashtag#ai hashtag#programming hashtag#softwareengineering

…more

Activate to view larger image,

View image

Activate to view larger image,

likeinsightfullove

1,752

108 comments

154 reposts

  

Like

  

Comment

  

Repost

  

Send

Feed post number 37

Addy’s profile photo

Addy Osmani reposted this

  

View Addy Osmani’s graphic link

Addy Osmani

• Following

Member of Technical Staff at Anthropic

1mo •

"Practical Loop Engineering"

  

My latest free deep-dive article: https://lnkd.in/gGVu_5fX ✏️

  

Loop engineering has fundamentally changed. We moved away from hand-rolled bash scripts and into a modern harness where autonomous, self-correcting feedback cycles are driven by two core primitives: goals and loops. Claude Code and Codex supports these ideas.

  

Understanding how to practically apply these concepts is the key to managing multiple agents without losing control of your codebase.

  

The goal primitive acts as your engine for bounded tasks. It forces an agent to iterate on a specific piece of work, repeatedly testing and adjusting its approach, until a provable, deterministic finish line is met. It relies on strict evaluation criteria so the agent knows exactly when a task is truly done, rather than just guessing what is good enough.

  

The loop primitive operates as your scheduler. It keeps an eye on external states or repeatedly executes patterns on a set cadence. It handles the recurring streams of well-defined work, acting as the heartbeat for your automated triage and system monitoring.

When you combine them, you unlock a highly capable workflow. You can build a system that automatically monitors for issues on a schedule and then relentlessly pursues a fix until your hard conditions are satisfied.

  

But practical loop engineering requires immense discipline. You have to clearly define what success looks like upfront, and you must build in independent verification so the agent writing the code isn't the one grading it. You can delegate the heavy lifting and the iteration to these primitives, but you can never delegate your taste or final judgment.

  

I hope the write-up is useful to some folks!

…more

Your document has finished loading

likeinsightfullove

749

74 comments

67 reposts