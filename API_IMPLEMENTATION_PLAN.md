# AI-Driven Development Framework API - Complete Implementation Plan

## Table of Contents
1. [Overview](#overview)
2. [Architecture](#architecture)
3. [Database Schema](#database-schema)
4. [API Endpoints Specification](#api-endpoints-specification)
5. [Workflow State Machine](#workflow-state-machine)
6. [Implementation Plan (Phased)](#implementation-plan-phased)
7. [Cost Estimation](#cost-estimation)
8. [LangFuse Integration](#langfuse-integration)
9. [Project Structure](#project-structure)
10. [Key Implementation Details](#key-implementation-details)

---

## Overview

### Purpose
Build a FastAPI backend that automates the AI-Driven Development Framework workflow from the ebook. Users submit a project idea and receive 3-4 generated documents (Event Storming Summary, PRD, Tech Stack, Execution Plan).

### Key Requirements
- **Authentication:** Single shared admin token
- **LLM Provider:** OpenRouter (multi-model support)
- **Observability:** LangFuse for cost tracking and monitoring
- **Storage:** PostgreSQL for state, documents, logs
- **Real-time Updates:** WebSocket for progress broadcasting
- **Rate Limiting:** SlowAPI (1 req/sec initially)
- **Deployment:** Docker, targeting 100 users
- **Smart Detection:** LLM-based decision for Event Storming and Horizontal/Vertical approach

### Tech Stack
```
Backend: FastAPI (Python 3.11+)
Database: PostgreSQL 15+
ORM: SQLAlchemy 2.0 + Alembic
Validation: Pydantic v2
LLM: OpenRouter API
Observability: LangFuse
Rate Limiting: SlowAPI
WebSockets: FastAPI native
Deployment: Docker + docker-compose
```

---

## Architecture

### High-Level Architecture Diagram

```
┌─────────────────────────────────────────────────┐
│ Frontend (Chatbot UI)                           │
│ ├── User enters idea                            │
│ ├── WebSocket connection for progress           │
│ └── Displays generated documents (MD)           │
└─────────────────┬───────────────────────────────┘
                  │ HTTP + WebSocket
                  ▼
┌─────────────────────────────────────────────────┐
│ FastAPI Backend                                 │
│ ├── Auth Middleware (admin token validation)   │
│ ├── Rate Limiting (SlowAPI: 1 req/sec)         │
│ │                                               │
│ ├── REST Endpoints:                             │
│ │   POST /api/v1/projects (create with idea)   │
│ │   GET  /api/v1/projects/{id}                 │
│ │   POST /api/v1/projects/{id}/start-workflow  │
│ │   GET  /api/v1/projects/{id}/documents       │
│ │   POST /api/v1/projects/{id}/retry           │
│ │   GET  /api/v1/projects/{id}/costs           │
│ │                                               │
│ ├── WebSocket Endpoint:                         │
│ │   WS /api/v1/projects/{id}/progress          │
│ │                                               │
│ ├── Background Tasks (FastAPI BG):             │
│ │   ├── Phase 0: Smart detection               │
│ │   ├── Phase 0.5: Event Storming (if needed)  │
│ │   ├── Phase 1-2: PRD Generation              │
│ │   ├── Phase 3: Tech Stack                    │
│ │   └── Phase 4: Execution Plan                │
│ │                                               │
│ └── Services:                                   │
│     ├── LLM Service (OpenRouter calls)         │
│     ├── Prompt Manager (templates from ebook)  │
│     └── State Manager (workflow transitions)   │
└─────────────────┬───────────────────────────────┘
                  │
        ┌─────────┴─────────┐
        ▼                   ▼
┌──────────────┐    ┌──────────────┐
│ PostgreSQL   │    │ LangFuse     │
│ (State+Docs) │    │ (Observ.)    │
└──────────────┘    └──────────────┘
        │                   │
        └───────────────────┘
                  │
                  ▼
        ┌──────────────┐
        │ OpenRouter   │
        │ (LLM API)    │
        └──────────────┘
```

---

## Database Schema

### Complete SQL Schema

```sql
-- Users table (admin access)
CREATE TABLE users (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    email VARCHAR(255) UNIQUE NOT NULL,
    admin_token VARCHAR(255) UNIQUE NOT NULL,
    is_active BOOLEAN DEFAULT true,
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);

-- Projects table
CREATE TABLE projects (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID REFERENCES users(id) ON DELETE CASCADE,
    idea TEXT NOT NULL,
    status VARCHAR(50) NOT NULL, -- CREATED, PROCESSING, COMPLETED, FAILED
    current_phase VARCHAR(50), -- SMART_DETECTION, EVENT_STORMING, PRD, TECH_STACK, EXECUTION_PLAN
    metadata JSONB DEFAULT '{}', -- stores smart detection results, retry count, etc.
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW(),
    completed_at TIMESTAMP
);

-- Workflow states (tracks progress through phases)
CREATE TABLE workflow_states (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    project_id UUID REFERENCES projects(id) ON DELETE CASCADE,
    phase VARCHAR(50) NOT NULL, -- SMART_DETECTION, EVENT_STORMING, PRD, TECH_STACK, EXECUTION_PLAN
    status VARCHAR(50) NOT NULL, -- PENDING, IN_PROGRESS, COMPLETED, FAILED
    input_data JSONB, -- LLM prompts, user answers
    output_data JSONB, -- LLM responses
    error_message TEXT,
    started_at TIMESTAMP,
    completed_at TIMESTAMP,
    created_at TIMESTAMP DEFAULT NOW()
);

-- Documents table (stores generated markdown)
CREATE TABLE documents (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    project_id UUID REFERENCES projects(id) ON DELETE CASCADE,
    type VARCHAR(50) NOT NULL, -- EVENT_STORMING, PRD, TECH_STACK, EXECUTION_PLAN
    content_md TEXT NOT NULL,
    metadata JSONB DEFAULT '{}', -- model used, generation params, etc.
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);

-- LLM logs (cost tracking, synced with LangFuse)
CREATE TABLE llm_logs (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    project_id UUID REFERENCES projects(id) ON DELETE CASCADE,
    workflow_state_id UUID REFERENCES workflow_states(id) ON DELETE CASCADE,
    phase VARCHAR(50) NOT NULL,
    model VARCHAR(100) NOT NULL,
    langfuse_trace_id VARCHAR(255), -- LangFuse trace ID for linking
    prompt_tokens INTEGER,
    completion_tokens INTEGER,
    total_tokens INTEGER,
    cost_usd DECIMAL(10, 6),
    latency_ms INTEGER,
    created_at TIMESTAMP DEFAULT NOW()
);

-- Indexes for performance
CREATE INDEX idx_projects_user_id ON projects(user_id);
CREATE INDEX idx_projects_status ON projects(status);
CREATE INDEX idx_workflow_states_project_id ON workflow_states(project_id);
CREATE INDEX idx_documents_project_id ON documents(project_id);
CREATE INDEX idx_llm_logs_project_id ON llm_logs(project_id);
```

---

## API Endpoints Specification

### Authentication
All endpoints require header: `Authorization: Bearer {ADMIN_TOKEN}`

### Endpoints

#### 1. Create Project
```http
POST /api/v1/projects
Content-Type: application/json

Request:
{
    "idea": "I want to build an online booking system for a hair salon...",
    "user_id": "uuid-here"
}

Response: 201 Created
{
    "project_id": "uuid",
    "status": "CREATED",
    "created_at": "2025-11-09T10:00:00Z"
}
```

#### 2. Start Workflow
```http
POST /api/v1/projects/{project_id}/start-workflow

Response: 200 OK
{
    "project_id": "uuid",
    "status": "PROCESSING",
    "current_phase": "SMART_DETECTION",
    "websocket_url": "ws://localhost:8000/api/v1/projects/{project_id}/progress"
}
```

#### 3. Get Project Status
```http
GET /api/v1/projects/{project_id}

Response: 200 OK
{
    "project_id": "uuid",
    "idea": "...",
    "status": "COMPLETED",
    "current_phase": "EXECUTION_PLAN",
    "metadata": {
        "use_event_storming": true,
        "use_vertical_approach": false,
        "total_cost_usd": 0.45,
        "total_duration_seconds": 342
    },
    "created_at": "...",
    "completed_at": "..."
}
```

#### 4. Get All Documents
```http
GET /api/v1/projects/{project_id}/documents

Response: 200 OK
{
    "project_id": "uuid",
    "documents": [
        {
            "type": "EVENT_STORMING",
            "content_md": "# Event Storming Summary...",
            "created_at": "..."
        },
        {
            "type": "PRD",
            "content_md": "# Product Requirements Document...",
            "created_at": "..."
        },
        {
            "type": "TECH_STACK",
            "content_md": "# Tech Stack Document...",
            "created_at": "..."
        },
        {
            "type": "EXECUTION_PLAN",
            "content_md": "# Handoff & Stages Plan...",
            "created_at": "..."
        }
    ]
}
```

#### 5. Get Single Document
```http
GET /api/v1/projects/{project_id}/documents/{type}

Response: 200 OK
{
    "type": "PRD",
    "content_md": "# Product Requirements Document...",
    "created_at": "...",
    "updated_at": "..."
}
```

#### 6. Retry Failed Workflow
```http
POST /api/v1/projects/{project_id}/retry
Content-Type: application/json

Request:
{
    "from_phase": "TECH_STACK"  // Optional, defaults to failed phase
}

Response: 200 OK
{
    "project_id": "uuid",
    "status": "PROCESSING",
    "current_phase": "TECH_STACK"
}
```

#### 7. Get Cost Breakdown
```http
GET /api/v1/projects/{project_id}/costs

Response: 200 OK
{
    "project_id": "uuid",
    "total_cost_usd": 0.45,
    "breakdown": [
        {
            "phase": "SMART_DETECTION",
            "model": "openai/gpt-4o-mini",
            "tokens": 1250,
            "cost_usd": 0.002
        },
        {
            "phase": "PRD",
            "model": "anthropic/claude-3.5-sonnet",
            "tokens": 8500,
            "cost_usd": 0.255
        }
    ]
}
```

#### 8. WebSocket Progress Updates
```http
WS /api/v1/projects/{project_id}/progress

Messages sent to client:

{
    "type": "phase_started",
    "phase": "PRD",
    "timestamp": "2025-11-09T10:05:23Z",
    "message": "Generating Product Requirements Document..."
}

{
    "type": "phase_progress",
    "phase": "PRD",
    "step": "Asking 15 questions",
    "progress_percent": 30,
    "timestamp": "..."
}

{
    "type": "phase_completed",
    "phase": "PRD",
    "duration_seconds": 45,
    "cost_usd": 0.15,
    "timestamp": "..."
}

{
    "type": "phase_failed",
    "phase": "TECH_STACK",
    "error": "OpenRouter API rate limit exceeded",
    "retry_available": true,
    "timestamp": "..."
}

{
    "type": "workflow_completed",
    "total_duration_seconds": 342,
    "total_cost_usd": 0.45,
    "documents_generated": 4,
    "timestamp": "..."
}
```

---

## Workflow State Machine

### Visual State Flow

```
START: Project Created
   │
   ├─> POST /projects/{id}/start-workflow
   │
   ▼
┌──────────────────────┐
│ SMART_DETECTION      │ (GPT-4o-mini analyzes idea)
│ Duration: ~5-10s     │
│ Cost: ~$0.001-0.002  │
└──────────┬───────────┘
           │
           ├─> Determines: use_event_storming (true/false)
           │
           ▼
      [Conditional Branch]
           │
           ├─> IF use_event_storming = true
           │   │
           │   ▼
           │ ┌──────────────────────┐
           │ │ EVENT_STORMING       │ (Phase 0.5)
           │ │ Duration: ~60-90s    │
           │ │ Cost: ~$0.05-0.10    │
           │ └──────────┬───────────┘
           │            │
           │            │ Generates: EVENT_STORMING.md
           │            │
           └────────────┘
                        │
                        ▼
           ┌──────────────────────┐
           │ PRD_GENERATION       │ (Phase 1-2)
           │ Duration: ~45-60s    │
           │ Cost: ~$0.15-0.25    │
           └──────────┬───────────┘
                      │
                      │ Generates: PRD.md
                      │
                      ▼
           ┌──────────────────────┐
           │ TECH_STACK          │ (Phase 3)
           │ Duration: ~30-45s    │
           │ Cost: ~$0.08-0.12    │
           └──────────┬───────────┘
                      │
                      │ Generates: TECH_STACK.md
                      │ Smart detection: horizontal vs vertical
                      │
                      ▼
           ┌──────────────────────┐
           │ EXECUTION_PLAN       │ (Phase 4)
           │ Duration: ~45-60s    │
           │ Cost: ~$0.12-0.18    │
           └──────────┬───────────┘
                      │
                      │ Generates: EXECUTION_PLAN.md
                      │
                      ▼
           ┌──────────────────────┐
           │ COMPLETED            │
           │ All docs ready       │
           └──────────────────────┘

ERROR HANDLING (any phase):
   │
   ├─> Network Error / Rate Limit / LLM Failure
   │
   ▼
┌──────────────────────┐
│ FAILED              │
│ Save error state    │
│ Notify via WS       │
└──────────┬───────────┘
           │
           ├─> POST /projects/{id}/retry
           │
           ▼
     Resume from failed phase
     (uses saved input_data)
```

### Phase Transitions Example

```python
# Example workflow_states records for one project:

# Record 1:
{
    "phase": "SMART_DETECTION",
    "status": "COMPLETED",
    "input_data": {"idea": "hair salon booking system..."},
    "output_data": {
        "use_event_storming": true,
        "reasoning": "Project has 5+ features, complex business rules..."
    }
}

# Record 2:
{
    "phase": "EVENT_STORMING",
    "status": "COMPLETED",
    "input_data": {"idea": "...", "prompts": ["..."]},
    "output_data": {"event_storming_md": "# Event Storming Summary..."}
}

# Record 3:
{
    "phase": "PRD",
    "status": "COMPLETED",
    "input_data": {"idea": "...", "event_storming_summary": "..."},
    "output_data": {"prd_md": "# Product Requirements Document..."}
}
```

---

## Implementation Plan (Phased)

### Phase 1: Core Infrastructure (Week 1)

**Goal:** Set up project foundation

**Tasks:**
- [ ] Initialize FastAPI project structure
- [ ] Set up PostgreSQL + Docker Compose
- [ ] Create SQLAlchemy models (all tables)
- [ ] Set up Alembic migrations
- [ ] Implement admin token auth middleware
- [ ] Add SlowAPI rate limiting
- [ ] Create health check endpoint
- [ ] Write tests for DB models

**Deliverable:**
- Running FastAPI app with DB
- Auth working
- Rate limiting working

### Phase 2: OpenRouter + LangFuse Integration (Week 1-2)

**Goal:** LLM service layer with observability

**Tasks:**
- [ ] Create LLMService class (OpenRouter client)
- [ ] Integrate LangFuse SDK
  - [ ] Trace creation per project
  - [ ] Span creation per phase
  - [ ] Cost tracking
- [ ] Implement prompt templates manager
  - [ ] Load prompts from ebook (INIT, TECH_STACK, etc.)
  - [ ] Dynamic variable substitution
- [ ] Create smart detection function (GPT-4o-mini)
- [ ] Write tests for LLM service
- [ ] Test cost tracking in LangFuse dashboard

**Deliverable:**
- LLMService can call OpenRouter
- All prompts templated
- LangFuse shows traces

### Phase 3: Workflow Engine (Week 2)

**Goal:** State machine implementation

**Tasks:**
- [ ] Create WorkflowEngine class
  - [ ] Phase orchestration
  - [ ] State persistence (workflow_states table)
  - [ ] Error handling & retry logic
- [ ] Implement each phase handler:
  - [ ] SmartDetectionPhase
  - [ ] EventStormingPhase
  - [ ] PRDGenerationPhase
  - [ ] TechStackPhase
  - [ ] ExecutionPlanPhase
- [ ] Document generation & storage
- [ ] Background task management (FastAPI BackgroundTasks)
- [ ] Write integration tests

**Deliverable:**
- Full workflow runs end-to-end
- Documents generated and saved

### Phase 4: REST API Endpoints (Week 2-3)

**Goal:** Complete REST API

**Tasks:**
- [ ] POST /api/v1/projects (create)
- [ ] POST /api/v1/projects/{id}/start-workflow
- [ ] GET /api/v1/projects/{id}
- [ ] GET /api/v1/projects/{id}/documents
- [ ] GET /api/v1/projects/{id}/documents/{type}
- [ ] POST /api/v1/projects/{id}/retry
- [ ] GET /api/v1/projects/{id}/costs
- [ ] OpenAPI/Swagger documentation
- [ ] Write API tests

**Deliverable:**
- Complete REST API
- Swagger docs

### Phase 5: WebSocket Implementation (Week 3)

**Goal:** Real-time progress updates

**Tasks:**
- [ ] WebSocket endpoint /api/v1/projects/{id}/progress
- [ ] Connection manager (track active connections)
- [ ] Integrate WS broadcasts into WorkflowEngine
  - [ ] phase_started
  - [ ] phase_progress
  - [ ] phase_completed
  - [ ] phase_failed
  - [ ] workflow_completed
- [ ] Handle disconnects/reconnects
- [ ] Write WS tests

**Deliverable:**
- WebSocket working
- Real-time progress updates

### Phase 6: Production Hardening (Week 3-4)

**Goal:** Production-ready

**Tasks:**
- [ ] Docker optimization (multi-stage build)
- [ ] Environment configuration (.env management)
- [ ] Logging (structured logs)
- [ ] Error monitoring (Sentry integration optional)
- [ ] Database connection pooling
- [ ] Graceful shutdown handling
- [ ] Load testing (100 concurrent users)
- [ ] Security audit (dependency scanning)
- [ ] Deployment documentation

**Deliverable:**
- Production-ready Docker image
- Deployment guide

---

## Cost Estimation

### Model Selection Strategy

```python
PHASE_MODELS = {
    "SMART_DETECTION": "openai/gpt-4o-mini",  # Fast, cheap analysis
    "EVENT_STORMING": "anthropic/claude-3.5-sonnet",  # Good at structured questioning
    "PRD": "anthropic/claude-3.5-sonnet",  # Complex document generation
    "TECH_STACK": "openai/gpt-4o",  # Technical decisions
    "EXECUTION_PLAN": "anthropic/claude-3.5-sonnet",  # Granular planning
}
```

### Cost Breakdown (Approximate)

| Phase | Model | Avg Tokens | Cost/Project | Duration |
|:------|:------|:-----------|:-------------|:---------|
| Smart Detection | GPT-4o-mini | 1,500 | $0.002 | 5-10s |
| Event Storming | Claude 3.5 Sonnet | 8,000 | $0.060 | 60-90s |
| PRD Generation | Claude 3.5 Sonnet | 12,000 | $0.090 | 45-60s |
| Tech Stack | GPT-4o | 6,000 | $0.090 | 30-45s |
| Execution Plan | Claude 3.5 Sonnet | 10,000 | $0.075 | 45-60s |
| **TOTAL (with Event Storming)** | | **~37,500** | **$0.317** | **~200-300s** |
| **TOTAL (without Event Storming)** | | **~29,500** | **$0.257** | **~140-210s** |

### Monthly Cost at Scale (100 users)

```
Assumptions:
- 100 users
- Average 2 projects/user/month = 200 projects/month
- 60% use Event Storming = 120 @ $0.317, 80 @ $0.257

Monthly LLM costs:
= (120 × $0.317) + (80 × $0.257)
= $38.04 + $20.56
= $58.60/month

Annual: ~$703
```

**Note:** OpenRouter prices vary by model. LangFuse tracking will show exact costs.

---

## LangFuse Integration

### Setup Pattern

```python
# app/services/langfuse_service.py
from langfuse import Langfuse

langfuse = Langfuse(
    public_key=settings.LANGFUSE_PUBLIC_KEY,
    secret_key=settings.LANGFUSE_SECRET_KEY,
    host=settings.LANGFUSE_HOST  # optional, defaults to cloud
)

class LangFuseTracker:
    def __init__(self, project_id: str, idea: str):
        self.trace = langfuse.trace(
            name=f"project_{project_id}",
            user_id=project_id,
            metadata={"idea": idea[:100]}
        )

    def track_phase(self, phase_name: str, model: str,
                    input_data: dict, output_data: dict,
                    tokens: dict, cost: float, duration_ms: int):

        generation = self.trace.generation(
            name=phase_name,
            model=model,
            input=input_data,
            output=output_data,
            usage={
                "input": tokens["prompt_tokens"],
                "output": tokens["completion_tokens"],
                "total": tokens["total_tokens"]
            },
            metadata={
                "cost_usd": cost,
                "duration_ms": duration_ms
            }
        )

        return generation.id  # langfuse_trace_id
```

### Usage in Workflow

```python
# app/workflow/engine.py
async def execute_prd_phase(project: Project):
    tracker = LangFuseTracker(project.id, project.idea)

    start_time = time.time()

    result = await llm_service.generate_prd(
        idea=project.idea,
        event_storming=event_storming_doc
    )

    duration_ms = int((time.time() - start_time) * 1000)

    # Track in LangFuse
    langfuse_trace_id = tracker.track_phase(
        phase_name="PRD_GENERATION",
        model="anthropic/claude-3.5-sonnet",
        input_data={"idea": project.idea},
        output_data={"prd_length": len(result.prd_md)},
        tokens=result.usage,
        cost=result.cost_usd,
        duration_ms=duration_ms
    )

    # Save to DB
    await save_llm_log(
        project_id=project.id,
        phase="PRD",
        langfuse_trace_id=langfuse_trace_id,
        **result.usage,
        cost_usd=result.cost_usd,
        duration_ms=duration_ms
    )
```

---

## Project Structure

```
api/
├── app/
│   ├── __init__.py
│   ├── main.py                    # FastAPI app entry
│   ├── config.py                  # Settings (pydantic-settings)
│   │
│   ├── api/
│   │   ├── __init__.py
│   │   ├── deps.py                # Dependencies (auth, db session)
│   │   ├── v1/
│   │   │   ├── __init__.py
│   │   │   ├── projects.py        # Project endpoints
│   │   │   └── websocket.py       # WebSocket endpoint
│   │
│   ├── core/
│   │   ├── __init__.py
│   │   ├── auth.py                # Admin token validation
│   │   ├── security.py            # Rate limiting
│   │   └── websocket_manager.py   # WS connection manager
│   │
│   ├── db/
│   │   ├── __init__.py
│   │   ├── base.py                # SQLAlchemy base
│   │   ├── session.py             # DB session management
│   │   └── models/
│   │       ├── __init__.py
│   │       ├── user.py
│   │       ├── project.py
│   │       ├── workflow_state.py
│   │       ├── document.py
│   │       └── llm_log.py
│   │
│   ├── schemas/
│   │   ├── __init__.py
│   │   ├── project.py             # Pydantic schemas
│   │   ├── document.py
│   │   └── workflow.py
│   │
│   ├── services/
│   │   ├── __init__.py
│   │   ├── llm_service.py         # OpenRouter client
│   │   ├── langfuse_service.py    # LangFuse tracking
│   │   └── prompt_manager.py      # Prompt templates
│   │
│   ├── workflow/
│   │   ├── __init__.py
│   │   ├── engine.py              # WorkflowEngine class
│   │   ├── state_machine.py       # State transitions
│   │   └── phases/
│   │       ├── __init__.py
│   │       ├── smart_detection.py
│   │       ├── event_storming.py
│   │       ├── prd_generation.py
│   │       ├── tech_stack.py
│   │       └── execution_plan.py
│   │
│   └── prompts/
│       ├── __init__.py
│       ├── smart_detection.txt
│       ├── event_storming.txt
│       ├── init_prompt.txt
│       ├── tech_stack_prompt.txt
│       └── stages_prompt.txt
│
├── alembic/
│   ├── versions/
│   └── env.py
│
├── tests/
│   ├── api/
│   ├── services/
│   ├── workflow/
│   └── conftest.py
│
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
├── pyproject.toml
├── .env.example
└── README.md
```

---

## Key Implementation Details

### 1. Smart Detection (LLM Analysis)

```python
# app/workflow/phases/smart_detection.py

SMART_DETECTION_PROMPT = """
Analyze this project idea and determine if Event Storming (business process discovery) is needed.

Project Idea: {idea}

Respond with JSON only:
{{
    "use_event_storming": true/false,
    "feature_count_estimate": number,
    "has_complex_business_logic": true/false,
    "reasoning": "brief explanation"
}}

Use Event Storming if:
- 4+ features
- Complex business rules/workflows
- Multiple user types with different permissions
- Business process automation

Skip Event Storming if:
- Simple CRUD app
- 1-3 features
- Straightforward user flow
"""

async def smart_detection(idea: str) -> dict:
    response = await llm_service.call(
        model="openai/gpt-4o-mini",
        prompt=SMART_DETECTION_PROMPT.format(idea=idea),
        temperature=0.3,
        response_format={"type": "json_object"}
    )
    return json.loads(response.content)
```

### 2. Horizontal vs Vertical Detection

```python
# In EXECUTION_PLAN phase, after PRD is generated

APPROACH_DETECTION_PROMPT = """
Based on this PRD, determine the best development approach.

PRD:
{prd_content}

Respond with JSON only:
{{
    "approach": "HORIZONTAL" or "VERTICAL",
    "reasoning": "brief explanation"
}}

Use VERTICAL if:
- 4+ features in scope
- Complex integration needs
- Need continuous testing/demos

Use HORIZONTAL if:
- 1-3 simple features
- Straightforward architecture
"""
```

### 3. WebSocket Progress Broadcasting

```python
# app/core/websocket_manager.py

class ConnectionManager:
    def __init__(self):
        self.active_connections: Dict[str, List[WebSocket]] = {}

    async def connect(self, project_id: str, websocket: WebSocket):
        await websocket.accept()
        if project_id not in self.active_connections:
            self.active_connections[project_id] = []
        self.active_connections[project_id].append(websocket)

    async def broadcast(self, project_id: str, message: dict):
        if project_id in self.active_connections:
            for connection in self.active_connections[project_id]:
                try:
                    await connection.send_json(message)
                except:
                    self.active_connections[project_id].remove(connection)

manager = ConnectionManager()

# In workflow engine:
await manager.broadcast(project_id, {
    "type": "phase_started",
    "phase": "PRD",
    "timestamp": datetime.utcnow().isoformat()
})
```

### 4. Error Handling and Retry Logic

```python
# app/workflow/engine.py

async def execute_phase_with_retry(phase_func, max_retries=3):
    for attempt in range(max_retries):
        try:
            result = await phase_func()
            return result
        except OpenRouterRateLimitError as e:
            if attempt < max_retries - 1:
                wait_time = 2 ** attempt  # Exponential backoff
                await asyncio.sleep(wait_time)
                continue
            raise
        except Exception as e:
            # Log error, save to workflow_states
            await save_error_state(phase, str(e))
            raise
```

---

## Next Steps

1. **Start with Phase 1:** Core infrastructure setup
2. **Build incrementally:** Don't skip phases
3. **Test continuously:** Write tests as you build
4. **Monitor costs:** Use LangFuse from the start
5. **Document:** Keep README updated

**Ready to begin implementation!** 🚀
