# From Idea to Working Code in 4-8 Hours: The Structured Framework for AI-Driven Development

---

## Chapter 1: The Problem

You already use AI coding tools. You've seen what they can do. You've experienced those magical moments when Claude or Cursor generates exactly what you need.

You've also experienced the other moments.

The AI builds features you didn't ask for. It over-engineers a simple task into a complex architecture. You spend 20 minutes explaining your project, only to realize the AI forgot everything when you resume work the next day. You ask for a booking form and get a full authentication system you never wanted.

### The Four Pain Points

**1. You Build the Wrong Thing**

You start with a vague idea: "Build me a booking system." The AI asks a few questions, then starts coding. Two hours later, you have a system with features you don't need and missing the ones you do. You spend another hour explaining what you actually wanted. The AI rebuilds it. Still not right. Repeat.

Without clear requirements upfront, the AI guesses. Sometimes it guesses right. Usually it doesn't.

**2. The AI Adds Unwanted Features**

You ask for a simple appointment booking feature. The AI gives you booking, cancellation, rescheduling, waitlists, email confirmations, SMS reminders, and a loyalty program.

It's trying to be helpful. But you just needed booking. Now you have to remove or ignore 70% of what it built. Or worse, you accept it all and end up maintaining code you never wanted.

**3. You Lose Context When Resuming Work**

You work on a project for two hours. Make solid progress. Save your work. Come back tomorrow.

"Continue where we left off," you tell the AI.

It has no idea where you were. You paste in files. Explain what you were doing. Remind it of decisions you made yesterday. By the time the AI is up to speed, you've wasted 15 minutes. And it still doesn't have the full context.

**4. Integration Becomes a Nightmare**

You build the backend first. Five API endpoints, all working perfectly. Then you build the frontend. Five pages, looking great. Now you need to connect them.

Nothing works. The API returns data in one format, the frontend expects another. You forgot to add CORS. The error messages don't match what the frontend expects. You spend three hours debugging integration issues that could have been avoided.

### What's Missing

You don't need better AI models. You don't need more features. You don't need longer context windows.

You need **structure**.

A systematic approach that forces clarity upfront. That prevents scope creep during execution. That maintains context across sessions. That integrates continuously instead of all at once.

### The Cost of No Structure

Without a framework, you waste time:

- **2-4 hours** clarifying requirements through trial and error
- **1-3 hours** removing unwanted features or fixing over-engineered code
- **1-2 hours** re-explaining context when resuming work
- **2-5 hours** debugging integration issues at the end

**Total waste: 6-14 hours** on a project that should take 4-8 hours.

The framework eliminates this waste.

### What You Need Instead

A structured process that:

1. **Forces clarity before coding** → Eliminate the wrong-thing problem
2. **Defines explicit scope boundaries** → Prevent feature creep
3. **Maintains documentation as memory** → Never lose context
4. **Integrates continuously** → Avoid big-bang integration failures
5. **Works with any AI tool** → Universal approach

This framework does all five.

---

<!-- PAGE BREAK -->

## Chapter 2: The Framework Overview

Here's how the framework works: you invest 30-60 minutes in structured planning, then execute with clarity. The AI knows exactly what to build, what NOT to build, and how to organize the work.

### The 8 Phases

| Phase | You Do | AI Does | Time | Output |
|:------|:-------|:--------|:-----|:-------|
| **0** | Define idea (1 sentence) | — | 5 min | Clear project statement |
| **0.5** | Use Event Storming (optional) | Asks 25-35 business questions | 45-90 min | Business domain map |
| **1** | Use INIT_PROMPT | Asks 15 requirement questions | 15 min | Your answers |
| **2** | Answer questions | Generates PRD | 5 min | Complete PRD document |
| **3** | Use TECH_STACK_PROMPT | Generates tech stack | 5 min | Justified tech choices |
| **4** | Use STAGES_PROMPT | Generates execution plan | 10 min | 100-150 checkboxes |
| **5-7** | Use STAGE_GATE_PROMPT | Builds + asks gate questions | 2-6 hrs | Working code |
| **8** | Use CONTINUE_PROMPT | Resumes seamlessly | 2 min | Context restored |

