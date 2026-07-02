# Prompt Engineering Playbook
## 30 Battle-Tested Prompts for AI Automation
### $15 — June 25, 2026

---

**Who this is for:** Freelancers, agency owners, and operators who build AI workflows for clients.
**What you get:** 30 prompts that consistently produce high-quality output across GPT-4, Claude, and DeepSeek.

---

## The Prompt Framework

Every prompt here follows the **R.A.C.E.** structure:

- **R**ole — Who the AI should act as
- **A**ction — What to do (specific verb)
- **C**ontext — Background information
- **E**xample — Expected output format

---

## SECTION 1: CONTENT GENERATION (Prompts 1–6)

### 1. Blog Post from Transcript
```
Role: You are a content repurposing specialist who turns raw transcripts into
publishable blog posts.

Action: Transform the following transcript into a 1,500-word blog post with:
- A compelling title (3 options)
- An introduction that hooks the reader
- 5-7 subheadings with supporting paragraphs
- Key takeaways in a bulleted summary at the bottom
- A call-to-action in the author bio

Context: The transcript is from a 20-minute podcast about [topic]. Target
audience is [industry] professionals who want practical, actionable advice.
Tone: professional but conversational. Avoid jargon.

Transcript:
[PASTE TRANSCRIPT HERE]

Example Output Format:
Title Option A: [title]
Title Option B: [title]
Title Option C: [title]

[Full blog post with markdown formatting]
```

### 2. Twitter/X Thread from Article
```
Role: You are a social media strategist who distills long-form content into
engaging Twitter threads that drive traffic and engagement.

Action: Convert the following article into a 10-tweet thread.
Each tweet must be under 280 characters.
- Tweet 1: Hook that makes people stop scrolling
- Tweets 2-9: Core insights, one per tweet
- Tweet 10: Call-to-action with link
- Add 2-3 relevant hashtags

Context: Article topic is [topic]. Brand voice is [tone]. Include a poll
in tweet 5 to boost engagement.

Article:
[PASTE ARTICLE HERE]

Example Output Format:
🧵 [THREAD START]

1/ [hook tweet]

2/ [insight]

...

10/ [CTA]
```

### 3. Email Sequence (5 Emails)
```
Role: You are a direct-response copywriter specializing in email marketing
for [industry] businesses.

Action: Write a 5-email nurture sequence for:
- Target: [audience description]
- Goal: Convert readers into [desired action]
- Tone: [warm/professional/urgent]

Each email must include:
- Subject line (max 60 chars)
- Preview text (max 90 chars)
- Body (150-200 words)
- Clear CTA

Structure:
Email 1: Value — useful information, no pitch
Email 2: Story — case study or testimonial
Email 3: Education — how-to or framework
Email 4: Social proof — what others are doing
Email 5: Offer — direct ask with urgency

Example Output Format:
--- EMAIL 1 ---
Subject: [subject line]
Preview: [preview text]

Body:
[email content]

CTA: [link/action]
```

### 4. LinkedIn Post — Thought Leadership
```
Role: You are a LinkedIn content strategist who writes posts that position
the poster as a thought leader in [industry].

Action: Write a LinkedIn post (1,200-1,500 characters) that:
- Opens with a provocative question or contrarian take
- Shares a personal story or lesson
- Provides 3 actionable insights
- Ends with a question to drive comments

Context: The poster is a [role] at [company]. Post should reinforce their
expertise in [niche]. Avoid generic motivational content.

Example Output Format:
[Post text — no markdown, LinkedIn-native]

--- 💬 Suggested Comment Moderation Reply ---
[Template for replying to first 10 comments]
```

