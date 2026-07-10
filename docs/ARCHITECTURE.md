# KAPWA Resort OS Architecture

## Overview

KAPWA is a monorepo containing a Python agent platform, a FastAPI service, a React operations dashboard, and Supabase schema files. The current implementation uses local mock data for core resort operations while establishing the interfaces required for a persistent backend.

## Runtime Flow

```text
Dashboard or CLI
      │
      ▼
FastAPI / agent-core
      │
      ▼
LangGraph classification and response nodes
      │
      ├── resort-tools
      ├── resort-data
      └── resort-types
```

The model adapter supports local Ollama models and OpenRouter-compatible hosted models.

## Workspace Packages

### `agent-core`

Owns model configuration, prompts, graph construction, classification, response generation, auditing, and the terminal interface.

### `agent-api`

Exposes chat, state, approvals, and settings routes through FastAPI. The current CORS configuration is permissive for development and must be restricted before production deployment.

### `resort-types`

Contains shared Pydantic models and enums for guests, reservations, rooms, staff, inventory, finance, audits, and agent state.

### `resort-data`

Provides mock JSON fixtures and a local data loader. This is development data, not the production persistence layer.

### `resort-tools`

Contains operational tools for reservations, staff workflows, and approval-sensitive actions.

### `dashboard`

A React/Vite interface that calls the FastAPI service and initializes a Supabase browser client from Vite environment variables.

## Database

The initial Supabase migration set creates the resort operational tables. Before production use, the team must verify:

- Row Level Security is enabled where required
- Policies enforce organization membership
- Service-role credentials never reach the browser
- Every tenant-owned table has an explicit tenant key
- Audit and approval records are immutable where appropriate
- Destructive operations have authorization and retention rules

## Production Gaps

The following items are not represented as complete production controls in the current codebase:

- User authentication and role authorization
- Multi-tenant organization boundaries
- Hardened CORS configuration
- Persistent agent memory and durable execution
- Secret management
- Rate limiting and abuse controls
- Structured logging, tracing, and alerting
- Production deployment manifests
- Complete automated test coverage

These gaps should remain visible in planning and pull requests until reproducibly implemented.

## Engineering Principles

1. Enforce access on the server and in the database, never only in the UI.
2. Keep customer differences in tenant-scoped configuration rather than code forks.
3. Require human approval for external communication, destructive changes, financial actions, and publishing.
4. Record enough execution context to audit agent decisions without unnecessarily retaining sensitive guest data.
5. Apply schema changes through migrations and document every required environment variable.
