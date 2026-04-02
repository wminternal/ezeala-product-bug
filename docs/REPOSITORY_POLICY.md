# Repository Visibility Policy

## Purpose

This document defines how the `wminternal` GitHub organization separates public and private repositories.

## Default Rule

All repositories are private by default.

Repositories may only be made public when they are explicitly approved for external visibility and contain no sensitive implementation details.

## Public Repositories

Public repositories are allowed only for intentionally external-facing assets, such as:

- public bug tracking
- public documentation
- approved open-source utilities
- approved developer-facing examples or assets

Public repositories must not contain:

- product source code not intended for disclosure
- infrastructure configuration
- internal runbooks
- customer or tenant data
- secrets, credentials, or tokens
- internal escalation contacts
- unreleased security-sensitive architecture details

Example public repository:

- `wminternal/ezeala-product-bug`

## Private Repositories

Private repositories must be used for:

- application source code
- backend services and APIs
- CI/CD configuration
- infrastructure and deployment automation
- internal scripts and operations tooling
- architecture diagrams and private runbooks
- cloud account, IAM, networking, and vendor integration material

Example private repository:

- `wminternal/EzeAla`

## Bug Tracking Rule

Public bug intake should go to the public bug repository.

Private engineering detail should stay in private repositories, internal issues, PRs, or operational notes.

## Approval Rule For Public Visibility

Before making any repository public, confirm:

1. No secrets exist in the current files.
2. No sensitive information exists in git history.
3. The repository has a clear README.
4. Security reporting is redirected to a private path.
5. The repository has a named maintainer or owning team.
6. The repository provides clear external value by being public.

## One-Line Standard

`wminternal` repositories are private by default; only explicitly approved external-facing repositories may be public.