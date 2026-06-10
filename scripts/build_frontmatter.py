#!/usr/bin/env python3
"""Prepend YAML front-matter to every skill/*.md file.

Run once to build; idempotent (strips existing front-matter first).
"""
import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    print("ERROR: pyyaml not installed."); sys.exit(1)

SKILL_DIR = Path(__file__).parent.parent / "skill"

# Per-file metadata (type + status).
# Sections are extracted live from the file body.
FILE_META = {
    "account_health":    {"type": "state",      "status": "active"},
    "active_constraints":{"type": "state",      "status": "active"},
    "archive_README":    {"type": "archive",     "status": "archived"},
    "changelog":         {"type": "changelog",   "status": "active"},
    "data":              {"type": "data",        "status": "active"},
    "dictionary":        {"type": "dictionary",  "status": "active"},
    "performance_log":   {"type": "state",       "status": "active"},
    "principles":        {"type": "principles",  "status": "active"},
    "router":            {"type": "router",      "status": "active"},
    "voice":             {"type": "voice",       "status": "skeleton"},
    "workflows":         {"type": "workflows",   "status": "active"},
}


def strip_frontmatter(text: str) -> str:
    """Remove existing YAML front-matter block if present."""
    if text.startswith("---"):
        try:
            end = text.index("\n---", 3)
            return text[end + 4:].lstrip("\n")
        except ValueError:
            pass
    return text


def extract_h1(body: str) -> str:
    for line in body.splitlines():
        m = re.match(r"^# (.+)$", line)
        if m:
            return m.group(1).strip()
    return ""


def extract_h2(body: str) -> list:
    headings = []
    for line in body.splitlines():
        m = re.match(r"^## (.+)$", line)
        if m:
            headings.append(m.group(1).strip())
    return headings


def build_frontmatter(name: str, title: str, ftype: str, status: str,
                      sections: list) -> str:
    meta = {
        "name": name,
        "title": title,
        "type": ftype,
        "status": status,
        "sections": sections,
    }
    return "---\n" + yaml.dump(
        meta,
        allow_unicode=True,
        default_flow_style=False,
        sort_keys=False,
        width=120,
    ).rstrip() + "\n---\n\n"


def process(path: Path):
    text = path.read_text(encoding="utf-8")
    body = strip_frontmatter(text)
    name = path.stem
    if name not in FILE_META:
        print(f"  SKIP (not in FILE_META): {path.name}")
        return
    info = FILE_META[name]
    title = extract_h1(body)
    sections = extract_h2(body)
    fm = build_frontmatter(name, title, info["type"], info["status"], sections)
    path.write_text(fm + body, encoding="utf-8")
    print(f"  OK   {path.name}  ({len(sections)} sections)")


def main():
    print(f"Building front-matter for files in {SKILL_DIR} ...\n")
    for path in sorted(SKILL_DIR.glob("*.md")):
        process(path)
    print("\nDone.")


if __name__ == "__main__":
    main()
