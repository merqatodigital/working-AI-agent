# Contributing to KAPWA Resort OS

## Workflow

1. Branch from `main` using `feature/`, `fix/`, `docs/`, or `chore/`.
2. Keep changes focused and reviewable.
3. Add or update tests when behavior changes.
4. Update documentation and `.env.example` files when configuration changes.
5. Run the relevant verification commands.
6. Open a pull request using the repository template.

## Local Verification

Python:

```bash
uv sync
uv run ruff check .
uv run pytest
python -m compileall apps packages
```

Dashboard:

```bash
cd apps/dashboard
npm install
npm run build
```

Record commands that could not be run and the exact blocker. Never report a check as passing unless it was actually executed successfully.

## Commit Style

Use clear Conventional Commit messages where practical:

```text
feat: add tenant-aware agent settings
fix: validate approval ownership
docs: document local Supabase setup
```

## Pull Request Requirements

Include:

- Problem and intended outcome
- Implementation summary
- Screenshots for interface changes
- Migration and environment-variable changes
- Commands run and results
- Security or tenant-isolation impact
- Known limitations and follow-up work

## Engineering Rules

- Do not commit secrets, real guest data, local databases, caches, or build output.
- Do not trust tenant IDs supplied by clients without authenticated membership checks.
- Use migrations for database changes.
- Preserve the approval boundary for risky actions.
- Avoid unrelated refactors inside feature changes.
