# Vertical Slice Development Guide

**Version:** 1.0  
**Purpose:** A comprehensive guide for organizing projects using the vertical-slice (iterative, feature-by-feature) development approach within the AI-Driven Development Framework.

---

## What is Vertical Slice Development?

Vertical Slice Development is an iterative approach where you build **complete features** one at a time, from backend to frontend to integration, rather than building all backends first, then all frontends.

### Traditional Horizontal Approach (Layered):
```
Stage 1: Setup
Stage 2: ALL Backend APIs
Stage 3: ALL Frontend Pages
Stage 4: Integration
Stage 5: Testing
```

**Problem:** You don't have a working system until Stage 4.

### Vertical Slice Approach (Feature-by-Feature):
```
Stage 1: Minimal Working Installation
Stage 2: Feature A (Backend + Frontend + Integration)
Stage 3: Feature B (Backend + Frontend + Integration)
Stage 4: Feature C (Backend + Frontend + Integration)
Stage 5: Polish & Finalization
```

**Benefit:** You have a working system after Stage 1, and each stage adds a complete, testable feature.

---

## Why Use Vertical Slices?

| Benefit | Description |
|:--------|:------------|
| **Always Deployable** | After Stage 1, you always have a working system you can deploy |
| **Early Feedback** | You can test and demo features immediately after they're built |
| **Reduced Integration Risk** | Integration happens continuously, not all at once at the end |
| **Better Motivation** | You see tangible progress after each stage |
| **Easier Debugging** | Problems are isolated to the current feature |
| **Stakeholder Demos** | You can show working features to stakeholders early and often |
| **Incremental Value** | Each stage delivers business value |
| **Flexibility** | You can reprioritize features based on feedback |

---

## How It Fits Into the Framework

The framework **fully supports** vertical slice development. You just need to communicate your preference when generating the Handoff Plan.

### Updated Workflow:

```
Phase 0-4: Planning (same as before)
    ↓
Phase 5: Execution - Stage 1 (Minimal Working Installation)
    ↓
Phase 6: Stage Gate
    ↓
Phase 7: Execution - Stage 2 (Feature A - Complete Vertical Slice)
    ↓
Phase 6: Stage Gate
    ↓
Phase 7: Execution - Stage 3 (Feature B - Complete Vertical Slice)
    ↓
... (repeat for all features)
    ↓
Phase 9: Completion
```

---

## Stage Structure for Vertical Slices

### Stage 1: Minimal Working Installation

**Goal:** Establish a basic end-to-end system with the simplest possible feature.

**What to include:**
- Project scaffolding (directories, config files)
- Basic backend with one simple endpoint (e.g., `GET /api/health`)
- Basic frontend with one simple page (e.g., homepage that calls the health endpoint)
- Docker/containerization setup
- End-to-end verification (frontend → backend → response)

**What NOT to include:**
- Any real business logic
- Database (unless absolutely necessary)
- Authentication
- Complex UI

**Time estimate:** 30-60 minutes

**Output:** A working, deployable system that does almost nothing, but proves the stack works.

---

### Stage 2-N: Feature Vertical Slices

**Goal:** Implement one complete feature from backend to frontend.

**Each feature stage should include:**

1. **Backend Development**
   - API endpoint(s) for the feature
   - Database models/migrations (if needed)
   - Business logic
   - Validation
   - Error handling
   - Unit tests

2. **Frontend Development**
   - UI components for the feature
   - Forms/inputs
   - Data display
   - Loading states
   - Error states

3. **Integration**
   - Connect frontend to backend API
   - Handle API responses
   - Handle errors
   - Update UI based on data

4. **End-to-End Testing**
   - Test the complete feature flow
   - Verify data persistence
   - Test edge cases
   - Verify error handling

**Time estimate:** 1-3 hours per feature (depending on complexity)

**Output:** A fully working, testable feature integrated into the system.

---

### Final Stage: Polish & Finalization

