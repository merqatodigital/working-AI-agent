# Contributing

## Workflow

1. Create a focused branch from `main`.
2. Make one logical change at a time.
3. Update documentation when behavior or configuration changes.
4. Run every available verification command locally.
5. Open a pull request with the problem, solution, verification, and remaining risks.

## Branch Names

Use short, descriptive names:

```text
feature/guest-agent-chat
fix/auth-session-refresh
docs/developer-setup
chore/dependency-update
```

## Commit Messages

Use clear, imperative commit messages, preferably following Conventional Commits:

```text
feat: add tenant-aware agent settings
fix: prevent cross-tenant data access
docs: document Supabase setup
```

## Pull Request Requirements

Every pull request should include:

- What changed and why
- Screenshots for interface changes
- Database migration notes when applicable
- New or changed environment variables
- Commands run and their results
- Known limitations or follow-up work

## Engineering Rules

- Never commit credentials or customer data.
- Preserve tenant isolation in every database query and API route.
- Use migrations for schema changes.
- Prefer small, reviewable pull requests.
- Do not bypass linting, type checking, tests, or build failures without documenting the reason.
- Avoid destructive production actions unless they are explicitly approved.

## Definition of Done

A change is complete only when its implementation, documentation, migration requirements, and reproducible verification are all present.
