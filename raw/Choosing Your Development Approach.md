# Choosing Your Development Approach

**Version:** 1.0  
**Purpose:** Help you decide between horizontal (layered) and vertical (feature-slice) development approaches.

---

## The Two Approaches

The framework supports **two different ways** to organize your project stages:

### 1. Horizontal Approach (Default)
Organize stages by **technology layer**:
- Stage 1: Setup
- Stage 2: All Backend APIs
- Stage 3: All Frontend Pages
- Stage 4: Integration
- Stage 5: Testing & Documentation

### 2. Vertical Approach (Iterative)
Organize stages by **business feature**:
- Stage 1: Minimal Working Installation
- Stage 2: Feature A (Backend + Frontend + Integration)
- Stage 3: Feature B (Backend + Frontend + Integration)
- Stage 4: Feature C (Backend + Frontend + Integration)
- Stage 5: Polish & Finalization

---

## Quick Decision Guide

### Choose **Horizontal** if:
- ✅ Your project is **very simple** (e.g., a landing page with one API)
- ✅ You have **1-3 features** total
- ✅ You're comfortable waiting until Stage 4 to see it work
- ✅ You prefer building all backends first, then all frontends
- ✅ Integration is straightforward and low-risk

**Example projects:**
- Random number generator (landing page + one API endpoint)
- Simple portfolio website
- Basic CRUD API with minimal UI

---

### Choose **Vertical** if:
- ✅ Your project has **4+ features**
- ✅ You want to see **working features early**
- ✅ You want to **demo progress** to stakeholders
- ✅ You prefer **continuous integration** over big-bang integration
- ✅ You want to **reduce risk** by integrating incrementally
- ✅ You're building a **business application** (e.g., booking system, e-commerce)

**Example projects:**
- Hair salon booking system
- E-commerce platform
- Project management tool
- Social media application
- Any multi-feature business application

---

## Detailed Comparison

| Aspect | Horizontal (Layered) | Vertical (Feature Slices) |
|:-------|:---------------------|:--------------------------|
| **Organization** | By technology layer | By business feature |
| **Stage 2** | "Backend Development" | "Feature A (complete)" |
| **Stage 3** | "Frontend Development" | "Feature B (complete)" |
| **First working system** | After Stage 4 (Integration) | After Stage 1 (Minimal Install) |
| **Integration** | All at once (big-bang) | Continuous (incremental) |
| **Risk** | Higher (late integration) | Lower (early integration) |
| **Feedback** | Late (after Stage 4) | Early (after each stage) |
| **Demos** | Hard until near end | Easy after each stage |
| **Debugging** | Complex (many changes at once) | Simple (isolated to one feature) |
| **Motivation** | Lower (no visible progress) | Higher (see features working) |
| **Flexibility** | Lower (hard to reprioritize) | Higher (easy to reprioritize) |
| **Best for** | Simple projects (1-3 features) | Complex projects (4+ features) |
| **Time to first demo** | 60-80% through project | 20-30% through project |
| **Complexity** | Lower (simpler plan) | Higher (more planning needed) |

---

## When Each Approach Shines

### Horizontal Approach is Best When:

**Scenario 1: Very Simple Project**
> "I'm building a landing page that displays a random number from a backend API."

**Why horizontal works:**
- Only 1-2 features total
- Integration is trivial
- No need for early demos
- Faster to plan (fewer stages)

**Scenario 2: Backend-First Project**
> "I'm building a REST API that will be consumed by a mobile app (built separately)."

**Why horizontal works:**
- Frontend isn't part of this project
- Focus is entirely on backend
- No integration needed yet

**Scenario 3: Prototype/POC**
> "I'm building a quick proof-of-concept to validate an idea."

