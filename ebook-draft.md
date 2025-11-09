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

## Chapter 5: Phase 1-2 - Generate the PRD

The PRD (Product Requirements Document) is your single source of truth. Everything the AI builds comes from this document. Get it right, and the AI builds exactly what you want. Get it wrong, and you waste hours fixing things.

### The Problem with Vague Requirements

**Traditional approach:**
- You: "Build me a booking system."
- AI: "Sure!" (Starts coding)
- AI builds: Authentication, payment processing, admin dashboard, email notifications, SMS reminders, analytics.
- You: "I just wanted customers to book appointments. Why did you build all this?"
- AI: "You didn't say NOT to."

**Framework approach:**
- You: Use INIT_PROMPT with your one-sentence idea.
- AI: Asks 15 specific questions.
- You: Answer all 15 questions.
- AI: Generates PRD with explicit scope (what IS included) and out-of-scope (what is NOT included).
- AI builds: Only what's in the PRD. Nothing more. Nothing less.

### The 15 Questions

The AI asks exactly 15 questions designed to extract every critical detail. These questions are grouped by category:

**Vision & Strategy (2 questions)**
1. What is the ultimate long-term vision for this project?
2. What business or personal goal does this support?

**Success Metrics (1 question)**
3. What specific, measurable metric defines success?

**User Stories & Functionality (3 questions)**
4. What are the core features users need to accomplish their goals?
5. What are the key user interactions and workflows?
6. What edge cases or error scenarios must the system handle?

**Non-Functional Requirements (3 questions)**
7. What are the performance requirements (response times, load capacity)?
8. What are the security requirements (authentication, data protection)?
9. What are the usability requirements (responsive design, accessibility)?

**Assumptions & Dependencies (2 questions)**
10. What assumptions are you making about users, technology, or environment?
11. What external dependencies does this project rely on?

**Scope (2 questions)**
12. What features MUST be included in the MVP?
13. What user stories are must-have vs. nice-to-have?

**Out of Scope (2 questions)**
14. What features are explicitly OUT of scope for the MVP?
15. What future enhancements should we NOT build now?

### How to Answer These Questions

**Be specific, not vague:**
- ❌ Vague: "The app should be fast."
- ✅ Specific: "API responses under 200ms, page load under 2 seconds."

**Use measurable criteria:**
- ❌ Vague: "The site should look good."
- ✅ Measurable: "Lighthouse score 95+, responsive on mobile."

**Be explicit about what's OUT:**
- ❌ Vague: "We'll add payments later."
- ✅ Explicit: "No payment processing in MVP. Manual invoicing only."

**Use your Event Storming Summary (if you did one):**
- MVP Scope → Informs Question 12
- Post-MVP Features → Informs Question 14
- Business Rules → Informs Question 10

### The PRD Structure (9 Sections)

After you answer the 15 questions, the AI generates a complete PRD with these sections:

| Section | Purpose | Example |
|:--------|:--------|:--------|
| **1. Project Overview & Vision** | Vision statement and problem | "A booking system to reduce salon no-shows by 50%" |
| **2. Success Metrics** | Measurable outcomes | "Reduce no-shows from 30% to 15% in 3 months" |
| **3. User Stories** | What users can do | "As a customer, I want to book online so I don't have to call" |
| **4. Non-Functional Requirements** | Performance, security, usability | "API response time < 200ms, mobile-responsive" |
| **5. Assumptions & Dependencies** | What we're assuming | "Users have modern browsers, email access" |
| **6. Scope & Features (MVP)** | What IS included | "✅ Online booking, ✅ Email reminders, ✅ Schedule view" |
| **7. Out of Scope** | What is NOT included | "❌ Payment processing, ❌ Mobile app, ❌ Reviews" |
| **8. Open Questions & Risks** | Unresolved items | "Do we support walk-ins? (TBD)" |
| **9. Change History** | Version tracking | "v1.0 - Initial PRD" |

### Critical: Scope vs. Out of Scope

Sections 6 and 7 are your defense against scope creep.

**Section 6 (Scope)** lists every feature included in the MVP. If it's not listed here, it doesn't get built.

**Section 7 (Out of Scope)** explicitly lists features you are NOT building. This prevents the AI from adding "helpful" extras.

**Example:**

**Scope (Section 6):**
- ✅ Customer can view services and prices
- ✅ Customer can book appointments
- ✅ Customer receives email confirmation
- ✅ Stylist can view daily schedule
- ✅ System prevents double-booking

**Out of Scope (Section 7):**
- ❌ No payment processing (manual invoicing for MVP)
- ❌ No customer reviews or ratings
- ❌ No SMS reminders (email only)
- ❌ No mobile app (web-only)
- ❌ No multi-location support (single salon only)

The AI uses Section 7 to prevent feature creep. When it's about to build something, it checks: "Is this in Section 6? No. Is it in Section 7? Yes, explicitly out of scope. Don't build it."

### PRD Template (Copy-Paste Ready)

```markdown
# Product Requirements Document: [Project Name]

## 1. Project Overview & Vision
- **Vision:** [One sentence describing the ultimate goal]
- **Problem:** [What pain point does this solve?]
- **Solution:** [High-level approach]

## 2. Strategic Alignment & Success Metrics
- **Business Goal:** [Why are we building this?]
- **Success Metrics:**
  - [Metric 1: Specific, measurable]
  - [Metric 2: Specific, measurable]

## 3. User Stories & Functional Requirements

| ID | User Story | Acceptance Criteria | Priority |
|:---|:-----------|:--------------------|:---------|
| US-01 | As a [user], I want to [action] so that [benefit] | - [Criteria 1]<br>- [Criteria 2] | Must-Have |
| US-02 | As a [user], I want to [action] so that [benefit] | - [Criteria 1]<br>- [Criteria 2] | Nice-to-Have |

## 4. Non-Functional Requirements (NFRs)

**Performance:**
- [Requirement 1: e.g., API response < 200ms]
- [Requirement 2: e.g., Page load < 2s]

**Security:**
- [Requirement 1: e.g., HTTPS only]
- [Requirement 2: e.g., Input validation]

**Usability:**
- [Requirement 1: e.g., Mobile-responsive]
- [Requirement 2: e.g., Lighthouse score 95+]

## 5. Assumptions & Dependencies

**Assumptions:**
- [Assumption 1: e.g., Users have modern browsers]
- [Assumption 2: e.g., Email delivery works]

**Dependencies:**
- [Dependency 1: e.g., External API availability]
- [Dependency 2: e.g., Email service provider]

## 6. Scope & Features (MVP)
- ✅ [Feature 1]
- ✅ [Feature 2]
- ✅ [Feature 3]

## 7. Out of Scope
- ❌ [Feature NOT included - with brief reason]
- ❌ [Feature NOT included - with brief reason]
- ❌ [Feature NOT included - with brief reason]

## 8. Open Questions & Risks

| Question/Risk | Impact | Status |
|:--------------|:-------|:-------|
| [Question 1] | High/Medium/Low | Open/Resolved |
| [Risk 1] | High/Medium/Low | Mitigated/Open |

## 9. Change History
- **v1.0** - [Date] - Initial PRD
```

