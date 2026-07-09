# Architecture

## Product Boundary

This repository is the intended home of MerQato's working AI agent platform. It should remain one multi-tenant product rather than a separate deployment or database project for every hospitality customer.

## Production Services

- **Application and preview deployments:** Vercel
- **Authentication, PostgreSQL, storage, and backend services:** Supabase
- **Source control and review:** GitHub
- **AI model access:** Provider adapters configured by environment variables

The imported codebase remains the source of truth. This document must be revised when the real implementation differs.

## Core Domains

### Identity and access

Users authenticate through Supabase Auth. Server-side authorization must verify organization membership and role before reading or changing tenant data.

### Tenancy

Every tenant-owned record should carry a stable tenant or organization identifier. Database policies and server-side checks must prevent cross-tenant access.

### Agent configuration

Agent identity, instructions, enabled tools, knowledge sources, channel configuration, and operational limits should be stored as structured, versionable data rather than hard-coded per customer.

### Conversations and execution

Conversation history, tool calls, approvals, failures, and execution results should be traceable. Sensitive data should be minimized and retained only as required.

### Knowledge and media

Files and structured knowledge should use tenant-scoped storage paths and database records. Upload validation, authorization, and deletion must be enforced server-side.

## Engineering Principles

1. **Tenant isolation first.** No convenience feature justifies weakening authorization.
2. **Configuration over forks.** Customer differences belong in data and settings, not separate codebases.
3. **Human approval for risky actions.** Publishing, destructive changes, financial actions, and external communication should use explicit approval boundaries.
4. **Observable execution.** Important agent actions need logs, status, errors, and audit context.
5. **Reproducible deployment.** Schema changes use migrations; configuration uses documented environment variables.
6. **No false completeness.** Documentation must distinguish implemented, planned, and unverified behavior.

## Expected Environments

- **Local:** developer machine with non-production credentials
- **Preview:** isolated Vercel preview using safe development or staging services
- **Production:** protected deployment with production-only credentials and controlled access

## Required Documentation After Source Import

Once the application code is added, document:

- Actual framework and runtime versions
- Package manager and lockfile
- Local setup and seed process
- Supabase migration workflow
- Authentication and authorization model
- Agent execution path
- Required third-party integrations
- Lint, type-check, test, and build commands
- Preview and production deployment process
