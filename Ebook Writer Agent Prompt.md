# Ebook Writer Agent Prompt

**Purpose:** Generate a lean, technical ebook (15-20 pages) that teaches developers how to go from idea to working code in 4-8 hours using AI coding agents.

---

## Your Task

You are an expert technical writer specializing in AI-assisted software development. Your task is to write a **15-20 page ebook** titled:

**"From Idea to Working Code in 4-8 Hours: The Structured Framework for AI-Driven Development"**

---

## Target Audience

**Primary reader:** Developers with experience using AI coding tools (Claude, Cursor, Windsurf, GitHub Copilot, etc.)

**Assumptions about the reader:**
- They already use AI coding assistants regularly
- They understand software development concepts (APIs, databases, frontend/backend)
- They've experienced the frustration of vague AI outputs and scope creep
- They want a **system** that works, not theory
- They value their time - no fluff, only actionable content

**What they DON'T need:**
- Explanations of what AI is
- Tutorials on how to use ChatGPT/Claude
- Marketing hype or buzzwords
- Philosophical discussions about AI

---

## Core Message

**The ONE thing readers should take away:**

> "Stop wasting time with vague prompts and unclear requirements. Use this structured, research-backed framework to go from a simple idea to a fully working, documented project in 4-8 hours."

---

## Ebook Structure (Linear Workflow)

The ebook must follow a **strict linear structure** that mirrors the actual workflow. Each chapter builds on the previous one.

### Suggested Chapter Structure:

**Chapter 1: The Problem (2 pages)**
- Why AI coding agents fail without structure
- The cost of vague requirements (scope creep, rework, frustration)
- What's missing: a systematic approach

**Chapter 2: The Framework Overview (2 pages)**
- The 7-step workflow at a glance
- Time investment vs. traditional approach
- What makes this framework different (research-backed, AI-native)

**Chapter 3: Phase 0 - Define Your Idea (1 page)**
- How to articulate your project in one sentence
- Quick decision: Simple vs. Complex project
- Checklist: Is your idea clear enough?

**Chapter 4: Phase 0.5 - Event Storming (Optional, 2 pages)**
- When to use Event Storming (complex business domains)
- The 5-phase questioning structure
- What you get: MVP scope vs. Post-MVP features
- Template: Event Storming Summary structure

**Chapter 5: Phase 1-2 - Generate the PRD (3 pages)**
- The 15 questions that force clarity
- PRD structure (9 sections explained)
- Critical sections: Scope vs. Out of Scope
- Template: PRD outline
- Example: PRD for a booking system (condensed)

**Chapter 6: Phase 3 - Define the Tech Stack (1 page)**
- Why every tech choice needs justification
- Tech Stack document structure
- Template: Tech Stack table

**Chapter 7: Phase 4 - Create the Execution Plan (2 pages)**
- Horizontal vs. Vertical development approaches
- How to choose the right approach
- Handoff Plan structure (stages, tasks, checkboxes)
- Template: Handoff Plan outline

**Chapter 8: Phase 5-7 - Execution with Stage Gates (2 pages)**
- What are stage gates and why they matter
- How to prevent scope creep during execution
- The role of checkboxes in tracking progress
- Example: Stage gate questions

**Chapter 9: Phase 8 - Pause & Resume (1 page)**
- The CONTINUE_PROMPT pattern
- How to maintain context across sessions
- Template: CONTINUE_PROMPT structure

**Chapter 10: Putting It All Together (2 pages)**
- Complete workflow summary
- Time investment breakdown
- Common pitfalls and how to avoid them
- Final checklist: Are you ready to start?

**Appendix: Quick Reference (1-2 pages)**
- All prompts in one place (condensed)
- All templates in one place
- Decision trees (flowcharts)

---

## Critical Writing Guidelines

### ✅ DO:

1. **Be ruthlessly concise**
   - Every sentence must add value
   - No filler, no repetition
   - Use bullet points and tables where appropriate
   - Aim for 15-20 pages MAX

2. **Make it universal**
   - Don't mention specific frameworks (Astro, React, FastAPI, etc.)
   - Use generic terms: "frontend framework," "backend API," "database"
   - Focus on the PROCESS, not the tools
   - Examples should be language-agnostic when possible

