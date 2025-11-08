# Complete Workflow: From Idea to First Line of Code

**Version:** 2.1  
**Purpose:** A step-by-step walkthrough of the entire AI-Driven Development Framework process, including optional Event Storming for complex business domains.

---

## Overview

This document walks you through the **complete flow from absolute start to finish** with concrete examples and time estimates for each phase.

---

## 🎯 PHASE 0: Before You Start

**What you have:** Just an idea in your head.

**Example:** "I want to build an API that shows random numbers on a web page."

**What you do:**
1. Write down your idea in **one sentence**
2. Do some quick research on tech stack (optional, but helpful)
3. Think about what you want to achieve (portfolio piece? production app? learning project?)

**Time estimate:** 5-10 minutes

**Output:** A clear, one-sentence project idea.

---

## 🎨 PHASE 0.5: Event Storming (Optional - For Complex Business Domains)

**When to use:** If your project involves complex business processes, multiple user types, or workflows (e.g., booking systems, e-commerce, workflow automation).

**When to skip:** If your project is simple (e.g., a landing page, a simple API) or you already have crystal-clear requirements.

**What you have:** Your one-sentence project idea from Phase 0.

**What you do:**
1. Open `EVENT_STORMING_GUIDE.md`
2. Copy the **EVENT_STORMING_PROMPT**
3. Replace the placeholder with your project idea
4. Paste it into your AI agent

**Example prompt:**
```
My project idea is: "I want to build an online booking system for a hair salon where customers can book appointments, stylists can manage their schedules, and the owner can see revenue reports."
```

**What the AI does:**

The AI conducts a structured Event Storming session by asking questions in 5 phases:

1. **Phase 1: Domain Discovery (5-7 questions)**
   - What are the main activities or processes?
   - Who are the key actors (users, roles)?
   - What triggers these activities?

2. **Phase 2: User Workflows (5-7 questions)**
   - What does a typical user journey look like?
   - What are the key decision points?
   - What happens when things go wrong?

3. **Phase 3: Business Rules & Constraints (3-5 questions)**
   - What business rules must the system enforce?
   - What are the constraints (time, capacity, permissions)?

4. **Phase 4: Pain Points & Opportunities (3-5 questions)**
   - What are the current pain points?
   - What manual work could be automated?

5. **Phase 5: MVP vs. Post-MVP (3-5 questions)**
   - What is absolutely essential for the first version?
   - What can wait until later?

**What you do:**
- Answer each question thoughtfully
- Think like a business owner, not a developer
- Describe **what happens**, not **how to implement** it
- Be specific about edge cases and scenarios

**What the AI generates:**

After all phases, the AI produces a comprehensive **Event Storming Summary Document** with:

1. Domain Overview
2. Key Domain Events (timeline)
3. User Workflows (step-by-step journeys)
4. Actors & Roles
5. Business Rules
6. Pain Points (problems identified)
7. Opportunities (features to consider)
8. **MVP Scope** (what to build first - prioritized)
9. **Post-MVP Features** (what to build later - prioritized)
10. Open Questions

**What you do next:**
1. **Review the Event Storming Summary** carefully
2. **Save it** as `EVENT_STORMING_SUMMARY.md`
3. Use it to inform your answers in Phase 1 (the 15 PRD questions)

**Time estimate:** 45-90 minutes

**Output:** ✅ `EVENT_STORMING_SUMMARY.md` with complete business domain understanding

**Value:** This phase saves days of rework by clarifying requirements upfront. The MVP Scope becomes your PRD scope, Post-MVP Features inform what's out of scope, and Business Rules become your assumptions.

---

## 📝 PHASE 1: Initial Requirements Gathering

**What you do:**
1. Open `ALL_PROMPTS.md`
2. Copy the **INIT_PROMPT**
3. Replace `[INSERT YOUR ONE-SENTENCE PROJECT IDEA HERE]` with your idea
4. Paste it into your AI agent (ChatGPT, Claude, etc.)

**Example prompt:**
```
My initial project idea is: "A simple web landing page built with Astro that displays a random number from a FastAPI backend API."
```

**What the AI does:**

The AI will ask you **exactly 15 questions** designed to extract all necessary information for a comprehensive PRD. Examples include:

