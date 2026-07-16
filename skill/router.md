---
file: router.md
version: Agent v1.0
updated: '2026-07-16'
status: active
provides:
- 入口點
- 啟動SOP
- 接案SOP
- Skill維護SOP
- 規則索引
- 衝突清單
- 決策節點
- Skill總版本號
- 四環境同步
- 雙引擎主從
sections:
- SECTION A
- SECTION B
- SECTION C
- SECTION D
- SECTION E
- SECTION F
- SECTION G
- SECTION H
- SECTION I
---

# 🎛️ Amy Skill Agent｜Router（進入點）

Skill Version: v2.18
Last Updated: 2026-07-16

> **版本行說明(v2.17 起)**:上方 `Skill Version` 行是**全系統總版本號的唯一 owner**。`changelog.md` 只記沿革、不作版本源;其他檔 frontmatter 的 version 欄僅標示該檔自身整合到哪版。進版 SOP:改本行 + changelog 新增條目,check.py VERSION 檢查兩者一致(紅燈擋 commit)。任何 AI 回報 Skill 版本一律以本行為準。

> **本檔性質**：所有 Claude 對話啟動時**第一個**讀取的檔案
> **建立日期**：2026-05-29
> **架構版本**：Agent v1.0
> **使用者**：Ivan（KOL 管理公司負責人）/ Amy（KOL）
> **服務對象**：Amy 親子（IG + 部落格 + Threads + Reels）
> **狀態**：🟢 現役

---

## 🚦 SECTION A：Claude 啟動 SOP（每次新對話必跑）

### Step 0：讀本檔（router.md）
進入點。本檔說明「哪份檔放什麼」「哪些規則被推翻」「怎麼跑案件」。

### Step 1：判斷對話類型
| 訊號 | 路徑 |
|---|---|
| Ivan / Amy 提到案件名、品牌名、要寫文案 | → 走 SECTION B「接案產製 SOP」 |
| 提到「修文案」「重寫」「改 v 幾」 | → 走 SECTION B，但跳過 Step 2 規劃，直接針對指定區調整 |
| 提到「Skill 升級」「Agent 重構」 | → 走 SECTION C「Skill 維護 SOP」 |
| 提到「帳號略過率」「健康度」 | → 走 SECTION D「狀態監測 SOP」 |
| 一般閒聊、提問、討論 | → 不跑 SOP，直接對話 |

### Step 2：依路徑載入對應檔案（按需，不全載）

---

## 📚 SECTION B：接案產製 SOP

### 🎯 核心原則（最高優先，凌駕一切）

> **Claude 預設以「演算法最佳化」為產製方向。**
> **廠商特殊要求僅在 Ivan 明確指令時採用，並在交付時標註例外處。**
> **未經 Ivan 確認的廠商要求，Claude 不主動採用。**

白話：廠商的話不是聖旨，Ivan 的話才是。Amy 的演算法健康度比廠商需求優先。

---

Claude 收到「要寫某店文案」時，依序跑這 6 步：

