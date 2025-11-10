# Technical Documentation: AI-Driven Development Framework API

**Version**: 1.0.0
**Last Updated**: 2025-11-09
**Architecture**: Async Python FastAPI + PostgreSQL + WebSockets

---

## Table of Contents

1. [System Architecture](#system-architecture)
2. [Database Schema](#database-schema)
3. [API Reference](#api-reference)
4. [WebSocket Events](#websocket-events)
5. [Workflow Engine](#workflow-engine)
6. [Core Services](#core-services)
7. [Configuration](#configuration)
8. [Deployment](#deployment)
9. [Development Guide](#development-guide)

---

## System Architecture

### High-Level Overview

```
┌─────────────────┐
│   Frontend      │
│   (React/Vue)   │
└────────┬────────┘
         │ HTTP REST + WebSocket
         ▼
┌─────────────────────────────────────────┐
│         FastAPI Application             │
│  ┌──────────────────────────────────┐   │
│  │   API Endpoints (v1)             │   │
│  │  - Projects CRUD                 │   │
│  │  - Documents                     │   │
│  │  - Costs                         │   │
│  └──────────────────────────────────┘   │
│  ┌──────────────────────────────────┐   │
│  │   WebSocket Manager              │   │
│  │  - Connection pool               │   │
│  │  - Broadcast messages            │   │
│  └──────────────────────────────────┘   │
│  ┌──────────────────────────────────┐   │
│  │   Workflow Engine                │   │
│  │  - Phase orchestration           │   │
│  │  - State machine                 │   │
│  │  - Phase handlers                │   │
│  └──────────────────────────────────┘   │
│  ┌──────────────────────────────────┐   │
│  │   LLM Service Layer              │   │
│  │  - OpenRouter client             │   │
│  │  - Prompt manager                │   │
│  │  - Cost calculator               │   │
│  └──────────────────────────────────┘   │
└─────────┬───────────────────────────────┘
          │
          ▼
┌─────────────────────┐      ┌──────────────────┐
│   PostgreSQL        │      │   OpenRouter API │
│   - Projects        │      │   (LLM Gateway)  │
│   - Workflows       │      └──────────────────┘
│   - Documents       │      ┌──────────────────┐
│   - LLM Logs        │      │   LangFuse       │
└─────────────────────┘      │   (Observability)│
                             └──────────────────┘
```

### Technology Stack

| Layer | Technology | Version | Purpose |
|-------|------------|---------|---------|
| **Framework** | FastAPI | 0.109.0 | Async web framework |
| **Runtime** | Python | 3.11+ | Application runtime |
| **Database** | PostgreSQL | 14+ | Persistent storage |
| **ORM** | SQLAlchemy | 2.0.25 | Database abstraction |
| **Validation** | Pydantic | 2.5.3 | Data validation |
| **Migrations** | Alembic | 1.13.1 | Database versioning |
| **Rate Limiting** | SlowAPI | 0.1.9 | Request throttling |
| **HTTP Client** | httpx | 0.26.0 | Async HTTP calls |
| **LLM Gateway** | OpenRouter | API | Multi-model access |
| **Observability** | LangFuse | 2.20.0 | LLM tracking |

---

## Database Schema

### Entity Relationship Diagram

```
┌─────────────┐
│    users    │
└──────┬──────┘
       │
       │ 1:N
       ▼
┌──────────────────┐
│    projects      │◄────────┐
└──────┬───────────┘         │
       │                     │
       │ 1:N                 │ 1:N
       ├─────────────────────┼──────────────────┐
       ▼                     ▼                  ▼
┌──────────────┐    ┌────────────────┐  ┌──────────────┐
│workflow_states│    │   documents    │  │   llm_logs   │
└──────────────┘    └────────────────┘  └──────────────┘
```

### Table Definitions

#### `users`
**File**: `api/app/db/models/user.py`

| Column | Type | Constraints | Description |
|--------|------|-------------|-------------|
| `id` | UUID | PK | User identifier |
| `email` | VARCHAR(255) | UNIQUE, NOT NULL | User email |
| `created_at` | TIMESTAMP | NOT NULL | Registration timestamp |

**Relationships**:
- `projects`: One-to-many with `projects` table

**Class**: `User(Base)`

---

#### `projects`
**File**: `api/app/db/models/project.py`

| Column | Type | Constraints | Description |
|--------|------|-------------|-------------|
| `id` | UUID | PK | Project identifier |
| `user_id` | UUID | FK(users.id), NOT NULL | Owner user ID |
| `idea` | TEXT | NOT NULL | Project idea (10-5000 chars) |
| `status` | VARCHAR(50) | NOT NULL | Workflow status enum |
| `current_phase` | VARCHAR(50) | NULL | Current workflow phase |
| `metadata` | JSONB | NOT NULL, DEFAULT {} | Phase results, costs, etc. |
| `created_at` | TIMESTAMP | NOT NULL | Creation timestamp |
| `updated_at` | TIMESTAMP | NOT NULL | Last update timestamp |
| `completed_at` | TIMESTAMP | NULL | Completion timestamp |

**Indexes**:
- `ix_projects_user_id` on `user_id`
- `ix_projects_status` on `status`

**Relationships**:
- `user`: Many-to-one with `users`
- `workflow_states`: One-to-many with `workflow_states`
- `documents`: One-to-many with `documents`
- `llm_logs`: One-to-many with `llm_logs`

**Class**: `Project(Base)`

**Enums**:
- **WorkflowStatus**: `CREATED`, `PROCESSING`, `COMPLETED`, `FAILED`
- **WorkflowPhase**: `SMART_DETECTION`, `EVENT_STORMING`, `PRD`, `TECH_STACK`, `EXECUTION_PLAN`

---

#### `workflow_states`
**File**: `api/app/db/models/workflow_state.py`

| Column | Type | Constraints | Description |
|--------|------|-------------|-------------|
| `id` | UUID | PK | State record ID |
| `project_id` | UUID | FK(projects.id), NOT NULL | Associated project |
| `phase` | VARCHAR(50) | NOT NULL | Workflow phase name |
| `status` | VARCHAR(50) | NOT NULL | Phase status |
| `input_data` | JSONB | NOT NULL | Phase input parameters |
| `output_data` | JSONB | NOT NULL | Phase results |
| `started_at` | TIMESTAMP | NOT NULL | Phase start time |
| `completed_at` | TIMESTAMP | NULL | Phase completion time |

**Indexes**:
- `ix_workflow_states_project_id` on `project_id`
- `ix_workflow_states_phase` on `phase`

**Relationships**:
- `project`: Many-to-one with `projects`
- `llm_logs`: One-to-many with `llm_logs`

**Class**: `WorkflowState(Base)`

---

#### `documents`
**File**: `api/app/db/models/document.py`

| Column | Type | Constraints | Description |
|--------|------|-------------|-------------|
| `id` | UUID | PK | Document ID |
| `project_id` | UUID | FK(projects.id), NOT NULL | Associated project |
| `document_type` | VARCHAR(50) | NOT NULL | Document type enum |
| `content_md` | TEXT | NOT NULL | Markdown content |
| `metadata` | JSONB | NOT NULL | Model used, tokens, etc. |
| `created_at` | TIMESTAMP | NOT NULL | Generation timestamp |

**Indexes**:
- `ix_documents_project_id` on `project_id`
- Unique constraint on `(project_id, document_type)`

**Relationships**:
- `project`: Many-to-one with `projects`

**Class**: `Document(Base)`

**Enums**:
- **DocumentType**: `EVENT_STORMING`, `PRD`, `TECH_STACK`, `EXECUTION_PLAN`

---

#### `llm_logs`
**File**: `api/app/db/models/llm_log.py`

| Column | Type | Constraints | Description |
|--------|------|-------------|-------------|
| `id` | UUID | PK | Log entry ID |
| `project_id` | UUID | FK(projects.id), NOT NULL | Associated project |
| `workflow_state_id` | UUID | FK(workflow_states.id), NULL | Associated state |
| `phase` | VARCHAR(50) | NOT NULL | Workflow phase |
| `model` | VARCHAR(100) | NOT NULL | LLM model identifier |
| `prompt_tokens` | INTEGER | NOT NULL | Input token count |
| `completion_tokens` | INTEGER | NOT NULL | Output token count |
| `total_tokens` | INTEGER | NOT NULL | Total tokens used |
| `cost_usd` | DECIMAL(10,6) | NOT NULL | API cost in USD |
| `latency_ms` | INTEGER | NOT NULL | Request duration |
| `langfuse_trace_id` | VARCHAR(255) | NULL | LangFuse trace ID |
| `created_at` | TIMESTAMP | NOT NULL | Log timestamp |

**Indexes**:
- `ix_llm_logs_project_id` on `project_id`
- `ix_llm_logs_langfuse_trace_id` on `langfuse_trace_id`

**Relationships**:
- `project`: Many-to-one with `projects`
- `workflow_state`: Many-to-one with `workflow_states`

**Class**: `LLMLog(Base)`

---

## API Reference

### Base URL
```
http://localhost:8000/api/v1
```

### Authentication
All endpoints (except health check) require Bearer token authentication:

```http
Authorization: Bearer <ADMIN_TOKEN>
```

**Header**: `Authorization`
**Scheme**: `Bearer`
**Token**: Value from `ADMIN_TOKEN` environment variable

**Implementation**: `api/app/core/auth.py:verify_admin_token()`

---

### Endpoints

#### 1. Create Project

**POST** `/projects`

**Purpose**: Create a new project from an idea.

**Authentication**: ✅ Required
**Rate Limit**: 10 requests/minute
**Handler**: `api/app/api/v1/projects.py:create_project()`

**Request Body**:
```json
{
  "idea": "Build a task management app with AI-powered prioritization",
  "user_id": "550e8400-e29b-41d4-a716-446655440000"
}
```

**Request Schema**: `ProjectCreate` (`api/app/schemas/project.py:10`)
- `idea`: string (10-5000 chars, required)
- `user_id`: UUID (required)

**Response** (201 Created):
```json
{
  "project_id": "123e4567-e89b-12d3-a456-426614174000",
  "status": "CREATED",
  "created_at": "2025-11-09T12:00:00Z"
}
```

**Response Schema**: `ProjectCreateResponse` (`api/app/schemas/project.py:49`)

**Errors**:
- `400 Bad Request`: Invalid input (idea too short/long)
- `401 Unauthorized`: Missing or invalid token
- `429 Too Many Requests`: Rate limit exceeded

---

#### 2. Start Workflow

**POST** `/projects/{project_id}/start-workflow`

**Purpose**: Start autonomous workflow execution in background.

**Authentication**: ✅ Required
**Rate Limit**: 5 requests/minute
**Handler**: `api/app/api/v1/projects.py:start_workflow()`

**Path Parameters**:
- `project_id`: UUID

**Response** (200 OK):
```json
{
  "project_id": "123e4567-e89b-12d3-a456-426614174000",
  "status": "PROCESSING",
  "current_phase": "SMART_DETECTION",
  "websocket_url": "ws://localhost:8000/api/v1/projects/123e4567-e89b-12d3-a456-426614174000/progress"
}
```

**Response Schema**: `ProjectStartWorkflowResponse` (`api/app/schemas/project.py:57`)

**Background Task**: `execute_workflow_background()` (`api/app/api/v1/projects.py:40`)

**Errors**:
- `400 Bad Request`: Workflow already running or completed
- `404 Not Found`: Project not found
- `401 Unauthorized`: Missing or invalid token

**Workflow Execution**:
- Uses FastAPI `BackgroundTasks` for non-blocking execution
- Updates project status to `PROCESSING`
- Broadcasts real-time updates via WebSocket
- Expected duration: 3-6 minutes for full workflow

---

#### 3. Get Project Status

**GET** `/projects/{project_id}`

**Purpose**: Retrieve current project status and metadata.

**Authentication**: ✅ Required
**Rate Limit**: 30 requests/minute
**Handler**: `api/app/api/v1/projects.py:get_project()`

**Path Parameters**:
- `project_id`: UUID

**Response** (200 OK):
```json
{
  "project_id": "123e4567-e89b-12d3-a456-426614174000",
  "idea": "Build a task management app...",
  "status": "COMPLETED",
  "current_phase": "EXECUTION_PLAN",
  "metadata": {
    "use_event_storming": true,
    "use_vertical_approach": false,
    "total_cost_usd": 0.45,
    "total_duration_seconds": 180,
    "smart_detection": {
      "use_event_storming": true,
      "feature_count_estimate": 8,
      "reasoning": "Complex domain with multiple features"
    }
  },
  "created_at": "2025-11-09T12:00:00Z",
  "updated_at": "2025-11-09T12:03:00Z",
  "completed_at": "2025-11-09T12:03:00Z"
}
```

**Response Schema**: `ProjectResponse` (`api/app/schemas/project.py:33`)

**Metadata Fields**:
- `use_event_storming`: Boolean - Whether Event Storming was run
- `use_vertical_approach`: Boolean - Development approach (vertical vs horizontal)
- `total_cost_usd`: Float - Total LLM API costs
- `total_duration_seconds`: Integer - Workflow duration
- `smart_detection`: Object - Smart Detection phase results

**Errors**:
- `404 Not Found`: Project not found
- `401 Unauthorized`: Missing or invalid token

---

#### 4. Get All Documents

**GET** `/projects/{project_id}/documents`

**Purpose**: Retrieve all generated documents for a project.

**Authentication**: ✅ Required
**Rate Limit**: 30 requests/minute
**Handler**: `api/app/api/v1/projects.py:get_project_documents()`

**Path Parameters**:
- `project_id`: UUID

**Response** (200 OK):
```json
{
  "project_id": "123e4567-e89b-12d3-a456-426614174000",
  "documents": [
    {
      "type": "EVENT_STORMING",
      "content_md": "# Event Storming Summary\n\n...",
      "metadata": {
        "model": "openai/gpt-4o"
      },
      "created_at": "2025-11-09T12:01:00Z"
    },
    {
      "type": "PRD",
      "content_md": "# Product Requirements Document\n\n...",
      "metadata": {
        "model": "openai/gpt-4o"
      },
      "created_at": "2025-11-09T12:02:00Z"
    },
    {
      "type": "TECH_STACK",
      "content_md": "# Tech Stack Document\n\n...",
      "metadata": {
        "model": "openai/gpt-4o"
      },
      "created_at": "2025-11-09T12:02:30Z"
    },
    {
      "type": "EXECUTION_PLAN",
      "content_md": "# Execution Plan\n\n...",
      "metadata": {
        "model": "openai/gpt-4o",
        "approach": "HORIZONTAL"
      },
      "created_at": "2025-11-09T12:03:00Z"
    }
  ]
}
```

**Response Schema**: `DocumentsResponse` (`api/app/schemas/document.py:22`)

**Document Types**:
- `EVENT_STORMING`: Business domain discovery (conditional)
- `PRD`: Product Requirements Document (always)
- `TECH_STACK`: Technology stack recommendations (always)
- `EXECUTION_PLAN`: Stage-gate execution plan (always)

**Errors**:
- `404 Not Found`: Project not found
- `401 Unauthorized`: Missing or invalid token

---

#### 5. Get Single Document

**GET** `/projects/{project_id}/documents/{document_type}`

**Purpose**: Retrieve a specific document by type.

**Authentication**: ✅ Required
**Rate Limit**: 30 requests/minute
**Handler**: `api/app/api/v1/projects.py:get_project_document()`

**Path Parameters**:
- `project_id`: UUID
- `document_type`: Enum (`EVENT_STORMING`, `PRD`, `TECH_STACK`, `EXECUTION_PLAN`)

**Response** (200 OK):
```json
{
  "type": "PRD",
  "content_md": "# Product Requirements Document\n\n## Project Overview\n...",
  "metadata": {
    "model": "openai/gpt-4o",
    "tokens": 3500
  },
  "created_at": "2025-11-09T12:02:00Z"
}
```

**Response Schema**: `DocumentResponse` (`api/app/schemas/document.py:9`)

**Errors**:
- `404 Not Found`: Project or document not found
- `400 Bad Request`: Invalid document type
- `401 Unauthorized`: Missing or invalid token

---

#### 6. Get Cost Breakdown

**GET** `/projects/{project_id}/costs`

**Purpose**: Retrieve detailed cost breakdown for all LLM API calls.

**Authentication**: ✅ Required
**Rate Limit**: 30 requests/minute
**Handler**: `api/app/api/v1/projects.py:get_project_costs()`

**Path Parameters**:
- `project_id`: UUID

**Response** (200 OK):
```json
{
  "project_id": "123e4567-e89b-12d3-a456-426614174000",
  "total_cost_usd": 0.4523,
  "breakdown": [
    {
      "phase": "SMART_DETECTION",
      "model": "openai/gpt-4o-mini",
      "tokens": 500,
      "cost_usd": 0.0015
    },
    {
      "phase": "EVENT_STORMING",
      "model": "openai/gpt-4o",
      "tokens": 3500,
      "cost_usd": 0.0875
    },
    {
      "phase": "PRD",
      "model": "openai/gpt-4o",
      "tokens": 4000,
      "cost_usd": 0.1000
    },
    {
      "phase": "TECH_STACK",
      "model": "openai/gpt-4o",
      "tokens": 3000,
      "cost_usd": 0.0750
    },
    {
      "phase": "EXECUTION_PLAN",
      "model": "openai/gpt-4o",
      "tokens": 7000,
      "cost_usd": 0.1883
    }
  ]
}
```

**Response Schema**: `ProjectCostResponse` (`api/app/schemas/project.py:75`)

**Cost Calculation**: `api/app/services/llm_service.py:131-142`

**Pricing** (per 1M tokens):
- `gpt-4o-mini`: $0.15 input / $0.60 output
- `gpt-4o`: $2.50 input / $10.00 output
- `claude-3.5-sonnet`: $3.00 input / $15.00 output

**Errors**:
- `404 Not Found`: Project not found
- `401 Unauthorized`: Missing or invalid token

---

### Health Check

#### GET `/health`

**Purpose**: Check API health status.

**Authentication**: ❌ Not Required
**Rate Limit**: None
**Handler**: `api/app/main.py:62`

**Response** (200 OK):
```json
{
  "status": "healthy",
  "service": "AI-Driven Development Framework API",
  "version": "1.0.0"
}
```

---

## WebSocket Events

### Connection

**Endpoint**: `ws://localhost:8000/api/v1/projects/{project_id}/progress`

**Authentication**: ⚠️ **NOT IMPLEMENTED** (See Security Review)

**Handler**: `api/app/api/v1/websocket.py:project_progress()`

**Connection Manager**: `api/app/core/websocket_manager.py:ConnectionManager`

**Connection Flow**:
```
Client                      Server
  │                           │
  ├─── WebSocket Handshake ──>│
  │                           │
  │<──── Accept Connection ───┤
  │                           │
  │<──── "connected" event ───┤
  │                           │
  │                           │ (workflow executing in background)
  │<── "phase_started" ───────┤
  │<── "phase_completed" ─────┤
  │<── "phase_started" ───────┤
  │     ...                   │
  │<── "workflow_completed" ──┤
  │                           │
  ├────── ping ──────────────>│
  │<────── pong ───────────────┤
  │                           │
```

---

### Event Types

#### 1. Connected

**Sent**: Immediately after WebSocket connection accepted

**Purpose**: Confirm connection and provide initial state

```json
{
  "type": "connected",
  "project_id": "123e4567-e89b-12d3-a456-426614174000",
  "current_status": "PROCESSING",
  "current_phase": "SMART_DETECTION",
  "message": "Connected to project progress updates",
  "timestamp": "2025-11-09T12:00:00.000Z"
}
```

**Fields**:
- `type`: Always `"connected"`
- `project_id`: UUID string
- `current_status`: Current workflow status
- `current_phase`: Current phase (or null if not started)
- `message`: Human-readable message
- `timestamp`: ISO 8601 timestamp

---

#### 2. Phase Started

**Sent**: When a workflow phase begins execution

**Broadcast Function**: `api/app/workflow/engine.py:_broadcast_phase_started()`

```json
{
  "type": "phase_started",
  "phase": "PRD",
  "message": "Generating Product Requirements Document (PRD)...",
  "timestamp": "2025-11-09T12:01:30.000Z"
}
```

**Fields**:
- `type`: Always `"phase_started"`
- `phase`: Phase enum value (`SMART_DETECTION`, `EVENT_STORMING`, `PRD`, `TECH_STACK`, `EXECUTION_PLAN`)
- `message`: Descriptive message of what's happening
- `timestamp`: ISO 8601 timestamp

**Phase Messages**:
- `SMART_DETECTION`: "Analyzing project complexity and determining workflow approach..."
- `EVENT_STORMING`: "Running Event Storming to discover business domain and events..."
- `PRD`: "Generating Product Requirements Document (PRD)..."
- `TECH_STACK`: "Determining optimal tech stack and architecture..."
- `EXECUTION_PLAN`: "Creating detailed execution plan with stage gates..."

---

#### 3. Phase Completed

**Sent**: When a workflow phase successfully completes

**Broadcast Function**: `api/app/workflow/engine.py:_broadcast_phase_completed()`

```json
{
  "type": "phase_completed",
  "phase": "PRD",
  "duration_seconds": 45,
  "cost_usd": 0.12,
  "timestamp": "2025-11-09T12:02:15.000Z"
}
```

**Fields**:
- `type`: Always `"phase_completed"`
- `phase`: Phase enum value
- `duration_seconds`: Integer - Phase execution time
- `cost_usd`: Float (6 decimal places) - LLM API cost for this phase
- `timestamp`: ISO 8601 timestamp

**Typical Durations**:
- `SMART_DETECTION`: 2-5 seconds
- `EVENT_STORMING`: 30-60 seconds
- `PRD`: 40-80 seconds
- `TECH_STACK`: 30-50 seconds
- `EXECUTION_PLAN`: 60-90 seconds

---

#### 4. Phase Failed

**Sent**: When a workflow phase encounters an error

**Broadcast Function**: `api/app/workflow/engine.py:_broadcast_phase_failed()`

```json
{
  "type": "phase_failed",
  "phase": "TECH_STACK",
  "error": "OpenRouter API rate limit exceeded",
  "retry_available": true,
  "timestamp": "2025-11-09T12:02:30.000Z"
}
```

**Fields**:
- `type`: Always `"phase_failed"`
- `phase`: Phase enum value
- `error`: Error message string
- `retry_available`: Boolean - Whether retry is possible
- `timestamp`: ISO 8601 timestamp

**Common Errors**:
- "OpenRouter API rate limit exceeded"
- "LLM response parsing failed"
- "Smart detection failed"
- "PRD generation failed"

---

#### 5. Workflow Completed

**Sent**: When entire workflow completes successfully

**Broadcast Function**: `api/app/workflow/engine.py:_broadcast_workflow_completed()`

```json
{
  "type": "workflow_completed",
  "total_duration_seconds": 180,
  "total_cost_usd": 0.4523,
  "documents_generated": 4,
  "timestamp": "2025-11-09T12:03:00.000Z"
}
```

**Fields**:
- `type`: Always `"workflow_completed"`
- `total_duration_seconds`: Integer - Total workflow time
- `total_cost_usd`: Float (6 decimal places) - Total LLM costs
- `documents_generated`: Integer - Number of documents (3 or 4)
- `timestamp`: ISO 8601 timestamp

**Documents Generated**:
- 3 documents: PRD, TECH_STACK, EXECUTION_PLAN (no Event Storming)
- 4 documents: EVENT_STORMING, PRD, TECH_STACK, EXECUTION_PLAN

---

#### 6. Workflow Failed

**Sent**: When workflow fails catastrophically (not phase-specific)

**Broadcast Function**: `api/app/workflow/engine.py:_handle_workflow_failure()`

```json
{
  "type": "workflow_failed",
  "error": "Database connection lost",
  "timestamp": "2025-11-09T12:02:00.000Z"
}
```

**Fields**:
- `type`: Always `"workflow_failed"`
- `error`: Error message string
- `timestamp`: ISO 8601 timestamp

---

#### 7. Pong

**Sent**: In response to client ping (keep-alive)

**Handler**: `api/app/api/v1/websocket.py:60-61`

**Client Sends**:
```json
"ping"
```

**Server Responds**:
```json
{
  "type": "pong",
  "timestamp": "2025-11-09T12:02:00.000Z"
}
```

**Purpose**: Keep connection alive, verify server responsiveness

---

### WebSocket Client Example (JavaScript)

```javascript
// Connect to WebSocket
const projectId = "123e4567-e89b-12d3-a456-426614174000";
const ws = new WebSocket(`ws://localhost:8000/api/v1/projects/${projectId}/progress`);

// Connection opened
ws.onopen = (event) => {
  console.log("WebSocket connected");
};

// Receive messages
ws.onmessage = (event) => {
  const message = JSON.parse(event.data);

  switch (message.type) {
    case "connected":
      console.log("Connected to project:", message.project_id);
      console.log("Current status:", message.current_status);
      break;

    case "phase_started":
      console.log(`Phase ${message.phase} started: ${message.message}`);
      updateUI({ phase: message.phase, status: "in-progress" });
      break;

    case "phase_completed":
      console.log(`Phase ${message.phase} completed in ${message.duration_seconds}s`);
      console.log(`Cost: $${message.cost_usd}`);
      updateUI({ phase: message.phase, status: "completed", cost: message.cost_usd });
      break;

    case "phase_failed":
      console.error(`Phase ${message.phase} failed: ${message.error}`);
      showError(message.error, message.retry_available);
      break;

    case "workflow_completed":
      console.log("Workflow completed!");
      console.log(`Total time: ${message.total_duration_seconds}s`);
      console.log(`Total cost: $${message.total_cost_usd}`);
      console.log(`Documents generated: ${message.documents_generated}`);
      showSuccess(message);
      ws.close();
      break;

    case "workflow_failed":
      console.error("Workflow failed:", message.error);
      showError(message.error, false);
      ws.close();
      break;

    case "pong":
      console.log("Pong received");
      break;
  }
};

// Handle errors
ws.onerror = (error) => {
  console.error("WebSocket error:", error);
};

// Handle close
ws.onclose = (event) => {
  console.log("WebSocket closed:", event.code, event.reason);
};

// Send ping every 30 seconds to keep connection alive
setInterval(() => {
  if (ws.readyState === WebSocket.OPEN) {
    ws.send("ping");
  }
}, 30000);
```

---

## Workflow Engine

### Overview

The Workflow Engine orchestrates autonomous execution of 5 phases to generate planning documents from a project idea.

**Main Class**: `WorkflowEngine` (`api/app/workflow/engine.py:30`)

**Entry Point**: `execute_workflow()` (`api/app/workflow/engine.py:168`)

---

### State Machine

**File**: `api/app/workflow/state_machine.py`

**Class**: `WorkflowStateMachine`

**Phase Flow**:

```
┌────────────────────┐
│  SMART_DETECTION   │ (Always runs, decides Event Storming)
└─────────┬──────────┘
          │
          ▼
    ┌─────────────┐
    │ use_event_  │
    │ storming?   │
    └──┬──────┬───┘
       │      │
   Yes │      │ No
       │      │
       ▼      │
┌──────────────┐   │
│EVENT_STORMING│   │
└──────┬───────┘   │
       │           │
       └───────┬───┘
               ▼
        ┌──────────┐
        │   PRD    │ (Always runs)
        └─────┬────┘
              ▼
        ┌──────────┐
        │TECH_STACK│ (Always runs)
        └─────┬────┘
              ▼
        ┌─────────────┐
        │EXECUTION_PLAN│ (Always runs)
        └─────────────┘
```

**Phase Transitions**:

| Current Phase | Next Phase (no ES) | Next Phase (with ES) |
|--------------|-------------------|---------------------|
| - | SMART_DETECTION | SMART_DETECTION |
| SMART_DETECTION | PRD | EVENT_STORMING |
| EVENT_STORMING | - | PRD |
| PRD | TECH_STACK | TECH_STACK |
| TECH_STACK | EXECUTION_PLAN | EXECUTION_PLAN |
| EXECUTION_PLAN | (complete) | (complete) |

**Function**: `get_next_phase()` (`api/app/workflow/state_machine.py`)

---

### Phase Handlers

All phase handlers inherit from `BasePhaseHandler` (`api/app/workflow/phases/base.py:15`)

**Base Methods**:
- `execute(input_data)` - Abstract method, implemented by each phase
- `run_with_state_tracking(input_data)` - Wraps execute() with state management
- `create_workflow_state()` - Creates DB record for phase execution
- `update_workflow_state()` - Updates DB record with results
- `save_llm_log()` - Logs LLM API call to database

---

#### Phase 1: Smart Detection

**File**: `api/app/workflow/phases/smart_detection.py`

**Class**: `SmartDetectionPhase(BasePhaseHandler)`

**Purpose**: Analyze project complexity and decide if Event Storming is needed

**LLM Model**: `openai/gpt-4o-mini` (cheap, fast)

**Prompt**: `api/app/prompts/smart_detection.txt`

**Input**:
```python
{"idea": "Build a task management app..."}
```

**Output**:
```python
{
  "use_event_storming": true,
  "feature_count_estimate": 8,
  "reasoning": "Complex domain with user management, tasks, projects, notifications, analytics"
}
```

**Response Format**: JSON object (enforced via `response_format={"type": "json_object"}`)

**Decision Logic**:
- 1-3 features: `use_event_storming = false`
- 4+ features: `use_event_storming = true`
- Complex domains (auth, payments, integrations): `use_event_storming = true`

**Expected Duration**: 2-5 seconds
**Expected Cost**: $0.001-$0.003

---

#### Phase 2: Event Storming (Conditional)

**File**: `api/app/workflow/phases/event_storming.py`

**Class**: `EventStormingPhase(BasePhaseHandler)`

**Purpose**: Discover business domain through autonomous 5-phase questioning

**LLM Model**: `openai/gpt-4o` (better reasoning for domain modeling)

**Prompt**: `api/app/prompts/event_storming.txt`

**Input**:
```python
{"idea": "Build a task management app..."}
```

**Output**:
```python
{
  "event_storming_md": "# Event Storming Summary\n\n## Domain Events\n...",
  "key_events": ["TaskCreated", "TaskAssigned", "TaskCompleted"],
  "aggregates": ["Task", "Project", "User"]
}
```

**5 Phases** (autonomous, LLM self-generates Q&A):
1. **Initial Exploration**: What is the core value?
2. **Event Discovery**: What events occur in the system?
3. **Command Identification**: What triggers these events?
4. **Aggregate Definition**: What are the core domain objects?
5. **Process Flow**: How do events flow through the system?

**Document Structure**:
```markdown
# Event Storming Summary

## Domain Events
- TaskCreated: When a new task is created
- TaskAssigned: When a task is assigned to a user
...

## Commands
- CreateTask: User creates a new task
- AssignTask: Manager assigns task to team member
...

## Aggregates
- Task: Core entity for work items
- Project: Collection of related tasks
...

## Process Flows
1. Task Creation Flow: CreateTask → TaskCreated → SendNotification
...
```

**Expected Duration**: 30-60 seconds
**Expected Cost**: $0.05-$0.15

---

#### Phase 3: PRD Generation

**File**: `api/app/workflow/phases/prd_generation.py`

**Class**: `PRDGenerationPhase(BasePhaseHandler)`

**Purpose**: Generate comprehensive Product Requirements Document

**LLM Model**: `openai/gpt-4o`

**Prompt**: `api/app/prompts/init_prompt.txt`

**Input**:
```python
{
  "idea": "Build a task management app...",
  "event_storming_summary": "# Event Storming Summary\n..." (optional)
}
```

**Output**:
```python
{
  "prd_md": "# Product Requirements Document\n\n...",
  "feature_count": 12,
  "complexity": "MEDIUM"
}
```

**PRD Structure** (15-question autonomous generation):
```markdown
# Product Requirements Document

## 1. Project Overview
- Product name, vision, target users

## 2. Core Features
- Feature 1: Description, acceptance criteria
- Feature 2: Description, acceptance criteria
...

## 3. User Stories
- As a user, I want to...

## 4. Non-Functional Requirements
- Performance, security, scalability

## 5. Success Metrics
- KPIs, analytics requirements

## 6. Technical Constraints
- Browser support, device compatibility

## 7. Out of Scope
- Explicitly excluded features
```

**Expected Duration**: 40-80 seconds
**Expected Cost**: $0.08-$0.20

---

#### Phase 4: Tech Stack

**File**: `api/app/workflow/phases/tech_stack.py`

**Class**: `TechStackPhase(BasePhaseHandler)`

**Purpose**: Recommend optimal technology stack with justifications

**LLM Model**: `openai/gpt-4o`

**Prompt**: `api/app/prompts/tech_stack_prompt.txt`

**Input**:
```python
{"prd_md": "# Product Requirements Document\n..."}
```

**Output**:
```python
{
  "tech_stack_md": "# Tech Stack Document\n\n...",
  "frontend": "React + TypeScript",
  "backend": "Node.js + Express",
  "database": "PostgreSQL"
}
```

**Tech Stack Structure**:
```markdown
# Tech Stack Document

## Frontend
**Choice**: React 18 + TypeScript + Tailwind CSS

**Justification**:
- React: Industry standard, large ecosystem, component reusability
- TypeScript: Type safety reduces bugs, better IDE support
- Tailwind: Rapid UI development, consistent design system

## Backend
**Choice**: Node.js + Express + TypeScript

**Justification**:
- Node.js: Full-stack JavaScript, excellent async I/O performance
- Express: Minimal, flexible, large middleware ecosystem
- TypeScript: Shared types with frontend

## Database
**Choice**: PostgreSQL 14

**Justification**:
- ACID compliance for data integrity
- JSON support for flexible schemas
- Excellent performance and scalability

## Infrastructure
**Choice**: Docker + AWS

**Justification**:
- Docker: Consistent environments, easy deployment
- AWS: Scalability, managed services (RDS, S3, ECS)

## Third-Party Services
- Authentication: Auth0 or Clerk
- Email: SendGrid
- Analytics: PostHog
```

**Expected Duration**: 30-50 seconds
**Expected Cost**: $0.05-$0.12

---

#### Phase 5: Execution Plan

**File**: `api/app/workflow/phases/execution_plan.py`

**Class**: `ExecutionPlanPhase(BasePhaseHandler)`

**Purpose**: Generate stage-gate execution plan with approach detection

**LLM Model**: `openai/gpt-4o`

**Prompts**:
- Approach detection: `api/app/prompts/approach_detection.txt`
- Plan generation: `api/app/prompts/stages_prompt.txt`

**Input**:
```python
{
  "prd_md": "# Product Requirements Document\n...",
  "tech_stack_md": "# Tech Stack Document\n..."
}
```

**Output**:
```python
{
  "execution_plan_md": "# Execution Plan\n\n...",
  "approach": "HORIZONTAL",  # or "VERTICAL"
  "stage_count": 3,
  "estimated_duration_weeks": 12
}
```

**Approach Detection**:
- Analyzes feature count and complexity
- **Horizontal**: 1-3 features, build infrastructure first
- **Vertical**: 4+ features, build complete feature slices

**Execution Plan Structure**:

**Horizontal Approach**:
```markdown
# Execution Plan (Horizontal Approach)

## Stage 1: Foundation
**Duration**: 2 weeks

**Deliverables**:
- Database schema
- Authentication system
- API framework
- Basic UI scaffolding

**Stage Gate Criteria**:
- [ ] User can register and log in
- [ ] API endpoints respond with 200 OK
- [ ] Database migrations run successfully

## Stage 2: Core Features
**Duration**: 4 weeks

**Deliverables**:
- All core features implemented
- Business logic complete
- API endpoints for all features

**Stage Gate Criteria**:
- [ ] All user stories completable
- [ ] Unit tests pass
- [ ] API integration tests pass

## Stage 3: Polish & Launch
**Duration**: 2 weeks

**Deliverables**:
- UI/UX refinement
- Performance optimization
- Production deployment

**Stage Gate Criteria**:
- [ ] Page load < 2 seconds
- [ ] Zero critical bugs
- [ ] Deployed to production
```

**Vertical Approach**:
```markdown
# Execution Plan (Vertical Approach)

## Stage 1: User Authentication Feature
**Duration**: 1 week

**Deliverables**:
- Complete login/register flow
- Database for users
- API endpoints for auth
- UI for login/register

**Stage Gate Criteria**:
- [ ] User can register
- [ ] User can log in
- [ ] Session management works

## Stage 2: Task Management Feature
**Duration**: 2 weeks

**Deliverables**:
- Create/edit/delete tasks
- Task list UI
- API for CRUD operations

**Stage Gate Criteria**:
- [ ] User can create tasks
- [ ] User can view their tasks
- [ ] User can mark tasks complete

...
```

**Expected Duration**: 60-90 seconds
**Expected Cost**: $0.10-$0.25

---

### Workflow Execution Flow

**Function**: `WorkflowEngine.execute_workflow()` (`api/app/workflow/engine.py:168`)

**Pseudocode**:
```python
async def execute_workflow():
    # 1. Initialize tracking
    tracker = LangFuseTracker(project_id, idea)
    start_time = datetime.utcnow()

    # 2. Phase 0: Smart Detection
    await broadcast_phase_started(SMART_DETECTION, "Analyzing...")
    result = await run_smart_detection(idea)
    await broadcast_phase_completed(SMART_DETECTION, duration, cost)
    use_event_storming = result.use_event_storming

    # 3. Phase 0.5: Event Storming (conditional)
    if use_event_storming:
        await broadcast_phase_started(EVENT_STORMING, "Running...")
        result = await run_event_storming(idea)
        await broadcast_phase_completed(EVENT_STORMING, duration, cost)
        await save_document(EVENT_STORMING, result.markdown)

    # 4. Phase 1: PRD Generation
    await broadcast_phase_started(PRD, "Generating...")
    result = await run_prd_generation(idea, event_storming_summary)
    await broadcast_phase_completed(PRD, duration, cost)
    await save_document(PRD, result.markdown)

    # 5. Phase 2: Tech Stack
    await broadcast_phase_started(TECH_STACK, "Determining...")
    result = await run_tech_stack(prd_md)
    await broadcast_phase_completed(TECH_STACK, duration, cost)
    await save_document(TECH_STACK, result.markdown)

    # 6. Phase 3: Execution Plan
    await broadcast_phase_started(EXECUTION_PLAN, "Creating...")
    result = await run_execution_plan(prd_md, tech_stack_md)
    await broadcast_phase_completed(EXECUTION_PLAN, duration, cost)
    await save_document(EXECUTION_PLAN, result.markdown)

    # 7. Finalize
    total_cost, total_duration = await calculate_totals()
    await broadcast_workflow_completed(total_duration, total_cost, doc_count)
    await update_project_status(COMPLETED, metadata={...})

    return True
```

**Error Handling**:
- Each phase wrapped in try/catch
- On failure: `await broadcast_phase_failed(phase, error)`
- Workflow stops on first phase failure
- Project status set to `FAILED`
- Error stored in project metadata

---

## Core Services

### LLM Service

**File**: `api/app/services/llm_service.py`

**Class**: `LLMService`

**Purpose**: Make LLM API calls via OpenRouter with cost calculation

**Initialization**:
```python
llm_service = LLMService()
```

**Main Method**: `call()`

**Signature**:
```python
async def call(
    model: str,
    prompt: str,
    temperature: float = 0.7,
    max_tokens: int = 4000,
    response_format: Optional[Dict[str, str]] = None,
    system_message: Optional[str] = None,
) -> LLMResponse
```

**Parameters**:
- `model`: OpenRouter model ID (e.g., `"openai/gpt-4o-mini"`)
- `prompt`: User prompt text
- `temperature`: Sampling temperature (0.0 = deterministic, 1.0 = creative)
- `max_tokens`: Maximum tokens to generate
- `response_format`: Optional `{"type": "json_object"}` for JSON mode
- `system_message`: Optional system prompt

**Returns**: `LLMResponse` object with:
- `content`: String - LLM response text
- `model`: String - Model used
- `usage`: Dict - Token counts (`prompt_tokens`, `completion_tokens`, `total_tokens`)
- `cost_usd`: Float - Calculated cost
- `latency_ms`: Int - Request duration
- `raw_response`: Dict - Full API response

**Cost Calculation** (`api/app/services/llm_service.py:131-142`):
```python
def _calculate_cost(model: str, usage: Dict[str, int]) -> float:
    pricing = MODEL_PRICING.get(model, {"input": 0, "output": 0})

    input_cost = (usage["prompt_tokens"] / 1_000_000) * pricing["input"]
    output_cost = (usage["completion_tokens"] / 1_000_000) * pricing["output"]

    return input_cost + output_cost
```

**Pricing Table**:
```python
MODEL_PRICING = {
    "openai/gpt-4o-mini": {"input": 0.150, "output": 0.600},      # per 1M tokens
    "openai/gpt-4o": {"input": 2.50, "output": 10.00},
    "anthropic/claude-3.5-sonnet": {"input": 3.00, "output": 15.00},
    "anthropic/claude-3-haiku": {"input": 0.25, "output": 1.25},
}
```

**Example Usage**:
```python
llm_service = LLMService()

response = await llm_service.call(
    model="openai/gpt-4o-mini",
    prompt="Analyze this project idea: Build a todo app",
    temperature=0.3,
    max_tokens=1000,
    response_format={"type": "json_object"}
)

print(f"Response: {response.content}")
print(f"Cost: ${response.cost_usd:.6f}")
print(f"Tokens: {response.usage['total_tokens']}")
```

---

### LangFuse Service

**File**: `api/app/services/langfuse_service.py`

**Class**: `LangFuseTracker`

**Purpose**: Track LLM costs, performance, and traces in LangFuse

**Initialization**:
```python
tracker = LangFuseTracker(
    project_id=UUID("123e4567-e89b-12d3-a456-426614174000"),
    idea="Build a task management app"
)
```

**Main Methods**:

#### `track_phase()`
```python
def track_phase(
    phase_name: str,
    model: str,
    input_data: Dict,
    output_data: Dict,
    tokens: Dict[str, int],
    cost: float,
    duration_ms: int,
) -> str:
    """Track a single phase execution.

    Returns:
        generation_id: LangFuse generation ID
    """
```

**Example**:
```python
generation_id = tracker.track_phase(
    phase_name="PRD Generation",
    model="openai/gpt-4o",
    input_data={"idea": "...", "event_storming": "..."},
    output_data={"prd_md": "...", "feature_count": 12},
    tokens={"prompt_tokens": 2000, "completion_tokens": 1500, "total_tokens": 3500},
    cost=0.0875,
    duration_ms=45000,
)
```

**LangFuse UI**: View trace at `https://cloud.langfuse.com`

#### `track_event()`
```python
def track_event(event_name: str, metadata: Optional[Dict] = None) -> None:
    """Track a workflow event."""
```

**Example**:
```python
tracker.track_event("workflow_started")
tracker.track_event("phase_failed", metadata={"error": "API timeout"})
```

#### `finalize()`
```python
def finalize(
    total_cost: float,
    total_duration_seconds: int,
    status: str,
    documents_generated: int,
) -> None:
    """Finalize trace with totals."""
```

**Example**:
```python
tracker.finalize(
    total_cost=0.4523,
    total_duration_seconds=180,
    status="completed",
    documents_generated=4,
)
```

**LangFuse Features Used**:
- **Traces**: Top-level workflow execution
- **Generations**: Individual LLM API calls
- **Events**: Workflow milestones
- **Metadata**: Custom data (costs, durations, errors)
- **Tagging**: Project ID, user ID

---

### Prompt Manager

**File**: `api/app/services/prompt_manager.py`

**Class**: `PromptManager`

**Purpose**: Load and render prompt templates with variable substitution

**Initialization**:
```python
prompt_manager = PromptManager()
```

**Prompts Directory**: `api/app/prompts/`

**Available Prompts**:
1. `smart_detection.txt` - Complexity analysis
2. `event_storming.txt` - Domain discovery (5-phase)
3. `init_prompt.txt` - PRD generation (15 questions)
4. `tech_stack_prompt.txt` - Technology recommendations
5. `stages_prompt.txt` - Execution plan generation
6. `approach_detection.txt` - Horizontal vs Vertical decision

**Main Methods**:

#### `load_prompt()`
```python
def load_prompt(prompt_name: str) -> str:
    """Load prompt template from file (with caching)."""
```

#### `render_prompt()`
```python
def render_prompt(prompt_name: str, **kwargs) -> str:
    """Render prompt with variable substitution."""
```

**Example**:
```python
prompt = prompt_manager.render_prompt(
    "smart_detection",
    idea="Build a task management app with AI-powered prioritization"
)
```

**Helper Methods** (shortcuts for specific prompts):
- `get_smart_detection_prompt(idea: str) -> str`
- `get_event_storming_prompt(idea: str) -> str`
- `get_init_prompt(idea: str, event_storming: str = "") -> str`
- `get_tech_stack_prompt(prd_md: str) -> str`
- `get_stages_prompt(prd_md: str, tech_stack_md: str, approach: str) -> str`
- `get_approach_detection_prompt(prd_md: str) -> str`

**Template Syntax**:
```python
# In prompt file: smart_detection.txt
"""
Analyze the following project idea:

{idea}

Respond with JSON...
"""

# In code:
prompt = prompt_manager.render_prompt("smart_detection", idea="Build a todo app")
```

---

### WebSocket Manager

**File**: `api/app/core/websocket_manager.py`

**Class**: `ConnectionManager`

**Purpose**: Manage WebSocket connections and broadcast messages

**Singleton Instance**:
```python
from app.core.websocket_manager import manager
```

**Data Structure**:
```python
active_connections: Dict[str, List[WebSocket]] = {}
# Key: project_id (as string)
# Value: List of WebSocket connections
```

**Methods**:

#### `connect()`
```python
async def connect(project_id: UUID, websocket: WebSocket) -> None:
    """Accept and register a WebSocket connection."""
```

**Example**:
```python
await manager.connect(project_id, websocket)
```

#### `disconnect()`
```python
def disconnect(project_id: UUID, websocket: WebSocket) -> None:
    """Unregister a WebSocket connection."""
```

**Example**:
```python
manager.disconnect(project_id, websocket)
```

#### `broadcast()`
```python
async def broadcast(project_id: UUID, message: dict) -> None:
    """Send message to all connected clients for a project.

    Automatically adds timestamp if not present.
    Removes dead connections automatically.
    """
```

**Example**:
```python
await manager.broadcast(
    project_id,
    {
        "type": "phase_started",
        "phase": "PRD",
        "message": "Generating PRD..."
    }
)
```

**Auto-Cleanup**:
- Detects broken connections during broadcast
- Removes dead connections from pool
- Logs cleanup actions

---

## Configuration

### Environment Variables

**File**: `api/app/config.py`

**Class**: `Settings(BaseSettings)`

**Configuration Loading**:
1. Reads from `.env` file
2. Reads from environment variables
3. Uses defaults if not found

**Variables**:

| Variable | Type | Default | Description |
|----------|------|---------|-------------|
| `PROJECT_NAME` | str | "AI-Driven..." | API name |
| `VERSION` | str | "1.0.0" | API version |
| `API_V1_PREFIX` | str | "/api/v1" | API route prefix |
| `DEBUG` | bool | False | Debug mode |
| `HOST` | str | "0.0.0.0" | Server host |
| `PORT` | int | 8000 | Server port |
| `POSTGRES_SERVER` | str | "localhost" | DB host |
| `POSTGRES_PORT` | int | 5432 | DB port |
| `POSTGRES_USER` | str | "postgres" | DB username |
| `POSTGRES_PASSWORD` | str | "postgres" | DB password |
| `POSTGRES_DB` | str | "ai_dev_framework" | DB name |
| `DATABASE_URL` | str | "postgresql+asyncpg://..." | Full DB connection string |
| `ADMIN_TOKEN` | str | "change-me-in-production" | ⚠️ API authentication token |
| `OPENROUTER_API_KEY` | str | "" | OpenRouter API key |
| `OPENROUTER_BASE_URL` | str | "https://openrouter.ai/api/v1" | OpenRouter endpoint |
| `LANGFUSE_PUBLIC_KEY` | str | "" | LangFuse public key |
| `LANGFUSE_SECRET_KEY` | str | "" | LangFuse secret key |
| `LANGFUSE_HOST` | str | "https://cloud.langfuse.com" | LangFuse instance |
| `RATE_LIMIT_PER_SECOND` | int | 1 | Global rate limit |
| `BACKEND_CORS_ORIGINS` | List[str] | ["http://localhost:3000", ...] | Allowed CORS origins |
| `LOG_LEVEL` | str | "INFO" | Logging level |

**Usage**:
```python
from app.config import settings

print(settings.ADMIN_TOKEN)
print(settings.DATABASE_URL)
```

**Property**:
```python
@property
def database_url_sync(self) -> str:
    """Get synchronous database URL for Alembic."""
    return self.DATABASE_URL.replace("+asyncpg", "")
```

---

## Deployment

### Docker Compose

**File**: `api/docker-compose.yml`

**Services**:
- `db`: PostgreSQL 14
- `api`: FastAPI application

**Start**:
```bash
docker-compose up -d
```

**Logs**:
```bash
docker-compose logs -f api
```

**Stop**:
```bash
docker-compose down
```

---

### Database Migrations

**Tool**: Alembic

**Directory**: `api/alembic/`

**Configuration**: `api/alembic.ini`, `api/alembic/env.py`

**Commands**:

```bash
# Create new migration
alembic revision --autogenerate -m "description"

# Apply migrations
alembic upgrade head

# Rollback one migration
alembic downgrade -1

# Show current version
alembic current

# Show migration history
alembic history
```

**Auto-Generate Migrations**:
```bash
# After modifying models
alembic revision --autogenerate -m "add new column to projects"
alembic upgrade head
```

---

### Production Deployment

**Recommended Stack**:
- **Reverse Proxy**: nginx or Caddy
- **ASGI Server**: uvicorn with multiple workers
- **Process Manager**: systemd or Docker Compose
- **Database**: Managed PostgreSQL (AWS RDS, Google Cloud SQL)
- **Secrets**: AWS Secrets Manager or HashiCorp Vault
- **Monitoring**: Prometheus + Grafana
- **Logging**: ELK stack or CloudWatch

**Example Production Start**:
```bash
uvicorn app.main:app \
  --host 0.0.0.0 \
  --port 8000 \
  --workers 4 \
  --log-config logging.yaml \
  --access-log \
  --proxy-headers \
  --forwarded-allow-ips='*'
```

**Nginx Configuration**:
```nginx
upstream fastapi {
    server 127.0.0.1:8000;
}

server {
    listen 80;
    server_name api.example.com;

    location / {
        proxy_pass http://fastapi;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }

    location /api/v1/projects/*/progress {
        proxy_pass http://fastapi;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
        proxy_read_timeout 3600s;
    }
}
```

---

## Development Guide

### Project Structure

```
api/
├── app/
│   ├── __init__.py
│   ├── main.py                    # FastAPI application entry point
│   ├── config.py                  # Configuration settings
│   │
│   ├── api/                       # API endpoints
│   │   ├── __init__.py
│   │   ├── deps.py                # Dependency injection
│   │   └── v1/
│   │       ├── __init__.py
│   │       ├── projects.py        # Project CRUD endpoints
│   │       └── websocket.py       # WebSocket endpoint
│   │
│   ├── core/                      # Core utilities
│   │   ├── __init__.py
│   │   ├── auth.py                # Authentication
│   │   ├── security.py            # Rate limiting
│   │   └── websocket_manager.py   # WebSocket connection pool
│   │
│   ├── db/                        # Database layer
│   │   ├── __init__.py
│   │   ├── base.py                # SQLAlchemy base
│   │   ├── session.py             # Database session management
│   │   └── models/
│   │       ├── __init__.py
│   │       ├── user.py
│   │       ├── project.py
│   │       ├── workflow_state.py
│   │       ├── document.py
│   │       └── llm_log.py
│   │
│   ├── schemas/                   # Pydantic schemas
│   │   ├── __init__.py
│   │   ├── project.py             # Project request/response schemas
│   │   ├── document.py            # Document schemas
│   │   └── workflow.py            # Workflow event schemas
│   │
│   ├── services/                  # Business logic
│   │   ├── __init__.py
│   │   ├── llm_service.py         # OpenRouter LLM client
│   │   ├── langfuse_service.py    # LangFuse tracking
│   │   └── prompt_manager.py      # Prompt template loader
│   │
│   ├── workflow/                  # Workflow engine
│   │   ├── __init__.py
│   │   ├── engine.py              # Main workflow orchestrator
│   │   ├── state_machine.py       # Phase transitions
│   │   ├── document_storage.py    # Document save utilities
│   │   └── phases/
│   │       ├── __init__.py
│   │       ├── base.py            # BasePhaseHandler
│   │       ├── smart_detection.py
│   │       ├── event_storming.py
│   │       ├── prd_generation.py
│   │       ├── tech_stack.py
│   │       └── execution_plan.py
│   │
│   └── prompts/                   # LLM prompt templates
│       ├── smart_detection.txt
│       ├── event_storming.txt
│       ├── init_prompt.txt
│       ├── tech_stack_prompt.txt
│       ├── stages_prompt.txt
│       └── approach_detection.txt
│
├── alembic/                       # Database migrations
│   ├── versions/
│   │   ├── 001_initial_schema.py
│   │   └── ...
│   ├── env.py
│   └── script.py.mako
│
├── tests/                         # Test suite
│   ├── __init__.py
│   ├── test_llm_service.py
│   ├── test_workflow.py
│   └── ...
│
├── .env                          # Environment variables (gitignored)
├── .env.example                  # Environment template
├── requirements.txt              # Python dependencies
├── docker-compose.yml            # Docker configuration
├── Dockerfile                    # Container image
├── alembic.ini                   # Alembic configuration
├── README.md                     # Setup guide
├── SECURITY_REVIEW.md            # Security analysis
└── TECHNICAL_DOCUMENTATION.md    # This document
```

---

### Adding a New Endpoint

1. **Define Schema** (`app/schemas/your_schema.py`):
```python
from pydantic import BaseModel

class YourRequest(BaseModel):
    field: str

class YourResponse(BaseModel):
    result: str
```

2. **Create Endpoint** (`app/api/v1/your_endpoint.py`):
```python
from fastapi import APIRouter, Depends
from app.core.auth import verify_admin_token
from app.schemas.your_schema import YourRequest, YourResponse

router = APIRouter()

@router.post("/your-endpoint", response_model=YourResponse, dependencies=[Depends(verify_admin_token)])
async def your_endpoint(data: YourRequest):
    return YourResponse(result=f"Processed: {data.field}")
```

3. **Register Router** (`app/main.py`):
```python
from app.api.v1 import your_endpoint

app.include_router(
    your_endpoint.router,
    prefix=f"{settings.API_V1_PREFIX}/your-path",
    tags=["your-tag"],
)
```

---

### Adding a New Database Model

1. **Create Model** (`app/db/models/your_model.py`):
```python
from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID
from app.db.base import Base
import uuid

class YourModel(Base):
    __tablename__ = "your_table"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String(255), nullable=False)
```

2. **Import Model** (`app/db/models/__init__.py`):
```python
from app.db.models.your_model import YourModel
```

3. **Create Migration**:
```bash
alembic revision --autogenerate -m "add your_table"
alembic upgrade head
```

---

### Testing

**Run Tests**:
```bash
pytest
pytest --cov=app
pytest --cov=app --cov-report=html
```

**Test Structure**:
```python
# tests/test_llm_service.py
import pytest
from app.services.llm_service import LLMService

@pytest.mark.asyncio
async def test_llm_call():
    service = LLMService()
    response = await service.call(
        model="openai/gpt-4o-mini",
        prompt="Say hello",
        max_tokens=10,
    )
    assert response.content
    assert response.cost_usd > 0
```

---

## Glossary

| Term | Definition |
|------|------------|
| **Phase** | A discrete step in the workflow (e.g., SMART_DETECTION, PRD) |
| **Workflow** | Complete execution of all phases from idea to execution plan |
| **Event Storming** | Domain discovery technique using events, commands, aggregates |
| **PRD** | Product Requirements Document |
| **Tech Stack** | Recommended technologies for implementing the project |
| **Execution Plan** | Stage-gate implementation roadmap |
| **Horizontal Approach** | Build infrastructure first, then features |
| **Vertical Approach** | Build complete feature slices one at a time |
| **Smart Detection** | LLM-based complexity analysis to decide workflow path |
| **Stage Gate** | Checkpoint with acceptance criteria between stages |
| **LangFuse** | LLM observability platform for tracking costs and performance |
| **OpenRouter** | Multi-model LLM API gateway |
| **Async** | Asynchronous Python programming (async/await) |
| **ORM** | Object-Relational Mapping (SQLAlchemy) |
| **UUID** | Universally Unique Identifier (128-bit) |
| **WebSocket** | Bidirectional real-time communication protocol |
| **Bearer Token** | HTTP authentication scheme |
| **Rate Limiting** | Request throttling to prevent abuse |

---

## Appendix: Complete Function Reference

### Workflow Engine

| Function | Location | Description |
|----------|----------|-------------|
| `execute_workflow()` | `api/app/workflow/engine.py:168` | Main workflow orchestration |
| `_run_smart_detection()` | `api/app/workflow/engine.py:342` | Execute Smart Detection phase |
| `_run_event_storming()` | `api/app/workflow/engine.py:347` | Execute Event Storming phase |
| `_run_prd_generation()` | `api/app/workflow/engine.py:352` | Execute PRD generation phase |
| `_run_tech_stack()` | `api/app/workflow/engine.py:362` | Execute Tech Stack phase |
| `_run_execution_plan()` | `api/app/workflow/engine.py:367` | Execute Execution Plan phase |
| `_broadcast_phase_started()` | `api/app/workflow/engine.py:91` | Send WebSocket phase start event |
| `_broadcast_phase_completed()` | `api/app/workflow/engine.py:108` | Send WebSocket phase complete event |
| `_broadcast_phase_failed()` | `api/app/workflow/engine.py:129` | Send WebSocket phase failed event |
| `_broadcast_workflow_completed()` | `api/app/workflow/engine.py:147` | Send WebSocket workflow complete event |
| `_calculate_totals()` | `api/app/workflow/engine.py:375` | Calculate total cost and duration |
| `_handle_workflow_failure()` | `api/app/workflow/engine.py:492` | Handle workflow errors |

### API Endpoints

| Function | Location | Description |
|----------|----------|-------------|
| `create_project()` | `api/app/api/v1/projects.py:60` | POST /projects |
| `start_workflow()` | `api/app/api/v1/projects.py:103` | POST /projects/{id}/start-workflow |
| `get_project()` | `api/app/api/v1/projects.py:163` | GET /projects/{id} |
| `get_project_documents()` | `api/app/api/v1/projects.py:199` | GET /projects/{id}/documents |
| `get_project_document()` | `api/app/api/v1/projects.py:242` | GET /projects/{id}/documents/{type} |
| `get_project_costs()` | `api/app/api/v1/projects.py:299` | GET /projects/{id}/costs |
| `project_progress()` | `api/app/api/v1/websocket.py:19` | WebSocket /projects/{id}/progress |

### Services

| Function | Location | Description |
|----------|----------|-------------|
| `LLMService.call()` | `api/app/services/llm_service.py:48` | Make LLM API call |
| `LangFuseTracker.track_phase()` | `api/app/services/langfuse_service.py:55` | Track phase in LangFuse |
| `PromptManager.render_prompt()` | `api/app/services/prompt_manager.py:35` | Render prompt template |
| `ConnectionManager.broadcast()` | `api/app/core/websocket_manager.py:46` | Broadcast WebSocket message |

---

**End of Technical Documentation**

**Version**: 1.0.0
**Last Updated**: 2025-11-09
**Maintainer**: Development Team
