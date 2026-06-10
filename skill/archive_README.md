---
file: archive_README.md
version: '1.0'
updated: '2026-05-29'
status: archived
provides:
- 歸檔說明
- 歷史版本索引
sections: []
---

# 🗄️ Archive(歸檔資料夾)

> **本資料夾性質**:Amy Skill 歷史版本,**不再現役**
> **歸檔日期**:2026-05-29
> **歸檔原因**:Agent v1.0 架構上線,22 份散亂舊檔整合為 7 份核心模組

---

## 🚨 給 Claude 的鐵則

1. **本資料夾的內容是「歷史紀錄」,不是「現役規則」**
2. **產製文案時,絕對不引用本資料夾任一檔案的規則**
3. **現役規則只在 `router.md`、`principles.md`、`workflows.md`、`dictionary.md`、`voice.md`、`data.md`**
4. **僅在 Ivan 明確要求「翻歷史」「看 v2.X 怎麼寫的」時讀取本資料夾**

---

## 📁 資料夾內容

### 主檔系列(9 份)
| 檔名 | 日期 | 整合到哪 | 狀態 |
|------|------|---------|------|
| `amy_skill_v2_3.md` | 2026-05-15 | 三檔法規 SOP → `workflows.md` PART VIII | 已整合 |
| `amy_skill_v2_4.md` | 2026-05-15 | 三檔法規 SOP → `workflows.md` PART VIII | 已整合 |
| `amy_skill_v2_6.md` | 2026-05-15 | 第一人稱低密度、Reels 五欄、IG 演算法 → `principles.md`、`workflows.md`、`data.md` | 已整合 |
| `amy_skill_v2_7.md` | 2026-05-16 | 動詞鎖定、業配感詞、標題提案 SOP、Carousels → 跨檔 | 已整合 |
| `amy_skill_v2_8.md` | 2026-05-17 | 菜名腦補、老闆名字準則 → `principles.md` | 已整合 |
| `amy_skill_v2_8_3.md` | 2026-05-17 | 留言→私訊機制 → `workflows.md` PART VII | 已整合 |
| `amy_skill_v2_9.md` | 2026-05-22 | Reels 雙版本、火力平均、人話檢測、避用詞 → `principles.md`、`workflows.md` | 已整合 |
| `amy_skill_compressed.md` | - | 早期壓縮版,規則已分散整合 | 已整合 |
| `amy_skill_final_2026_05_29.md` | 2026-05-29 | 七大決策 → 部分整合(分級制/30-50s禁止區已推翻) | 部分整合 |

### Addendum 補強檔(3 份)
| 檔名 | 日期 | 整合到哪 | 狀態 |
|------|------|---------|------|
| `amy_skill_v2_10_addendum.md` | 2026-05-28 | 略過率對策、Reels 開頭規則 → `principles.md`、`data.md` | 已整合(含已推翻的分級制) |
| `amy_skill_v2_11_addendum.md` | 2026-05-28 | 三產物分工、口播工程、視角校正、評論員腔 → `principles.md` | 已整合 |
| `amy_skill_v2_12_addendum.md` | 2026-05-29 | 體驗真實性分流 → `principles.md` 鐵則 1 | 已整合 |

### QUICKREF 速覽版(5-6 份)
| 檔名 | 用途 |
|------|------|
| `amy_skill_v2_7_QUICKREF.md` ~ `v2_11_QUICKREF.md` | 各版本的手機速查 cheat sheet |

說明:速覽版是舊版本的精簡版,Agent v1.0 用 router.md 取代速查功能。

### 開發日記(1 份)
| 檔名 | 用途 |
|------|------|
| `ig_algorithm_dev_log.md` | 2026-05-29 IG 演算法 15 階段討論紀錄 → 整合進 `changelog.md` |

---

## 🔄 為什麼歸檔不刪除?

1. **歷史可追溯** — Ivan 想看「為什麼某條規則存在」時可翻
2. **規則演進脈絡** — 哪條規則何時誕生、何時被推翻,有原始檔對照
3. **未來除錯** — 若 Agent v1.0 整合有遺漏,可回頭翻舊檔補
4. **學習庫** — Amy Skill 的演進史也是 KOL Skill 設計的學習資產

---

## 🔍 如何從歸檔追蹤一條規則?

如果想查「某條規則的來源」:

1. **查 `changelog.md` SECTION B 規則生死簿** → 找該規則的演進歷史
2. **依日期定位對應版本** → 例如 2026-05-22 → v2.9
3. **打開 `archive/amy_skill_v2_9.md`** → 看當時原始寫法
4. **比對 `changelog_diffs/`** → 看跟前一版的具體改動

---

## ⚠️ Claude 不引用歸檔的例外

唯一例外:**Ivan 明確要求**

例如:
- ✅ Ivan:「翻一下 v2.7 怎麼寫廠商素材動詞鎖定」 → 可讀
- ✅ Ivan:「看一下 ig_algorithm_dev_log 第三階段的決策」 → 可讀
- ❌ 平常產製文案 → 絕對不讀

---

**Archive README 結束**

> 這個資料夾的存在意義:讓 Amy Skill 的演進史可追溯,但不污染現役規則