**Total planning time:** 40-60 minutes (simple) or 90-150 minutes (complex business apps)

**Total execution time:** 2-6 hours

**Total project time:** 3-8 hours from idea to working code

### Compare to Traditional Approach

**Without the framework:**

You ↓ AI ↓ Time ↓ Result
- "Build me a booking system" → Asks 3-5 vague questions → 15 min → Starts coding
- Realizes it's wrong → Rebuilds → 1 hr → Still not quite right
- Adds features you didn't ask for → Argues with AI → 30 min → Remove unwanted code
- Lose context overnight → Re-explain everything → 20 min → Partial context
- Backend done, frontend done → Integration fails → 3 hrs → Debugging nightmare
- **Total: 8-20 hours** with frustration and rework

**With the framework:**

You ↓ AI ↓ Time ↓ Result
- Answer 15 structured questions → Generates perfect PRD → 20 min → Single source of truth
- Approve tech stack → Justifies every choice → 5 min → No over-engineering
- Review execution plan → 150 checkboxes → 10 min → Nothing forgotten
- Stage gates prevent scope creep → Asks before adding features → 25 min → Only what you want
- Resume work next day → Full context instantly → 2 min → Zero time wasted
- **Total: 4-8 hours** with confidence and control

### What Makes This Framework Different

**1. Research-Backed**

This isn't one person's opinion. The framework synthesizes best practices from:

- Atlassian (progressive disclosure, "just enough" documentation)
- Product School (living documents, comprehensive PRD structure)
- Anthropic (simplicity, transparency for AI agents)
- Industry experts (documentation as AI memory)

Every document structure, every prompt, every principle comes from proven approaches.

**2. AI-Native**

This framework was designed FOR AI agents, not adapted from human workflows.

Traditional PRDs are written for humans to read. This PRD is written for AI to execute against. The structure forces the information AI needs: explicit scope boundaries, measurable success metrics, clear assumptions.

Traditional handoff plans are high-level summaries. This handoff plan has 100-150 granular checkboxes because AI needs that level of detail.

**3. Stage Gates Prevent Over-Engineering**

Before starting each major phase, the AI must ask 3-5 clarifying questions. This prevents the AI from making assumptions or adding features you didn't request.

Without stage gates: "Build the backend" → AI builds 10 endpoints, authentication, caching, rate limiting, logging, monitoring.

With stage gates: "Before building the backend, I need to ask: Should I include authentication in this stage, or is that out of scope for the MVP?"

You: "Out of scope."

AI: Builds only what you need.

**4. Granular Plans (100-150 Checkboxes)**

A typical MVP generates a handoff plan with 100-150 checkboxes across 5-7 stages.

Why so many? Because AI needs explicit instructions. "Build the frontend" is too vague. "Create homepage component with loading state and error handling" is clear.

Every checkbox is verifiable. Either it's done or it's not. No ambiguity.

**5. Continuity System**

The CONTINUE_PROMPT solves the context-loss problem. You paste in three documents (PRD, Tech Stack, Handoff Plan with progress marked), and the AI instantly knows:

- What you're building
- Why you're building it
- What technologies you're using
- What's already done
- What's next

Zero time wasted re-explaining. Zero context loss.

### The Two Optional Enhancements

**Event Storming (Phase 0.5)**

For complex business applications, spend 45-90 minutes in an AI-facilitated Event Storming session before creating the PRD. The AI asks targeted questions to discover your business domain, user workflows, and pain points.

When to use: Booking systems, e-commerce, workflow automation, multi-role applications.

When to skip: Simple projects with clear requirements.

**Vertical Slice Development**

Instead of building all backend APIs first, then all frontend pages (horizontal), build one complete feature at a time from backend to frontend to integration (vertical).

When to use: Projects with 4+ features, need early demos, continuous integration.

When to skip: Very simple projects (1-3 features).

Both approaches are fully supported. You choose based on your project needs.

### What You Get at the End

After 4-8 hours, you have:

