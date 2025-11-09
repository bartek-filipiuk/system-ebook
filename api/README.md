# AI-Driven Development Framework API

FastAPI backend that automates the AI-Driven Development Framework workflow.

## Features

- Automated workflow from project idea to execution plan
- Smart detection for Event Storming and development approach
- Real-time progress updates via WebSocket
- Cost tracking with LangFuse
- Multi-model support via OpenRouter
- PostgreSQL for state persistence

## Quick Start

### Prerequisites

- Docker and Docker Compose
- Python 3.11+ (for local development)

### Setup

1. **Clone and navigate to API directory**
   ```bash
   cd api
   ```

2. **Copy environment file**
   ```bash
   cp .env.example .env
   ```

3. **Update .env with your keys**
   - `ADMIN_TOKEN`: Set a secure admin token
   - `OPENROUTER_API_KEY`: Your OpenRouter API key
   - `LANGFUSE_PUBLIC_KEY` and `LANGFUSE_SECRET_KEY`: Your LangFuse keys

4. **Start with Docker Compose**
   ```bash
   docker-compose up -d
   ```

5. **Run migrations**
   ```bash
   docker-compose exec api alembic upgrade head
   ```

6. **Access the API**
   - API: http://localhost:8000
   - Docs: http://localhost:8000/docs
   - Health: http://localhost:8000/health

## Development Setup (Local)

### Install dependencies

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### Run PostgreSQL

```bash
docker-compose up -d db
```

### Run migrations

```bash
alembic upgrade head
```

### Start development server

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

## Database Migrations

### Create a new migration

```bash
alembic revision --autogenerate -m "description"
```

### Apply migrations

```bash
alembic upgrade head
```

### Rollback migration

```bash
alembic downgrade -1
```

## API Documentation

Once running, visit:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## Project Structure

```
api/
├── app/
│   ├── api/           # API endpoints
│   ├── core/          # Auth, security
│   ├── db/            # Database models
│   ├── schemas/       # Pydantic schemas
│   ├── services/      # Business logic
│   ├── workflow/      # Workflow engine
│   └── prompts/       # LLM prompts
├── alembic/           # Database migrations
├── tests/             # Test suite
└── docker-compose.yml # Docker setup
```

## Testing

```bash
pytest
pytest --cov=app
```

## Phase 1 Status ✅

- [x] FastAPI project structure
- [x] PostgreSQL with Docker Compose
- [x] SQLAlchemy models
- [x] Alembic migrations
- [x] Admin token authentication
- [x] Rate limiting (SlowAPI)
- [x] Health check endpoint
- [x] CORS middleware
- [x] Logging configuration

## Phase 2 Status ✅

- [x] OpenRouter LLM service with cost calculation
- [x] LangFuse integration with tracing
- [x] Prompt template manager (6 prompts)
- [x] Smart detection prompts
- [x] Pydantic schemas for API
- [x] Comprehensive test suite

## Next Steps (Phase 3)

- [ ] Workflow engine implementation
- [ ] Phase handlers (Smart Detection, Event Storming, PRD, Tech Stack, Execution Plan)
- [ ] State machine for workflow transitions
- [ ] Document generation and storage
- [ ] Error handling and retry logic

## License

See main project license.
