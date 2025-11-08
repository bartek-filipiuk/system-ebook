# AI-Driven Development Framework v2.0

**A production-ready, research-backed framework for building software projects with AI coding agents.**

---

## What's Inside This Package?

This framework provides everything you need to take a project from a simple idea to a fully planned, AI-ready development task. It is based on extensive research of industry best practices from leading organizations including Atlassian, Product School, Aha!, Anthropic, and Miquido.

### Core Documents

1.  **`AI_DRIVEN_DEVELOPMENT_FRAMEWORK.md`** – The complete, comprehensive guide.
    *   Philosophy and workflow
    *   All document schemas (PRD, Tech Stack, Handoff Plan)
    *   All prompts with detailed explanations
    *   A full worked example using Astro + FastAPI

2.  **`EVENT_STORMING_GUIDE.md`** – AI-facilitated Event Storming for complex business domains.
    *   When to use Event Storming vs. skip it
    *   Complete Event Storming prompt
    *   Example session with hair salon booking system
    *   How it integrates with the framework

3.  **`COMPLETE_WORKFLOW.md`** – Step-by-step walkthrough from idea to code.
    *   All phases explained in detail
    *   Time estimates for each phase
    *   Visual timeline
    *   Includes optional Event Storming phase

4.  **`QUICK_START_GUIDE.md`** – A condensed, step-by-step guide to get started immediately.

5.  **`ALL_PROMPTS.md`** – All the prompts in one place for easy copy-paste access.

6.  **`README.md`** – This file, your starting point.

---

## Who Is This For?

*   **Solo developers** who want to use AI coding agents to build projects faster.
*   **Product managers** who need to create clear, AI-consumable specifications.
*   **Teams** who want a structured, repeatable process for AI-assisted development.
*   **Anyone** who is tired of vague requirements and wants a system that works.

---

## Why Use This Framework?

### The Problem

Most people approach AI coding agents with vague instructions and then wonder why the results are inconsistent or off-target. Without a clear structure, the AI makes assumptions, over-engineers solutions, or misses critical requirements.

### The Solution

This framework provides:

*   **Event Storming (Optional):** Discovers business domain before technical planning.
*   **Structured Prompts:** Forces the AI to ask the right questions upfront.
*   **Clear Documentation:** Creates a single source of truth for the project.
*   **Granular Plans:** Breaks down work into trackable, verifiable tasks.
*   **Stage Gates:** Prevents scope creep by requiring clarification before each new phase.
*   **Continuity:** Enables you to pause and resume work without losing context.

### The Result

You get:

*   **Faster Development:** The AI knows exactly what to build.
*   **Higher Quality:** Clear requirements lead to better code.
*   **Less Rework:** Fewer misunderstandings mean fewer iterations.
*   **Full Control:** You maintain oversight through stage gates and checkboxes.

---

## How to Use This Framework

### Option 1: Quick Start (Recommended for First-Time Users)

1.  Read the **`QUICK_START_GUIDE.md`**.
2.  Follow the 7 steps.
3.  Use the prompts from **`ALL_PROMPTS.md`**.

### Option 2: Deep Dive (Recommended for Complex Projects)

1.  Read the full **`AI_DRIVEN_DEVELOPMENT_FRAMEWORK.md`**.
2.  Study the example project to understand the flow.
3.  Adapt the schemas and prompts to your specific needs.

---

## The Workflow (At a Glance)

| Step | You Do | AI Does | Output |
| :--- | :--- | :--- | :--- |
| 0 | Define your idea | — | Your notes |
| 0.5 (Optional) | Use `EVENT_STORMING_PROMPT` | Asks 25-35 questions about business domain | `EVENT_STORMING_SUMMARY.md` |
| 1 | Use `INIT_PROMPT` | Asks 15 questions | Questions |
| 2 | Answer questions | Generates PRD | `PRD.md` |
| 3 | Use `TECH_STACK_PROMPT` | Generates Tech Stack | `TECH_STACK.md` |
| 4 | Use `STAGES_PROMPT` | Generates Handoff Plan | `HANDOFF_STAGES.md` |
| 5 | Use `STAGE_GATE_PROMPT` | Asks stage questions, executes tasks | Code + progress |
| 6 | Use `CONTINUE_PROMPT` | Resumes work | Continuation |

---

## Key Principles

This framework is built on three core principles:

1.  **Clarity Over Comprehensiveness:** "Just enough" documentation to eliminate ambiguity, not to document every possibility.
2.  **Structure is Freedom:** A rigid structure gives the AI the clarity it needs to make effective implementation decisions.
3.  **Documentation as AI Memory:** Documentation is a dynamic, evolving memory store for the AI agent, not a static reference for humans.

---

## What Makes This Framework Different?

*   **Research-Backed:** Based on best practices from industry leaders, not personal opinion.
*   **AI-Native:** Designed specifically for AI agents, not adapted from human workflows.
*   **Stage Gates:** Prevents over-engineering by requiring clarification before each phase.
*   **Granular Plans:** 100-150 checkboxes for a typical MVP, ensuring nothing is missed.
*   **Continuity System:** The `CONTINUE_PROMPT` enables seamless resumption of work.

---

## Example Project

The framework includes a complete worked example:

**Project:** A simple landing page using Astro that fetches a random number from a FastAPI backend.

**What's Included:**
*   The 15 questions the AI asks
*   Sample answers
*   The generated PRD
*   The generated Tech Stack document
*   The generated Handoff Plan with all stages and tasks

This example demonstrates the entire process from start to finish.

---

## Research Foundation

This framework synthesizes insights from:

*   **Atlassian:** "Just enough" documentation, progressive disclosure, collaboration principles
*   **Product School:** Living documents, comprehensive PRD structure
*   **Aha!:** Strategic alignment, explicit assumptions
*   **Anthropic:** Simplicity, transparency, tool documentation for AI agents
*   **Miquido:** Handoff checklists, knowledge transfer best practices
*   **Industry Experts:** Documentation as AI memory patterns

All research sources are documented in the main framework document.

---

## Getting Started Right Now

### For Simple Projects:
1.  Open **`QUICK_START_GUIDE.md`**.
2.  Define your project idea in one sentence.
3.  Copy the `INIT_PROMPT` from **`ALL_PROMPTS.md`**.
4.  Paste it into your AI agent and replace the placeholder with your idea.
5.  Answer the 15 questions.
6.  Follow the remaining steps.

### For Complex Business Applications:
1.  Open **`EVENT_STORMING_GUIDE.md`** first.
2.  Copy the `EVENT_STORMING_PROMPT` from **`ALL_PROMPTS.md`**.
3.  Complete the Event Storming session (45-90 minutes).
4.  Save the Event Storming Summary.
5.  Then proceed with the `INIT_PROMPT` using insights from Event Storming.
6.  Follow the remaining steps.

That's it. You're on your way to building your project with AI.

---

## License

This framework is **free to use and adapt** for any project, personal or commercial.

---

## Version History

*   **v2.1 (2025-10-27):** Added Event Storming guide for complex business domains. Updated workflow to include optional Phase 0.5.
*   **v2.0 (2025-10-27):** Complete rewrite based on comprehensive industry research. Added stage gates, granular planning, and continuity system.
*   **v1.0 (Initial):** Basic framework with PRD, Tech Stack, and Handoff documents.

---

## Questions or Feedback?

This framework is a living document. If you have suggestions for improvements or encounter any issues, feel free to adapt it to your needs.

---

**Ready to build? Start with the Quick Start Guide!**