```
┌─ Step 1：事實核對（最高優先）─────────────┐
│  ☐ 店家品類正確？（不腦補成串燒/義式...）   │
│  ☐ 地理位置正確？（永和 ≠ 台北）          │
│  ☐ 廠商指定品項清單？                     │
│  ☐ KOL 實際吃過哪些？哪些只是活動告知？   │
│  ☐ 廠商有特殊要求嗎？                     │
│     → 有（Ivan 明說）→ 寫 cases/<案件>.md │
│     → 沒有 → 全照演算法最佳化做           │
│  → 查 principles.md（不腦補 + 體驗真實性） │
└────────────────────────────────────────┘
        ↓
┌─ Step 2：規劃六區交付包 ──────────────────┐
│  1. IG/FB 單篇照片貼文（長版 800-1000 字）│ <!-- DLV-1 -->
│     ↳ 收藏型粉絲 / FB 受眾               │
│  2. 部落格 WordPress                     │
│     ↳ SEO 累積                          │
│  3. Threads（~420 字）                   │ <!-- DLV-3 -->
│     ↳ 短衝                              │
│  4. Reels 影片分鏡（五欄）                │
│     ↳ 影片本體                          │
│  5. 🆕 IG 演算法版 Caption（400-450 字） │ <!-- DLV-5 -->
│     ↳ 衝陌生觸及主力                    │
│     ↳ 黃金比例 50/200/100/50(+50緩衝)   │
│  6. Reels Caption（短版 200-300 字）    │ <!-- DLV-6 -->
│     ↳ 配 Reels 影片發                   │
│  → 查 workflows.md                       │
└────────────────────────────────────────┘
        ↓
┌─ Step 3：Hook 提案（不寫死、給選）────────┐
│  ☐ 產 8-12 個 Hook，分 3-4 組讓 Amy 挑   │
│  ☐ 三產物分工：標題/大字幕/口播不照抄    │
│  ☐ 雙版本工作流：SEO 版 vs 情緒版        │
│  → 查 principles.md + dictionary.md      │
└────────────────────────────────────────┘
        ↓
┌─ Step 4：產製六區內容 ───────────────────┐
│  ☐ 套用感官詞光譜（🟢🟡🔴）              │
│  ☐ 避開 AI 寫作符號（——、不是X而是Y）   │
│  ☐ 第一人稱低密度（≤4-6 次）             │
│  ☐ Reels 口播字數 ≤ 秒數×4.5            │
│  ☐ 體驗真實性分流（沒體驗的不寫過程）   │
│  → 查 dictionary.md + voice.md           │
└────────────────────────────────────────┘
        ↓
┌─ Step 5：全平台清點（程式跑表）─────────┐
│  ☐ 列出廠商指定全部品項+活動             │
│  ☐ 對照 6 個版位逐格確認                 │
│     (IG長文/部落格/Threads/Reels影片/    │
│      IG演算法版/Reels caption)           │
│  ☐ 任一空格要補上或解釋                  │
│  → 查 workflows.md「交付物清點表」       │
└────────────────────────────────────────┘
        ↓
┌─ Step 6：發稿前完整檢查 ─────────────────┐
│  ☐ 五大禁忌（自我介紹/場景/Logo/過渡語/慢熱）│
│  ☐ Reels 三選一鉤子                      │
│  ☐ 結尾重看誘因                          │
│  ☐ 影片長度（業配 30-45s）              │
│  ☐ 撈本週帳號健康度                      │
│  → 查 data.md + state.md                 │
└────────────────────────────────────────┘
```

---

### 📢 三種 IG 貼文發稿工作流

每個案件在 IG 上發三支貼文：

| 順序 | 貼文類型 | 用哪些區 | 主要任務 |
|---|---|---|---|
| A | **Reels 影片貼文** | 第 4 區（影片）+ 第 6 區（短 caption）| 衝陌生觸及（演算法成長引擎）|
| B | **演算法版單張照片** | 主圖 + 第 5 區（400-450(DLV-5) 字）| 接住 Reels 流量、衝陌生觸及 |
| C | **長文版單張照片** | 主圖 + 第 1 區（800-1000(DLV-1) 字）| 收藏型粉絲、FB 受眾 |

**發布順序建議**：

```
週四 18:00  發 Reels（衝陌生觸及）
週四 21:00  發演算法版單張照片（接觸及波段）
週五 12:00  發長文版單張照片（累積收藏轉化）
週五前      部落格上架（SEO 累積）
週五 12:00+ 同步 Threads
```

**錯開原則**：A、B 兩支間隔 ≥3 小時，避免演算法判定重複內容。

---

### 📦 交付包裝（六區寫完後固定一步）

六區產製 + 清點 + 發稿前檢查通過後，**自動套交付包裝層輸出「可複製 HTML 頁」**（DLV-PKG-H5，全案件預設）。

- 規格與骨架路徑：`workflows.md` PART II「B-PKG」+ PART I「A-7」
- 骨架正本：`amy-skill/assets/dlv_pkg_h5_template.html`
- 定位：包裝層，不佔 DLV-1~6 編號；STATE 不進骨架

---

## 🛠️ SECTION C：Skill 維護 SOP

當 Ivan 提到「Skill 升級 / Agent 重構 / 加規則」時：

1. **不直接動檔**——先討論方向，得到 Ivan「動手」明確指令才動
2. 動檔前先看 `changelog.md`，確認該規則是否已存在或被推翻過
3. 新規則寫入後，同步更新本檔（router.md）的 SECTION E 索引表
4. 任何改動寫入 `changelog.md` 時間線
5. **進版時同步改本檔頂部 `Skill Version` 行**(總版本號唯一 owner),與 changelog 最新條目保持一致(check.py VERSION 檢查)

---

## 📊 SECTION D：狀態監測 SOP