### 5. Video Script (60-Second Short)
```
Role: You are a video scriptwriter who creates ultra-engaging short-form
content optimized for TikTok/Reels/Shorts algorithms.

Action: Write a 60-second video script that:
- Hooks in the first 3 seconds
- Delivers one clear insight
- Ends with a curiosity gap CTA

Context: Topic is [topic]. Target audience is [demographic].
Visual style: [talking head / screen share / B-roll].

Example Output Format:
:00-:03 | HOOK | "[spoken hook line]" | [visual cue]
:04-:15 | PROBLEM | "[describe the pain point]" | [visual cue]
:16-:45 | SOLUTION | "[deliver the insight in 3 steps]" | [visual cue]
:46-:55 | EXAMPLE | "[real example or demonstration]" | [visual cue]
:56-:60 | CTA | "[call-to-action]" | [visual cue]

Caption text for auto-generated subtitles:
[caption]
```

### 6. Product Description (E-Commerce)
```
Role: You are a conversion copywriter specializing in e-commerce product
descriptions that sell without being pushy.

Action: Write a product description for:
- Product: [product name]
- Price: [$X]
- Target customer: [demographic + pain point]

Include:
- 3 benefit-driven bullet points
- Sensory-rich paragraph (50 words)
- Technical specifications table
- 60-word "story" about why this exists
- SEO meta description (160 chars max)

Example Output Format:
## [Product Name]
[Price]

[Benefit bullets]

[Story paragraph]

### Specifications
| Spec | Detail |

### SEO Meta
[meta description]
```

---

## SECTION 2: BUSINESS & OPERATIONS (Prompts 7–14)

### 7. SOP Generator
```
Role: You are a documentation specialist who writes crystal-clear SOPs
that anyone can follow on their first read.

Action: Create a Standard Operating Procedure for [process/ task].

The SOP must include:
1. Purpose (one sentence)
2. Prerequisites (tools, access, knowledge needed)
3. Step-by-step instructions (numbered, one action per step)
4. Decision tree for common edge cases
5. Expected output / success criteria
6. Troubleshooting: top 3 things that go wrong

Context: The reader is a [role] who has [experience level] experience.
The process takes approximately [time] to complete.

Example Output Format:
## SOP: [Title]
**Purpose:** ...
**Prerequisites:** ...
**Estimated time:** ...

### Procedure
1. ...
2. ...
3. ...

### Edge Cases
- If X happens: do Y
- If Z happens: do W

### Troubleshooting
| Problem | Cause | Solution |
```

### 8. Competitor Analysis
```
Role: You are a competitive intelligence analyst. Your analysis is used
by the strategy team to inform product decisions and positioning.

Action: Analyze the following competitor and provide a structured report.

Competitor: [competitor name]
Market: [industry/niche]
My product/service: [brief description]

Report structure:
1. Company overview (size, funding, trajectory)
2. Product/feature breakdown (what they do better/worse)
3. Pricing comparison
4. Target audience overlap
5. GTM/branding strategy summary
6. 3 specific ways we can differentiate
7. Recommended immediate actions (ranked by effort/impact)

Example Output Format:
# Competitor Analysis: [Company]

## Overview
...

## Feature Comparison
| Feature | Them | Us | Gap |
```

### 9. Value Proposition Generator
```
Role: You are a positioning consultant who helps companies articulate
their value in one sentence.

Action: Generate 10 distinct value proposition options for:
- Company: [company name]
- Product/service: [description]
- Target customer: [demographic]
- Key differentiator: [what makes them unique]
- Competitors: [main competitors]

Each value proposition must:
- Be under 140 characters
- Include the target customer
- Include the specific outcome
- Sound distinct from competitors
- Pass the "so what?" test

After listing 10, recommend the top 3 and explain why.

Example Output Format:
## Value Propositions

1. [VP1] — [why it works]
2. [VP2] — [why it works]
...
```

### 10. Cold Email Writer (Custom)
```
Role: You are a senior BDR at a top SaaS company who personally writes
every outreach email and averages 15% reply rates.

Action: Write a personalized cold email for:
- Prospect name: [name]
- Company: [co]
- Role: [title]
- Trigger event / context: [what prompted this outreach]
- My offer: [what I'm selling]
- Target outcome: [book meeting / reply / download]

Rules:
- Max 120 words
- Must reference something specific about them or their company
- One clear CTA
- No buzzwords or fluff
- Include a PS if there's a relevant social proof point

Example Output Format:
Subject: [subject]

Hi [Name],

[opening line — reference + context]

[body — value prop + proof]

[CTA]

Best,
[Your Name]

[PS if applicable]
```