**Goal:** Prepare the system for production.

**What to include:**
- Code refactoring
- Performance optimization
- Comprehensive error handling
- Security hardening
- Documentation
- Final end-to-end testing
- Deployment preparation

**Time estimate:** 1-2 hours

**Output:** Production-ready system.

---

## How to Specify Vertical Slices in the Framework

### Method 1: Modify the STAGES_PROMPT (Recommended)

When you reach Phase 4 (Stages Plan Generation), use this **modified STAGES_PROMPT**:

```markdown
Perfect. The Tech Stack is defined.

Now for the final planning step before coding: **Step 3: Staged Handoff Plan.**

Your task is to create a `HANDOFF_STAGES_PLAN.md` document. This document will break down the entire development process into logical, sequential stages.

**IMPORTANT: Development Approach Preference**

I prefer a **vertical-slice, iterative development approach**:

1. **Stage 1 must create a Minimal Working Installation:**
   - Basic project scaffolding
   - Simple backend endpoint (e.g., GET /api/health)
   - Simple frontend page that calls the backend
   - Docker/containerization setup
   - End-to-end verification
   - NO business logic, NO real features yet

2. **Each subsequent stage (2-N) must implement ONE complete feature as a vertical slice:**
   - Backend API for the feature
   - Frontend UI for the feature
   - Integration between backend and frontend
   - End-to-end testing of the feature
   - Each stage should result in a fully working, testable increment

3. **Final stage should be Polish & Finalization:**
   - Code refactoring
   - Error handling
   - Documentation
   - Final testing

**Critical Rules:**
- Organize stages by FEATURE, not by LAYER (backend/frontend)
- Do NOT create separate "backend stage" and "frontend stage"
- Each feature stage must deliver a complete, working feature
- Each stage must build on the previous working system

Use the PRD User Stories (Section 3) to determine which features to build and in what order. Prioritize based on the Priority column (Must-Have first).

The plan must be so clear and granular that an AI coding agent can follow it from start to finish without ambiguity.

Here are the documents for your reference:

**PRD:**
---
[Paste the full PRD Markdown here.]
---

**Tech Stack:**
---
[Paste the full Tech Stack Markdown here.]
---

Generate the Staged Handoff Plan now.
```

---

### Method 2: Add to PRD Assumptions

In your PRD (Section 5: Assumptions & Dependencies), add:

```markdown
## 5. Assumptions & Dependencies

**Development Approach:**
- We will use a vertical-slice, iterative development approach
- Stage 1 will establish a minimal working installation (basic backend + basic frontend + end-to-end connection)
- Each subsequent stage will implement ONE complete feature (backend + frontend + integration + testing)
- Stages will be organized by FEATURE, not by LAYER (backend/frontend)
- Each stage will result in a fully working, testable increment
```

Then the AI will automatically respect this when generating the Handoff Plan.

---

## Example: Hair Salon Booking System (Vertical Slices)

### Complete Handoff Plan

