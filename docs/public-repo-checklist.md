# Public Repository Approval Checklist

Use this checklist before making any `wminternal` repository public.

## Required Checks

1. Confirm the repository has a legitimate public purpose.
2. Confirm the repository does not contain secrets, credentials, or private tokens.
3. Confirm the repository does not expose customer, tenant, or operationally sensitive data.
4. Confirm git history has been reviewed for accidental disclosures.
5. Confirm the README clearly states the repository purpose.
6. Confirm there is a `SECURITY.md` or equivalent security reporting guidance.
7. Confirm a maintainer or owning team is identified.
8. Confirm the public content does not reveal private architecture details beyond what is intentionally disclosed.
9. Confirm issue templates and contact paths are appropriate for public use.
10. Confirm the repo adds value by being public rather than private.

## For Public Bug Repositories Specifically

1. Confirm normal bugs can be reported safely without exposing internal details.
2. Confirm security vulnerabilities are redirected to a private reporting channel.
3. Confirm issue forms collect version, severity, and reproduction details.
4. Confirm the application links directly to the public bug tracker rather than the organization root.

## Approval Outcome

If any required check fails, keep the repository private until the issue is resolved.