### 11. Pricing Strategy Consultant
```
Role: You are a pricing strategist who has advised 50+ SaaS and service
businesses on pricing optimization.

Action: Analyze my current pricing and recommend changes.

My current pricing:
[describe your current pricing tiers and amounts]

My costs: [fixed + variable per unit]
My market: [industry]
My competitors: [list competitors and their pricing]
My typical customer: [demographic + willingness to pay]

Provide:
1. Three alternative pricing structures with rationale
2. Suggested price points for each
3. Psychological pricing tactics to apply
4. A/B testing plan to validate changes
5. Common pricing mistakes in this market

Example Output Format:
# Pricing Strategy Review

## Current Analysis
...

## Option 1: [name]
...
```

### 12. Customer Interview Question Bank
```
Role: You are a user research specialist who designs interview guides
that uncover insights product teams can act on.

Action: Generate a customer interview guide for:
- Target customer: [description]
- Product area: [what we're researching]
- Decision stage: [pre-purchase / early usage / power user / churned]

Include:
- 5 warm-up questions (build rapport)
- 10 core questions (behavior, not opinion — "tell me about the last
  time you..." not "would you...")
- 5 follow-up probes for deep answers
- Closing questions (permission to follow up)

Context: We want to understand [specific research goal].

Example Output Format:
# Interview Guide: [Topic]

## Warm-Up (5 min)
1. ...
2. ...

## Core Questions (25 min)
1. ...
...
```

### 13. Hiring Job Description Optimizer
```
Role: You are a talent acquisition strategist who writes job descriptions
that attract top talent and reduce time-to-hire.

Action: Optimize the following job description for:
- Role: [title]
- Level: [junior/mid/senior]
- Market: [city/remote]

Provide:
1. An optimized job title (tested for search+appeal)
2. A rewritten "About the Role" paragraph (100 words)
3. 5 bullet points for responsibilities (action-verb led)
4. 5 bullet points for requirements (must-have vs nice-to-have)
5. 3 bullet points for "Why Join Us" (differentiators)
6. Salary range recommendation
7. 3 channels to post on besides LinkedIn

Current text:
[PASTE CURRENT JD]

Example Output Format:
## Optimized JD: [Title]

### Title
...
```

### 14. Meeting Agenda & Notes Template
```
Role: You are a meeting effectiveness coach who helps teams cut meeting
time by 40% while improving outcomes.

Action: Create a meeting template for:
- Meeting type: [1:1 / standup / client review / strategy / post-mortem]
- Duration: [minutes]
- Participants: [attendees + roles]

Template must include:
- Pre-read section (what to review before)
- Agenda with time allocations
- Decision log (decisions made, by whom)
- Action items (owner, task, due date)
- Score: was this meeting worth having? (1-10)

Example Output Format:
## [Meeting Type] Template
**Duration:** [X] min
**Cadence:** [weekly/biweekly/ad-hoc]

### Pre-Read (complete before meeting)
...

### Agenda
| Time | Item | Owner |
```

---

## SECTION 3: PRODUCTIVITY & AUTOMATION (Prompts 15–22)

### 15. AI Task Decomposer
```
Role: You are an AI workflow architect who breaks complex tasks into
agent-delegatable subtasks.

Action: Decompose the following task into a dependency graph of AI-
executable subtasks.

Task: [describe the complex task]
Constraints: [budget, time, tools available]
Output format: Must be in JSON with subtask_id, description, dependencies,
estimated_complexity (1-5), and suggested_agent_type.

Task:
[PASTE TASK DESCRIPTION]

Example Output Format:
{
  "task": "[task name]",
  "subtasks": [
    {
      "id": "s1",
      "description": "...",
      "dependencies": [],
      "complexity": 3,
      "agent_type": "research"
    },
    ...
  ]
}
```

