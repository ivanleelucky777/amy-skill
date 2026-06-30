#!/usr/bin/env python3
"""Regenerate AUTO-FILELIST and AUTO-INDEX blocks in skill/router.md
from each skill file's YAML front-matter.

Markers in router.md:
  <!-- AUTO-FILELIST START --> ... <!-- AUTO-FILELIST END -->
  <!-- AUTO-INDEX START --> ... <!-- AUTO-INDEX END -->
"""
import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    print("ERROR: pyyaml not installed."); sys.exit(1)

SKILL_DIR = Path(__file__).parent.parent / "skill"
ROUTER_PATH = SKILL_DIR / "router.md"

STATUS_EMOJI = {"active": "🟢", "skeleton": "🟡", "archived": "🔵"}


def parse_frontmatter(text: str):
    if not text.startswith("---"):
        return None, text
    try:
        end = text.index("\n---", 3)
    except ValueError:
        return None, text
    raw = text[3:end].strip()
    try:
        return yaml.safe_load(raw), text[end + 4:].lstrip("\n")
    except yaml.YAMLError:
        return None, text


def load_all_metas() -> list[dict]:
    metas = []
    for path in sorted(SKILL_DIR.glob("*.md")):
        if path.name == "router.md":
            continue
        text = path.read_text(encoding="utf-8")
        meta, _ = parse_frontmatter(text)
        if meta and isinstance(meta, dict) and "file" in meta:
            meta["_path"] = path
            metas.append(meta)
    return metas


_DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")


def compute_latest_updated(metas: list[dict]) -> str:
    """router 自身日期 = 所有其他 skill 檔裡最新的 updated。
    updated 用 ISO YYYY-MM-DD,字串 max 即等於時間 max。
    無任何有效日期時 fall back 到建檔日 2026-05-29。
    """
    dates = [
        str(m["updated"])
        for m in metas
        if m.get("updated") and _DATE_RE.match(str(m["updated"]))
    ]
    return max(dates) if dates else "2026-05-29"


def build_filelist(metas: list[dict], latest: str) -> str:
    lines = [
        "<!-- AUTO-FILELIST START -->",
        "| 檔名 | 版本 | 更新日期 | 狀態 |",
        "|---|---|---|---|",
        # router.md itself first — 日期取所有其他檔的最新 updated
        f"| `router.md` | Agent v1.0 | {latest} | {STATUS_EMOJI['active']} active |",
    ]
    for m in metas:
        if m.get("status") == "archived":
            continue
        fname = m.get("file", m["_path"].name)
        ver = m.get("version", "—")
        upd = m.get("updated", "—")
        st = m.get("status", "active")
        emoji = STATUS_EMOJI.get(st, "⚪")
        lines.append(f"| `{fname}` | {ver} | {upd} | {emoji} {st} |")
    lines.append("<!-- AUTO-FILELIST END -->")
    return "\n".join(lines)


def build_index(metas: list[dict]) -> str:
    # Also include router.md provides
    router_text = ROUTER_PATH.read_text(encoding="utf-8")
    router_meta, _ = parse_frontmatter(router_text)

    rows = []
    all_metas = ([router_meta] if router_meta else []) + metas
    for m in all_metas:
        fname = m.get("file", "")
        for topic in m.get("provides", []):
            rows.append((topic, fname))

    lines = [
        "<!-- AUTO-INDEX START -->",
        "| 主題 | 查哪份檔 |",
        "|---|---|",
    ]
    for topic, fname in rows:
        lines.append(f"| {topic} | `{fname}` |")
    lines.append("<!-- AUTO-INDEX END -->")
    return "\n".join(lines)


FILELIST_RE = re.compile(
    r"<!-- AUTO-FILELIST START -->.*?<!-- AUTO-FILELIST END -->",
    re.DOTALL,
)
INDEX_RE = re.compile(
    r"<!-- AUTO-INDEX START -->.*?<!-- AUTO-INDEX END -->",
    re.DOTALL,
)


FM_UPDATED_RE = re.compile(r"(?m)^(updated:\s*).*$")


def set_router_frontmatter_updated(text: str, latest: str) -> str:
    """回寫 router 自身 front-matter 的 updated = latest(只動 front-matter 區塊)。"""
    if not text.startswith("---"):
        return text
    try:
        end = text.index("\n---", 3)
    except ValueError:
        return text
    head, rest = text[:end], text[end:]
    head = FM_UPDATED_RE.sub(rf"\g<1>'{latest}'", head, count=1)
    return head + rest


def update_router(filelist_block: str, index_block: str, latest: str):
    text = ROUTER_PATH.read_text(encoding="utf-8")

    if not FILELIST_RE.search(text):
        print("ERROR: AUTO-FILELIST markers not found in router.md")
        sys.exit(1)
    if not INDEX_RE.search(text):
        print("ERROR: AUTO-INDEX markers not found in router.md")
        sys.exit(1)

    text = FILELIST_RE.sub(filelist_block, text)
    text = INDEX_RE.sub(index_block, text)
    text = set_router_frontmatter_updated(text, latest)
    ROUTER_PATH.write_text(text, encoding="utf-8")


def main():
    print("gen_router.py: loading front-matter from skill/*.md ...")
    metas = load_all_metas()
    print(f"  Loaded {len(metas)} non-router files")

    latest = compute_latest_updated(metas)
    print(f"  router 自身 updated = 最新 {latest}")

    filelist = build_filelist(metas, latest)
    index = build_index(metas)

    update_router(filelist, index, latest)
    print("  router.md AUTO-FILELIST regenerated")
    print("  router.md AUTO-INDEX regenerated")
    print(f"  router.md front-matter updated → {latest}")
    print("Done.")


if __name__ == "__main__":
    main()