### Example: Hair Salon Booking System PRD (Condensed)

**Section 1: Vision**
"A web-based booking system to reduce salon no-shows and eliminate phone-based scheduling."

**Section 2: Success Metrics**
- Reduce no-shows from 30% to 15% within 3 months
- Handle 80% of bookings online (vs. 0% currently)

**Section 3: User Stories (Condensed)**
- US-01: As a customer, I want to view available time slots so I can book at my convenience (Must-Have)
- US-02: As a customer, I want to receive email confirmation so I remember my appointment (Must-Have)
- US-03: As a stylist, I want to view my daily schedule so I know my appointments (Must-Have)

**Section 4: NFRs**
- Performance: Page load < 2s, API response < 200ms
- Security: HTTPS only, input validation, no sensitive data stored
- Usability: Mobile-responsive, accessible (WCAG AA)

**Section 6: Scope**
✅ View services, ✅ Book appointments, ✅ Email confirmations, ✅ Stylist schedule view, ✅ Double-booking prevention

**Section 7: Out of Scope**
❌ Payment processing, ❌ Reviews, ❌ SMS, ❌ Mobile app, ❌ Multi-location

### Checklist: Is Your PRD Complete?

Before moving to the next phase, verify:

- [ ] All 15 questions answered with specific details
- [ ] Success metrics are measurable (not "improve performance" but "API < 200ms")
- [ ] User stories have clear acceptance criteria
- [ ] Out of Scope section explicitly lists what you're NOT building
- [ ] No technical implementation details (those come in Tech Stack phase)
- [ ] Every must-have feature is listed in Scope section

### What Happens Next

You save the PRD as `PRODUCT_REQUIREMENTS_DOCUMENT.md`. This becomes your single source of truth.

Every decision the AI makes from now on references this document. "Should I add authentication?" → Check PRD. "Is it in Scope? No. Is it in Out of Scope? Yes. Don't build it."

**Time invested:** 20-25 minutes (15 min answering questions + 5-10 min reviewing PRD)

**Time saved:** 3-6 hours of building the wrong thing and reworking.

**Next:** Generate the Tech Stack based on the PRD.

---

<!-- PAGE BREAK -->

## Chapter 6: Phase 3 - Define the Tech Stack

Every technology choice needs a justification. Not "I like this framework" but "This framework meets the < 200ms API response requirement from the PRD."

The Tech Stack document forces the AI to justify every choice by referencing specific requirements from the PRD. No over-engineering. No technology for technology's sake.

### The Problem: Unjustified Tech Choices

**Without the framework:**
- You: "Build the backend."
- AI: Chooses a tech stack based on... its training data? Popular trends? Random selection?
- AI picks: A microservices architecture with Kubernetes, Redis caching, PostgreSQL, message queues, and GraphQL.
- You: "I just needed a simple API. Why is this so complex?"

**With the framework:**
- You: Use TECH_STACK_PROMPT with your PRD.
- AI: Analyzes PRD requirements (performance < 200ms, simple CRUD operations, single-server deployment).
- AI generates: Tech Stack document with justified choices.
- Every technology choice references a specific PRD requirement.
- Result: A stack that matches your needs, not the AI's assumptions.

### The Tech Stack Document Structure

The AI generates a document with three main sections:

**1. Frontend Stack**

| Category | Technology | Version | Justification (PRD Reference) |
|:---------|:-----------|:--------|:------------------------------|
| Framework | [Choice] | [Version] | "Chosen to meet NFR: Lighthouse score 95+" |
| Styling | [Choice] | [Version] | "Chosen for rapid development (PRD: 4-week timeline)" |

**2. Backend Stack**

| Category | Technology | Version | Justification (PRD Reference) |
|:---------|:-----------|:--------|:------------------------------|
| Framework | [Choice] | [Version] | "Chosen for performance: < 200ms API response (NFR Section 4)" |
| Database | [Choice] | [Version] | "Chosen for simplicity: Single-table schema (Scope Section 6)" |

**3. Infrastructure & DevOps**

| Category | Tool | Justification (PRD Reference) |
|:---------|:-----|:------------------------------|
| Containerization | [Choice] | "Required by PRD: Easy deployment (Assumption Section 5)" |
| Hosting | [Choice] | "Chosen for cost: < $20/month (Success Metric Section 2)" |

### Every Choice is Justified

Notice the pattern: Every technology selection includes "Chosen to meet [specific PRD requirement]."

The AI can't just pick popular frameworks. It must justify each choice by pointing to:
- A performance requirement (NFR Section 4)
- A scope limitation (Scope Section 6)
- A business constraint (Success Metrics Section 2)
- An assumption (Assumptions Section 5)

### Example: Hair Salon Booking System Tech Stack (Condensed)

**Frontend:**
- Framework: Modern frontend framework → "Chosen for mobile-responsive requirement (NFR: responsive design)"
- Styling: Utility-first CSS → "Chosen for rapid UI development (MVP timeline: 4 weeks)"

**Backend:**
- Framework: Fast API framework → "Chosen to meet NFR: API response < 200ms"
- Database: Relational DB → "Chosen for data relationships (bookings ↔ services ↔ stylists)"
- ORM: Database toolkit → "Chosen for type safety (PRD NFR: data integrity)"

**Infrastructure:**
- Containerization: Docker → "Required for easy deployment (PRD Assumption: single-server deployment)"
- Hosting: Cloud platform → "Chosen for low cost and scalability (Success Metric: operating cost)"

### What This Prevents