### 16. Decision Matrix Generator
```
Role: You are a decision analysis expert who uses structured frameworks
to eliminate bias from complex choices.

Action: Create a weighted decision matrix for:

Decision to make: [what we're deciding]
Options (2-6): [list options]
Criteria (3-7): [list criteria]

For each criterion, provide:
- Weight (1-10)
- Why this weight is justified

Then score each option against each criterion on 1-10 scale.
Include: weighted scores, ranking, sensitivity analysis.

Context: [any additional information]

Example Output Format:
# Decision Matrix: [Topic]

## Criteria & Weights
| Criterion | Weight | Rationale |

## Scores
| Option | Criterion 1 | Criterion 2 | Weighted Total |
```

### 17. PRD Generator
```
Role: You are a senior product manager who writes PRDs that engineering
teams can build from without clarification loops.

Action: Write a Product Requirements Document for:

Product/feature: [name]
Target user: [description]
Problem statement: [what problem]
Success metrics: [KPIs]
Constraints: [technical, timeline, budget]

The PRD must include:
1. Executive summary (3 sentences max)
2. User stories (at least 8, prioritized P0-P2)
3. Acceptance criteria for each P0 story
4. Edge cases & error states
5. Out of scope (explicitly)
6. Dependencies & risks

Example Output Format:
# PRD: [Feature Name]

## Executive Summary
...

## User Stories
### P0 — Must Have
- As a [user], I want [goal] so that [reason]
  **AC:** ...
```

### 18. Technical Specs from PRD
```
Role: You are a senior software architect who translates product
requirements into implementable technical specifications.

Action: Generate a technical spec for the following PRD/user stories:

PRD/User Stories:
[PASTE CONTENT]

Tech stack: [languages, frameworks, infra]
Constraints: [performance, scalability, security]

Spec must include:
1. System architecture overview
2. Data model (entities, relationships, key fields)
3. API endpoints (method, path, request, response)
4. Database schema changes
5. Error handling strategy
6. Testing strategy (unit, integration, e2e)
7. Migration/data backfill plan if applicable

Example Output Format:
# Technical Spec: [Feature]

## Architecture
...

## Data Model
...
```

### 19. Error Message & User Guidance Writer
```
Role: You are a UX writer who turns technical errors into helpful,
empathetic user messages.

Action: Rewrite the following technical error messages into user-facing
messages that are clear, actionable, and reassuring.

Error messages to rewrite:
[PASTE ERROR MESSAGES]

For each, provide:
1. User-facing message (max 100 chars)
2. Next step instruction
3. What NOT to say (common bad patterns)
4. Suggested visual treatment (toast / modal / inline)

Context: Product is [product name]. User profile: [technical level].

Example Output Format:
## Error: [original]
**User message:** [rewritten]
**Next step:** [instruction]
**Avoid:** [bad pattern]
```

### 20. Onboarding Flow Designer
```
Role: You are a product-led growth specialist who designs onboarding
flows that hit the "aha moment" in the first session.

Action: Design a 5-step onboarding flow for:

Product: [name]
Core value prop: [one sentence]
Ideal user action in first session: [key activation event]
User skill level: [beginner/intermediate/expert]

For each step, specify:
1. What the user sees
2. What the user does
3. What success looks like
4. Drop-off risk (low/medium/high)
5. How to handle abandonment

Example Output Format:
# Onboarding Flow: [Product]

## Step 1: [Name]
**See:** [visual description]
**Do:** [user action]
**Success:** [outcome]
**Drop-off risk:** [level]
**Abandonment recovery:** [tactic]
```

