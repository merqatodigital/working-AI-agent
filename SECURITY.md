# Security Policy

## Reporting

Do not open a public issue for exposed credentials, authentication bypasses, cross-tenant access, prompt-injection paths involving privileged tools, or guest-data exposure.

Report vulnerabilities privately to `merqato.digital@gmail.com` with reproduction steps, impact, affected components, and any suggested remediation.

## Current Maturity

KAPWA is an early-stage codebase and is not yet approved for handling production guest or payment data. Authentication, tenant isolation, CORS, database policies, rate limiting, logging, and deployment controls require explicit verification before public exposure.

## Secrets

Never commit API keys, Supabase service-role keys, OAuth secrets, access tokens, passwords, or `.env` files. If a credential enters Git history, rotate it immediately; deleting the file in a later commit is insufficient.

## Agent Safety

Actions that publish externally, alter reservations, change money-related records, send messages, delete data, or affect guest commitments must require appropriate authorization and, where designed, explicit human approval.
