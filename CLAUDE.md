> 全域鐵則見 ~/.claude/CLAUDE.md。本檔只寫本專案特有事實。

## 是什麼
Amy 親子 KOL 多平台社群內容產製 skill，供 Claude.ai 對話介面使用。涵蓋 IG/FB/Threads/WordPress/Reels 業配與自費貼文。不是 web 服務，不常駐。

## 啟動/重啟
按需手動執行，無常駐，勿嘗試重啟。
本 skill 在 Claude.ai 對話中自動觸發（當使用者提到為 Amy 產製內容時）。
Claude Code 不直接跑這套 skill；SKILL.md 明確說明「自動化需另做版本，不要直接沿用」。

## 關鍵檔 / 指令
- `SKILL.md`：skill 入口外殼，說明架構，首讀
- `skill/router.md`：每次啟動必先讀，神經中樞（對話分流、規則索引、衝突清單）
- `skill/principles.md`：三大鐵則（體驗真實性 / 不腦補 / 演算法優先）
- `skill/workflows.md`：六區交付包 SOP
- `skill/state/`：動態狀態（帳號健康度、當前限制、成效），產製前讀，絕不寫進交付物
- `skill/archive_README.md`：說明歸檔資料夾，產製時不引用 archive/ 內容

## 雷區
- 不引用 `skill/archive/` 內任何舊版規則產製內容（最常見災難，會產出整包錯內容）
- 不把 `skill/state/` 內容寫進交付物（state 會過期污染後續案件）
- 這套 skill 只供 Claude.ai 對話，不可直接用於 Claude Code 排程/自動化

## VanHex 正本
系統分布正本在 Google Drive：`我的雲端硬碟/VanHex/VanHex_系統分布.md`（本機無 Drive 連接器、系統現況先讀本機鏡像 /root/work-reminder/docs/VanHex_系統分布.md（以 Drive 為最終正本、鏡像可能落後）；不確定就問使用者，勿自寫系統清單）。凡結構性變動（新服務/改 port/改啟動方式/狀態改變）須當次提醒使用者更新 Drive 正本。