**Why horizontal works:**
- Speed is more important than process
- No need for incremental demos
- Throwaway code (won't be maintained)

---

### Vertical Approach is Best When:

**Scenario 1: Multi-Feature Business Application**
> "I'm building a hair salon booking system with customer booking, stylist schedules, and email reminders."

**Why vertical works:**
- 3+ distinct features
- Each feature has value on its own
- Can demo booking feature before building schedule view
- Reduces integration risk

**Scenario 2: Stakeholder Demos Required**
> "I need to show progress to my client every week."

**Why vertical works:**
- Each stage delivers a working feature to demo
- Stakeholders see tangible progress
- Can get feedback and adjust priorities

**Scenario 3: Uncertain Requirements**
> "I'm not 100% sure what features we need yet."

**Why vertical works:**
- Build and test one feature at a time
- Get user feedback early
- Pivot or reprioritize based on learnings
- Don't waste time building features that won't be used

**Scenario 4: Team Collaboration**
> "Multiple developers will work on this project."

**Why vertical works:**
- Each developer can own a complete feature
- Less merge conflicts (working on different features)
- Clear ownership and accountability

---

## Hybrid Approach (Advanced)

You can also **mix both approaches**:

```
Stage 1: Minimal Working Installation (Vertical)
Stage 2: Core Backend APIs (Horizontal)
Stage 3: Feature A (Vertical Slice)
Stage 4: Feature B (Vertical Slice)
Stage 5: Feature C (Vertical Slice)
Stage 6: Polish & Finalization (Horizontal)
```

**When to use hybrid:**
- You have shared backend infrastructure that multiple features depend on
- You want to build the foundation first, then features incrementally

---

## How to Specify Your Choice

### For Horizontal Approach (Default):
Use the standard `STAGES_PROMPT` from `ALL_PROMPTS.md`. No modifications needed.

### For Vertical Approach:
Use the modified `STAGES_PROMPT_VERTICAL_SLICES.md` instead of the standard prompt.

### For Hybrid Approach:
Use the standard `STAGES_PROMPT` but add custom instructions:

```markdown
**Stage Organization Preference:**

Please organize stages as follows:
- Stage 1: Minimal Working Installation
- Stage 2: Core Backend Infrastructure (database, authentication, shared services)
- Stages 3-N: One complete feature per stage (backend + frontend + integration)
- Final Stage: Polish & Finalization

Organize Stages 3-N by FEATURE, not by LAYER.
```

---

## Real-World Examples

### Example 1: Simple Project → Horizontal

**Project:** "A landing page that displays cryptocurrency prices from a CoinGecko API."

**Stages (Horizontal):**
1. Setup (scaffolding, Docker)
2. Backend (API proxy to CoinGecko)
3. Frontend (price display page)
4. Integration & Testing
5. Documentation

**Total stages:** 5  
**Time to first working system:** After Stage 4 (~70% through)

---

### Example 2: Complex Project → Vertical

**Project:** "A task management app with user auth, projects, tasks, and team collaboration."

**Stages (Vertical):**
1. Minimal Working Installation
2. User Registration & Login (complete feature)
3. Project Creation & Listing (complete feature)
4. Task Creation & Management (complete feature)
5. Team Collaboration (complete feature)
6. Polish & Finalization

**Total stages:** 6  
**Time to first working system:** After Stage 1 (~15% through)  
**Time to first real feature:** After Stage 2 (~30% through)

---

## Summary: Which Should You Choose?

| Your Situation | Recommended Approach |
|:---------------|:---------------------|
| Simple project (1-3 features) | **Horizontal** |
| Complex project (4+ features) | **Vertical** |
| Need early demos | **Vertical** |
| Backend-only project | **Horizontal** |
| Uncertain requirements | **Vertical** |
| Prototype/POC | **Horizontal** |
| Team collaboration | **Vertical** |
| Solo developer, clear requirements | **Either** (your preference) |

---

## Still Not Sure?

**Default recommendation:** If you're unsure, **choose Vertical**.

**Why?**
- Works well for both simple and complex projects
- Reduces risk through continuous integration
- Provides early feedback
- More motivating (see progress sooner)
- Easier to course-correct

**The only downside:** Slightly more planning upfront (but the framework handles this for you).

---

## Changing Your Mind Mid-Project

**Can you switch approaches mid-project?**

**Yes, but it's not recommended.** If you realize the approach isn't working:

1. **Pause execution**
2. **Update the PRD** if needed
3. **Regenerate the Handoff Plan** with the new approach
4. **Resume from the current working state**

**Better approach:** Choose carefully upfront based on the guidance above.

---

## Final Recommendation

- **Simple projects (1-3 features):** Use **Horizontal** (standard `STAGES_PROMPT`)
- **Complex projects (4+ features):** Use **Vertical** (`STAGES_PROMPT_VERTICAL_SLICES.md`)
- **When in doubt:** Use **Vertical** (safer, more flexible)

---

**Ready to choose? Proceed to the appropriate STAGES_PROMPT!** 🚀