```markdown
# Handoff & Stages Plan: Hair Salon Booking System

---

## Stage 1: Minimal Working Installation

**Goal:** Establish a basic end-to-end system with project scaffolding and a simple health check.

- [ ] **Task 1.1: Project Scaffolding**
    - [ ] Create monorepo directory structure: `salon-booking/`
    - [ ] Create `backend/` subdirectory
    - [ ] Create `frontend/` subdirectory
    - [ ] Create root `README.md` with project overview
    - [ ] Initialize Git repository

- [ ] **Task 1.2: Backend Setup**
    - [ ] Create `backend/main.py`
    - [ ] Initialize FastAPI app
    - [ ] Create `GET /api/health` endpoint that returns `{"status": "ok"}`
    - [ ] Add CORS middleware for frontend domain
    - [ ] Create `backend/requirements.txt` with dependencies

- [ ] **Task 1.3: Frontend Setup**
    - [ ] Initialize React app in `frontend/`
    - [ ] Create homepage component
    - [ ] Add API client to call `GET /api/health`
    - [ ] Display "System is running" when health check succeeds
    - [ ] Add error handling for failed health check

- [ ] **Task 1.4: Containerization**
    - [ ] Create `backend/Dockerfile`
    - [ ] Create `frontend/Dockerfile`
    - [ ] Create `docker-compose.yml` in root
    - [ ] Configure networking between services

- [ ] **Task 1.5: End-to-End Verification**
    - [ ] Run `docker-compose up`
    - [ ] Visit frontend in browser
    - [ ] Verify "System is running" message appears
    - [ ] Check browser console for errors

**Expected Output:** A working, deployable system with basic frontend and backend connected.

---

## Stage 2: Service Catalog Feature (Vertical Slice)

**Goal:** Implement the ability to view available salon services.

- [ ] **Task 2.1: Backend - Services API**
    - [ ] Create database model for Service (id, name, duration, price)
    - [ ] Create database migration
    - [ ] Seed database with sample services (Haircut, Coloring, Styling)
    - [ ] Create `GET /api/services` endpoint
    - [ ] Return list of all services as JSON
    - [ ] Write unit test for services endpoint

- [ ] **Task 2.2: Frontend - Services Display**
    - [ ] Create `ServicesPage` component
    - [ ] Create `ServiceCard` component
    - [ ] Fetch services from `GET /api/services`
    - [ ] Display services in a grid layout
    - [ ] Show service name, duration, and price
    - [ ] Add loading spinner while fetching
    - [ ] Add error message if fetch fails

- [ ] **Task 2.3: Integration**
    - [ ] Connect `ServicesPage` to backend API
    - [ ] Handle API response
    - [ ] Handle network errors
    - [ ] Add navigation link from homepage to services page

- [ ] **Task 2.4: End-to-End Testing**
    - [ ] Navigate to services page
    - [ ] Verify all seeded services appear
    - [ ] Verify correct data is displayed
    - [ ] Test error handling (stop backend, verify error message)

**Expected Output:** Users can view a list of available services with pricing.

---

## Stage 3: Appointment Booking Feature (Vertical Slice)

**Goal:** Implement the ability for customers to book appointments.

- [ ] **Task 3.1: Backend - Booking API**
    - [ ] Create database model for Booking (id, service_id, customer_name, customer_email, date, time)
    - [ ] Create database migration
    - [ ] Create `POST /api/bookings` endpoint
    - [ ] Validate booking data (required fields, valid date/time)
    - [ ] Check for double-booking (same time slot)
    - [ ] Save booking to database
    - [ ] Return booking confirmation with booking ID
    - [ ] Write unit tests for booking endpoint

- [ ] **Task 3.2: Frontend - Booking Form**
    - [ ] Create `BookingPage` component
    - [ ] Create `BookingForm` component
    - [ ] Add service selection dropdown
    - [ ] Add date picker (only future dates)
    - [ ] Add time picker (business hours only)
    - [ ] Add customer name input
    - [ ] Add customer email input
    - [ ] Add form validation (all fields required)
    - [ ] Add submit button

- [ ] **Task 3.3: Integration**
    - [ ] Connect form to `POST /api/bookings`
    - [ ] Handle successful booking (show confirmation)
    - [ ] Handle validation errors (display error messages)
    - [ ] Handle double-booking error (suggest alternative times)
    - [ ] Clear form after successful booking

- [ ] **Task 3.4: End-to-End Testing**
    - [ ] Fill out booking form with valid data
    - [ ] Submit booking
    - [ ] Verify confirmation message appears
    - [ ] Check database to confirm booking was saved
    - [ ] Test double-booking prevention (try to book same slot twice)
    - [ ] Test form validation (submit with missing fields)

**Expected Output:** Customers can book appointments through the UI, and bookings are saved to the database.

---

## Stage 4: Schedule View Feature (Vertical Slice)

**Goal:** Implement the ability for stylists to view their schedule.

- [ ] **Task 4.1: Backend - Schedule API**
    - [ ] Create `GET /api/schedule` endpoint
    - [ ] Accept query parameters: date (optional, defaults to today)
    - [ ] Query bookings for the specified date
    - [ ] Join with services table to get service details
    - [ ] Return bookings sorted by time
    - [ ] Write unit tests for schedule endpoint

- [ ] **Task 4.2: Frontend - Schedule View**
    - [ ] Create `SchedulePage` component
    - [ ] Create `ScheduleCalendar` component
    - [ ] Fetch schedule from `GET /api/schedule`
    - [ ] Display bookings in chronological order
    - [ ] Show time, customer name, service name
    - [ ] Add date navigation (previous/next day)
    - [ ] Add "Today" button to jump to current date
    - [ ] Show "No bookings" message if schedule is empty

- [ ] **Task 4.3: Integration**
    - [ ] Connect calendar to backend API
    - [ ] Handle date changes (fetch new data)
    - [ ] Handle loading state
    - [ ] Handle errors
    - [ ] Auto-refresh every 5 minutes

- [ ] **Task 4.4: End-to-End Testing**
    - [ ] Create test bookings for today
    - [ ] Navigate to schedule page
    - [ ] Verify bookings appear in correct order
    - [ ] Test date navigation
    - [ ] Test "Today" button
    - [ ] Verify auto-refresh works

**Expected Output:** Stylists can view their daily schedule with all bookings.

---

## Stage 5: Email Reminder Feature (Vertical Slice)

**Goal:** Implement automated email reminders 24 hours before appointments.

- [ ] **Task 5.1: Backend - Email Service**
    - [ ] Install email library (e.g., `python-email`)
    - [ ] Configure SMTP settings
    - [ ] Create email template for reminders
    - [ ] Create `send_reminder_email()` function
    - [ ] Write unit test for email function (mock SMTP)

- [ ] **Task 5.2: Backend - Scheduled Job**
    - [ ] Install scheduler library (e.g., `APScheduler`)
    - [ ] Create scheduled job that runs hourly
    - [ ] Query bookings happening in 24 hours
    - [ ] Send reminder email for each booking
    - [ ] Log sent reminders
    - [ ] Handle email failures gracefully

- [ ] **Task 5.3: Frontend - Reminder Preferences (Optional)**
    - [ ] Add checkbox to booking form: "Send me a reminder"
    - [ ] Update booking model to include `send_reminder` field
    - [ ] Only send reminders if customer opted in

- [ ] **Task 5.4: Integration & Testing**
    - [ ] Create a test booking for tomorrow
    - [ ] Manually trigger the scheduled job
    - [ ] Verify reminder email is sent
    - [ ] Check email content is correct
    - [ ] Verify reminder is logged

**Expected Output:** Customers receive automated email reminders 24 hours before their appointments.

---

## Stage 6: Polish & Finalization

**Goal:** Prepare the system for production deployment.

- [ ] **Task 6.1: Code Refactoring**
    - [ ] Review all code for consistency
    - [ ] Extract repeated logic into helper functions
    - [ ] Add comments to complex sections
    - [ ] Remove console.log statements
    - [ ] Remove unused imports

- [ ] **Task 6.2: Error Handling**
    - [ ] Add try-catch blocks to all API calls
    - [ ] Add user-friendly error messages
    - [ ] Add logging for server errors
    - [ ] Add 404 page for invalid routes
    - [ ] Add validation error messages

- [ ] **Task 6.3: Documentation**
    - [ ] Update root README with setup instructions
    - [ ] Document API endpoints (request/response format)
    - [ ] Document environment variables
    - [ ] Add troubleshooting section
    - [ ] Add screenshots to README

- [ ] **Task 6.4: Final Testing**
    - [ ] Test complete user journey (view services → book → receive confirmation)
    - [ ] Test stylist journey (view schedule)
    - [ ] Test all error scenarios
    - [ ] Test on different browsers
    - [ ] Run all unit tests
    - [ ] Fix any bugs found

**Expected Output:** Production-ready salon booking system with complete documentation.

---

## Summary

| Stage | Feature | Time Estimate |
|:------|:--------|:--------------|
| 1 | Minimal Working Installation | 30-60 min |
| 2 | Service Catalog | 1-2 hours |
| 3 | Appointment Booking | 2-3 hours |
| 4 | Schedule View | 1-2 hours |
| 5 | Email Reminders | 1-2 hours |
| 6 | Polish & Finalization | 1-2 hours |
| **Total** | **Complete MVP** | **7-12 hours** |
```

