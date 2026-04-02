# ezeala-product-bug

Public bug-tracking repository for EzeAla product issues.

This repository is intentionally separate from the private application codebase. It is used to capture product bugs, regressions, release impact, and fix status without exposing internal source code.

## What To Report Here

- Product bugs
- Regressions
- Production incidents that affect end users
- UI, API, AI, workflow, and data consistency issues

## What Not To Report Here

- Security vulnerabilities
- Secrets, credentials, or customer-sensitive data
- General feature requests unless the team explicitly asks for them here

For security issues, use a private support or security contact path instead of filing a public issue.

## Reporting A Bug

1. Open the Issues tab.
2. Choose the appropriate issue form.
3. Fill in the reproduction steps, expected behavior, actual behavior, and version details.
4. Submit the issue.

## Tracking Model

Each issue should capture:

- Found in version
- Fixed in version
- Severity
- Area
- Regression status

Recommended release version format:

- `v1.4.0` for feature releases
- `v1.4.1` for bug-fix releases
- `v1.4.2` for follow-up fixes

Recommended issue title format:

- `BUG-104: Manual ticket creation does not appear on the board immediately`

## Workflow

1. New issues start with `needs-triage`.
2. Triage adds severity, area, and found-version details.
3. Confirmed bugs get the `confirmed` label.
4. Active work gets the `in-progress` label and linked PR.
5. Merged fixes get the `fixed` label.
6. Deployed fixes get the `released` label and a `fixed in version` value.

## Repository Contents

- `.github/ISSUE_TEMPLATE/bug-report.yml`: standard product bug form
- `.github/ISSUE_TEMPLATE/regression-report.yml`: regression-focused form
- `.github/ISSUE_TEMPLATE/config.yml`: GitHub issue form configuration
- `SECURITY.md`: public security reporting guidance
- `docs/versioning-and-triage.md`: release, versioning, and triage process
- `docs/REPOSITORY_POLICY.md`: public/private repository visibility policy
- `docs/public-repo-checklist.md`: approval checklist for public repositories
- `labels.json`: suggested GitHub label import manifest
- `scripts/sync_labels.py`: sync labels from `labels.json` to GitHub

## Sync Labels To GitHub

Use the included script to create or update labels in the GitHub repository.

Requirements:

- `python3`
- either GitHub CLI authenticated with `gh auth login`, or a `GITHUB_TOKEN`

Optional flags:

- `--labels-file labels.json`
- `--dry-run`

The script will:

- create labels that do not exist
- update labels whose color or description differ
- leave unrelated labels untouched

## Suggested Next Steps

1. Create a new GitHub repository named `ezeala-product-bug`.
2. Push this folder as its own repository.
3. Enable GitHub Issues.
4. Import labels from `labels.json` using GitHub CLI or a label sync tool.
5. Create milestones for upcoming releases such as `v1.4.1` and `v1.4.2`.