**Prevents over-engineering:**
- PRD says "simple CRUD API" → AI won't suggest microservices
- PRD says "single salon" → AI won't suggest multi-tenancy architecture
- PRD says "MVP timeline: 4 weeks" → AI won't suggest complex tech requiring long learning curves

**Prevents under-engineering:**
- PRD says "API response < 200ms" → AI won't suggest slow frameworks
- PRD says "handle 1000 concurrent users" → AI won't suggest single-threaded solutions
- PRD says "real-time updates" → AI will suggest WebSocket or similar

### Architecture Diagram (Optional)

The Tech Stack document may include a simple text-based architecture diagram showing how components connect:

```
User (Browser)
    ↓
Frontend (Port 3000)
    ↓ (HTTP/HTTPS)
Backend API (Port 8000)
    ↓
Database (Port 5432)
```

### Time Investment

- **You paste PRD into TECH_STACK_PROMPT:** 1 minute
- **AI generates Tech Stack document:** 2 minutes
- **You review and approve:** 2 minutes
- **Total:** ~5 minutes

**Value:** Prevents hours of debugging incompatible technologies or removing over-engineered solutions.

### Checklist: Is Your Tech Stack Complete?

Before proceeding, verify:

- [ ] Every technology choice has a justification
- [ ] Every justification references a specific PRD section
- [ ] No over-engineering (tech matches PRD scope)
- [ ] No under-engineering (tech meets PRD NFRs)
- [ ] Architecture is appropriate for project scale

### What Happens Next

You save the Tech Stack document as `TECH_STACK_DOCUMENT.md`. The AI will use this (along with the PRD) to generate the execution plan.

**Next:** Create the staged execution plan with 100-150 checkboxes.

---

<!-- PAGE BREAK -->

## Chapter 7: Phase 4 - Create the Execution Plan

The Handoff Plan breaks your project into 100-150 verifiable checkboxes. Every task is granular, explicit, and trackable. Nothing is forgotten. Nothing is vague.

### The Problem: Vague Plans

**Without the framework:**
- AI: "I'll build the backend, then the frontend, then integrate them."
- You: "Sounds good."
- Two hours later: AI built 8 features you didn't ask for, missed 3 you did, and you have no idea what's done vs. what's left.

**With the framework:**
- AI generates: A 5-stage plan with 120 checkboxes.
- You know exactly: What gets built, in what order, and how to verify it's done.
- Result: Complete visibility. Zero surprises.

### The Two Development Approaches

Before generating the plan, choose your approach:

**Horizontal (Layer-by-Layer):**
- Stage 1: Setup
- Stage 2: All backend APIs
- Stage 3: All frontend pages
- Stage 4: Integration
- Stage 5: Testing & docs

**When to use:** Simple projects (1-3 features), straightforward integration.

**Vertical (Feature-by-Feature):**
- Stage 1: Minimal working installation (basic end-to-end system)
- Stage 2: Feature A (backend + frontend + integration)
- Stage 3: Feature B (backend + frontend + integration)
- Stage 4: Feature C (backend + frontend + integration)
- Stage 5: Polish & finalization

**When to use:** Projects with 4+ features, need early demos, continuous integration.

### Decision Guide

| Your Situation | Approach |
|:---------------|:---------|
| 1-3 features total | Horizontal |
| 4+ features | Vertical |
| Need early demos | Vertical |
| Simple project, fast execution | Horizontal |
| Complex business app | Vertical |
| Solo MVP build | Either (your preference) |

**When in doubt:** Use Vertical. It's safer (continuous integration) and more flexible.

### The Handoff Plan Structure

Regardless of approach, the plan has this structure:

**5-7 High-Level Stages** → Each stage has a clear goal

**3-5 Tasks per Stage** → Each task is a logical unit of work

**3-7 Checkboxes per Task** → Each checkbox is verifiable (done or not done)

**Total: 100-150 Checkboxes** for a typical MVP

### Example: Horizontal Approach

```markdown
## Stage 1: Project Setup & Environment
Goal: Create foundational project structure

Task 1.1: Initialize Project Structure
  [ ] Create root project directory
  [ ] Create backend subdirectory
  [ ] Create frontend subdirectory
  [ ] Initialize git repository
  [ ] Create root README.md

Task 1.2: Backend Environment Setup
  [ ] Create package manager config file
  [ ] Install backend framework
  [ ] Create virtual environment
  [ ] Install dependencies
  [ ] Verify backend runs (hello world endpoint)

Task 1.3: Frontend Environment Setup
  [ ] Initialize frontend framework
  [ ] Install UI dependencies
  [ ] Configure build tools
  [ ] Verify frontend runs (hello world page)

## Stage 2: Backend API Development
Goal: Implement all API endpoints

Task 2.1: Database Setup
  [ ] Create database models
  [ ] Write database migrations
  [ ] Seed database with test data
  [ ] Verify database connection

Task 2.2: Implement Booking Endpoint
  [ ] Create POST /api/bookings route
  [ ] Add request validation
  [ ] Add double-booking prevention logic
  [ ] Add error handling
  [ ] Write unit tests for endpoint

[... continues for all backend endpoints ...]

## Stage 3: Frontend Development
[... all frontend pages ...]

## Stage 4: Integration
[... connect frontend to backend ...]

## Stage 5: Testing & Documentation
[... final testing and docs ...]
```

### Example: Vertical Approach

```markdown
## Stage 1: Minimal Working Installation
Goal: Establish basic end-to-end system

Task 1.1: Project Scaffolding
  [ ] Create project structure
  [ ] Initialize backend with health endpoint
  [ ] Initialize frontend with homepage
  [ ] Verify end-to-end connection (frontend calls backend)

## Stage 2: Booking Feature (Complete Vertical Slice)
Goal: Customer can book appointments

Task 2.1: Backend - Booking API
  [ ] Create booking database model
  [ ] Create POST /api/bookings endpoint
  [ ] Add validation logic
  [ ] Add double-booking prevention
  [ ] Write unit tests

Task 2.2: Frontend - Booking Form
  [ ] Create booking form component
  [ ] Add form validation
  [ ] Add service selection dropdown
  [ ] Add date/time picker
  [ ] Add submit button

Task 2.3: Integration - Connect Booking Feature
  [ ] Connect form to API endpoint
  [ ] Handle successful booking (show confirmation)
  [ ] Handle errors (show error messages)
  [ ] Test end-to-end booking flow

## Stage 3: Schedule View Feature (Complete Vertical Slice)
[... backend + frontend + integration for schedule view ...]

## Stage 4: Email Reminders Feature (Complete Vertical Slice)
[... backend + frontend + integration for reminders ...]

## Stage 5: Polish & Finalization
[... code cleanup, final testing, docs ...]
```