當 Ivan 提到「帳號狀態」「略過率」「健康度」時：

1. 讀 `state/account_health.md` 看上次紀錄
2. 詢問 Ivan 本週數據（自動爬蟲未啟用，避免帳號風險）
3. 更新數據後，重算紅綠燈狀態
4. 若狀態變動（綠→黃 / 黃→紅），同步更新 `state/active_constraints.md`

---

## 📁 SECTION E：規則索引表（哪個主題去查哪份檔）

### 🟢 現役檔案清單

<!-- AUTO-FILELIST START -->
| 檔名 | 版本 | 更新日期 | 狀態 |
|---|---|---|---|
| `router.md` | Agent v1.0 | 2026-07-16 | 🟢 active |
| `account_health.md` | 1.0 | 2026-05-29 | 🟢 active |
| `active_constraints.md` | 1.0 | 2026-05-29 | 🟢 active |
| `changelog.md` | Agent v1.0 + v2.18 | 2026-07-16 | 🟢 active |
| `data.md` | Agent v1.0 + v2.18 | 2026-07-16 | 🟢 active |
| `dictionary.md` | Agent v1.0 | 2026-05-29 | 🟢 active |
| `performance_log.md` | 1.0 | 2026-05-29 | 🟢 active |
| `principles.md` | Agent v1.0 + v2.16 | 2026-06-30 | 🟢 active |
| `voice.md` | Agent v1.0 | 2026-05-29 | 🟡 skeleton |
| `workflows.md` | Agent v1.0 + v2.18 | 2026-07-16 | 🟢 active |
<!-- AUTO-FILELIST END -->

### 📂 動態資料夾

| 路徑 | 用途 |
|---|---|
| `state/account_health.md` | 帳號健康度（每週更新） |
| `state/performance_log.md` | 成效歸因日誌 |
| `state/active_constraints.md` | 當前限制（廠商特殊要求紀錄、Ivan 例外指令、其他短期限制） |
| `cases/<案件代號>.md` | 案件專屬規則（從新案開始累積） |
| `assets/dlv_pkg_h5_template.html` | 交付包裝層骨架正本（DLV-PKG-H5；放 repo 根目錄 `assets/`，check.py 只掃 `skill/` 故不碰它） |

### 主題 → 對應檔案 查找表

<!-- AUTO-INDEX START -->
| 主題 | 查哪份檔 |
|---|---|
| 入口點 | `router.md` |
| 啟動SOP | `router.md` |
| 接案SOP | `router.md` |
| Skill維護SOP | `router.md` |
| 規則索引 | `router.md` |
| 衝突清單 | `router.md` |
| 決策節點 | `router.md` |
| Skill總版本號 | `router.md` |
| 四環境同步 | `router.md` |
| 雙引擎主從 | `router.md` |
| 帳號健康度 | `account_health.md` |
| 略過率監測 | `account_health.md` |
| IG健康度 | `account_health.md` |
| 週快照 | `account_health.md` |
| 當前接案限制 | `active_constraints.md` |
| 廠商例外指令 | `active_constraints.md` |
| 業配暫停機制 | `active_constraints.md` |
| 歸檔說明 | `archive_README.md` |
| 歷史版本索引 | `archive_README.md` |
| 版本演進沿革 | `changelog.md` |
| 規則生死簿 | `changelog.md` |
| 案件學習索引 | `changelog.md` |
| 數據來源檔案庫 | `changelog.md` |
| IG演算法數據 | `data.md` |
| Reels長度分軌 | `data.md` |
| 帳號健康度指標 | `data.md` |
| 產業基準數據 | `data.md` |
| Carousels設計 | `data.md` |
| FB演算法 | `data.md` |
| Threads演算法 | `data.md` |
| WordPress SEO | `data.md` |
| 詞彙黑名單 | `dictionary.md` |
| 感官詞光譜 | `dictionary.md` |
| AI寫作符號禁用 | `dictionary.md` |
| 男性腔禁用 | `dictionary.md` |
| 評論員腔禁用 | `dictionary.md` |
| 廣告法風險詞 | `dictionary.md` |
| 替換對照表 | `dictionary.md` |
| 案件成效歸因 | `performance_log.md` |
| Hook效果追蹤 | `performance_log.md` |
| 學習筆記 | `performance_log.md` |
| 寫作原則 | `principles.md` |
| 三大鐵則 | `principles.md` |
| 體驗真實性分流 | `principles.md` |
| 商品案真實性判斷 | `principles.md` |
| 聯名IP告知框架 | `principles.md` |
| 不腦補 | `principles.md` |
| 演算法優先 | `principles.md` |
| 第一人稱低密度 | `principles.md` |
| 女性視角校正 | `principles.md` |
| 口播工程 | `principles.md` |
| 標題人話檢測 | `principles.md` |
| 鉤子白話鐵則 | `principles.md` |
| Amy語氣庫 | `voice.md` |
| Amy個人定位 | `voice.md` |
| Amy禁用詞 | `voice.md` |
| 語氣樣本庫 | `voice.md` |
| 受眾畫像 | `voice.md` |
| 六區交付包 | `workflows.md` |
| 案型分流 | `workflows.md` |
| 商品導購案 | `workflows.md` |
| 交付包裝層 | `workflows.md` |
| 可複製HTML頁 | `workflows.md` |
| 接案工作流 | `workflows.md` |
| Reels分鏡製作 | `workflows.md` |
| IG標題提案SOP | `workflows.md` |
| 全平台清點 | `workflows.md` |
| 發稿工作流 | `workflows.md` |
| CTA三層 | `workflows.md` |
| 法規處理SOP | `workflows.md` |
| WordPress部落格 | `workflows.md` |
| 演算法月檢 | `workflows.md` |
<!-- AUTO-INDEX END -->