- "What is the ultimate long-term vision for this page?"
- "What specific, measurable metric will define the project's success?"
- "Should the user be able to trigger getting a new number without a full page refresh?"
- "What is the expected range for the random number?"
- "What is the acceptable response time for the backend API endpoint?"
- "Are there any specific security considerations?"
- "Does the user interface need to be responsive and work on mobile devices?"
- "Are we assuming a modern browser environment?"
- "Should the project include unit tests for the backend API?"
- "Should the project be fully containerized with Docker?"
- "Are we storing any of the generated numbers in a database?"
- "Is any form of user authentication completely out of scope?"

**What you do:**
- Answer all 15 questions **clearly and completely**
- Be specific (e.g., "95+ Lighthouse score" not "good performance")
- Be honest about unknowns (the AI will help you decide)

**Time estimate:** 15-20 minutes

**Output:** Your 15 detailed answers.

---

## 📋 PHASE 2: PRD Generation

**What the AI does:**

The AI takes your 15 answers and generates a complete **`PRODUCT_REQUIREMENTS_DOCUMENT.md`** with the following sections:

1. **Project Overview & Vision**
   - Project vision statement
   - Problem statement

2. **Strategic Alignment & Success Metrics**
   - Business goal
   - Measurable success metrics (SMART format)

3. **User Stories & Functional Requirements**
   - Table with ID, User Story, Acceptance Criteria, Priority

4. **Non-Functional Requirements (NFRs)**
   - Performance requirements
   - Security requirements
   - Scalability requirements
   - Usability requirements

5. **Assumptions & Dependencies**
   - What we're assuming
   - What we depend on

6. **Scope & Features (MVP)**
   - Checklist of included features

7. **Out of Scope**
   - Explicit list of what we're NOT building

8. **Open Questions & Risks**
   - Table tracking unresolved items

9. **Change History**
   - Version tracking

**What you do:**
1. **Review the PRD carefully** (this is your single source of truth)
2. Check if anything is missing or incorrect
3. Ask the AI to revise specific sections if needed
4. **Save the PRD** to a file: `PRODUCT_REQUIREMENTS_DOCUMENT.md`

**Time estimate:** 5-10 minutes

**Output:** ✅ `PRODUCT_REQUIREMENTS_DOCUMENT.md`

---

## 🛠️ PHASE 3: Tech Stack Definition

**What you do:**
1. Open `ALL_PROMPTS.md`
2. Copy the **TECH_STACK_PROMPT**
3. Paste the **entire PRD** into the prompt where indicated
4. Send it to the AI

**What the AI does:**

The AI analyzes the PRD and generates **`TECH_STACK_DOCUMENT.md`** with:

1. **Frontend Stack**
   - Table with: Category, Technology, Version, Justification
   - Example: "Astro 4.0+ - Chosen to meet the NFR of a 95+ Lighthouse score"

2. **Backend Stack**
   - Table with: Category, Technology, Version, Justification
   - Example: "FastAPI 0.100+ - Chosen for high performance to meet <200ms NFR"

3. **Infrastructure & DevOps**
   - Table with: Category, Tool, Justification
   - Example: "Docker Compose - Required by PRD for easy deployment"

4. **Architecture Diagram**
   - Mermaid diagram showing data flow
   - Example:
     ```mermaid
     graph TD
         A[User] --> B[Frontend: Astro];
         B --> C[Backend: FastAPI];
         C --> B;
     ```

**Every technology choice includes a justification that references the PRD.**

**What you do:**
1. **Review the tech stack**
2. Verify all choices make sense for your project
3. Check that justifications align with PRD requirements
4. Ask for changes if needed
5. **Save the Tech Stack document** to: `TECH_STACK_DOCUMENT.md`

**Time estimate:** 5 minutes

**Output:** ✅ `TECH_STACK_DOCUMENT.md`

---

## 📊 PHASE 4: Staged Handoff Plan Generation

**What you do:**
1. Open `ALL_PROMPTS.md`
2. Copy the **STAGES_PROMPT**
3. Paste **both the PRD and Tech Stack** into the prompt where indicated
4. Send it to the AI

**What the AI does:**

The AI generates **`HANDOFF_STAGES_PLAN.md`** with a granular, checkbox-driven execution plan:

**Structure:**
- **5-7 high-level stages**
- Each stage has **3-5 tasks**
- Each task has **3-7 sub-tasks** (checkboxes)
- **Total: ~100-150 checkboxes** for a typical MVP

**Example structure:**

