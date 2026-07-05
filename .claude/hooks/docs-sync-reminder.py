#!/usr/bin/env python3
"""Stop hook: lembra de atualizar docs apos commit so-de-codigo."""
import json
import os
import subprocess
import sys

DOC_PREFIXES = ("docs/", ".junie/")
DOC_FILES = ("README.md", "Makefile")
CODE_PREFIXES = ("src/", "tests/")


def git(args, cwd):
    return subprocess.run(
        ["git"] + args, cwd=cwd, capture_output=True, text=True, timeout=5
    )


def main() -> int:
    try:
        data = json.load(sys.stdin)
    except (json.JSONDecodeError, ValueError):
        return 0

    if data.get("stop_hook_active"):
        return 0

    root = os.environ.get("CLAUDE_PROJECT_DIR") or os.getcwd()
    top = git(["rev-parse", "--show-toplevel"], root)
    if top.returncode != 0:
        return 0
    root = top.stdout.strip()

    head = git(["rev-parse", "HEAD"], root).stdout.strip()
    if not head:
        return 0

    marker = os.path.join(root, ".git", ".docs-sync-nudged")
    try:
        if open(marker, "r", encoding="utf-8").read().strip() == head:
            return 0
    except OSError:
        pass

    changed = git(
        ["diff-tree", "--no-commit-id", "--name-only", "-r", "--root", "HEAD"], root
    )
    if changed.returncode != 0:
        return 0
    files = [f for f in changed.stdout.splitlines() if f.strip()]
    if not files:
        return 0

    touched_code = any(f.startswith(CODE_PREFIXES) for f in files)
    touched_docs = any(f.startswith(DOC_PREFIXES) or f in DOC_FILES for f in files)

    if touched_code and not touched_docs:
        try:
            with open(marker, "w", encoding="utf-8") as fh:
                fh.write(head)
        except OSError:
            pass
        subject = git(["log", "-1", "--pretty=%s"], root).stdout.strip()
        reason = (
            f"O ultimo commit ('{subject}') tocou codigo mas nenhum documento. "
            "Se a mudanca afetou stack, arquitetura, comandos (Makefile) ou "
            "aprendizado, ofereca atualizar a documentacao (em commit separado). "
            "Se nao se aplica, apenas confirme e finalize."
        )
        print(json.dumps({"decision": "block", "reason": reason}))

    return 0


if __name__ == "__main__":
    sys.exit(main())
