# MerQato Working AI Agent

A production-oriented foundation for MerQato's multi-tenant AI agent platform.

> **Repository status:** Initial developer setup is in progress. The application source code still needs to be imported into this repository before local development or deployment can begin.

## Purpose

This repository is intended to contain the working MerQato AI agent platform: a shared system where hospitality businesses can configure and operate AI agents from one secure, multi-tenant application.

The production stack is expected to use:

- **GitHub** for source control and collaboration
- **Vercel** for application hosting and deployments
- **Supabase** for authentication, PostgreSQL, storage, and backend services

## Current State

The repository currently includes the developer documentation and project standards required before the application code is imported.

No production application, database migration, deployment, or environment configuration should be assumed complete unless it is present in the repository and verified by the documented commands.

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/merqatodigital/working-AI-agent.git
cd working-AI-agent
```

### 2. Import or confirm the application source

The actual application source must be added before continuing. Once imported, update this README with the real framework, package manager, setup commands, and verified runtime requirements.

### 3. Configure environment variables

Copy the example environment file after the application defines its required variables:

```bash
cp .env.example .env.local
```

Never commit `.env`, `.env.local`, API keys, service-role keys, access tokens, or customer credentials.

## Repository Standards

- Work from a feature branch; do not develop directly on `main`.
- Use pull requests for review and traceability.
- Keep secrets out of Git history.
- Add migrations for database changes.
- Document every required environment variable in `.env.example`.
- Run the project's lint, type-check, test, and build commands before merging.
- Do not claim a feature is complete without reproducible verification.

## Planned Repository Structure

The exact structure must follow the imported application, but a typical layout may include:

```text
.
├── app/ or src/          Application source
├── components/          Shared interface components
├── lib/                 Shared services and utilities
├── public/              Static assets
├── supabase/            Database migrations and configuration
├── tests/               Automated tests
├── docs/                Architecture and operating documentation
├── .env.example         Safe environment variable template
└── README.md             Developer entry point
```

## Architecture

See [`docs/ARCHITECTURE.md`](docs/ARCHITECTURE.md) for the initial system boundaries and production principles.

## Contributing

See [`CONTRIBUTING.md`](CONTRIBUTING.md) before making changes.

## Security

See [`SECURITY.md`](SECURITY.md) for vulnerability reporting and secret-handling requirements.

## License

Copyright © MerQato Digital. All rights reserved.

No license is granted to use, copy, modify, or distribute this software unless MerQato Digital provides written permission or adds a separate license file.