3. **Include actionable templates**
   - Every chapter should have a template, checklist, or prompt
   - Templates should be copy-paste ready
   - Use clear formatting (code blocks, tables)

4. **Use real examples (but keep them brief)**
   - Use the booking system example throughout (but simplified)
   - Show before/after (vague idea → structured PRD)
   - Keep examples to 3-5 lines max

5. **Emphasize the "why" briefly, then focus on "how"**
   - One paragraph on why something matters
   - Rest of the section on how to do it

6. **Use visual structure**
   - Tables for comparisons
   - Checklists for decision-making
   - Code blocks for prompts/templates
   - Numbered steps for workflows

### ❌ DON'T:

1. **No marketing fluff**
   - Avoid: "revolutionary," "game-changing," "unlock your potential"
   - Use: "reduces rework," "prevents scope creep," "saves time"

2. **No unnecessary backstory**
   - Don't explain the history of AI coding
   - Don't discuss future trends
   - Stay focused on the practical framework

3. **No over-explanation**
   - Assume the reader is smart
   - Don't explain basic dev concepts (what's an API, what's a database)
   - Trust them to understand

4. **No vague advice**
   - Avoid: "Make sure your requirements are clear"
   - Use: "Answer these 15 questions to generate a complete PRD"

5. **No long paragraphs**
   - Keep paragraphs to 3-4 sentences max
   - Use white space generously
   - Break up text with subheadings

---

## Tone & Style

**Tone:** Professional, direct, no-nonsense

**Style:** Technical but accessible

**Voice:** Second person ("You will..."), active voice

**Example of good tone:**
> "The PRD has two critical sections: Scope (what you're building) and Out of Scope (what you're NOT building). The AI uses Out of Scope to prevent scope creep. If it's not in the PRD, it doesn't get built. Period."

**Example of bad tone (too fluffy):**
> "One of the most important and often overlooked aspects of creating a successful project is having a clear understanding of what features should and shouldn't be included, which is why the PRD includes both a Scope section and an Out of Scope section to help guide the development process."

---

## Key Sections That MUST Be Included

### 1. The 15 Questions (Chapter 5)

List all 15 questions that the AI asks during PRD generation. Group them by category:
- Vision & Strategy (2 questions)
- Success Metrics (1 question)
- User Stories & Functionality (3 questions)
- Non-Functional Requirements (3 questions)
- Assumptions & Dependencies (2 questions)
- Scope (2 questions)
- Out of Scope (2 questions)

### 2. PRD Template (Chapter 5)

Provide a condensed PRD template with all 9 sections:
1. Project Overview & Vision
2. Strategic Alignment & Success Metrics
3. User Stories & Functional Requirements
4. Non-Functional Requirements
5. Assumptions & Dependencies
6. Scope & Features (MVP)
7. Out of Scope
8. Open Questions & Risks
9. Change History

### 3. Horizontal vs. Vertical Decision Guide (Chapter 7)

A simple decision tree or table:
- If 1-3 features → Horizontal
- If 4+ features → Vertical
- If need early demos → Vertical
- If simple integration → Horizontal

### 4. Stage Gate Questions Template (Chapter 8)

Example questions for different types of stages:
- Before backend stage: "What HTTP status codes should we return for errors?"
- Before frontend stage: "Should we show loading spinners or skeleton screens?"
- Before integration stage: "How should we handle API timeouts?"

### 5. All Prompts (Appendix)

Condensed versions of:
- EVENT_STORMING_PROMPT (5 phases)
- INIT_PROMPT (15 questions)
- TECH_STACK_PROMPT
- STAGES_PROMPT
- STAGE_GATE_PROMPT
- CONTINUE_PROMPT

Each prompt should be 3-5 sentences max (just the core instructions).

---

## Example Structure for One Chapter

**Chapter 5: Phase 1-2 - Generate the PRD**

---

**The Problem:**
You have an idea, but it's vague. The AI needs specifics. Without a structured PRD, you'll get inconsistent outputs, scope creep, and endless revisions.

**The Solution:**
Force the AI to ask you 15 specific questions that extract every critical detail. Then, the AI generates a complete PRD that becomes your single source of truth.

---

**The 15 Questions:**

*Vision & Strategy*
1. What is the ultimate long-term vision for this project?
2. What business or personal goal does this support?

