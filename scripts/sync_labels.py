#!/usr/bin/env python3

import argparse
import json
import os
import shutil
import subprocess
import sys
import urllib.error
import urllib.parse
import urllib.request


API_ROOT = "https://api.github.com"


def parse_args():
    parser = argparse.ArgumentParser(description="Sync GitHub labels from a labels.json file.")
    parser.add_argument("--repo", required=True, help="GitHub repository in owner/name format")
    parser.add_argument("--labels-file", default="labels.json", help="Path to labels json file")
    parser.add_argument("--dry-run", action="store_true", help="Print changes without applying them")
    return parser.parse_args()


def build_request(url, token, method="GET", payload=None):
    headers = {
        "Accept": "application/vnd.github+json",
        "Authorization": f"Bearer {token}",
        "X-GitHub-Api-Version": "2022-11-28",
        "User-Agent": "ezeala-product-bug-label-sync",
    }
    data = None
    if payload is not None:
        data = json.dumps(payload).encode("utf-8")
        headers["Content-Type"] = "application/json"
    return urllib.request.Request(url, data=data, headers=headers, method=method)


def github_request(url, token, method="GET", payload=None):
    request = build_request(url, token, method=method, payload=payload)
    with urllib.request.urlopen(request) as response:
        body = response.read().decode("utf-8")
        if not body:
            return None
        return json.loads(body)


def load_labels(path):
    with open(path, "r", encoding="utf-8") as handle:
        data = json.load(handle)
    if not isinstance(data, list):
        raise ValueError("labels file must contain a JSON array")
    return data


def get_existing_labels(repo, token):
    labels = []
    page = 1
    while True:
        query = urllib.parse.urlencode({"per_page": 100, "page": page})
        url = f"{API_ROOT}/repos/{repo}/labels?{query}"
        page_items = github_request(url, token)
        if not page_items:
            break
        labels.extend(page_items)
        if len(page_items) < 100:
            break
        page += 1
    return {item["name"]: item for item in labels}


def ensure_token():
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        return token

    gh_path = shutil.which("gh")
    if gh_path:
        result = subprocess.run(
            [gh_path, "auth", "token"],
            check=False,
            capture_output=True,
            text=True,
        )
        if result.returncode == 0:
            gh_token = result.stdout.strip()
            if gh_token:
                return gh_token

    raise RuntimeError("Authentication required. Set GITHUB_TOKEN or login via `gh auth login`.")


def sync_labels(repo, labels_file, dry_run):
    token = ensure_token()
    desired_labels = load_labels(labels_file)
    existing_labels = get_existing_labels(repo, token)

    created = 0
    updated = 0
    skipped = 0

    for label in desired_labels:
        name = label["name"]
        desired_color = label["color"].lower().lstrip("#")
        desired_description = label.get("description") or ""
        current = existing_labels.get(name)

        if current is None:
            print(f"CREATE {name}")
            if not dry_run:
                github_request(
                    f"{API_ROOT}/repos/{repo}/labels",
                    token,
                    method="POST",
                    payload={
                        "name": name,
                        "color": desired_color,
                        "description": desired_description,
                    },
                )
            created += 1
            continue

        current_color = (current.get("color") or "").lower().lstrip("#")
        current_description = current.get("description") or ""

        if current_color == desired_color and current_description == desired_description:
            print(f"SKIP   {name}")
            skipped += 1
            continue

        print(f"UPDATE {name}")
        if not dry_run:
            github_request(
                f"{API_ROOT}/repos/{repo}/labels/{urllib.parse.quote(name, safe='')}",
                token,
                method="PATCH",
                payload={
                    "new_name": name,
                    "color": desired_color,
                    "description": desired_description,
                },
            )
        updated += 1

    print(f"\nSummary: created={created}, updated={updated}, skipped={skipped}, dry_run={dry_run}")


def main():
    args = parse_args()
    try:
        sync_labels(args.repo, args.labels_file, args.dry_run)
    except FileNotFoundError as exc:
        print(f"File not found: {exc}", file=sys.stderr)
        return 1
    except urllib.error.HTTPError as exc:
        error_body = exc.read().decode("utf-8", errors="replace")
        print(f"GitHub API error {exc.code}: {error_body}", file=sys.stderr)
        return 1
    except Exception as exc:
        print(str(exc), file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())