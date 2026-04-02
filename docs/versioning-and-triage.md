# Versioning And Triage

## Release Versioning

Use semantic versioning for the product:

- `MAJOR.MINOR.PATCH`
- Example: `v1.4.0`

Recommended interpretation:

- `MAJOR`: breaking or product-wide release changes
- `MINOR`: new features without breaking compatibility
- `PATCH`: bug-fix release

Examples:

- `v1.4.0`: feature release
- `v1.4.1`: bug-fix release
- `v1.4.2`: follow-up fix release

## Bug Tracking Fields

Every bug should capture these values:

- Found in version
- Fixed in version
- Last known working version
- Severity
- Product area
- Regression status

## Labels

Suggested status labels:

- `needs-triage`
- `confirmed`
- `in-progress`
- `fixed`
- `released`

Suggested severity labels:

- `critical`
- `high`
- `medium`
- `low`

Suggested area labels:

- `frontend`
- `backend`
- `api`
- `ai`
- `auth`
- `billing`
- `helpdesk`
- `dashboard`
- `filing`
- `documents`
- `settings`
- `infrastructure`

Special labels:

- `bug`
- `regression`

## Milestones

Create one milestone per release version.

Examples:

- `v1.4.1`
- `v1.4.2`
- `v1.5.0`

When a fix is planned for a release, assign the issue to that milestone.

## Bug ID Convention

Use a human-readable ID in the issue title.

Examples:

- `BUG-101: Dashboard compliance summary is misleading with zero properties`
- `BUG-102: Manual ticket creation does not refresh the board`
- `REGRESSION-014: Viewing stored quotes consumes usage`

## Triage Workflow

1. New issue is submitted with `needs-triage`.
2. Triage verifies whether the issue is reproducible.
3. Add severity and area labels.
4. Record the found version and last known working version.
5. Mark confirmed issues with `confirmed`.
6. Assign a milestone representing the target release.
7. Link the implementation PR when work starts.
8. Mark the issue `fixed` after merge.
9. Mark the issue `released` after deployment.
10. Record the fixed version in the issue body or comment history.

## Recommended Release Comment Template

When a bug is fixed, leave a comment like this:

```text
Fixed by PR #106.
Found in version: v1.4.0
Fixed in version: v1.4.1
Status: fixed
```

After deployment:

```text
Released to production in v1.4.1.
Status: released
```