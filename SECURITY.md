# Security Policy

## Supported Reporting Path

This repository is a public bug tracker. Do not report security vulnerabilities in public issues.

If you believe you have found a security issue, use a private reporting path instead of creating a public issue.

Recommended private reporting options:

- GitHub private vulnerability reporting, if enabled for this repository
- A private security contact email managed by the EzeAla team
- A private support or incident intake channel controlled by the `wminternal` organization

## What Not To Include In Public Issues

Do not post any of the following in public issues:

- API keys, tokens, or secrets
- Internal URLs not intended for disclosure
- Customer data or tenant information
- Authentication bypass details
- AWS account details, IAM policies, or infrastructure secrets
- Database connection strings or stack traces containing secrets

## Public Bug Reports vs Security Reports

Use public issues only for normal product bugs such as:

- UI defects
- workflow failures
- non-sensitive API behavior problems
- regressions without exploit details

Use private reporting for:

- privilege escalation
- authentication bypass
- sensitive data exposure
- remote code execution
- injection vulnerabilities
- SSRF, XSS, CSRF, or secret leakage

## Response Expectations

When a valid security report is received through a private channel, the team should:

1. Acknowledge receipt.
2. Triage severity and affected systems.
3. Contain and remediate as needed.
4. Coordinate disclosure only after the issue is fixed and safe to discuss.

## Organization Rule

`wminternal` repositories are private by default. Public repositories must not expose implementation details that materially increase risk.