---

## Stage Gate Questions for Vertical Slices

### Before Stage 2 (Service Catalog):
1. "Should services be hard-coded or stored in a database?"
2. "Do you want to display service images, or just text information?"
3. "Should services be categorized (e.g., Hair, Nails, Spa)?"

### Before Stage 3 (Appointment Booking):
1. "Should customers be able to choose a specific stylist, or auto-assign?"
2. "Do you want to show available time slots, or let customers pick any time?"
3. "Should booking confirmation be sent via email, or just displayed on screen?"
4. "How should we handle conflicts if two users try to book the same slot?"

### Before Stage 4 (Schedule View):
1. "Should the schedule view be calendar-style or list-style?"
2. "Do you want to show past bookings, or only upcoming ones?"
3. "Should stylists be able to mark bookings as completed?"

### Before Stage 5 (Email Reminders):
1. "Should reminders be sent 24 hours before, or a different timeframe?"
2. "Do you want SMS reminders in addition to email?"
3. "Should customers be able to opt out of reminders?"

---

## Tips for Success

### ✅ DO:
- Start with the absolute minimum in Stage 1
- Build one complete feature per stage
- Test end-to-end after each stage
- Deploy/demo after each stage if possible
- Keep features small and focused
- Prioritize must-have features first

### ❌ DON'T:
- Build all backends first, then all frontends
- Move to the next feature before the current one works
- Skip end-to-end testing
- Add "nice to have" features before must-haves
- Build features that aren't in the PRD