---

## ⚠️ SECTION F：衝突清單（已推翻的舊規則）

**Claude 看到舊檔提到下列規則時，一律不採用：**

| 已推翻規則 | 推翻日期 | 推翻原因 | 替代規則 |
|---|---|---|---|
| 30-50 秒禁止區 | 2026-05-29 | 無業界數據支持，實際 30-45 秒是業配甜蜜區 | 業配 30-45s / 自費 15-25s（data.md 長度分軌） |
| A 版業配 15-28 秒一刀切 | 2026-05-29 | 對親子餐廳業配太短 | 30-45 秒分軌 |
| 標題強制只能放地點 | 2026-05-29 | 太僵化 | 雙版本工作流（SEO 重 vs 情緒重，Amy 自選） |
| 單一長度規則 | 2026-05-29 | 應依目標分軌 | 業配/自費/多平台分軌 |
| 「全篇嚴禁第一人稱」 | 2026-05-15（v2.6） | 失去 Amy 個人視角 | 第一人稱低密度（≤4-6 次，禁流水帳開頭） |
| 美食探店做輪播 | 2026-05-15 | 探店主力是 Reels + 單張長文，輪播是教學/食譜強項 | 探店預設不做輪播 |
| 五區交付包（無 400-450(DLV-5) 字演算法版）| 2026-05-29 | 漏掉演算法甜蜜點字數 | 六區交付包（新增 IG 演算法版 400-450 字 Caption） |
| A/B/C/D 案件分級制 | 2026-05-29 | Ivan 不採用分級邏輯，廠商案全接 | 核心原則：演算法優先 + Ivan 指令例外（見 SECTION B 開頭） |
| 「禁接 D 級案件 4 週」期間限制 | 2026-05-29 | 分級制廢除後此規則無效 | 無，改為「廠商特殊要求紀錄」 |

### 衝突解決原則
- **新版自動贏舊版**：日期較新的規則永遠優先
- **看到舊檔規則時 Claude 必查本表**，確認該規則是否被推翻
- **Claude 不得引用「歸檔」資料夾中的內容當依據**

---

## 🗄️ SECTION G：歸檔清單（不再現役）

**以下舊檔已歸檔，僅供歷史參考，產製時不查閱：**

```
archive/
├─ amy_skill_v2_3.md         （2026 初期版本）
├─ amy_skill_v2_4.md
├─ amy_skill_v2_6.md
├─ amy_skill_v2_7.md
├─ amy_skill_v2_8.md
├─ amy_skill_v2_8_3.md
├─ amy_skill_v2_9.md         （前主檔，已被新架構整合）
├─ amy_skill_compressed.md
├─ amy_skill_v2_10_addendum.md    ⚠️ 含已推翻規則
├─ amy_skill_v2_11_addendum.md    （v2.11 六規已整合進 principles.md）
├─ amy_skill_v2_12_addendum.md    （體驗真實性分流已整合進 principles.md）
├─ amy_skill_final_2026_05_29.md  （部分整合：Hook 模板/長度分軌/雙版本/400 字 caption 保留；A/B/C/D 分級制/禁接 D 級期間/30-50 秒禁止區已推翻）
├─ ig_algorithm_dev_log.md        （已整合進 changelog.md）
└─ *_QUICKREF.md / *_diff.md      （歷史紀錄性質）
```

