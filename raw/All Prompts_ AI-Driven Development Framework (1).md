# All Prompts: AI-Driven Development Framework

This document contains all the prompts you need, ready to copy and paste.

---

## 1. INIT_PROMPT

**When to use:** At the very beginning of a new project.

```
You are an expert AI software architect and project manager. Your task is to guide me through a structured process to define and plan a new software project for an AI coding agent to build.

We will follow a multi-stage process:
1.  **PRD Generation:** You will first help me create a detailed Product Requirements Document (PRD).
2.  **Tech Stack Definition:** Based on the PRD, you will define the technology stack.
3.  **Staged Plan:** Finally, you will create a step-by-step execution plan with stages and checklists.

Let's begin with **Step 1: PRD Generation.**

My initial project idea is: **[INSERT YOUR ONE-SENTENCE PROJECT IDEA HERE]**

Based on this idea, your immediate and only task is to ask me exactly **15 clarifying questions** to gather all necessary details for a comprehensive PRD. The questions must be designed to extract information for all sections of the PRD, including:

- Project Vision & Strategic Goals
- Measurable Success Metrics
- Specific User Stories and their Acceptance Criteria
- Key Non-Functional Requirements (Performance, Security, etc.)
- Assumptions and potential Dependencies
- What is explicitly IN and OUT of scope for the MVP
- Any known Risks or Open Questions

Do not ask fewer or more than 15 questions. After I provide the answers, you will then generate the complete PRD document. 

Begin by asking the 15 questions now.
```

---

## 2. TECH_STACK_PROMPT

**When to use:** After the PRD has been successfully generated.

```
Excellent. The PRD is now complete and provides a clear picture of the project's requirements.

Now, let's move to **Step 2: Tech Stack Definition.**

Based *only* on the PRD we just created, your task is to generate a `TECH_STACK_DOCUMENT.md`. This document must detail the technologies, frameworks, and infrastructure for the project.

Use the provided PRD as your single source of truth. The document must follow the established schema, including sections for Frontend, Backend, and Infrastructure/DevOps. For every technology choice, you must provide a concise justification in the table, directly referencing a requirement from the PRD (e.g., "Chosen for its high performance to meet the <150ms NFR.").

Finally, include a simple Mermaid diagram illustrating the high-level architecture.

Here is the complete PRD for your reference:

---
[PASTE THE FULL PRD MARKDOWN HERE]
---

Generate the Tech Stack document now.
```

---

## 3. STAGES_PROMPT

**When to use:** After the Tech Stack document has been generated.

**Note:** If you prefer vertical-slice (iterative, feature-by-feature) development instead of the default horizontal approach, use `STAGES_PROMPT_VERTICAL_SLICES.md` instead of this prompt.

```
Perfect. The Tech Stack is defined.

Now for the final planning step before coding: **Step 3: Staged Handoff Plan.**

Your task is to create a `HANDOFF_STAGES_PLAN.md` document. This document will break down the entire development process into logical, sequential stages. Each stage must contain a list of specific, actionable tasks, and each task must be broken down further into verifiable sub-tasks formatted as checkboxes.

The plan must be so clear and granular that an AI coding agent can follow it from start to finish without ambiguity. The stages should logically progress from project setup, to backend development, to frontend development, to final integration and documentation.

Use the PRD and the Tech Stack documents as your only guides.

Here are the documents for your reference:

**PRD:**
---
[PASTE THE FULL PRD MARKDOWN HERE]
---

**Tech Stack:**
---
[PASTE THE FULL TECH STACK MARKDOWN HERE]
---

Generate the Staged Handoff Plan now.
```

---

## 4. STAGE_GATE_PROMPT

**When to use:** When the AI agent completes all tasks in a stage and is ready to move to the next.

```
You have successfully completed all tasks for **Stage [CURRENT STAGE NUMBER]: [CURRENT STAGE NAME]**.

Before proceeding to **Stage [NEXT STAGE NUMBER]: [NEXT STAGE NAME]**, you must ask me **3 to 5 clarifying questions** specific to the goals of the upcoming stage. These questions should be designed to resolve any potential ambiguities and ensure your implementation plan for this stage is efficient and precisely aligned with the PRD.

Here are the goals for the next stage:

[LIST THE GOAL AND KEY TASKS FOR THE NEXT STAGE FROM THE HANDOFF PLAN]

Do not start work on the next stage until I have answered your questions.

Ask the stage-gate questions now.
```

---