### Why 100-150 Checkboxes?

**"Build the backend" is too vague for AI.**

What does "build the backend" mean?
- Which endpoints?
- What validation?
- What error handling?
- What tests?
- What documentation?

**"Create POST /api/bookings endpoint" is clear for AI.**

But even that breaks down into:
- [ ] Create route handler
- [ ] Add request body validation
- [ ] Add business logic (double-booking check)
- [ ] Add error handling
- [ ] Return JSON response
- [ ] Write unit test

Six checkboxes for one endpoint. Clear. Verifiable. No ambiguity.

### What Makes a Good Checkbox?

**Good checkboxes are:**
- **Specific:** "Create homepage component" not "Build frontend"
- **Verifiable:** Either done or not done, no gray area
- **Atomic:** One clear action per checkbox
- **Ordered:** Logical sequence (setup before build, backend before integration)

**Bad checkboxes:**
- [ ] Make the app work (vague)
- [ ] Improve performance (not verifiable)
- [ ] Build everything (not atomic)

**Good checkboxes:**
- [ ] Create database connection with error handling
- [ ] Write unit test for booking endpoint (200 status)
- [ ] Add CORS middleware for frontend domain

### Time Investment

- **You paste PRD + Tech Stack into STAGES_PROMPT:** 2 minutes
- **AI generates Handoff Plan:** 5 minutes
- **You review stages and checkboxes:** 3 minutes
- **Total:** ~10 minutes

**Value:** Prevents hours of missed requirements and forgotten tasks.

### How the AI Uses This Plan

During execution (Phases 5-7):

1. AI reads the current stage goal
2. AI executes Task 1.1
3. AI checks off each checkbox as completed: [x]
4. AI moves to Task 1.2
5. When stage is complete, AI stops and waits for stage gate
6. You review progress, AI asks questions about next stage
7. AI continues with next stage

The checkboxes provide progress tracking. You always know: "We're 60% through Stage 3, Task 3.2."

### Checklist: Is Your Execution Plan Complete?

Before proceeding, verify:

- [ ] Plan has 5-7 logical stages
- [ ] Each stage has a clear goal
- [ ] Each task has 3-7 checkboxes
- [ ] Total checkboxes: 100-150 (adjust based on project size)
- [ ] Checkboxes are specific and verifiable
- [ ] Order makes sense (setup → build → integrate → test)
- [ ] Approach matches project needs (horizontal vs. vertical)

### What Happens Next

You save the Handoff Plan as `HANDOFF_STAGES_PLAN.md`. Now you have all three documents:
- ✅ PRD (what to build)
- ✅ Tech Stack (how to build it)
- ✅ Handoff Plan (step-by-step execution)

**Planning phase complete.** Total time invested: 40-60 minutes (simple) or 90-150 minutes (complex with Event Storming).

**Next:** Start execution with stage gates.

---

<!-- PAGE BREAK -->

## Chapter 8: Phase 5-7 - Execution with Stage Gates

Planning is complete. Now the AI builds. But it doesn't build blindly. Stage gates ensure the AI asks clarifying questions before each major phase, preventing over-engineering and scope creep.

### The Problem: Unchecked Execution

**Without stage gates:**
- AI completes Stage 1 (Setup)
- AI immediately starts Stage 2 (Backend)
- AI builds 10 endpoints, authentication, caching, logging, rate limiting
- You: "I only needed 3 endpoints. Why did you build all this?"
- AI: "You didn't tell me not to."

**With stage gates:**
- AI completes Stage 1
- AI stops and asks: "Before building the backend, I need clarification: Should I include authentication in this stage?"
- You: "No, that's out of scope per the PRD."
- AI: "Understood. I'll build only the 3 endpoints listed in the PRD."
- AI builds exactly what you need.

### What is a Stage Gate?

A stage gate is a mandatory pause between stages where the AI asks 3-5 clarifying questions specific to the upcoming work.

**Purpose:**
- Prevents assumptions
- Prevents over-engineering
- Ensures implementation matches your vision
- Provides a checkpoint for review

**When it happens:**
After completing all tasks in a stage, before starting the next stage.

### The Stage Gate Flow

```
Stage 1: Setup
  [x] All tasks complete
        ↓
    STAGE GATE (AI asks 3-5 questions about Stage 2)
        ↓
    You answer questions
        ↓
Stage 2: Backend Development
  [ ] Tasks begin (with your clarifications in mind)
```

### Example Stage Gate Questions

**Before Backend Stage:**
1. "Should I include user authentication in this stage, or is that out of scope per Section 7?"
2. "What HTTP status codes should we return for validation errors?"
3. "Do you want comprehensive logging for all API requests, or minimal logging?"
4. "Should I add rate limiting to the API endpoints?"
5. "How should we handle database connection errors?"

**Before Frontend Stage:**
1. "Should we show loading spinners or skeleton screens while data loads?"
2. "How should we handle API timeout errors (retry, show error, redirect)?"
3. "Do you want form validation to happen on blur or on submit?"
4. "Should error messages be inline or in a toast notification?"

**Before Integration Stage:**
1. "Should the frontend poll the backend for updates, or is one-time fetch sufficient?"
2. "How should we handle CORS issues if they arise?"
3. "Do you want to mock the backend during frontend development, or connect immediately?"

### The Pattern: Specific Implementation Questions

Notice: Stage gate questions are NOT about requirements (those are in the PRD). They're about **implementation details** that the PRD doesn't specify.

**Not in PRD:** Which HTTP status code for errors? (Implementation detail)

**In PRD:** System must validate booking data. (Requirement)

**Stage gate question:** "Should validation errors return 400 or 422 status codes?"

This keeps the PRD focused on WHAT to build, while stage gates handle HOW to build it.

### How to Answer Stage Gate Questions

**Be decisive:**
- Don't say "whatever you think is best"
- Pick an option: "Use 400 for all client errors"
- Reference the PRD when relevant: "Per Section 7, no rate limiting for MVP"