```
Stage 1: Project Scaffolding & Environment Setup
  Goal: Create foundational structure
  
  Task 1.1: Initialize Monorepo Structure
    [ ] Create root project directory
    [ ] Create frontend subdirectory
    [ ] Create backend subdirectory
    [ ] Create root README.md
    [ ] Initialize Git repository
  
  Task 1.2: Set Up Backend Environment
    [ ] Navigate to backend directory
    [ ] Create pyproject.toml
    [ ] Create virtual environment
    [ ] Install dependencies
  
  Task 1.3: Set Up Frontend Environment
    [ ] Navigate to frontend directory
    [ ] Initialize Astro project
    [ ] Install Tailwind CSS
    [ ] Verify default site runs

Stage 2: Backend API Development
  Goal: Build and validate core API endpoints
  
  Task 2.1: Implement Random Number Endpoint
    [ ] Create main.py
    [ ] Create FastAPI app instance
    [ ] Implement GET /api/random
    [ ] Return JSON response
    [ ] Add CORS middleware
  
  Task 2.2: Write Backend Unit Tests
    [ ] Add pytest to dependencies
    [ ] Create tests directory
    [ ] Write test for 200 status code
    [ ] Write test for response structure

Stage 3: Frontend UI & Logic Development
  [continues...]

Stage 4: Containerization & Integration
  [continues...]

Stage 5: Finalization & Documentation
  [continues...]
```

**What you do:**
1. **Review the plan thoroughly**
2. Check if the stage order makes sense
3. Verify nothing critical is missing
4. Ensure tasks are granular enough to track
5. **Save the Handoff Plan** to: `HANDOFF_STAGES_PLAN.md`

**Time estimate:** 5-10 minutes

**Output:** ✅ `HANDOFF_STAGES_PLAN.md`

---

## ✅ CHECKPOINT: You Now Have Everything

At this point, you have created:
- ✅ `PRODUCT_REQUIREMENTS_DOCUMENT.md`
- ✅ `TECH_STACK_DOCUMENT.md`
- ✅ `HANDOFF_STAGES_PLAN.md`

**Total time invested so far:** 35-55 minutes

**You are now ready to start coding!**

This upfront investment will save you hours (or days) of rework, confusion, and scope creep.

---

## 💻 PHASE 5: Execution - Stage 1

**What you do:**
1. Give the **Handoff Plan** to your AI coding agent
2. Instruct it: "Start with Stage 1, Task 1.1. Execute each sub-task and mark it complete."

**What the AI does:**

The AI reads the Stage 1 goals and begins executing Task 1.1, checking off each sub-task as it completes them:

```
Task 1.1: Initialize Monorepo Structure
  [x] Create root project directory: random-number-generator
  [x] Create frontend subdirectory
  [x] Create backend subdirectory
  [x] Create root README.md with project overview
  [x] Initialize Git repository
```

The AI will then move to Task 1.2, Task 1.3, etc., until all of Stage 1 is complete.

**What you do:**
- **Monitor progress** (watch the AI work)
- **Verify each task** is completed correctly
- **Update the Handoff Plan** with marked checkboxes
- **Test** that everything works as expected

**Time estimate:** Varies by complexity (Stage 1 might take 10-20 minutes)

**Output:** Working project scaffolding with all Stage 1 tasks complete.

---

## 🚪 PHASE 6: Stage Gate (Before Stage 2)

**What happens:**
- The AI finishes all tasks in Stage 1
- **STOP!** Don't proceed to Stage 2 yet

**Why?**
The stage gate ensures the AI asks clarifying questions specific to the next stage, preventing over-engineering and keeping focus on the MVP.

**What you do:**
1. Open `ALL_PROMPTS.md`
2. Copy the **STAGE_GATE_PROMPT**
3. Fill in the current and next stage information
4. Send it to the AI

**Example:**
```
You have successfully completed all tasks for Stage 1: Project Scaffolding & Environment Setup.

Before proceeding to Stage 2: Backend API Development, you must ask me 3 to 5 clarifying questions specific to the goals of the upcoming stage.

Here are the goals for the next stage:
- Implement the /api/random endpoint
- Write backend unit tests

Ask the stage-gate questions now.
```

**What the AI does:**

The AI asks 3-5 specific questions about Stage 2 to clarify implementation details:

1. "Should the API return just a number, or a JSON object with additional metadata?"
2. "What HTTP status code should be returned if an error occurs?"
3. "Do you want logging for each API request?"
4. "Should the tests cover edge cases, or just happy path scenarios?"
5. "Do you want the API to support query parameters (e.g., min/max range)?"

**What you do:**
- Answer each question clearly
- This ensures Stage 2 implementation stays focused and aligned with your vision

**Time estimate:** 5 minutes

**Output:** Clear answers that guide Stage 2 implementation.

---

## 💻 PHASE 7: Execution - Stage 2

