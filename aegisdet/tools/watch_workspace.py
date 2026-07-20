from __future__ import annotations

import argparse
import hashlib
from pathlib import Path
import subprocess
import sys
import time

ROOT = Path(__file__).resolve().parents[1]
WATCH_DIRS = ("src", "scripts", "tests", "configs", "apps", "docs", ".github")
EXCLUDE = {"__pycache__", ".pytest_cache", ".mypy_cache", ".ruff_cache"}


def snapshot() -> str:
    digest = hashlib.sha256()
    for name in WATCH_DIRS:
        base = ROOT / name
        if not base.exists():
            continue
        for p in sorted(base.rglob("*")):
            if not p.is_file() or any(part in EXCLUDE for part in p.parts) or p.suffix == ".pyc":
                continue
            stat = p.stat()
            digest.update(p.relative_to(ROOT).as_posix().encode())
            digest.update(str(stat.st_mtime_ns).encode())
            digest.update(str(stat.st_size).encode())
    return digest.hexdigest()


def sync(reason: str) -> None:
    subprocess.run(
        [sys.executable, "tools/workspace_sync.py", "sync", "--reason", reason],
        cwd=ROOT,
        check=False,
    )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--interval", type=float, default=2.0)
    args = parser.parse_args()

    previous = snapshot()
    sync("watcher-start")
    print("AegisDet watcher active. Press Ctrl+C to stop.")
    try:
        while True:
            time.sleep(args.interval)
            current = snapshot()
            if current != previous:
                previous = current
                sync("file-change")
    except KeyboardInterrupt:
        print("AegisDet watcher stopped.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
