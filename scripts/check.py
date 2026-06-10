#!/usr/bin/env python3
"""Validate skill/*.md files — three checks:
  1. Front-matter completeness  (file, version, updated, status, provides, sections)
  2. Cross-file section references exist in target file's sections list
  3. retired.yml blacklist — no retired terms in active skill files
"""
import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    print("ERROR: pyyaml not installed."); sys.exit(1)

REPO_ROOT = Path(__file__).parent.parent
SKILL_DIR = REPO_ROOT / "skill"
RETIRED_YAML = REPO_ROOT / "retired.yml"

REQUIRED_KEYS = {"file", "version", "updated", "status", "provides", "sections"}
VALID_STATUSES = {"active", "skeleton", "archived"}

# Files where blacklist warnings are suppressed (they document retired rules)
BLACKLIST_EXEMPT = {"router.md", "changelog.md", "archive_README.md"}

# Cross-reference pattern: `filename.md` followed by KEYWORD IDENTIFIER.
# The middle part must NOT contain | (table cell boundary) or another backtick,
# which would mean the KEYWORD belongs to a different cell / a different reference.
XREF_RE = re.compile(
    r"`([\w_/]+\.md)`[^`\n\|]{0,60}?"
    r"\b(SECTION|PART|鐵則|原則|表|附錄|學習)\s+"
    r"([\w\-]+)",
    re.UNICODE,
)

# ── helpers ─────────────────────────────────────────────────────────────────

def parse_frontmatter(text: str):
    """Return (meta_dict, body) or (None, text) on failure."""
    if not text.startswith("---"):
        return None, text
    try:
        end = text.index("\n---", 3)
    except ValueError:
        return None, text
    try:
        meta = yaml.safe_load(text[3:end].strip())
    except yaml.YAMLError as exc:
        return f"YAML parse error: {exc}", text
    if not isinstance(meta, dict):
        return "front-matter is not a mapping", text
    return meta, text[end + 4:].lstrip("\n")


def load_all(skill_dir: Path) -> dict[str, tuple]:
    """Return {filename: (meta, body)} for all .md in skill_dir."""
    result = {}
    for path in sorted(skill_dir.glob("*.md")):
        text = path.read_text(encoding="utf-8")
        meta, body = parse_frontmatter(text)
        result[path.name] = (meta, body, path)
    return result


# ── Check 1: front-matter completeness ──────────────────────────────────────

def check1_frontmatter(fname: str, meta, body: str) -> list[str]:
    errs = []
    if meta is None:
        return [f"  [FM] No front-matter (must start with ---)"]
    if isinstance(meta, str):
        return [f"  [FM] {meta}"]

    missing = REQUIRED_KEYS - meta.keys()
    if missing:
        errs.append(f"  [FM] Missing keys: {sorted(missing)}")

    if meta.get("file") != fname:
        errs.append(f"  [FM] 'file' should be '{fname}', got '{meta.get('file')}'")

    if meta.get("status") not in VALID_STATUSES:
        errs.append(f"  [FM] Invalid status '{meta.get('status')}'; valid: {sorted(VALID_STATUSES)}")

    if not isinstance(meta.get("provides"), list) or not meta.get("provides"):
        errs.append("  [FM] 'provides' must be a non-empty list")

    if not isinstance(meta.get("sections"), list):
        errs.append("  [FM] 'sections' must be a list (may be empty for archive files)")

    return errs


# ── Check 2: cross-file section references ───────────────────────────────────

def check2_xrefs(fname: str, body: str, all_files: dict) -> list[str]:
    errs = []
    for m in XREF_RE.finditer(body):
        ref_file = m.group(1)
        keyword = m.group(2)
        sec_id = m.group(3)
        section_str = f"{keyword} {sec_id}"

        # Resolve filename: strip leading path component if present (e.g. state/)
        bare = Path(ref_file).name
        if bare not in all_files:
            # File not tracked — skip silently (may be cases/ etc.)
            continue

        target_meta, _, _ = all_files[bare]
        if not isinstance(target_meta, dict):
            continue  # skip broken files (already flagged in check1)

        target_sections = target_meta.get("sections", [])
        if not isinstance(target_sections, list):
            continue

        # Build candidates to check:
        #   "PART H-4" → ["PART H-4", "H-4"]
        #   "表 3-6"   → ["表 3-6", "表 3", "3-6", "3"]  (numeric range: accept if start matches)
        candidates = [section_str, sec_id]
        m_range = re.match(r"^(\d+)-(\d+)$", sec_id)
        if m_range:
            start = m_range.group(1)
            candidates += [f"{keyword} {start}", start]

        if not any(c in target_sections for c in candidates):
            errs.append(
                f"  [XREF] {fname} → `{ref_file}` {section_str}"
                f" not found in {bare} sections"
            )
    return errs


# ── Check 3: retired.yml blacklist ───────────────────────────────────────────

def load_retired() -> list[str]:
    if not RETIRED_YAML.exists():
        return []
    with RETIRED_YAML.open(encoding="utf-8") as f:
        data = yaml.safe_load(f)
    if not data or "retired" not in data:
        return []
    return [str(r.get("term", r)) if isinstance(r, dict) else str(r)
            for r in data["retired"]]


def check3_blacklist(fname: str, body: str, retired_terms: list[str]) -> list[str]:
    if fname in BLACKLIST_EXEMPT:
        return []
    # Signals that a line is documenting (not using) a retired rule
    SUPPRESS = ("推翻", "已推翻", "已廢除", "廢除", "不採用", "撤回",
                "誤用", "謹慎", "被誤用", "無效", "無業界", "已整合")
    errs = []
    for term in retired_terms:
        if term not in body:
            continue
        for i, line in enumerate(body.splitlines(), 1):
            if term in line and not any(s in line for s in SUPPRESS):
                errs.append(f"  [RETIRED] '{term}' found at line ~{i}")
                break  # one report per term per file
    return errs


# ── Main ─────────────────────────────────────────────────────────────────────

def main():
    all_files = load_all(SKILL_DIR)
    retired_terms = load_retired()

    if not all_files:
        print(f"ERROR: no .md files in {SKILL_DIR}"); sys.exit(1)

    print(f"Checking {len(all_files)} files in {SKILL_DIR.relative_to(Path.cwd())} ...\n")
    if retired_terms:
        print(f"  Retired blacklist: {len(retired_terms)} terms loaded\n")

    all_ok = True
    for fname, (meta, body, path) in all_files.items():
        file_errs = []
        file_errs += check1_frontmatter(fname, meta, body)
        file_errs += check2_xrefs(fname, body, all_files)
        file_errs += check3_blacklist(fname, body, retired_terms)

        if file_errs:
            all_ok = False
            print(f"FAIL  {fname}")
            for e in file_errs:
                print(e)
        else:
            print(f"OK    {fname}")

    print()
    if all_ok:
        print("All checks passed.")
        sys.exit(0)
    else:
        print("Some checks FAILED.")
        sys.exit(1)


if __name__ == "__main__":
    main()