**When you don't know:**
- Ask the AI for a recommendation: "What's standard practice?"
- Make a decision based on AI's suggestion
- Document it for consistency

**Keep answers brief:**
- One sentence per answer
- Be specific: "Show loading spinners" not "make it look nice"

### Time Investment per Stage Gate

- **AI asks 3-5 questions:** 30 seconds
- **You read and answer:** 3-4 minutes
- **Total:** ~5 minutes per gate

**For 5 stages = ~25 minutes total across entire project**

**Value:** Prevents 2-4 hours of removing over-engineered features or fixing wrong implementation choices.

### Execution Pattern

The full execution flow looks like this:

**Phase 5: Execute Stage 1**
- AI works through all tasks
- Checks off each checkbox: [x]
- Time: 15-30 minutes

**Phase 6: Stage Gate #1**
- AI asks 3-5 questions about Stage 2
- You answer
- Time: 5 minutes

**Phase 7: Execute Stage 2**
- AI works through all tasks with your clarifications
- Checks off checkboxes
- Time: 30-60 minutes

**Repeat:** Phases 6-7 for each remaining stage (Stage 3, 4, 5...)

### What Gets Built

As the AI works:
- **Checkboxes get marked:** [x] Create database model
- **You can track progress:** "Stage 2, Task 2.3, 75% complete"
- **Code gets written:** Actual working implementation
- **Tests get written:** Unit tests as specified in checkboxes
- **Documentation gets created:** READMEs, API docs, etc.

### How to Monitor Progress

The Handoff Plan becomes a living document:

**Before execution:**
```markdown
Stage 2: Backend Development
Task 2.1: Database Setup
  [ ] Create database models
  [ ] Write migrations
  [ ] Seed test data
```

**During execution:**
```markdown
Stage 2: Backend Development
Task 2.1: Database Setup
  [x] Create database models
  [x] Write migrations
  [ ] Seed test data  ← Currently working on this
```

**After completion:**
```markdown
Stage 2: Backend Development
Task 2.1: Database Setup
  [x] Create database models
  [x] Write migrations
  [x] Seed test data
```

### What to Review Between Stages

After each stage completes:

1. **Test what was built:** Run the code, verify it works
2. **Review checkboxes:** Ensure all are truly complete
3. **Check PRD alignment:** Does it match Section 6 (Scope)?
4. **Update Handoff Plan:** Mark all completed checkboxes as [x]

**Don't rush.** Take 5-10 minutes to verify before proceeding to the next gate.

### Common Stage Gate Questions by Stage Type

**Setup/Infrastructure Stages:**
- Which package manager versions?
- Where should config files live?
- What environment variables are needed?

**Backend Stages:**
- What error response format?
- What logging level?
- What test coverage threshold?

**Frontend Stages:**
- What loading state UX?
- What error handling UX?
- What responsive breakpoints?

**Integration Stages:**
- How to handle API failures?
- What retry logic?
- What caching strategy?

**Testing/Polish Stages:**
- What test scenarios to prioritize?
- What documentation to include?
- What performance benchmarks?

### When Stage Gates Save You

**Scenario 1: Preventing Authentication Overreach**
- AI about to build login system
- Gate question: "Should I implement authentication?"
- You: "No, explicitly out of scope in PRD Section 7"
- **Saved:** 2 hours of removing auth code

**Scenario 2: Clarifying Error Handling**
- AI about to build error handling
- Gate question: "Should errors show in modals or inline?"
- You: "Inline, below the form field"
- **Saved:** 1 hour of reworking error UI

**Scenario 3: Avoiding Over-Testing**
- AI about to write tests
- Gate question: "Should I write integration tests or just unit tests?"
- You: "Unit tests only for MVP per time constraints"
- **Saved:** 2 hours of integration test setup

### Execution Complete

After all stages:
- ✅ All 100-150 checkboxes marked complete
- ✅ Working code implementing exactly what's in the PRD
- ✅ Tests passing
- ✅ Documentation complete
- ✅ Zero scope creep (stage gates prevented it)

**Total execution time:** 2-6 hours depending on project complexity

**Next:** How to pause and resume work without losing context.

---

<!-- PAGE BREAK -->

## Chapter 9: Phase 8 - Pause & Resume

You don't finish projects in one sitting. You work for two hours, stop for a meeting, come back later. Or you build for a day, resume the next morning. Without the framework, you waste 15-20 minutes re-explaining everything. With the framework, you resume in 2 minutes with zero context loss.

### The Problem: Lost Context

**Traditional approach:**
- You: "Continue where we left off."
- AI: "What project are we working on?"
- You: *Explains the project again*
- AI: "What have we built so far?"
- You: *Lists what's done*
- AI: "What should I work on next?"
- You: *Explains next steps*
- **Time wasted:** 15-20 minutes

**Framework approach:**
- You: Use CONTINUE_PROMPT with three documents
- AI: "I've reviewed the context. Last completed: Stage 2, Task 2.3. Next task: Stage 3, Task 3.1 - Create Landing Page UI. Shall I proceed?"
- You: "Yes."
- **Time wasted:** 2 minutes

### The CONTINUE_PROMPT Pattern

The CONTINUE_PROMPT is a structured way to restore full context. You paste three documents:

