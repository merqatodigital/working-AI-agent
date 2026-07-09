# Security Policy

## Reporting a Vulnerability

Do not open a public GitHub issue for suspected security vulnerabilities, exposed credentials, authentication bypasses, tenant-isolation failures, or customer-data exposure.

Report the issue privately to MerQato Digital at `merqato.digital@gmail.com` with:

- A concise description of the issue
- Affected route, component, or service
- Reproduction steps
- Potential impact
- Suggested remediation, when known

## Secret Handling

Never commit:

- `.env` files
- Supabase service-role keys
- AI provider API keys
- OAuth client secrets
- Access or refresh tokens
- Customer credentials or personal data

If a secret is committed, removing the file is not enough. Revoke or rotate the credential immediately and clean the Git history when required.

## Multi-Tenant Requirements

All application and database changes must preserve tenant isolation. Authorization must be enforced server-side and, where applicable, through Supabase Row Level Security. Client-provided tenant identifiers must never be trusted without validating the authenticated user's membership and permissions.

## Dependency and Deployment Safety

- Review dependency changes before merging.
- Keep lockfiles committed once the package manager is established.
- Restrict production environment access.
- Use separate development, preview, and production credentials.
- Do not log secrets, full tokens, or sensitive guest information.