**What the AI does:**

Now the AI proceeds to Stage 2 with your clarifications in mind. It executes all tasks in Stage 2, marking checkboxes as complete:

```
Stage 2: Backend API Development

Task 2.1: Implement Random Number Endpoint
  [x] Create main.py in backend directory
  [x] Create FastAPI app instance
  [x] Implement GET endpoint at /api/random
  [x] Return JSON response: {"number": <random_int>}
  [x] Add CORS middleware for frontend domain

Task 2.2: Write Backend Unit Tests
  [x] Add pytest to backend dependencies
  [x] Create tests directory
  [x] Write test verifying 200 status code
  [x] Write test verifying response structure
```

**What you do:**
- Monitor and verify each task
- Test the API endpoint manually if desired
- Mark checkboxes in your Handoff Plan

**Time estimate:** 20-30 minutes (varies by stage complexity)

**Output:** Working backend API with tests.

---

## 🔁 REPEAT: Stage Gates for All Remaining Stages

**The pattern continues:**

1. **Complete a stage** (AI executes all tasks)
2. **Stage gate** (AI asks 3-5 questions about the next stage)
3. **Answer questions** (you provide clarifications)
4. **Execute next stage** (AI proceeds with clarity)

**Stages to complete:**
- ✅ Stage 1: Project Setup
- ✅ Stage 2: Backend API (just completed)
- 🔄 Stage 3: Frontend UI & Logic
- 🔄 Stage 4: Containerization & Integration
- 🔄 Stage 5: Finalization & Documentation

**Each stage gate takes ~5 minutes. Each stage execution takes 15-40 minutes depending on complexity.**

---

## ⏸️ PHASE 8: Pause & Resume (Optional)

**Scenario:** You need to stop work and come back later (end of day, meeting, etc.).

**What you do when pausing:**
1. Save all documents with current checkbox progress
2. Note where you stopped (e.g., "Completed Stage 2, about to start Stage 3")

**What you do when resuming:**
1. Open `ALL_PROMPTS.md`
2. Copy the **CONTINUE_PROMPT**
3. Paste in:
   - Full PRD
   - Full Tech Stack
   - Full Handoff Plan with `[x]` marking all completed tasks
4. Send to the AI

**Example:**
```
We are resuming work on the "Random Number Generator" project.

[Full PRD pasted here]
[Full Tech Stack pasted here]
[Full Handoff Plan with progress pasted here]

Please review the context and state the next step.
```

**What the AI does:**

The AI loads all context and responds:

> "I've reviewed the project context. Here's the current state:
> 
> **Last completed task:** Stage 2, Task 2.2 - Write Backend Unit Tests
> 
> **Next task:** Stage 3, Task 3.1 - Create the Landing Page UI
> 
> This task involves:
> - Modifying the main Astro page
> - Using Tailwind CSS for styling
> - Creating a placeholder for the random number
> - Adding a button to fetch new numbers
> 
> Shall I proceed with this task?"

**What you do:**
- Confirm: "Yes, proceed."
- The AI continues exactly where you left off

**Time estimate:** 2 minutes to resume

**Output:** Seamless continuation with zero context loss.

---

## 🎉 PHASE 9: Completion

**What happens:**
- All stages are complete
- All checkboxes are marked ✅
- The AI has executed the entire Handoff Plan

**Final checklist:**

```
✅ Stage 1: Project Setup - COMPLETE
✅ Stage 2: Backend API - COMPLETE
✅ Stage 3: Frontend UI - COMPLETE
✅ Stage 4: Integration - COMPLETE
✅ Stage 5: Documentation - COMPLETE
```

**Final steps:**
1. **Test the entire application end-to-end**
   - Run `docker-compose up`
   - Visit the frontend in a browser
   - Verify the random number displays
   - Click "New Number" button
   - Verify a new number is fetched

2. **Review the code**
   - Check for code quality
   - Ensure comments are clear
   - Verify tests pass

3. **Review documentation**
   - Ensure README is complete
   - Verify setup instructions work

4. **Deploy (if needed)**
   - Follow your deployment process
   - Test in production environment

**Time estimate:** 30-60 minutes for final review and testing

**Output:** 🎉 **A complete, working, documented project!**

---

## Visual Timeline

