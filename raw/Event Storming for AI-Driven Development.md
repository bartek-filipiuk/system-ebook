# Event Storming for AI-Driven Development

**Version:** 1.0  
**Purpose:** A structured AI-facilitated Event Storming session to discover business processes, user workflows, and requirements before creating the PRD.  
**Position in Framework:** **Phase 0.5** - Between initial idea and PRD generation.

---

## What is This?

Event Storming is a collaborative workshop technique for exploring complex business domains. In this AI-adapted version, **you play the role of the business stakeholder/client**, and **the AI acts as the facilitator**, asking targeted questions to discover:

- **Domain Events** (what happens in your business)
- **User Workflows** (how users interact with the system)
- **Business Rules** (constraints and logic)
- **Pain Points** (problems to solve)
- **Opportunities** (features to build)
- **MVP Scope** (what to build first)
- **Post-MVP Features** (what comes later)

---

## When to Use Event Storming

### ✅ Use Event Storming When:

- Your project involves **complex business processes** (e.g., e-commerce, booking systems, workflow automation)
- You need to understand **user journeys** across multiple steps
- You're building a **business application** (not just a simple landing page)
- You want to **discover requirements** through conversation
- You need to identify **MVP vs. post-MVP features**
- You're not 100% sure what to build yet

### ❌ Skip Event Storming When:

- Your project is very simple (e.g., "display a random number")
- You already have crystal-clear requirements
- You're building a purely technical tool with no business logic
- Time is extremely limited

---

## How It Fits Into the Framework

The updated workflow now looks like this:

```
Step 0: Initial Idea (1 sentence)
    ↓
Step 0.5: EVENT STORMING SESSION (NEW!)
    ↓ [Output: Business process map, MVP scope]
    ↓
Step 1: INIT_PROMPT (15 questions)
    ↓
Step 2: PRD Generation
    ↓
Step 3: Tech Stack
    ↓
Step 4: Stages Plan
    ↓
Step 5-9: Execution
```

**Event Storming happens BEFORE the 15 questions**, helping you clarify your business domain so you can answer those questions more effectively.

---

## The Event Storming Prompt

Copy and paste this prompt into your AI agent to begin the session.

### `EVENT_STORMING_PROMPT.md`

```markdown
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

## Example Session Flow

Here's what a typical Event Storming session looks like:

### Your Input (Project Idea)
> "I want to build an online booking system for a hair salon where customers can book appointments, stylists can manage their schedules, and the owner can see revenue reports."

### AI's Response (Phase 1 Questions)

The AI asks 5-7 questions about your domain:

1. "What are the main types of services offered at the salon (e.g., haircut, coloring, styling)?"
2. "Walk me through what happens from the moment a customer decides to book an appointment until they leave the salon."
3. "Who are the key actors in this system? (e.g., customers, stylists, receptionists, owners)"
4. "What triggers the booking process? Does a customer call, walk in, or book online?"
5. "What happens after an appointment is completed? (e.g., payment, feedback, rebooking)"
6. "Are there any recurring appointments or loyalty programs?"
7. "What happens if a customer needs to cancel or reschedule?"

### You Answer Each Question

You provide detailed answers based on your business knowledge.

### AI Moves to Phase 2

The AI then asks 5-7 questions about user workflows, and so on through all 5 phases.

### AI Generates the Summary

After all phases, the AI produces a comprehensive **Event Storming Summary Document** that looks like this:

---

## Example Output: Event Storming Summary

```markdown
# Event Storming Summary: Hair Salon Booking System

## 1. Domain Overview

This system manages the end-to-end appointment booking process for a hair salon, including customer bookings, stylist schedule management, and business reporting.

## 2. Key Domain Events (Timeline)

1. **Customer Browses Services** – Customer views available services and prices
2. **Customer Selects Service** – Customer chooses a specific service
3. **Customer Checks Availability** – System shows available time slots
4. **Customer Books Appointment** – Appointment is created and confirmed
5. **Reminder Sent** – System sends reminder 24 hours before appointment
6. **Customer Arrives** – Customer checks in at salon
7. **Service Delivered** – Stylist completes the service
8. **Payment Processed** – Customer pays for the service
9. **Feedback Requested** – System asks for review/rating
10. **Appointment Completed** – Appointment is marked as done

## 3. User Workflows

### Customer Booking Journey
1. Customer visits website/app
2. Browses services and prices
3. Selects desired service
4. Chooses preferred stylist (optional)
5. Picks available time slot
6. Enters contact information
7. Confirms booking
8. Receives confirmation email/SMS

### Stylist Schedule Management Journey
1. Stylist logs into dashboard
2. Views daily/weekly schedule
3. Marks availability/unavailability
4. Receives notification of new booking
5. Prepares for appointment
6. Marks appointment as complete
7. Views earnings summary

### Owner Reporting Journey
1. Owner logs into admin dashboard
2. Views revenue reports (daily/weekly/monthly)
3. Sees booking statistics
4. Reviews stylist performance
5. Identifies peak times
6. Exports data for accounting

## 4. Actors & Roles

| Actor | Role | Key Actions |
|:------|:-----|:------------|
| Customer | Books and attends appointments | Browse, book, cancel, pay, review |
| Stylist | Delivers services | Manage schedule, view bookings, complete appointments |
| Owner | Manages business | View reports, manage stylists, set prices |
| System | Automates processes | Send reminders, process payments, generate reports |