---

## Troubleshooting

### "The AI generated a horizontal plan instead of vertical slices"

**Solution:** Use the modified STAGES_PROMPT with explicit instructions about vertical slices.

### "A feature stage is too large"

**Solution:** Break it into two smaller features. For example, split "Booking Feature" into:
- Stage 2: View Available Time Slots
- Stage 3: Submit Booking

### "I want to change the order of features"

**Solution:** Reorder the stages in the Handoff Plan before starting execution. Just make sure dependencies are respected (e.g., you need Service Catalog before Booking).

### "A feature needs backend changes after frontend is done"

**Solution:** That's fine! Within a stage, you can iterate. The key is that the stage isn't "done" until the feature works end-to-end.

---

## Comparison: Horizontal vs. Vertical

| Aspect | Horizontal (Layered) | Vertical (Feature Slices) |
|:-------|:---------------------|:--------------------------|
| **Organization** | By technology layer | By business feature |
| **First working system** | After integration stage | After Stage 1 |
| **Integration** | All at once (risky) | Continuous (safe) |
| **Feedback** | Late | Early and often |
| **Demos** | Hard until near end | Easy after each stage |
| **Debugging** | Complex (many changes) | Simple (isolated feature) |
| **Motivation** | Low (no visible progress) | High (see features working) |
| **Best for** | Small, simple projects | Medium to large projects |

---

## Final Thoughts

Vertical slice development is **ideal for AI-driven projects** because:

1. The AI can focus on one feature at a time
2. You can verify the AI's work after each stage
3. You can course-correct early if something goes wrong
4. You always have a working system to fall back on

**The framework fully supports this approach – just communicate your preference when generating the Handoff Plan!**

---

**Ready to build with vertical slices? Use the modified STAGES_PROMPT and start with Stage 1!** 🚀

