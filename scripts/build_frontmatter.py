#!/usr/bin/env python3
"""Rewrite front-matter for all skill/*.md files to match spec:
   file, version, updated, status, provides, sections
"""
import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    print("ERROR: pyyaml not installed."); sys.exit(1)

SKILL_DIR = Path(__file__).parent.parent / "skill"

# sections = identifiers that can be cross-referenced from OTHER files,
# formatted exactly as they appear after "filename.md " in the body text.
FILE_META = {
    "account_health": {
        "version": "1.0",
        "updated": "2026-05-29",
        "status": "active",
        "provides": ["帳號健康度", "略過率監測", "IG健康度", "週快照"],
        "sections": ["本週快照", "每週監測 SOP", "歷史紀錄", "趨勢分析", "本檔維護 SOP"],
    },
    "active_constraints": {
        "version": "1.0",
        "updated": "2026-05-29",
        "status": "active",
        "provides": ["當前接案限制", "廠商例外指令", "業配暫停機制"],
        "sections": ["PART A", "PART B", "PART C", "接案前必查清單"],
    },
    "archive_README": {
        "version": "1.0",
        "updated": "2026-05-29",
        "status": "archived",
        "provides": ["歸檔說明", "歷史版本索引"],
        "sections": [],
    },
    "changelog": {
        "version": "Agent v1.0 + v2.13",
        "updated": "2026-06-09",
        "status": "active",
        "provides": ["版本演進沿革", "規則生死簿", "案件學習索引", "數據來源檔案庫"],
        "sections": [
            "SECTION 0", "SECTION A", "SECTION B",
            "SECTION C", "SECTION D", "SECTION E",
            "SECTION F", "SECTION G",
        ],
    },
    "data": {
        "version": "Agent v1.0 + v2.13",
        "updated": "2026-06-09",
        "status": "active",
        "provides": [
            "IG演算法數據", "Reels長度分軌", "帳號健康度指標",
            "產業基準數據", "Carousels設計", "FB演算法", "Threads演算法", "WordPress SEO",
        ],
        "sections": [
            "SECTION 0", "SECTION X",
            "PART A", "PART B", "PART C", "PART D",
            "PART E", "PART F", "PART G", "PART H", "PART I",
            # sub-sections referenced as "PART X-N"
            "PART H-1", "PART H-2", "PART H-3", "PART H-4",
            # sub-sections referenced standalone
            "A-1", "A-2", "A-3",
            "B-1", "B-2", "B-3", "B-4", "B-5", "B-6", "B-7", "B-8", "B-9",
            "C-1", "C-2", "C-3",
            "D-1", "D-2", "D-3",
            "E-1", "E-2", "E-3", "E-4", "E-5",
            "F-1", "F-2", "F-3", "F-4",
            "G-1", "G-2", "G-3", "G-4",
            "H-1", "H-2", "H-3", "H-4",
            "I-1", "I-2", "I-3", "I-4", "I-5",
        ],
    },
    "dictionary": {
        "version": "Agent v1.0",
        "updated": "2026-05-29",
        "status": "active",
        "provides": [
            "詞彙黑名單", "感官詞光譜", "AI寫作符號禁用",
            "男性腔禁用", "評論員腔禁用", "廣告法風險詞", "替換對照表",
        ],
        "sections": [
            "SECTION 0", "SECTION X", "SECTION Y",
            "表 1", "表 2", "表 3", "表 4", "表 5",
            "表 6", "表 7", "表 8", "表 9", "表 10",
        ],
    },
    "performance_log": {
        "version": "1.0",
        "updated": "2026-05-29",
        "status": "active",
        "provides": ["案件成效歸因", "Hook效果追蹤", "學習筆記"],
        "sections": ["紀錄模板", "已紀錄案件", "累積分析", "本檔維護 SOP"],
    },
    "principles": {
        "version": "Agent v1.0 + v2.13",
        "updated": "2026-06-09",
        "status": "active",
        "provides": [
            "寫作原則", "三大鐵則", "體驗真實性分流", "不腦補",
            "演算法優先", "第一人稱低密度", "女性視角校正",
            "口播工程", "標題人話檢測", "鉤子白話鐵則",
        ],
        "sections": [
            "PART I", "PART II", "PART III", "PART IV", "PART V",
            "鐵則 1", "鐵則 2", "鐵則 3",
            "原則 A", "原則 B", "原則 C", "原則 D", "原則 E",
            "原則 F", "原則 G", "原則 H", "原則 I", "原則 J",
            "原則 K", "原則 L", "原則 M", "原則 N", "原則 O", "原則 P",
            "學習 1", "學習 2", "學習 3", "學習 4", "學習 5",
            "附錄 1", "附錄 2",
        ],
    },
    "router": {
        "version": "Agent v1.0",
        "updated": "2026-05-29",
        "status": "active",
        "provides": [
            "入口點", "啟動SOP", "接案SOP",
            "Skill維護SOP", "規則索引", "衝突清單", "決策節點",
        ],
        "sections": [
            "SECTION A", "SECTION B", "SECTION C",
            "SECTION D", "SECTION E", "SECTION F",
            "SECTION G", "SECTION H", "SECTION I",
        ],
    },
    "voice": {
        "version": "Agent v1.0",
        "updated": "2026-05-29",
        "status": "skeleton",
        "provides": [
            "Amy語氣庫", "Amy個人定位", "Amy禁用詞", "語氣樣本庫", "受眾畫像",
        ],
        "sections": [
            "SECTION 0", "SECTION A", "SECTION B", "SECTION C",
            "SECTION D", "SECTION E", "SECTION F", "SECTION G",
            "SECTION X", "SECTION Y",
        ],
    },
    "workflows": {
        "version": "Agent v1.0 + v2.13",
        "updated": "2026-06-09",
        "status": "active",
        "provides": [
            "六區交付包", "接案工作流", "Reels分鏡製作",
            "IG標題提案SOP", "全平台清點", "發稿工作流",
            "CTA三層", "法規處理SOP", "WordPress部落格",
        ],
        "sections": [
            "PART I", "PART II", "PART III", "PART IV", "PART V",
            "PART VI", "PART VII", "PART VIII", "PART IX", "PART X",
            "附錄 1", "附錄 2", "附錄 3", "附錄 4", "附錄 5",
        ],
    },
}


def strip_frontmatter(text: str) -> str:
    if text.startswith("---"):
        try:
            end = text.index("\n---", 3)
            return text[end + 4:].lstrip("\n")
        except ValueError:
            pass
    return text


def build_fm(meta: dict) -> str:
    return (
        "---\n"
        + yaml.dump(meta, allow_unicode=True, default_flow_style=False,
                    sort_keys=False, width=120).rstrip()
        + "\n---\n\n"
    )


def process(path: Path):
    stem = path.stem
    if stem not in FILE_META:
        print(f"  SKIP  {path.name}")
        return
    info = FILE_META[stem]
    body = strip_frontmatter(path.read_text(encoding="utf-8"))
    meta = {
        "file": path.name,
        "version": info["version"],
        "updated": info["updated"],
        "status": info["status"],
        "provides": info["provides"],
        "sections": info["sections"],
    }
    path.write_text(build_fm(meta) + body, encoding="utf-8")
    print(f"  OK    {path.name}  ({len(info['sections'])} sections, {len(info['provides'])} provides)")


def main():
    print(f"Building spec-compliant front-matter for {SKILL_DIR} ...\n")
    for path in sorted(SKILL_DIR.glob("*.md")):
        process(path)
    print("\nDone.")


if __name__ == "__main__":
    main()