⚠️ **重要**：歸檔僅供 Ivan 翻閱「為什麼這條規則存在」的歷史脈絡，**Claude 產製時不引用**。

---

## 👤 SECTION H：決策節點對照表（誰決定什麼）

| 決策類型 | 由誰決定 | Claude 應做的事 |
|---|---|---|
| 補資訊（地址、營業時間等基本） | Claude 自行 | 直接補 |
| 文字風格修正（女性視角、語氣） | Claude 自行 | 直接改 |
| Hook 內容 / 標題選擇 | **Amy** | 給 8-12 個選項分組 |
| 主軸切換（爆款方向變更） | **Ivan** | 確認後再動 |
| **廠商特殊要求是否採用** | **Ivan**（必須明確指令） | 預設不採用、以演算法為主；Ivan 明說要照做才改 |
| 體驗事實核對（吃過沒吃過、店家品類） | **Ivan / Amy** | 不確定一律問，不腦補 |
| Skill 升級 / 新規則加入 | **Ivan** | 提案後等「動手」指令 |
| 帳號狀態評估 | **Ivan**（數據提供）→ Claude 分析 | 詢問→分析→建議 |
| 發稿時程 | **Ivan / Amy** | 提供建議排程表 |
| WordPress 後台直接排稿 | **Claude 可代操**（待 workflows.md 補齊操作 SOP） | 等操作 SOP 寫好 |

---

## 🆕 SECTION I：本檔更新規則

- 任何規則衝突 → 更新本檔 SECTION F「衝突清單」
- 任何新規則加入 → 更新本檔 SECTION E「規則索引表」
- 任何檔案歸檔 → 更新本檔 SECTION G「歸檔清單」
- 任何 SOP 變動 → 更新本檔 SECTION B/C/D 對應流程

**本檔是 Agent 的「神經中樞」，所有檔案的元資訊都在這。**

---

## 治理守則(2026-06-14 重構鎖定)

1. 一事實一 owner:交付規格 owner=workflows.md PART II(DLV-1~6);長度/數據 owner=data.md。其他檔引用一律用 DLV-/PRIN- 等 ID 指標,不複製數值。
2. 改規則前先判類別:CLASS-S 結構(區數/身份/字數)、CLASS-R 規則、CLASS-T 狀態。
3. 每次 commit 前 pre-commit hook 自動跑 check.py(含 COUNT 區數一致 + DEDUP 字數不重複),紅燈擋 commit。
4. 歷史/退版文字用 suppress 標記(已退版/已升級/沿革語境),不竄改史實。
5. 舊案不回改編號,靠對照表翻譯(五區→六區、第5區→DLV-6、1-D→DLV-5)。
6. STATE 檔(account_health/performance_log/active_constraints)不進 skill 打包。
7. **四環境同步(v2.17)**:GitHub `amy-skill` 為唯一正本(SSOT);SGP1 鏡像、Claude Project 知識庫、ChatGPT Project 知識庫皆為快取。版本沉澱進版時依序同步:GitHub 正本 → SGP1 → Claude Project → ChatGPT Project,一律用**完整替換檔**(不用 diff)。快取與正本衝突時以正本為準;各 AI 產文前回報載入版本號,版本不符即為漂移警訊。
8. **雙引擎主從(v2.17)**:Claude Project 為**主系統**(生產環境),ChatGPT Project 為**次系統**(比稿引擎),一套標準、兩級執行權限。三邊界:(a) **裁決權**——規則解讀、衝突裁定、Skill 升級只在主系統定案,次系統對規則有疑義時拿回主系統,不自行解釋;(b) **沉澱單向**——不論哪邊產出勝出,規則沉澱一律走 主系統討論 → GitHub 正本 → 同步四環境,次系統永遠是同步終點、不是起點;(c) **次系統輸出視同外稿**——進交付流程前依主系統規則掃一次(體驗真實性、禁用詞、字數規格),等同外部初稿待審。

---

**Router 結束**

> 下一步：讀對應路徑的檔案（principles / workflows / dictionary / data / state）