1. **PRD** (what you're building)
2. **Tech Stack** (how you're building it)
3. **Handoff Plan with progress** (what's done, what's next)

The AI reads all three and instantly knows everything.

### What to Include

**Document 1: Full PRD**
- All 9 sections
- No modifications needed
- This tells the AI what you're building and why

**Document 2: Full Tech Stack**
- All technology choices
- All justifications
- This tells the AI how you're building it

**Document 3: Handoff Plan with Progress**
- All stages and tasks
- Checkboxes marked [x] for completed items
- Checkboxes unmarked [ ] for pending items
- This tells the AI what's done and what's next

### How It Works

You paste the CONTINUE_PROMPT with all three documents into your AI tool. The AI:

1. **Loads the PRD** → Understands project scope and requirements
2. **Loads the Tech Stack** → Understands technology choices
3. **Loads the Handoff Plan** → Sees progress (60 checkboxes done, 90 remaining)
4. **Identifies last completed task** → "Stage 2, Task 2.3 - Write unit tests"
5. **Identifies next task** → "Stage 3, Task 3.1 - Create landing page UI"
6. **Asks for confirmation** → "Shall I proceed with Task 3.1?"

You confirm. The AI continues exactly where you left off.

### Example: Resuming After Overnight Break

**What you do:**
1. Open CONTINUE_PROMPT template
2. Paste full PRD
3. Paste full Tech Stack
4. Paste Handoff Plan with all completed tasks marked [x]
5. Send to AI

**AI response:**
> "I've reviewed the project context. Here's the current state:
>
> **Project:** Hair Salon Booking System
>
> **Last completed task:** Stage 2, Task 2.4 - Write Backend Unit Tests (all checkboxes complete)
>
> **Next task:** Stage 3, Task 3.1 - Create Landing Page UI
>
> This task involves:
> - Create main page component
> - Add Tailwind CSS styling
> - Create header with salon name
> - Add "Book Appointment" CTA button
> - Ensure mobile-responsive design
>
> Should I proceed with this task?"

**You:** "Yes, proceed."

**AI:** *Starts building exactly what's needed, with full context*

### When to Use CONTINUE_PROMPT

**Use it when:**
- Resuming work after a break (overnight, lunch, meeting)
- Switching to a new AI session
- Starting work on a different device
- Need to bring someone else up to speed
- Context feels lost or AI seems confused

**Don't need it when:**
- Working continuously in the same session
- AI still has full context from earlier in the conversation

### Time Saved

**Without framework:**
- Re-explaining project: 5 minutes
- Listing what's done: 5 minutes
- Explaining next steps: 5 minutes
- AI asking clarifying questions: 5 minutes
- **Total:** 15-20 minutes per resume

**With framework:**
- Paste CONTINUE_PROMPT: 1 minute
- AI reviews and responds: 1 minute
- **Total:** 2 minutes per resume

**If you resume 3 times during a project:** Save 45-60 minutes

### The Magic: Zero Context Loss

The three documents contain everything:
- PRD → What and why
- Tech Stack → How and with what
- Handoff Plan → Where you are

No detail is lost. No decision is forgotten. The AI knows as much on Day 2 as it did on Day 1.

### Checklist: Before Pausing Work

When you need to stop working:

- [ ] Save all three documents (PRD, Tech Stack, Handoff Plan)
- [ ] Mark all completed checkboxes as [x] in the Handoff Plan
- [ ] Note where you stopped (optional, for your reference)
- [ ] Close your session

That's it. When you return, use CONTINUE_PROMPT to restore everything instantly.

**Next:** Putting it all together.

---

<!-- PAGE BREAK -->

## Chapter 10: Putting It All Together

You now have the complete framework. Let's review the full workflow, time investment, and how to avoid common pitfalls.

### The Complete 8-Phase Workflow

Here's the end-to-end process:

```
Phase 0: Define Your Idea (5-10 min)
   ↓ [Output: One-sentence project description]
   ↓
Phase 0.5: Event Storming - OPTIONAL (45-90 min)
   ↓ [Output: Business process map, MVP scope]
   ↓
Phase 1: Requirements Gathering (15-20 min)
   ↓ [AI asks 15 questions]
   ↓
Phase 2: Generate PRD (5-10 min)
   ↓ [Output: 9-section PRD document]
   ↓
Phase 3: Define Tech Stack (10-15 min)
   ↓ [Output: Tech Stack document with justifications]
   ↓
Phase 4: Create Execution Plan (5-10 min)
   ↓ [Output: Handoff Plan with 100-150 checkboxes]
   ↓
Phase 5-7: Execute with Stage Gates (2-6 hours)
   ↓ [Execute → Gate → Execute → Gate → ...]
   ↓
Phase 8: Pause & Resume (2 min per resume)
   ↓ [Use CONTINUE_PROMPT as needed]
   ↓
✅ WORKING MVP
```

**Total time:** 4-8 hours for most MVPs.

### Time Investment Breakdown

**Planning Time:**
- Without Event Storming: 40-60 minutes
- With Event Storming: 90-150 minutes

**Execution Time:**
- Simple project (1-3 features): 2-4 hours
- Complex project (4-6 features): 4-6 hours
- Large project (7+ features): 6-8 hours

**Stage Gates (built into execution):**
- 5 minutes per gate × 5 stages = 25 minutes total

**Resume Time (if needed):**
- 2 minutes per resume × 3 resumes = 6 minutes total

**Example Timeline for Salon Booking System:**
- Phase 0: Define Idea (5 min)
- Phase 0.5: Event Storming (60 min)
- Phase 1-2: Requirements + PRD (25 min)
- Phase 3: Tech Stack (12 min)
- Phase 4: Execution Plan (8 min)
- Phase 5-7: Execution (5 hours including stage gates)
- Phase 8: Resume twice (4 min)
- **Total: 6 hours 54 minutes**

### What You Get at the End

**Three Documents:**
1. PRD - The single source of truth (what to build)
2. Tech Stack - Technology choices (how to build)
3. Handoff Plan - Execution roadmap (step-by-step)

**Working Code:**
- Functional MVP implementing exactly what's in the PRD
- No scope creep (stage gates prevented it)
- No over-engineering (tech stack matched requirements)
- No missing features (100-150 checkboxes ensured completeness)

**Tests:**
- Unit tests for critical functionality
- Integration tests if specified in PRD

**Documentation:**
- README with setup instructions
- API documentation (if applicable)
- Architecture notes

**Ready to ship** or iterate based on user feedback.

### Common Pitfalls and How to Avoid Them

**Pitfall 1: Skipping Event Storming for Complex Projects**
- **Symptom:** You're unclear about requirements, business rules, or user workflows
- **Fix:** If your project has 4+ features or complex business logic, do Event Storming (Phase 0.5)
- **Cost of skipping:** 2-4 hours reworking the PRD when you realize requirements were unclear

**Pitfall 2: Vague PRD**
- **Symptom:** AI asks too many questions during execution, builds wrong features
- **Fix:** Answer all 15 PRD questions thoroughly. Use specific examples. Be explicit about scope AND out-of-scope.
- **Cost of vagueness:** 3-5 hours removing unwanted features and adding missing ones

**Pitfall 3: Over-Engineering the Tech Stack**
- **Symptom:** AI suggests microservices, Redis, Kubernetes for a simple MVP
- **Fix:** Every technology choice must reference a PRD requirement. If the PRD doesn't require it, don't add it.
- **Cost of over-engineering:** 2-4 hours learning and configuring unnecessary tech

**Pitfall 4: Too Few Checkboxes**
- **Symptom:** Handoff Plan has 30-40 checkboxes for a complex project
- **Fix:** Break tasks down further. "Build backend" → 20 specific checkboxes. Aim for 100-150 total.
- **Cost of vague plan:** 2-3 hours debugging missing functionality

**Pitfall 5: Skipping Stage Gates**
- **Symptom:** AI builds too much, wrong implementation, scope creep
- **Fix:** Stop after each stage. Let AI ask 3-5 clarifying questions. Answer them decisively.
- **Cost of skipping gates:** 2-4 hours removing over-engineered features

**Pitfall 6: Not Using CONTINUE_PROMPT**
- **Symptom:** After resuming, AI is confused, asks basic questions, rebuilds things
- **Fix:** Always use CONTINUE_PROMPT with all three documents when resuming work
- **Cost of not using it:** 15-20 minutes per resume × 3 resumes = 1 hour wasted

**Pitfall 7: Changing Requirements Mid-Execution**
- **Symptom:** "Actually, can we add authentication?" (when it's out of scope in PRD)
- **Fix:** If requirements change, stop execution. Update the PRD. Regenerate affected parts of Handoff Plan. Then resume.
- **Cost of ad-hoc changes:** 1-2 hours fixing inconsistencies between code and PRD

**Pitfall 8: Ignoring the PRD During Execution**
- **Symptom:** AI builds features not in the PRD, or misses features that are in it
- **Fix:** Reference the PRD constantly. Every stage gate, every checkpoint: "Does this match Section 6 of the PRD?"
- **Cost of ignoring PRD:** 3-6 hours of rework

### The Framework vs. Traditional Development

Let's compare one final time:

**Traditional Approach:**
- Start coding immediately
- Requirements emerge during development
- Build features AI thinks you need
- Discover missing features at the end
- Rework and remove scope creep
- **Total time:** 12-20 hours (6-14 hours wasted)

**Framework Approach:**
- Invest 40-150 min in planning
- Execute with clear roadmap
- Build only what PRD specifies
- Stage gates prevent overreach
- Zero scope creep
- **Total time:** 4-8 hours (30-70% time saved)

**The math:**
- **Upfront investment:** 1-2.5 hours
- **Time saved during execution:** 6-14 hours
- **Net time saved:** 4-12 hours per project

**Over 10 projects:** 40-120 hours saved (1-3 weeks of work)

### Your Framework Checklist

Before starting your next project, verify you have:

**Phase 0:**
- [ ] One-sentence project description
- [ ] Decision: Simple or complex?
- [ ] Decision: Event Storming or skip to PRD?

**Phase 0.5 (if applicable):**
- [ ] Event Storming session complete
- [ ] 10-section Event Storming Summary document
- [ ] MVP scope identified

**Phase 1-2:**
- [ ] All 15 PRD questions answered
- [ ] PRD with all 9 sections complete
- [ ] Scope section lists 5-10 concrete features
- [ ] Out-of-Scope section lists what NOT to build
- [ ] Success criteria defined (Section 2)

**Phase 3:**
- [ ] Tech Stack document with 3 sections (Frontend, Backend, Infrastructure)
- [ ] Every technology choice has PRD justification
- [ ] No over-engineering (nothing that doesn't map to a requirement)

**Phase 4:**
- [ ] Handoff Plan with 5-7 stages
- [ ] 100-150 checkboxes total (adjust for project size)
- [ ] Approach chosen: Horizontal or Vertical
- [ ] Each checkbox is specific and verifiable

**Phase 5-7:**
- [ ] Stage gate questions answered for each stage
- [ ] Checkboxes marked [x] as work completes
- [ ] Code built matches PRD exactly
- [ ] Tests written per Handoff Plan

**Phase 8:**
- [ ] All three documents saved (PRD, Tech Stack, Handoff Plan)
- [ ] CONTINUE_PROMPT used when resuming
- [ ] Progress tracked in Handoff Plan

### Are You Ready to Start?

You have everything you need:
- ✅ A structured 8-phase process
- ✅ Templates for every document
- ✅ Stage gates to prevent mistakes
- ✅ Continuity system to avoid context loss
- ✅ Proven approach that saves 30-70% of development time

**Your next steps:**

1. **Start with a simple project first** (1-3 features) to learn the framework
2. **Use the templates in the Appendix** (all prompts are provided verbatim)
3. **Follow the phases in order** (don't skip the planning)
4. **Be disciplined with stage gates** (don't let AI run wild)
5. **Track progress religiously** (mark those checkboxes)

**After 1-2 projects using this framework:**
- You'll internalize the process
- Planning will become automatic
- You'll spot scope creep instantly
- You'll ship MVPs in 4-8 hours consistently

**After 5-10 projects:**
- The framework becomes second nature
- You'll adapt it to your specific needs
- You'll have saved 40-120 hours of development time
- You'll have shipped more products than you thought possible

### One Final Thought

The difference between developers who ship and developers who don't isn't talent. It's structure.

This framework gives you structure. Use it. Trust the process. Build with clarity.

**Now go build something.** 🚀

---

<!-- PAGE BREAK -->

## Appendix: Quick Reference

This appendix contains everything you need to start using the framework immediately: decision trees, all prompts verbatim, and key templates.

### Quick Start Flowchart

```
START: Do you have a project idea?
   ↓
   YES
   ↓
Step 1: Write one-sentence description
   ↓
Step 2: Is your project complex (4+ features, business logic)?
   ↓
   YES → Run EVENT_STORMING_PROMPT (45-90 min)
   NO → Skip to Step 3
   ↓
Step 3: Run INIT_PROMPT → Answer 15 questions (15-20 min)
   ↓
Step 4: AI generates PRD → Review & approve (5-10 min)
   ↓
Step 5: Run TECH_STACK_PROMPT with PRD (10-15 min)
   ↓
Step 6: AI generates Tech Stack → Review & approve (5 min)
   ↓
Step 7: Run STAGES_PROMPT with PRD + Tech Stack (5-10 min)
   ↓
Step 8: AI generates Handoff Plan → Review & approve (5 min)
   ↓
Step 9: Execute Stage 1 → AI works through checkboxes
   ↓
Step 10: Run STAGE_GATE_PROMPT → Answer 3-5 questions
   ↓
Step 11: Execute next stage → Repeat steps 9-10 for all stages
   ↓
Step 12: If you need to pause → Use CONTINUE_PROMPT to resume
   ↓
✅ DONE: Working MVP in 4-8 hours
```

### Decision Tree: Should I Use Event Storming?

```
Q1: Does your project have 4+ features?
   ↓
   YES → Use Event Storming
   NO → Continue to Q2
   ↓
Q2: Does your project involve complex business logic?
   ↓
   YES → Use Event Storming
   NO → Continue to Q3
   ↓
Q3: Are you unclear about requirements?
   ↓
   YES → Use Event Storming
   NO → Skip Event Storming, go to INIT_PROMPT
```

### Decision Tree: Horizontal vs. Vertical Development?

```
Q1: How many features does your project have?
   ↓
   1-3 features → Use HORIZONTAL (default STAGES_PROMPT)
   4+ features → Continue to Q2
   ↓
Q2: Do you need to demo progress early?
   ↓
   YES → Use VERTICAL
   NO → Continue to Q3
   ↓
Q3: Is integration complex or risky?
   ↓
   YES → Use VERTICAL (safer, continuous integration)
   NO → Either approach works (choose VERTICAL when in doubt)
```

---

<!-- PAGE BREAK -->

### All Prompts (Copy-Paste Ready)

#### 0. EVENT_STORMING_PROMPT (Optional)

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

#### 1. INIT_PROMPT

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

#### 2. TECH_STACK_PROMPT

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

<!-- PAGE BREAK -->

#### 3. STAGES_PROMPT

**When to use:** After the Tech Stack document has been generated.

**Note:** If you prefer vertical-slice (iterative, feature-by-feature) development instead of the default horizontal approach, use the vertical-slice variant instead of this prompt.

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

#### 4. STAGE_GATE_PROMPT

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

#### 5. CONTINUE_PROMPT

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

<!-- PAGE BREAK -->

### Key Templates Summary

#### PRD Structure (9 Sections)

```markdown
# Product Requirements Document: [Project Name]

## 1. Project Overview & Vision
- Vision: [One sentence]
- Problem: [What pain point does this solve?]
- Solution: [High-level approach]

## 2. Strategic Alignment & Success Metrics
- Business Goals: [3-5 goals]
- Success Metrics: [5-7 quantifiable metrics]

## 3. Target Users & Personas
- Primary User: [Description]
- Secondary Users: [If applicable]

## 4. User Stories & Acceptance Criteria
- User Story 1: As a [user], I want [goal] so that [reason]
  - Acceptance: [Specific criteria]
- [Repeat for 5-10 core stories]

## 5. Functional Requirements by Feature
- Feature 1: [Name]
  - Description: [What it does]
  - Requirements: [Detailed list]
- [Repeat for all features]

## 6. Scope & In-Scope Features (MVP)
- ✅ Feature A
- ✅ Feature B
- [List all in-scope features]

## 7. Explicitly Out-of-Scope (Post-MVP)
- ❌ Feature X (Phase 2)
- ❌ Feature Y (Phase 3)
- [List all explicitly excluded features]

## 8. Non-Functional Requirements
- Performance: [Specific metrics]
- Security: [Requirements]
- Usability: [Standards]
- Scalability: [Limits]

## 9. Assumptions, Dependencies, Risks
- Assumptions: [List]
- Dependencies: [External factors]
- Risks: [Potential issues]
- Open Questions: [Unresolved items]
```

#### Tech Stack Structure (3 Sections)

```markdown
# Tech Stack Document: [Project Name]

## Frontend

| Technology | Version | Justification (PRD Reference) |
|:-----------|:--------|:------------------------------|
| [Framework] | [X.X] | [Why this choice? Link to PRD requirement] |
| [Library 1] | [X.X] | [Justification] |
| [Library 2] | [X.X] | [Justification] |

## Backend

| Technology | Version | Justification (PRD Reference) |
|:-----------|:--------|:------------------------------|
| [Framework] | [X.X] | [Why this choice? Link to PRD requirement] |
| [Database] | [X.X] | [Justification] |
| [Library] | [X.X] | [Justification] |

## Infrastructure & DevOps

| Technology | Version | Justification (PRD Reference) |
|:-----------|:--------|:------------------------------|
| [Deployment] | [X.X] | [Why this choice? Link to PRD requirement] |
| [CI/CD] | [X.X] | [Justification] |
```

#### Handoff Plan Structure (5-7 Stages)

```markdown
# Handoff & Stages Plan: [Project Name]

## Stage 1: [Stage Name]
**Goal:** [Clear objective for this stage]

Task 1.1: [Task Name]
  [ ] Subtask 1
  [ ] Subtask 2
  [ ] Subtask 3

Task 1.2: [Task Name]
  [ ] Subtask 1
  [ ] Subtask 2

[Repeat for all tasks in stage]

## Stage 2: [Stage Name]
[Same structure]

## Stage 3: [Stage Name]
[Same structure]

[Continue for 5-7 stages total]
```

### Time Budget Reference

| Phase | Time Investment |
|:------|:----------------|
| Phase 0: Define Idea | 5-10 minutes |
| Phase 0.5: Event Storming (optional) | 45-90 minutes |
| Phase 1: Answer 15 Questions | 15-20 minutes |
| Phase 2: Review PRD | 5-10 minutes |
| Phase 3: Review Tech Stack | 10-15 minutes |
| Phase 4: Review Handoff Plan | 5-10 minutes |
| **Total Planning** | **40-150 minutes** |
| Phase 5-7: Execution | 2-6 hours |
| Phase 8: Resume (if needed) | 2 min per resume |
| **Total Project** | **4-8 hours** |

### Common Pitfalls Checklist

Before starting execution, verify:

- [ ] PRD has clear Scope (Section 6) AND Out-of-Scope (Section 7)
- [ ] Every tech choice in Tech Stack references a PRD requirement
- [ ] Handoff Plan has 100-150 checkboxes (not 30-40)
- [ ] You've chosen Horizontal or Vertical approach consciously
- [ ] You're prepared to stop at stage gates (don't skip them)
- [ ] You have all three documents saved for CONTINUE_PROMPT
- [ ] You know where to find these prompts when you need them

**You're ready. Go build.** ✅

---

<!-- END OF EBOOK -->