```
┌─────────────────────────────────────────────────────────────┐
│                    PLANNING PHASE                           │
│          (35-55 min simple / 90-150 min complex)            │
└─────────────────────────────────────────────────────────────┘

Idea (1 sentence)
    ↓ [5-10 min]
[OPTIONAL] EVENT_STORMING_PROMPT → AI asks 25-35 questions
    ↓ [45-90 min for complex business domains]
Event Storming Summary ✅
    ↓
INIT_PROMPT → AI asks 15 Questions (informed by Event Storming)
    ↓ [15-20 min]
You answer all 15 questions
    ↓ [5-10 min]
AI generates PRD ✅
    ↓ [5 min]
TECH_STACK_PROMPT → You paste PRD
    ↓ [5 min]
AI generates Tech Stack ✅
    ↓ [5-10 min]
STAGES_PROMPT → You paste PRD + Tech Stack
    ↓ [5-10 min]
AI generates Handoff Plan ✅

┌─────────────────────────────────────────────────────────────┐
│                   EXECUTION PHASE                           │
│                   (2-6 hours typical)                       │
└─────────────────────────────────────────────────────────────┘

Stage 1: Project Setup [10-20 min]
    ↓
STAGE_GATE_PROMPT → AI asks 3-5 questions [5 min]
    ↓
Stage 2: Backend API [20-30 min]
    ↓
STAGE_GATE_PROMPT → AI asks 3-5 questions [5 min]
    ↓
Stage 3: Frontend UI [20-40 min]
    ↓
STAGE_GATE_PROMPT → AI asks 3-5 questions [5 min]
    ↓
Stage 4: Integration [15-30 min]
    ↓
STAGE_GATE_PROMPT → AI asks 3-5 questions [5 min]
    ↓
Stage 5: Documentation [15-20 min]
    ↓
Final Testing & Review [30-60 min]

┌─────────────────────────────────────────────────────────────┐
│                   PROJECT COMPLETE! 🎉                      │
└─────────────────────────────────────────────────────────────┘
```

---

## Key Principles to Remember

### ✅ DO:
- **Invest time in planning** (saves hours later)
- **Answer all questions thoroughly** (garbage in = garbage out)
- **Use stage gates** (prevents over-engineering)
- **Review each document** before moving forward
- **Test as you go** (don't wait until the end)
- **Update checkboxes** (track your progress)
- **Use CONTINUE_PROMPT** when resuming (maintains context)

### ❌ DON'T:
- Skip the 15 questions (you'll regret it)
- Skip stage gates (you'll get scope creep)
- Let the AI proceed without reviewing documents
- Assume the AI remembers context without CONTINUE_PROMPT
- Rush through the planning phase
- Add features not in the PRD (scope creep!)

---

## Time Investment Summary

| Phase | Time | Value |
|:------|:-----|:------|
| Event Storming (optional) | 45-90 min | Deep business understanding |
| Planning (Phases 0-4) | 35-55 min | Prevents hours of rework |
| Stage 1 Execution | 10-20 min | Foundation for everything |
| Stage Gates (5 total) | 25 min | Prevents over-engineering |
| Stage Execution (2-5) | 2-4 hours | Actual coding work |
| Final Review | 30-60 min | Quality assurance |
| **TOTAL (Simple)** | **3-6 hours** | **Complete, documented project** |
| **TOTAL (Complex)** | **4-8 hours** | **Complete, well-understood project** |

**Traditional approach without framework:** 8-20 hours with multiple rewrites and scope confusion.

**Time saved:** 5-14 hours on a typical MVP project.

---

## What Makes This Flow Work

1. **Event Storming (Optional):** Discovers business domain before technical planning.
2. **Structured Questions:** The 15 questions force you to think through all aspects upfront.
3. **Single Source of Truth:** The PRD prevents confusion and scope creep.
4. **Justified Decisions:** Every tech choice references a requirement.
5. **Granular Tasks:** 100-150 checkboxes ensure nothing is forgotten.
6. **Stage Gates:** Prevent over-engineering by requiring clarification.
7. **Continuity System:** CONTINUE_PROMPT enables seamless pause/resume.
8. **AI as Partner:** The AI maintains documentation as it works.

---

## Ready to Start?

### For Simple Projects:
1. Open `QUICK_START_GUIDE.md` for a condensed version
2. Open `ALL_PROMPTS.md` to copy the INIT_PROMPT
3. Define your project idea in one sentence
4. Begin with PHASE 1!

### For Complex Business Applications:
1. Open `EVENT_STORMING_GUIDE.md` first
2. Copy the EVENT_STORMING_PROMPT
3. Complete the Event Storming session (PHASE 0.5)
4. Then proceed to PHASE 1 with your Event Storming Summary

**Good luck with your project!** 🚀

