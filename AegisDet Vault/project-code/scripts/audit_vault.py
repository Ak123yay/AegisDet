from __future__ import annotations

import argparse
import py_compile
import re
import subprocess
import sys
from collections import Counter, defaultdict
from pathlib import Path

REQUIRED = [
    "START_HERE.md", "TASKS.md", "CURRENT_STATE.md", "PROJECT_CONTEXT.md",
    "CONTEXT_LOCK.md", "FOUNDATION_MODEL.md", "DOMAIN_LOCK.md", "BUILD_PATH.md",
    "AGENTS.md", "wiki/_master-index.md", "wiki/_code-map.md",
]
PLACEHOLDERS = [
    "Record the exact dataset version and model configuration",
    "Define the hypothesis or purpose",
    "Summary\n" + "Build Order.",
]

def resolve_links(root: Path, markdown_files: list[Path]):
    exact = {p.relative_to(root).with_suffix("").as_posix(): p for p in markdown_files}
    stems: dict[str, list[Path]] = defaultdict(list)
    for p in markdown_files:
        stems[p.stem.lower()].append(p)
    unresolved, ambiguous = [], []
    total = 0
    for p in markdown_files:
        text = p.read_text(encoding="utf-8", errors="replace")
        for raw in re.findall(r"\[\[([^\]]+)\]\]", text):
            total += 1
            target = raw.split("|", 1)[0].split("#", 1)[0].strip().removesuffix(".md").replace("\\", "/")
            if not target:
                continue
            candidates = []
            keys = [target, f"wiki/{target}", (p.parent.relative_to(root) / target).as_posix()]
            for key in keys:
                if key in exact:
                    candidates.append(exact[key])
            if not candidates:
                candidates = stems.get(Path(target).name.lower(), [])
            candidates = list(dict.fromkeys(candidates))
            if not candidates:
                unresolved.append((p.relative_to(root).as_posix(), raw))
            elif len(candidates) > 1:
                ambiguous.append((p.relative_to(root).as_posix(), raw, [x.relative_to(root).as_posix() for x in candidates]))
    return total, unresolved, ambiguous

def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[2])
    args = parser.parse_args()
    root = args.root.resolve()
    markdown = sorted(root.rglob("*.md"))
    files = [p for p in root.rglob("*") if p.is_file()]
    dirs = [p for p in root.rglob("*") if p.is_dir()]
    missing = [x for x in REQUIRED if not (root / x).exists()]
    tiny = [p.relative_to(root).as_posix() for p in markdown if p.stat().st_size < 180]
    placeholder_hits = []
    for p in markdown:
        text = p.read_text(encoding="utf-8", errors="replace")
        if any(marker in text for marker in PLACEHOLDERS):
            placeholder_hits.append(p.relative_to(root).as_posix())
    total_links, unresolved, ambiguous = resolve_links(root, markdown)
    stems = defaultdict(list)
    for p in markdown:
        stems[p.stem.lower()].append(p.relative_to(root).as_posix())
    duplicate_stems = {k: v for k, v in stems.items() if len(v) > 1 and k != "readme"}

    python_files = sorted((root / "project-code").rglob("*.py"))
    compile_errors = []
    for p in python_files:
        try:
            py_compile.compile(str(p), doraise=True)
        except Exception as exc:
            compile_errors.append((p.relative_to(root).as_posix(), repr(exc)))

    test = subprocess.run(
        [sys.executable, "-m", "unittest", "discover", "-s", "tests", "-v"],
        cwd=root / "project-code", env={**dict(__import__("os").environ), "PYTHONPATH": "src"},
        text=True, capture_output=True,
    )

    checks = {
        "required control files": not missing,
        "at least 175 markdown files": len(markdown) >= 175,
        "no unresolved links": not unresolved,
        "no ambiguous links": not ambiguous,
        "no non-README duplicate stems": not duplicate_stems,
        "no notes under 180 bytes": not tiny,
        "no legacy placeholder boilerplate": not placeholder_hits,
        "python syntax compiles": not compile_errors,
        "unit tests pass": test.returncode == 0,
        "vault root is AegisDet Vault": root.name == "AegisDet Vault",
    }
    passed = all(checks.values())
    report = [
        "# VAULT AUDIT", "", f"- Root: `{root.name}`", f"- Markdown files: {len(markdown)}",
        f"- Total files: {len(files)}", f"- Directories: {len(dirs)}", f"- Obsidian links: {total_links}",
        f"- Python files: {len(python_files)}", f"- Overall: **{'PASS' if passed else 'FAIL'}**", "", "## Checks", "",
    ]
    for name, ok in checks.items():
        report.append(f"- [{'x' if ok else ' '}] {name}")
    details = {
        "Missing required files": missing,
        "Tiny notes under 180 bytes": tiny,
        "Legacy placeholder hits": placeholder_hits,
        "Unresolved links": unresolved,
        "Ambiguous links": ambiguous,
        "Duplicate stems": duplicate_stems,
        "Python compile errors": compile_errors,
    }
    for heading, values in details.items():
        report += ["", f"## {heading}", ""]
        if values:
            for value in values[:200]:
                report.append(f"- `{value}`")
        else:
            report.append("- None")
    report += ["", "## Unit-test output", "", "```text", (test.stdout + test.stderr).strip(), "```", "",
               "## Interpretation", "",
               "A PASS means the vault and starter code are internally consistent. It does not mean model experiments have been completed or that AegisDet has beaten its baseline."]
    output = root / "output" / "VAULT_AUDIT.md"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text("\n".join(report) + "\n", encoding="utf-8")
    print("\n".join(report[:30]))
    print(f"\nFull report: {output}")
    return 0 if passed else 1

if __name__ == "__main__":
    raise SystemExit(main())