### 21. API Client Code Generator
```
Role: You are an API documentation and SDK specialist who generates
ready-to-run client code.

Action: Generate API client code for:

API: [name/source]
Language: [Python / JavaScript / both]
Authentication: [API key / OAuth / none]
Endpoints needed: [list or "all documented"]
Error handling: [retry logic, rate limiting]

Generate:
1. Working client class with auth
2. Methods for each endpoint
3. Error handling
4. Example usage

API Documentation:
[PASTE OR DESCRIBE]

Example Output Format:
# [Language] API Client for [Service]

```python
class [ServiceName]Client:
...
```
```

### 22. Test Data Generator
```
Role: You are a QA automation engineer who generates realistic test data
for development, staging, and demo environments.

Action: Generate test data for:

Schema/data model:
[DESCRIBE TABLES OR COLLECTIONS]

Volume: [X rows/documents]
Realism: [realistic / edge-case heavy / both]
Format: [JSON / CSV / SQL INSERTs]

Constraints:
- Ensure referential integrity (foreign keys match)
- Include edge cases (nulls, empty strings, max lengths)
- No real PII — use fake names, emails, addresses

Example Output Format:
```json
[
  {
    "id": 1,
    ...
  }
]
```
---

## SECTION 4: ANALYSIS & STRATEGY (Prompts 23–30)

### 23. Market Research Synthesizer
```
Role: You are a market research analyst who synthesizes raw data into
actionable strategic recommendations.

Action: Analyze the following market data and produce a concise report.

Data sources provided:
[PASTE MARKET DATA — links, notes, statistics]

Research question: [specific question to answer]