## 5. Business Rules

- A customer can only book one appointment at a time
- Appointments must be at least 2 hours in the future
- Cancellations must be made at least 24 hours in advance
- Stylists can set their own availability within business hours
- Business hours: Monday-Saturday, 9 AM - 7 PM
- Each service has a fixed duration (e.g., haircut = 30 min, coloring = 90 min)
- No double-booking: one stylist, one customer per time slot
- Payment is required at the time of service (not at booking)

## 6. Pain Points (Current Problems)

- **Manual Scheduling:** Currently done via phone calls, prone to errors
- **No-Shows:** Customers forget appointments, no automated reminders
- **Double Bookings:** Happens when multiple people answer phones
- **Limited Visibility:** Owner can't see real-time booking status
- **Time-Consuming:** Stylists spend too much time on phone instead of serving customers
- **No Customer History:** Can't track repeat customers or preferences

## 7. Opportunities (Features to Consider)

- **Automated Reminders:** Reduce no-shows by 50%
- **Online Booking:** 24/7 availability, no phone calls needed
- **Customer Profiles:** Track preferences, history, favorite stylists
- **Loyalty Program:** Reward repeat customers
- **Dynamic Pricing:** Surge pricing during peak hours
- **Waitlist:** Fill cancellations automatically
- **Mobile App:** Better customer experience
- **Analytics Dashboard:** Data-driven business decisions

## 8. MVP Scope (Build First)

**Must-Have Features:**
1. ✅ Customer can view services and prices
2. ✅ Customer can see available time slots
3. ✅ Customer can book an appointment
4. ✅ Customer receives booking confirmation (email)
5. ✅ Stylist can view their schedule
6. ✅ Stylist can mark availability
7. ✅ System prevents double-booking
8. ✅ Owner can view basic revenue report
9. ✅ Automated reminder sent 24 hours before appointment
10. ✅ Customer can cancel appointment (with 24-hour rule)

**Out of MVP (but important):**
- Payment processing (manual for now)
- Customer reviews/ratings
- Stylist performance metrics
- Mobile app (web-only for MVP)

## 9. Post-MVP Features (Build Later)

**Phase 2 (After MVP Launch):**
- Online payment integration
- Customer reviews and ratings
- SMS reminders (in addition to email)
- Customer profile with booking history

**Phase 3 (Future Enhancements):**
- Mobile app (iOS/Android)
- Loyalty program
- Waitlist functionality
- Advanced analytics dashboard
- Multi-location support

**Phase 4 (Nice to Have):**
- Dynamic pricing
- AI-powered stylist recommendations
- Integration with accounting software
- Marketing automation

## 10. Open Questions

| Question | Impact | Status |
|:---------|:-------|:-------|
| Do we need to support walk-in appointments? | Medium | To be decided |
| Should customers be able to choose specific stylists? | High | Yes - confirmed |
| How do we handle stylist sick days? | Medium | To be decided |
| Do we need multi-language support? | Low | Not for MVP |
| Should we integrate with Google Calendar? | Medium | Post-MVP |
```

---

## What Happens Next?

After the Event Storming session, you have a **comprehensive understanding** of your business domain. Now you can proceed to the standard framework:

1. **Use the Event Storming Summary** to inform your answers to the 15 PRD questions
2. The **MVP Scope** from Event Storming becomes the "Scope & Features" section of your PRD
3. The **Post-MVP Features** inform your "Out of Scope" section
4. The **Business Rules** become your "Assumptions & Dependencies"
5. The **Pain Points** inform your "Problem Statement"

---

## Time Investment

- **Event Storming Session:** 45-90 minutes
- **Review Summary:** 10-15 minutes
- **Total:** ~1-2 hours

**Value:** Saves days of rework by clarifying requirements upfront.

---

## Tips for a Successful Session

### ✅ DO:
- Think like a business owner, not a developer
- Describe what happens, not how to implement it
- Be specific about edge cases
- Challenge the AI if questions don't make sense
- Ask for clarification if needed
- Take your time with answers

### ❌ DON'T:
- Rush through the questions
- Think about technical implementation yet
- Skip phases
- Give vague answers like "it depends"
- Worry about perfection (you can refine later)

---

## Integration with the Framework

The updated **COMPLETE_WORKFLOW.md** now includes:

```
PHASE 0: Initial Idea (5-10 min)
    ↓
PHASE 0.5: EVENT STORMING SESSION (45-90 min) ← NEW!
    ↓ [Output: Event Storming Summary]
    ↓
PHASE 1: Initial Requirements Gathering (15-20 min)
    ↓ [AI asks 15 questions, informed by Event Storming]
    ↓
PHASE 2: PRD Generation (5-10 min)
    ↓ [PRD includes insights from Event Storming]
    ↓
... (rest of the workflow continues)
```

---

## When to Skip Event Storming

If your project is simple (e.g., "a landing page that shows a random number"), you can skip Event Storming and go straight to the INIT_PROMPT. Event Storming adds the most value for **complex business applications** with multiple user types, workflows, and business rules.

---

## Ready to Start?

1. Copy the **EVENT_STORMING_PROMPT** above
2. Replace `[INSERT YOUR PROJECT IDEA HERE]` with your idea
3. Paste it into your AI agent
4. Answer the questions thoughtfully
5. Review the generated Event Storming Summary
6. Proceed to the standard framework (INIT_PROMPT)

**Good luck discovering your business domain!** 🚀

