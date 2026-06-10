#!/usr/bin/env python3
"""Validate YAML front-matter in all skill/*.md files."""
import sys
import re
from pathlib import Path

try:
    import yaml
except ImportError:
    print("ERROR: pyyaml not installed. Run: pip install pyyaml")
    sys.exit(1)

SKILL_DIR = Path(__file__).parent.parent / "skill"
REQUIRED_KEYS = {"name", "title", "type", "status", "sections"}
VALID_TYPES = {
    "router", "principles", "workflows", "dictionary",
    "voice", "data", "changelog", "state", "archive",
}
VALID_STATUSES = {"active", "skeleton", "archived"}

errors = []
warnings = []


def parse_frontmatter(text: str):
    """Return (meta_dict, body_text) or raise ValueError."""
    if not text.startswith("---"):
        raise ValueError("No front-matter found (file must start with ---)")
    end = text.index("\n---", 3)
    raw_yaml = text[3:end].strip()
    body = text[end + 4:].lstrip("\n")
    meta = yaml.safe_load(raw_yaml)
    if not isinstance(meta, dict):
        raise ValueError("Front-matter is not a YAML mapping")
    return meta, body


def extract_h2(body: str) -> list[str]:
    """Return ordered list of H2 heading texts (## stripped)."""
    headings = []
    for line in body.splitlines():
        m = re.match(r"^## (.+)$", line)
        if m:
            headings.append(m.group(1).strip())
    return headings


def check_file(path: Path) -> list[str]:
    file_errors = []
    text = path.read_text(encoding="utf-8")
    name = path.stem

    try:
        meta, body = parse_frontmatter(text)
    except (ValueError, yaml.YAMLError) as exc:
        file_errors.append(f"  [front-matter] {exc}")
        return file_errors

    # Required keys
    missing = REQUIRED_KEYS - meta.keys()
    if missing:
        file_errors.append(f"  [keys] Missing required keys: {sorted(missing)}")

    # name matches filename
    if meta.get("name") != name:
        file_errors.append(
            f"  [name] Expected '{name}', got '{meta.get('name')}'"
        )

    # type valid
    if meta.get("type") not in VALID_TYPES:
        file_errors.append(
            f"  [type] '{meta.get('type')}' not in {sorted(VALID_TYPES)}"
        )

    # status valid
    if meta.get("status") not in VALID_STATUSES:
        file_errors.append(
            f"  [status] '{meta.get('status')}' not in {sorted(VALID_STATUSES)}"
        )

    # sections matches actual H2 headings
    declared = meta.get("sections")
    if not isinstance(declared, list) or len(declared) == 0:
        file_errors.append("  [sections] Must be a non-empty list")
    else:
        actual = extract_h2(body)
        if declared != actual:
            # Show diff
            declared_set = set(declared)
            actual_set = set(actual)
            extra = declared_set - actual_set
            missing_h = actual_set - declared_set
            if extra:
                file_errors.append(
                    f"  [sections] In front-matter but NOT in body: {sorted(extra)}"
                )
            if missing_h:
                file_errors.append(
                    f"  [sections] In body but NOT in front-matter: {sorted(missing_h)}"
                )
            if declared != actual and not extra and not missing_h:
                file_errors.append(
                    f"  [sections] Order mismatch.\n"
                    f"    declared: {declared}\n"
                    f"    actual:   {actual}"
                )

    return file_errors


def main():
    md_files = sorted(SKILL_DIR.glob("*.md"))
    if not md_files:
        print(f"ERROR: No .md files found in {SKILL_DIR}")
        sys.exit(1)

    print(f"Checking {len(md_files)} files in {SKILL_DIR.relative_to(Path.cwd())} ...\n")

    all_ok = True
    for path in md_files:
        file_errors = check_file(path)
        if file_errors:
            all_ok = False
            print(f"FAIL  {path.name}")
            for e in file_errors:
                print(e)
        else:
            print(f"OK    {path.name}")

    print()
    if all_ok:
        print("All checks passed.")
        sys.exit(0)
    else:
        print("Some checks FAILED.")
        sys.exit(1)


if __name__ == "__main__":
    main()