## 5. CONTINUE_PROMPT

**When to use:** When you are resuming work on a project after a pause.

```
We are resuming work on the **"[PROJECT NAME]"** project.

I am providing you with the full project context, including the PRD, the Tech Stack, and the Handoff Plan with its current progress. Your task is to:

1.  Thoroughly review all provided documents to fully load the project context.
2.  Acknowledge the current state by summarizing the last task that was completed.
3.  State the very next sub-task on the checklist that needs to be executed.
4.  Wait for my confirmation before you proceed with executing that next task.

Here is the complete project context:

**1. Product Requirements Document (PRD):**
---
[PASTE FULL PRD CONTENT HERE]
---

**2. Tech Stack & Architecture:**
---
[PASTE FULL TECH STACK CONTENT HERE]
---

**3. Handoff & Stages Plan (Current Progress):**
---
[PASTE HANDOFF/STAGES CONTENT HERE, WITH [x] MARKING ALL COMPLETED SUB-TASKS]
---

Please review the context and state the next step. Do not take any action until I confirm.
```

---

**End of Prompts Document**

Copy and paste these prompts as needed throughout your project workflow.




---

## 0. EVENT_STORMING_PROMPT (Optional - For Complex Business Domains)

**When to use:** Before INIT_PROMPT, if your project involves complex business processes, multiple user types, or workflows.

```
You are an expert business analyst and Event Storming facilitator. Your task is to help me explore my business domain through a structured Event Storming session.

I will play the role of the **business stakeholder/client**, and you will act as the **facilitator**, asking me targeted questions to discover:

1. **Domain Events** – Key things that happen in my business
2. **User Workflows** – How users interact with the system
3. **Business Rules** – Constraints and logic
4. **Pain Points** – Problems to solve
5. **Opportunities** – Features to build
6. **MVP Scope** – What to build first
7. **Post-MVP Features** – What comes later

---

## My Project Idea

[INSERT YOUR PROJECT IDEA HERE - Can be 1-3 sentences]

**Example:** "I want to build an online booking system for a hair salon where customers can book appointments, stylists can manage their schedules, and the owner can see revenue reports."

---

## Your Task

Conduct a **Big Picture Event Storming session** with me by asking questions in the following sequence:

### Phase 1: Domain Discovery (5-7 questions)
Ask me about the key events that happen in my business domain. Focus on:
- What are the main activities or processes?
- Who are the key actors (users, roles)?
- What triggers these activities?
- What are the outcomes?

### Phase 2: User Workflows (5-7 questions)
Ask me about how users interact with the system. Focus on:
- What does a typical user journey look like?
- What are the key decision points?
- What happens when things go wrong?
- What are the different user types?

### Phase 3: Business Rules & Constraints (3-5 questions)
Ask me about the rules and logic. Focus on:
- What business rules must the system enforce?
- What are the constraints (time, capacity, permissions)?
- What validations are needed?

### Phase 4: Pain Points & Opportunities (3-5 questions)
Ask me about problems and improvements. Focus on:
- What are the current pain points in the process?
- What manual work could be automated?
- What would make the biggest impact?

### Phase 5: MVP vs. Post-MVP (3-5 questions)
Ask me about prioritization. Focus on:
- What is absolutely essential for the first version?
- What can wait until later?
- What would be nice to have but not critical?

---

## Output Format

After I answer all your questions, generate a comprehensive **Event Storming Summary Document** with the following sections:

1. **Domain Overview** – High-level summary of the business domain
2. **Key Domain Events** – Timeline of major events
3. **User Workflows** – Step-by-step user journeys
4. **Actors & Roles** – Who interacts with the system
5. **Business Rules** – Constraints and logic
6. **Pain Points** – Problems identified
7. **Opportunities** – Features to consider
8. **MVP Scope** – What to build first (prioritized)
9. **Post-MVP Features** – What to build later (prioritized)
10. **Open Questions** – Anything still unclear

---

## Important Instructions

- Ask questions **one phase at a time**
- Wait for my answers before moving to the next phase
- If my answer is unclear, ask follow-up questions
- Help me think through edge cases and scenarios
- Challenge assumptions when appropriate
- Keep the focus on **what happens** (events), not **how to implement** (technical details)

Begin by asking the **Phase 1: Domain Discovery** questions now.
```

---

**Note:** After completing Event Storming, save the generated summary as `EVENT_STORMING_SUMMARY.md` and use it to inform your answers when you proceed to the INIT_PROMPT (15 questions).

