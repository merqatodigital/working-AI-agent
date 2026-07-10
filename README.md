# KAPWA Resort OS

AI-powered resort operations platform for hospitality teams. KAPWA combines a LangGraph-based agent, operational tools, a FastAPI service, a React dashboard, and a Supabase-ready data model in one Python workspace.

## Status

**Early-stage working codebase.** The repository contains the agent core, API, dashboard, resort domain models, mock data, operational tools, database migrations, and basic tests. Authentication, production tenant isolation, deployment configuration, and full end-to-end verification still require completion before production use.

## What It Does

KAPWA is designed to route resort requests across guest relations, reservations, front desk, housekeeping, maintenance, staff coordination, inventory, purchasing, finance analysis, and owner reporting.

Current capabilities include:

- Intent, department, and urgency classification
- LangGraph agent execution
- Ollama and OpenRouter model configuration
- Resort data access through typed Python packages
- Human approval records for sensitive actions
- FastAPI routes for chat, operational state, approvals, and model settings
- React/Vite operations dashboard
- Supabase migrations for the initial resort schema

## Architecture

```text
apps/
├── agent-api/          FastAPI service and HTTP routes
└── dashboard/          React + TypeScript + Vite dashboard

packages/
├── agent-core/         LangGraph graph, prompts, nodes, CLI, and LLM config
├── resort-data/        Mock JSON fixtures and data loader
├── resort-tools/       Operational tools and approval workflows
└── resort-types/       Shared Pydantic models and enums

supabase/
├── migrations/         Initial PostgreSQL schema migrations
└── seed.sql            Development seed data
```

See [`docs/ARCHITECTURE.md`](docs/ARCHITECTURE.md) for system boundaries and production considerations.

## Technology

- Python 3.12
- `uv` workspace management
- LangGraph and LangChain
- FastAPI and Uvicorn
- Pydantic
- React 18, TypeScript, and Vite
- Tailwind CSS
- Supabase
- Ollama or OpenRouter

## Prerequisites

Install:

- Python 3.12
- [`uv`](https://docs.astral.sh/uv/)
- Node.js 20 or newer
- npm
- Ollama, or an OpenRouter API key
- Supabase CLI only when applying the included migrations locally

## Local Setup

### 1. Clone and install Python dependencies

```bash
git clone https://github.com/merqatodigital/working-AI-agent.git
cd working-AI-agent
uv sync
```

### 2. Configure the model provider

```bash
cp .env.example .env
```

The default configuration expects Ollama at `http://localhost:11434` using `qwen2.5:3b`.

For OpenRouter, set:

```env
KAPWA_LLM_PROVIDER=openrouter
KAPWA_LLM_MODEL=deepseek/deepseek-chat
OPENROUTER_API_KEY=your_key_here
```

Never commit real credentials.

### 3. Start the API

```bash
uv run --package agent-api uvicorn agent_api.main:app --reload --port 8001
```

Verify it at `http://localhost:8001/health`. Interactive API documentation is available at `http://localhost:8001/docs`.

### 4. Start the dashboard

```bash
cd apps/dashboard
cp .env.example .env.local
npm install
npm run dev
```

The dashboard expects the API at `http://localhost:8001` unless `VITE_AGENT_API_URL` is changed.

### 5. Run the terminal agent

From the repository root:

```bash
uv run --package agent-core python -m agent_core.cli
```

## Dashboard Environment Variables

| Variable | Purpose |
|---|---|
| `VITE_AGENT_API_URL` | FastAPI base URL |
| `VITE_SUPABASE_URL` | Supabase project URL |
| `VITE_SUPABASE_ANON_KEY` | Public Supabase anonymous key |

## Database

The `supabase/migrations/` directory currently defines guests, reservations, rooms, staff, tasks, inventory, audit logs, approvals, and policies.

Before production deployment, review every migration, verify Row Level Security policies, and confirm authenticated tenant isolation. The current repository should not be treated as production-secure merely because the schema files exist.

## Verification

Run the available checks from the repository root:

```bash
uv run ruff check .
uv run pytest
python -m compileall apps packages
```

Build the dashboard separately:

```bash
cd apps/dashboard
npm install
npm run build
```

## Development Workflow

Read [`CONTRIBUTING.md`](CONTRIBUTING.md) before changing the code. Use feature branches and pull requests; do not commit secrets or generated artifacts.

## Security

Security issues should be reported privately according to [`SECURITY.md`](SECURITY.md). In particular, authorization, tenant boundaries, CORS restrictions, secret storage, and database policies must be hardened before exposing this system publicly.

## Ownership

Copyright © MerQato Digital. All rights reserved.

This repository is source-available for authorized MerQato development only. No permission is granted to copy, distribute, sublicense, or commercially use the software without written authorization from MerQato Digital.
