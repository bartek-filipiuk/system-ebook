# Modified STAGES_PROMPT for Vertical Slice Development

**When to use:** During Phase 4 (Stages Plan Generation) if you prefer vertical-slice, iterative development.

**Copy and paste this prompt instead of the standard STAGES_PROMPT from `ALL_PROMPTS.md`.**

---

```markdown
Perfect. The Tech Stack is defined.

Now for the final planning step before coding: **Step 3: Staged Handoff Plan.**

Your task is to create a `HANDOFF_STAGES_PLAN.md` document. This document will break down the entire development process into logical, sequential stages using a **vertical-slice, iterative development approach**.

---

## Development Approach: Vertical Slices

**CRITICAL INSTRUCTIONS:**

### Stage 1: Minimal Working Installation
The first stage MUST create a minimal working installation that proves the stack works end-to-end:
- Basic project scaffolding (directories, config files, Git repo)
- Simple backend with ONE trivial endpoint (e.g., `GET /api/health` that returns `{"status": "ok"}`)
- Simple frontend with ONE page that calls the backend endpoint and displays the response
- Docker/containerization setup (if specified in Tech Stack)
- End-to-end verification (frontend → backend → response)
- **NO business logic, NO real features, NO database yet** (unless absolutely necessary)

**Goal:** Prove that the frontend can talk to the backend. Nothing more.

### Stages 2-N: Feature Vertical Slices
Each subsequent stage MUST implement ONE complete feature as a vertical slice:

**Each feature stage must include all 4 layers:**
1. **Backend Development**
   - API endpoint(s) for this specific feature
   - Database models/migrations (if needed for this feature)
   - Business logic for this feature
   - Validation and error handling
   - Unit tests for the backend

2. **Frontend Development**
   - UI components for this specific feature
   - Forms, inputs, displays
   - Loading and error states
   - Styling

3. **Integration**
   - Connect frontend to backend API
   - Handle API responses
   - Handle errors
   - Update UI based on data

4. **End-to-End Testing**
   - Test the complete feature flow
   - Verify data persistence (if applicable)
   - Test edge cases
   - Verify error handling

**Goal:** Deliver a fully working, testable feature that integrates into the existing system.

### Final Stage: Polish & Finalization
The last stage MUST focus on production readiness:
- Code refactoring and cleanup
- Comprehensive error handling
- Performance optimization
- Security hardening
- Documentation (README, API docs)
- Final end-to-end testing
- Deployment preparation

---

## Critical Rules for Stage Organization

1. **Organize by FEATURE, not by LAYER**
   - ❌ WRONG: "Stage 2: All Backend APIs", "Stage 3: All Frontend Pages"
   - ✅ CORRECT: "Stage 2: User Registration Feature", "Stage 3: User Login Feature"

2. **Each feature stage delivers a complete vertical slice**
   - ❌ WRONG: Backend in one stage, frontend in another
   - ✅ CORRECT: Backend + Frontend + Integration in the same stage

3. **Each stage builds on a working system**
   - After Stage 1, the system is working (even if trivial)
   - After Stage 2, the system is working with Feature A
   - After Stage 3, the system is working with Features A + B
   - And so on...

4. **Use PRD User Stories to determine features**
   - Each User Story (from PRD Section 3) should map to one feature stage
   - Prioritize based on the Priority column (Must-Have first)
   - If a User Story is too large, split it into multiple stages

5. **Keep features small and focused**
   - Aim for 3-7 feature stages (not counting Stage 1 and final stage)
   - Each feature stage should take 1-3 hours to complete
   - If a feature is too large, break it into smaller features

---

## Task Breakdown Within Each Stage

For each stage, break down the work into specific, actionable tasks with checkbox sub-tasks:

**Example for a feature stage:**

```
## Stage 3: Appointment Booking Feature (Vertical Slice)

**Goal:** Implement the ability for customers to book appointments.

- [ ] **Task 3.1: Backend - Booking API**
    - [ ] Create database model for Booking
    - [ ] Create database migration
    - [ ] Create POST /api/bookings endpoint
    - [ ] Validate booking data
    - [ ] Check for double-booking
    - [ ] Save booking to database
    - [ ] Return booking confirmation
    - [ ] Write unit tests

- [ ] **Task 3.2: Frontend - Booking Form**
    - [ ] Create BookingPage component
    - [ ] Create BookingForm component
    - [ ] Add service selection dropdown
    - [ ] Add date/time pickers
    - [ ] Add customer info inputs
    - [ ] Add form validation
    - [ ] Add submit button

- [ ] **Task 3.3: Integration**
    - [ ] Connect form to POST /api/bookings
    - [ ] Handle successful booking
    - [ ] Handle validation errors
    - [ ] Handle double-booking errors
    - [ ] Clear form after success

- [ ] **Task 3.4: End-to-End Testing**
    - [ ] Submit valid booking
    - [ ] Verify confirmation appears
    - [ ] Check database for saved booking
    - [ ] Test double-booking prevention
    - [ ] Test form validation
```

---

## Your Task

Using the PRD and Tech Stack documents provided below, generate a complete `HANDOFF_STAGES_PLAN.md` following the vertical-slice approach described above.

**The plan must:**
- Start with Stage 1: Minimal Working Installation
- Include 3-7 feature stages (one per User Story from the PRD)
- End with a Polish & Finalization stage
- Have 3-5 tasks per stage
- Have 3-7 checkbox sub-tasks per task
- Be clear enough for an AI coding agent to execute without ambiguity

---

## Documents for Reference

**PRD:**
---
[PASTE THE FULL PRD MARKDOWN HERE]
---

**Tech Stack:**
---
[PASTE THE FULL TECH STACK MARKDOWN HERE]
---

Generate the Staged Handoff Plan now using the vertical-slice approach.
```

---

## How to Use This Prompt

1. **Copy the entire prompt above** (everything between the triple backticks)
2. **Replace `[PASTE THE FULL PRD MARKDOWN HERE]`** with your actual PRD
3. **Replace `[PASTE THE FULL TECH STACK MARKDOWN HERE]`** with your actual Tech Stack document
4. **Paste it into your AI agent**
5. **The AI will generate a vertical-slice Handoff Plan**

---

## What You'll Get

A Handoff Plan structured like this:

```
Stage 1: Minimal Working Installation
  - Basic scaffolding
  - Simple backend endpoint
  - Simple frontend page
  - End-to-end connection

Stage 2: [Feature A] (Vertical Slice)
  - Backend for Feature A
  - Frontend for Feature A
  - Integration
  - Testing

Stage 3: [Feature B] (Vertical Slice)
  - Backend for Feature B
  - Frontend for Feature B
  - Integration
  - Testing

...

Final Stage: Polish & Finalization
  - Refactoring
  - Error handling
  - Documentation
  - Final testing
```

---

## Comparison with Standard STAGES_PROMPT

| Aspect | Standard STAGES_PROMPT | Vertical Slice STAGES_PROMPT |
|:-------|:-----------------------|:-----------------------------|
| **Organization** | By technology layer | By business feature |
| **Stage 2** | "Backend Development" | "Feature A (Backend + Frontend)" |
| **Stage 3** | "Frontend Development" | "Feature B (Backend + Frontend)" |
| **Working system** | After Stage 4 | After Stage 1 |
| **Best for** | Simple projects | Medium to complex projects |

---

**Use this modified prompt to generate vertical-slice Handoff Plans!** 🚀

