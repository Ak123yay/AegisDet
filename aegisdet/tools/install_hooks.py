from __future__ import annotations

from pathlib import Path
import os
import stat
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
HOOKS = ROOT / ".githooks"


def run(*args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(args, cwd=ROOT, text=True, check=False)


def main() -> int:
    if not (ROOT / ".git").exists():
        print("Git is not initialized in the aegisdet folder.")
        print("Run: git init")
        print("Then rerun: python tools/install_hooks.py")
        return 1

    result = run("git", "config", "core.hooksPath", ".githooks")
    if result.returncode != 0:
        print("Failed to configure core.hooksPath.", file=sys.stderr)
        return result.returncode

    for hook in HOOKS.iterdir():
        if hook.is_file():
            hook.chmod(hook.stat().st_mode | stat.S_IEXEC)

    sync = run(sys.executable, "tools/workspace_sync.py", "sync", "--reason", "hook-install")
    if sync.returncode != 0:
        return sync.returncode

    print("AegisDet hooks installed.")
    print("Configured: git config core.hooksPath .githooks")
    print("Run: python tools/workspace_sync.py check")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