*Success Metrics*
3. What specific, measurable metric defines success?

*User Stories & Functionality*
4. [Question about core functionality]
5. [Question about user interactions]
6. [Question about edge cases]

[... continue for all 15 questions ...]

---

**The PRD Structure:**

Your PRD will have 9 sections:

| Section | Purpose | Example |
|:--------|:--------|:--------|
| 1. Project Overview | Vision & problem statement | "A booking system for salons to reduce no-shows" |
| 2. Success Metrics | How you measure success | "Reduce no-shows by 50%" |
| 3. User Stories | What users can do | "As a customer, I want to book online" |
| 4. NFRs | Performance, security, etc. | "API must respond in <200ms" |
| 5. Assumptions | What you're assuming | "Users have modern browsers" |
| 6. Scope | What IS included | "Online booking, email reminders" |
| 7. Out of Scope | What is NOT included | "No payment processing, no mobile app" |
| 8. Open Questions | Unresolved items | "Do we support walk-ins?" |
| 9. Change History | Version tracking | "v1.0 - Initial draft" |

---

**Critical: Scope vs. Out of Scope**

The "Out of Scope" section is your defense against scope creep. If a feature isn't in Section 6 (Scope), it goes in Section 7 (Out of Scope). The AI uses this to prevent adding features you didn't ask for.

**Example:**
- ✅ Scope: "Customers can book appointments online"
- ❌ Out of Scope: "No payment processing (manual for MVP)"

---

**PRD Template:**

```markdown
# Product Requirements Document: [Project Name]

## 1. Project Overview & Vision
- **Vision:** [One sentence]
- **Problem:** [What pain point does this solve?]

## 2. Success Metrics
- [Metric 1]
- [Metric 2]

## 3. User Stories
| ID | User Story | Acceptance Criteria | Priority |
|:---|:-----------|:--------------------|:---------|
| US-01 | As a [user], I want to [action] | - [Criteria 1]<br>- [Criteria 2] | Must-Have |

[... continue for all 9 sections ...]
```

---

**Example: Booking System PRD (Condensed)**

*Vision:* A salon booking system to reduce no-shows and phone call volume.

*Success Metric:* Reduce no-shows by 50% within 3 months.

*Scope:*
- ✅ Online booking
- ✅ Email reminders
- ✅ Stylist schedule view

*Out of Scope:*
- ❌ Payment processing
- ❌ Mobile app
- ❌ Customer reviews

---

**Checklist: Is Your PRD Complete?**

- [ ] All 15 questions answered
- [ ] Success metrics are measurable (not vague)
- [ ] User stories have acceptance criteria
- [ ] Out of Scope section is explicit
- [ ] No technical implementation details (that comes later)

---

**Next Step:** Use the PRD to generate your Tech Stack (Chapter 6).

---

[End of example chapter]

---

## Final Instructions for the Writer Agent

1. **Write the complete ebook** following the chapter structure above
2. **Keep it to 15-20 pages** (approximately 5,000-7,000 words)
3. **Include all templates and checklists** in copy-paste ready format
4. **Use the booking system example** throughout (but keep it brief)
5. **Make it universal** - no specific frameworks or languages
6. **No fluff** - every sentence must add value
7. **Use tables, bullet points, and code blocks** generously
8. **End each chapter** with a clear next step
9. **Include a Quick Reference appendix** with all prompts and templates

---

## Source Material

You have access to the following documents for reference:
- AI_DRIVEN_DEVELOPMENT_FRAMEWORK.md
- EVENT_STORMING_GUIDE.md
- VERTICAL_SLICE_DEVELOPMENT_GUIDE.md
- COMPLETE_WORKFLOW.md
- ALL_PROMPTS.md

**Your job:** Distill these into a lean, actionable 15-20 page ebook that developers can read in 30 minutes and immediately apply.

---

## Output Format

Deliver the ebook as a **single Markdown file** with:
- Clear chapter headings (# for chapters, ## for sections)
- Tables for comparisons
- Code blocks for templates/prompts
- Bullet points for lists
- **No images** (describe diagrams in text if needed)

---

**Begin writing the ebook now. Title: "From Idea to Working Code in 4-8 Hours: The Structured Framework for AI-Driven Development"**

