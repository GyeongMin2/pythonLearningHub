#!/usr/bin/env python3
"""Backdate local Git commits from commit_history.json.

Usage:
  python make_commits.py --dry-run
  python make_commits.py
"""

from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
from collections import Counter
from datetime import datetime
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent
HISTORY_PATH = REPO_ROOT / "commit_history.json"
TARGET_EMAIL = "kgmksw@naver.com"
KST_OFFSET = "+0900"
SAMPLE_COUNT = 5


def run_git(args: list[str], env: dict[str, str] | None = None) -> str:
    """Run a git command and return stdout. Exit clearly on failure."""
    merged_env = os.environ.copy()
    if env:
        merged_env.update(env)
    result = subprocess.run(
        ["git", *args],
        cwd=REPO_ROOT,
        env=merged_env,
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        stderr = (result.stderr or "").strip()
        stdout = (result.stdout or "").strip()
        detail = stderr or stdout or "(no output)"
        print(f"[ERROR] git {' '.join(args)} failed (exit {result.returncode}): {detail}", file=sys.stderr)
        sys.exit(result.returncode)
    return (result.stdout or "").strip()


def git_config_value(key: str) -> str:
    result = subprocess.run(
        ["git", "config", "--get", key],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        return ""
    return (result.stdout or "").strip()


def resolve_author_name() -> str:
    configured = git_config_value("user.name")
    if configured:
        return configured
    return "GyeongMin"


def print_identity_check(author_name: str) -> None:
    config_email = git_config_value("user.email")
    config_name = git_config_value("user.name")
    print("=== Current git config ===")
    print(f"  user.name  = {config_name or '(not set)'}")
    print(f"  user.email = {config_email or '(not set)'}")
    print(f"  target email for commits = {TARGET_EMAIL}")
    print(f"  author/committer name for commits = {author_name}")
    if config_email != TARGET_EMAIL:
        print(
            f"[WARN] git config user.email ({config_email or 'empty'}) "
            f"differs from target {TARGET_EMAIL}. "
            "Commits will still use the target email via GIT_AUTHOR_EMAIL / GIT_COMMITTER_EMAIL."
        )
    else:
        print("[OK] git config user.email matches the target email.")
    print()


def parse_date(date_str: str) -> datetime:
    # Accept "YYYY-MM-DDTHH:MM:SS" (and optional timezone already present)
    cleaned = date_str.strip()
    if cleaned.endswith("Z"):
        cleaned = cleaned[:-1]
    # Strip trailing offset if present so we can attach +0900 ourselves for git
    for sep in ("+", "-"):
        # Look for offset after the date portion (index > 10)
        idx = cleaned.find(sep, 10)
        if idx != -1 and "T" in cleaned[:idx]:
            cleaned = cleaned[:idx].rstrip()
            break
    return datetime.strptime(cleaned, "%Y-%m-%dT%H:%M:%S")


def format_git_date(date_str: str) -> str:
    dt = parse_date(date_str)
    return f"{dt.strftime('%Y-%m-%dT%H:%M:%S')} {KST_OFFSET}"


def load_history() -> list[dict]:
    if not HISTORY_PATH.is_file():
        print(
            f"[ERROR] {HISTORY_PATH.name} not found at repo root ({HISTORY_PATH}). "
            "Create it before running this script.",
            file=sys.stderr,
        )
        sys.exit(1)
    with HISTORY_PATH.open(encoding="utf-8") as f:
        data = json.load(f)
    if not isinstance(data, list):
        print("[ERROR] commit_history.json must be a JSON array.", file=sys.stderr)
        sys.exit(1)
    return data


def print_statistics(entries: list[dict]) -> None:
    if not entries:
        print("=== Statistics ===")
        print("  No commits in history.")
        print()
        return

    total = len(entries)
    day_counts: Counter[str] = Counter()
    month_counts: Counter[str] = Counter()
    seen_paths: set[str] = set()
    new_file_ops = 0
    modify_ops = 0

    for entry in entries:
        dt = parse_date(entry["date"])
        day_counts[dt.strftime("%Y-%m-%d")] += 1
        month_counts[dt.strftime("%Y-%m")] += 1
        files = entry.get("files") or {}
        if isinstance(files, dict):
            paths = files.keys()
        else:
            paths = files
        for path in paths:
            if path in seen_paths:
                modify_ops += 1
            else:
                new_file_ops += 1
                seen_paths.add(path)

    active_days = len(day_counts)
    avg_per_day = total / active_days if active_days else 0.0
    first_date = parse_date(entries[0]["date"]).strftime("%Y-%m-%d")
    last_date = parse_date(entries[-1]["date"]).strftime("%Y-%m-%d")
    file_ops = new_file_ops + modify_ops
    new_ratio = (new_file_ops / file_ops * 100) if file_ops else 0.0
    mod_ratio = (modify_ops / file_ops * 100) if file_ops else 0.0

    print("=== Statistics ===")
    print(f"  Total commits     : {total}")
    print(f"  Active days       : {active_days}")
    print(f"  Avg commits/day   : {avg_per_day:.2f}")
    print(f"  First date        : {first_date}")
    print(f"  Last date         : {last_date}")
    print(f"  New-file ops      : {new_file_ops} ({new_ratio:.1f}%)")
    print(f"  Modify ops        : {modify_ops} ({mod_ratio:.1f}%)")
    print("  Commits per month :")
    for month in sorted(month_counts):
        print(f"    {month}: {month_counts[month]}")
    print()


def print_samples(entries: list[dict], count: int = SAMPLE_COUNT) -> None:
    print(f"=== Sample entries (up to {count}) ===")
    if not entries:
        print("  (none)")
        print()
        return
    for i, entry in enumerate(entries[:count]):
        files = entry.get("files") or {}
        if isinstance(files, dict):
            paths = list(files.keys())
        else:
            paths = list(files)
        print(f"  [{i + 1}] date={entry.get('date')}")
        print(f"      message={entry.get('message')}")
        print(f"      files={paths}")
    if len(entries) > count:
        print(f"  ... and {len(entries) - count} more")
    print()


def write_files(files: dict[str, str]) -> list[str]:
    written: list[str] = []
    for rel_path, content in files.items():
        path = REPO_ROOT / rel_path
        path.parent.mkdir(parents=True, exist_ok=True)
        if not isinstance(content, str):
            content = "" if content is None else str(content)
        path.write_text(content, encoding="utf-8")
        written.append(rel_path)
    return written


def commit_entry(entry: dict, author_name: str) -> None:
    files = entry.get("files")
    if not isinstance(files, dict) or not files:
        print(f"[ERROR] Entry missing non-empty files dict: {entry!r}", file=sys.stderr)
        sys.exit(1)
    message = entry.get("message")
    if not message:
        print(f"[ERROR] Entry missing message: {entry!r}", file=sys.stderr)
        sys.exit(1)
    date_str = entry.get("date")
    if not date_str:
        print(f"[ERROR] Entry missing date: {entry!r}", file=sys.stderr)
        sys.exit(1)

    paths = write_files(files)
    run_git(["add", "--", *paths])

    git_date = format_git_date(date_str)
    env = {
        "GIT_AUTHOR_DATE": git_date,
        "GIT_COMMITTER_DATE": git_date,
        "GIT_AUTHOR_NAME": author_name,
        "GIT_AUTHOR_EMAIL": TARGET_EMAIL,
        "GIT_COMMITTER_NAME": author_name,
        "GIT_COMMITTER_EMAIL": TARGET_EMAIL,
    }
    run_git(["commit", "-m", message], env=env)


def main() -> None:
    parser = argparse.ArgumentParser(description="Create backdated commits from commit_history.json")
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print stats and sample entries only; do not write files or commit",
    )
    args = parser.parse_args()

    author_name = resolve_author_name()
    print_identity_check(author_name)

    entries = load_history()
    print_statistics(entries)

    if args.dry_run:
        print_samples(entries)
        print("[dry-run] No files written, no git commits created.")
        return

    print(f"Creating {len(entries)} commits...")
    for i, entry in enumerate(entries, start=1):
        commit_entry(entry, author_name)
        if i % 25 == 0 or i == len(entries):
            print(f"  Progress: {i}/{len(entries)}")

    print("Done. Commits created locally only (no push).")


if __name__ == "__main__":
    main()