Report structure:
1. Key finding (one sentence)
2. Evidence (what the data says)
3. Market signals (emerging trends)
4. Blind spots (what we don't know)
5. 3 strategic recommendations (ranked by effort/impact)

Example Output Format:
# Market Research: [Topic]

## Key Finding
...

## Evidence
| Data Point | Source | Implication |
```

### 24. SWOT Generator
```
Role: You are a business strategy consultant who runs SWOT analyses
that lead directly to action items.

Action: Perform a SWOT analysis for:

Company/product: [name]
Market: [industry/niche]
Time horizon: [6 months / 1 year / 3 years]

For each quadrant (Strengths, Weaknesses, Opportunities, Threats):
- 3–5 specific points
- Each point must reference a specific fact, not a generic statement

Then produce:
- 3 strategies that leverage Strengths + Opportunities
- 3 strategies that address Weaknesses + mitigate Threats
- 3 quick wins (can do this week)

Example Output Format:
# SWOT: [Company]

## Strengths
1. [specific strength] — [evidence]

## Strategies
### Strength × Opportunity
1. ...
```

### 25. OKR Generator
```
Role: You are an OKR coach who helps teams set ambitious but achievable
objectives with measurable key results.

Action: Generate a set of OKRs for:

Team/department: [name]
Company goal alignment: [which company objective this supports]
Quarter: [Q1/Q2/Q3/Q4 YYYY]
Current state: [brief context on where we are now]

Generate:
- 3 Objectives (qualitative, inspirational)
- 3-4 Key Results per Objective (quantitative, measurable)
- 1 "stretch" KR per Objective (hard but possible)
- Confidence level for each KR (low/medium/high)

Example Output Format:
# OKRs: QX YYYY — [Team]

## Objective 1: [description]
**KR1:** [metric from X to Y]
**KR2:** [metric from X to Y]
...
```

### 26. AARRR (Pirate Metrics) Audit
```
Role: You are a growth analyst who uses the AARRR framework to diagnose
leaks in the customer funnel.

Action: Conduct a pirate metrics audit for:

Business: [description]
Funnel stages defined:
- Acquisition: [how users find you]
- Activation: [first "aha" moment]
- Retention: [how users come back]
- Revenue: [how you monetize]
- Referral: [how users bring others]

For each stage, identify:
1. Current metric (if available)
2. Benchmark for this industry
3. The biggest leak
4. 3 fixes ordered by impact
5. Tool/experiment to validate

Example Output Format:
# Pirate Metrics Audit: [Company]

## Acquisition
**Current:** [metric]
**Benchmark:** [industry avg]
**Biggest leak:** [description]
**Fixes:** 1. ..., 2. ..., 3. ...
**Validation:** [experiment]
```

### 27. Risk Registry Generator
```
Role: You are an enterprise risk manager who identifies, qualifies, and
quantifies project risks before they materialize.

Action: Create a risk registry for:

Project: [name]
Timeline: [duration]
Budget: [$]
Team size: [people]
Key dependencies: [list]
Stakeholders: [list]

For each risk, provide:
1. Risk description
2. Probability (1-5)
3. Impact (1-5)
4. Risk score (P × I)
5. Mitigation strategy
6. Contingency plan
7. Owner

Example Output Format:
# Risk Registry: [Project]

| # | Risk | Prob | Impact | Score | Mitigation | Contingency | Owner |
|---|---|---|---|---|---|---|---|
```

### 28. Launch Checklist Generator
```
Role: You are a release manager who creates pre-flight checklists that
prevent launch-day disasters.

Action: Generate a launch checklist for:

Launch type: [product / feature / campaign / event]
Platform: [web / mobile / physical / hybrid]
Team size: [number of people]
Go-live date: [date]
Risk level: [low / medium / high]

Checklist categories:
- Legal & compliance
- Technical readiness
- Marketing & comms
- Customer support prep
- Sales enablement
- Post-launch monitoring

Each item must have: owner, deadline, status (pre-flight / ready / blocked).

Example Output Format:
# Launch Checklist: [Name]

## Legal & Compliance
| Item | Owner | Deadline | Status |
```

### 29. Customer Journey Map Generator
```
Role: You are a CX designer who maps customer journeys to identify
pain points and delight opportunities.

Action: Create a customer journey map for:

Persona: [name, role, goals]
Product/service: [name]
Stage: [awareness → consideration → purchase → retention → advocacy]

For each stage, document:
1. Customer actions
2. Touchpoints (where they interact)
3. Emotions (😊😐😠 at each step)
4. Pain points
5. Opportunities
6. Metrics to track

Example Output Format:
# Customer Journey: [Persona]

## Stage 1: Awareness
**Actions:** [what they do]
**Touchpoints:** [where]
**Emotions:** [😊]
**Pain points:** [issues]
**Opportunities:** [ideas]
**Metrics:** [KPIs]
```

### 30. Negotiation Preparation Template
```
Role: You are a negotiation strategist who has trained sales teams at
Fortune 500 companies on deal negotiation.

Action: Prepare a negotiation brief for:

Deal type: [sales / partnership / vendor / employment]
Counterparty: [name/company]
My BATNA: [best alternative if no deal]
Their likely BATNA: [estimate]
My ideal outcome: [terms]
Walk-away point: [minimum acceptable terms]

Provide:
1. Opening strategy (what to say first)
2. 3 concessions to give (in order)
3. 3 concessions to ask for
4. Common tactics they might use and how to counter
5. The "if-then" script for each concession

Example Output Format:
# Negotiation Brief: [Deal/Party]

## Key Parameters
**My BATNA:** ...
**Their likely BATNA:** ...
**Walk-away:** ...

## Strategy
**Opening:** ...

## Concessions
### Give
1. ...
```

---

## PROMPT PERFORMANCE TIPS

1. **Temperature:** 0.2–0.4 for structured output (SOPs, code), 0.7–0.9 for creative (copy, ideation)
2. **Model choice:** GPT-4o for marketing/ad copy, Claude for analysis/strategy, DeepSeek for technical/code
3. **Token budget:** Add "Be concise — use [X] tokens or fewer" for cost-sensitive runs
4. **Iteration loop:** Always follow up with "Make it more specific to [context]" rather than regenerating
5. **Output format enforcement:** Always end with "ONLY OUTPUT VALID JSON" or "USE MARKDOWN" to control parsing

---

*Product Factory • June 25, 2026 • $15 Suggested Retail*