✅ Working code (fully functional MVP)
✅ Complete documentation (PRD, Tech Stack, Handoff Plan)
✅ Justified tech choices (every decision documented)
✅ Test coverage (included in checkboxes)
✅ Clear scope boundaries (you know exactly what's in and out)
✅ Context preservation (resume work anytime with CONTINUE_PROMPT)
✅ Zero technical debt from scope creep

Not a prototype. Not a proof-of-concept. A production-ready MVP.

**Next:** Let's start with Phase 0.

---

<!-- PAGE BREAK -->

## Chapter 3: Phase 0 - Define Your Idea

Before you use any prompts, before you open your AI tool, you need one thing: a clear project idea.

Not a business plan. Not a feature list. Not a technical specification. Just one sentence that describes what you're building.

### The One-Sentence Rule

Your project idea must fit in one sentence. If you can't describe it in one sentence, it's not clear enough yet.

**Good examples:**
- "An online booking system for a hair salon where customers can book appointments and stylists can manage schedules."
- "A dashboard that displays real-time cryptocurrency prices from an external API."
- "A task management app where teams can create projects, assign tasks, and track completion."

**Bad examples:**
- "A booking system." (Too vague - what kind? Who uses it?)
- "I want to build something like Calendly but better with more features and also maybe some AI." (Not one sentence, unclear scope)
- "A platform." (Meaningless without context)

### The Quick Decision: Simple or Complex?

Once you have your one-sentence idea, ask yourself:

**Does this involve complex business processes, multiple user roles, or workflows?**

→ **YES**: Use Event Storming (Phase 0.5) before moving to the PRD.

Examples: booking systems, e-commerce, project management, multi-tenant SaaS.

→ **NO**: Skip Event Storming and go straight to INIT_PROMPT (Phase 1).

Examples: landing pages, simple dashboards, single-feature tools, APIs without complex business logic.

### Phase 0 Checklist

Before proceeding, verify:

- [ ] Your idea fits in one sentence
- [ ] You know who will use the system
- [ ] You know the primary problem it solves
- [ ] You've decided: Event Storming (complex) or skip to PRD (simple)

That's it. Five minutes of clarity now saves hours of confusion later.

### Example: Hair Salon Booking System

**One-sentence idea:**
"An online booking system for a hair salon where customers can book appointments, stylists manage their schedules, and the owner views revenue reports."

**Quick decision:**
- Complex business process? Yes (booking, scheduling, payments)
- Multiple user roles? Yes (customer, stylist, owner)
- Workflows? Yes (booking flow, cancellation flow, reminder flow)

**Decision:** Use Event Storming before creating the PRD.

### Example: Cryptocurrency Dashboard

**One-sentence idea:**
"A dashboard that displays real-time prices for the top 10 cryptocurrencies using the CoinGecko API."

**Quick decision:**
- Complex business process? No (just display data)
- Multiple user roles? No (viewers only)
- Workflows? No (fetch and display)

**Decision:** Skip Event Storming, go straight to INIT_PROMPT.

### What's Next?

**If complex:** Proceed to Chapter 4 (Event Storming).

**If simple:** Skip to Chapter 5 (Generate the PRD).

---

<!-- PAGE BREAK -->

## Chapter 4: Phase 0.5 - Event Storming (Optional)

Event Storming is for complex business applications. If your project involves multiple user roles, business workflows, or domain logic, spend 45-90 minutes here. You'll save days of rework later.

If your project is simple (a landing page, a dashboard, a single-feature tool), skip this chapter and go to Chapter 5.

### What Event Storming Does

Traditional approach: You describe your idea vaguely. The AI guesses at requirements. You build. Realize it's wrong. Rebuild.

Event Storming approach: The AI asks 25-35 targeted questions about your business domain. You answer. The AI generates a complete business model with MVP scope defined. You build it right the first time.

### The 5-Phase Questioning Structure

The AI acts as a facilitator and asks questions in five phases:

**Phase 1: Domain Discovery (5-7 questions)**
- What are the main activities in your business?
- Who are the key actors (users, roles)?
- What triggers these activities?
- What are the outcomes?

**Phase 2: User Workflows (5-7 questions)**
- What does a typical user journey look like?
- What are the decision points?
- What happens when things go wrong?
- How do different user types interact?

**Phase 3: Business Rules & Constraints (3-5 questions)**
- What rules must the system enforce?
- What are the constraints (time, capacity, permissions)?
- What validations are needed?

**Phase 4: Pain Points & Opportunities (3-5 questions)**
- What are the current problems?
- What manual work could be automated?
- What would make the biggest impact?

**Phase 5: MVP vs. Post-MVP (3-5 questions)**
- What is absolutely essential for the first version?
- What can wait until later?
- What would be nice to have but not critical?

### What You Get: The Event Storming Summary

After you answer all questions, the AI generates a comprehensive document with 10 sections:

1. **Domain Overview** - High-level summary of your business
2. **Key Domain Events** - Timeline of what happens in your system
3. **User Workflows** - Step-by-step user journeys
4. **Actors & Roles** - Who interacts with the system
5. **Business Rules** - Constraints and logic the system must enforce
6. **Pain Points** - Problems identified
7. **Opportunities** - Features to consider
8. **MVP Scope** - What to build first (prioritized)
9. **Post-MVP Features** - What to build later (prioritized)
10. **Open Questions** - Anything still unclear

### Example: Hair Salon Booking System

**Your one-sentence idea:**
"An online booking system for a hair salon where customers can book appointments, stylists manage schedules, and the owner views revenue reports."

**Phase 1 - Domain Discovery (AI asks):**
- What types of services does the salon offer?
- Walk me through what happens from booking to completion.
- Who are the key actors in this system?
- What triggers the booking process?
- What happens after an appointment is completed?

**You answer each question. The AI moves to Phase 2.**

**Phase 2 - User Workflows (AI asks):**
- What does a customer's booking journey look like?
- How do stylists manage their availability?
- What happens if a customer cancels?
- What are the different user types and their needs?

**You answer. AI continues through all 5 phases.**

**What the AI generates (condensed example):**

```markdown
# Event Storming Summary: Hair Salon Booking System

## MVP Scope (Build First)
✅ Customer can view services and prices
✅ Customer can see available time slots
✅ Customer can book an appointment
✅ Customer receives email confirmation
✅ Stylist can view their schedule
✅ Stylist can mark availability
✅ System prevents double-booking
✅ Owner can view basic revenue report
✅ Automated reminder 24 hours before appointment
✅ Customer can cancel (with 24-hour rule)

## Out of MVP (Post-MVP Features)
❌ Payment processing (manual for MVP)
❌ Customer reviews/ratings
❌ SMS reminders
❌ Mobile app
❌ Loyalty program
❌ Multi-location support
```

### How This Feeds Into the PRD

The Event Storming Summary becomes your reference when answering the 15 PRD questions:

- **MVP Scope** → Becomes "Scope & Features" in PRD
- **Post-MVP Features** → Becomes "Out of Scope" in PRD
- **Business Rules** → Becomes "Assumptions & Dependencies" in PRD
- **Pain Points** → Informs "Problem Statement" in PRD
- **User Workflows** → Becomes "User Stories" in PRD

You don't copy-paste. You use it to inform your answers. The result: a PRD grounded in real business understanding.

### When to Skip Event Storming

Skip if your project:
- Has no business logic (just displays data)
- Has one user type with a simple workflow
- Is a technical tool (API, library, utility)
- Has crystal-clear requirements already

Use Event Storming if your project:
- Involves multiple user roles
- Has business workflows (booking, ordering, approvals)
- Needs to solve real business problems
- Has unclear or evolving requirements

### Time Investment

- **Event Storming session:** 45-90 minutes
- **Review summary:** 10 minutes
- **Total:** ~1-2 hours

**Value:** Prevents 1-3 days of building the wrong thing.

### Quick Reference: When to Use

| Project Type | Use Event Storming? |
|:-------------|:-------------------|
| Booking system | ✅ Yes |
| E-commerce platform | ✅ Yes |
| Task management app | ✅ Yes |
| Landing page | ❌ No |
| Simple dashboard | ❌ No |
| REST API (no business logic) | ❌ No |
| Portfolio website | ❌ No |

**Next:** Whether you used Event Storming or not, you're now ready to generate the PRD.

---

<!-- PAGE BREAK -->

