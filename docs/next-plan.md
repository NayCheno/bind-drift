# 下一步严格计划

目标不是“继续堆功能”，而是把当前 56/100 左右的状态推进到 CCF-B borderline / weak accept 可能区间。计划按“阻断接收的风险优先级”排序。

当前必须承认的事实是：`evaluation_summary` 里主 warning 数是 11，`wrapper-fix` precision 已升到 0.7273、P@10 为 0.7，这是好消息；但 build oracle 为 0，manual review 在 evaluation summary 中没有读到任何 labeled warning。同时 `manual_review_summary` 又显示有 112 条双人标注、agreement 1.0，但 true labeled warnings 为 0。所以下一步的核心不是再增加 detector，而是把实验闭环做实。

## 总目标

下一轮完成后，评分目标应从 56/100 提升到至少：

- 65/100：可以作为 CCF-B borderline workshop/system-track 风格投稿
- 70/100：可以认真冲 CCF-B 正会

最低可接受目标：

- artifact 自洽
- manual review 能被 `evaluation_summary` 正确读取
- 主 warning set 有非零人工真阳性
- baseline/ablation 显示 BindDrift 明确优于简单基线
- case study 全部来自 adjudicated true positives

## 阶段 0：先冻结主实验口径

### 问题

现在最大隐患是：不同文件对“主结果”的说法不一致。`evaluation_summary` 说 warnings 是 11。`manual_review_summary` 说 112 条已双人标注但 0 true。runtime 表之前又显示 latest run 有 17,910 warnings。这个状态下，审稿人会先质疑实验口径，而不是讨论方法。

### 解决方案

建立一个强制的 `run_manifest.json`，每次 paper build 只允许引用 manifest 中声明的文件。

建议新增：

```text
data/replay/latest/run_manifest.json
```

内容必须包括：

```json
{
  "run_id": "latest",
  "canonical_warning_file": "data/replay/latest/warnings.jsonl",
  "canonical_review_file": "data/replay/latest/manual_review.csv",
  "canonical_drift_facts_file": "data/replay/latest/drift_facts.jsonl",
  "canonical_database": ".binddrift/binddrift.sqlite3",
  "warning_count": 11,
  "drift_fact_count": 17910,
  "reviewed_warning_count": 11,
  "pair_count": 20,
  "version_count": 21,
  "sha256": {
    "warnings.jsonl": "...",
    "manual_review.csv": "...",
    "drift_facts.jsonl": "..."
  }
}
```

同时修改 paper build 和 eval all，让以下文件都必须读取同一个 manifest：

- `paper/tables/evaluation_summary.json`
- `paper/tables/manual_review_summary.json`
- `paper/tables/runtime_scalability.json`
- `paper/tables/baselines_ablations.json`

新增 hard fail：

```python
assert evaluation_summary["warnings"] == run_manifest["warning_count"]
assert manual_review_summary["source_run_id"] == run_manifest["run_id"]
assert reviewed_warning_count <= warning_count
assert warnings_jsonl_sha == manifest_sha
```

如果有任何不一致，paper build 直接失败，不生成 paper tables。

### 验收标准

必须全部满足：

1. `data/replay/latest/warnings.jsonl` 非空，且行数 = `evaluation_summary["warnings"]`
2. `data/replay/latest/manual_review.csv` 存在
3. `manual_review_summary["source_run_id"] == "latest"`
4. `evaluation_summary.manual_review.labeled_warnings == manual_review_summary.labeled_warnings`，或者有明确字段解释 `filtered_labeled_warnings`
5. `runtime_scalability.json` 中 `latest.warnings` 与 `evaluation_summary.warnings` 口径一致；如果一个是 drift facts，一个是 promoted warnings，必须字段改名为 `drift_facts` 与 `promoted_warnings`
6. paper build 在上述任一条件不满足时失败

通过标准：artifact consistency 100%。

如果这一阶段不完成，不进入下一阶段。

## 阶段 1：修复 manual review 读入与 warning identity

### 问题

`manual_review_summary` 能看到 112 条标注，但 `evaluation_summary` 的 manual review 是 0 条 labeled。这说明 label key、`pair_id`、`warning_id`、`run_id` 或 review CSV 路径至少有一个不一致。

### 解决方案

定义永久稳定的 warning identity，不再只依赖 `W-000001` 这种局部编号。

新增字段：

```json
{
  "warning_uid": "sha256(run_id|pair_id|old_version|new_version|type|symbol|indicator|old_value|new_value)",
  "run_id": "latest",
  "pair_id": "latest-p010-v6.10-to-v6.11",
  "warning_id": "W-000001"
}
```

manual review CSV 必须包含：

```text
warning_uid,run_id,pair_id,warning_id,type,symbol,rank,score,reviewer1_label,reviewer2_label,adjudicated_label,adjudication_notes
```

`load_manual_labels` 的优先级：

```text
warning_uid > pair_id:warning_id > warning_id
```

但 paper 主表只能使用 `warning_uid` 匹配。`warning_id` 只作为展示编号。

同时新增诊断命令：

```bash
uv run binddrift eval check-label-join \
  --warnings data/replay/latest/warnings.jsonl \
  --manual-review data/replay/latest/manual_review.csv
```

输出：

```json
{
  "warnings": 11,
  "review_rows": 11,
  "matched_review_rows": 11,
  "unmatched_warnings": [],
  "orphan_review_rows": [],
  "label_distribution": {
    "TRUE_WRAPPER_FIX": 3,
    "TRUE_SEMANTIC_DRIFT": 2,
    "BENIGN_DRIFT": 4,
    "FALSE_POSITIVE": 2
  }
}
```

### 验收标准

必须全部满足：

1. `check-label-join.matched_review_rows == warning_count`
2. `orphan_review_rows == []`
3. `unmatched_warnings == []`
4. `evaluation_summary.manual_review.labeled_warnings > 0`
5. `evaluation_summary.manual_review.label_distribution` 非空
6. `manual_review_summary.labeled_warnings` 与 `evaluation_summary.manual_review.labeled_warnings` 一致

硬性目标：

- 主 warning set 如果是 11 条，则至少 11/11 完成 adjudicated label

如果仍然出现 `manual_review_summary` 有标签，但 `evaluation_summary` 读不到，这一阶段失败。

## 阶段 2：禁止 single-version warning 进入 CCF-B 主实验

### 问题

你当前很多 single-version review 目标会被标成 UNCLEAR，理由是“no historical baseline”。这类 warning 可以作为 pilot，但不能作为 CCF-B 主实验主张。因为 BindDrift 的论文定位是 cross-version API/contract drift，不是单版本 risk scanner。

当前 scope 说 BindDrift 是 warning/prioritization artifact，检测 Linux C API change 可能 stale Rust binding/helper/wrapper/safe abstraction。所以主实验必须有 old/new version comparison。

### 解决方案

增加 main evidence gate：

```python
def eligible_for_main_warning(w):
    return (
        w["old_version"] is not None
        and w["new_version"] is not None
        and w["old_version"] != w["new_version"]
        and w["pair_id"] is not None
        and w["promotion_status"] == "promoted"
    )
```

所有 single-version warning：

```text
old_version = null
pair_id = null
```

只进入：

```text
data/single_version_review_targets.jsonl
```

不进入：

```text
paper/tables/evaluation_summary.json
paper/tables/manual_review_summary.json
paper/cases/
```

如果你想保留 single-version 结果，可以在 appendix 中单独报告：

```text
Exploratory single-version review targets
```

不能放在主 precision / P@K 表里。

### 验收标准

必须全部满足：

1. paper 主 warning set 中 `old_version` 非空
2. paper 主 warning set 中 `pair_id` 非空
3. `manual_review.csv` 中没有 “no historical baseline” 作为 adjudicated UNCLEAR 的主要原因
4. `evaluation_summary` 中单独报告：
   - `promoted_replay_warnings`
   - `single_version_review_targets`
5. 两者不能混算

硬性目标：

- 主 warning set 中 single-version warning 数 = 0

## 阶段 3：重新构造主 warning set，目标不是 11 条，而是 top-100 可审

### 问题

现在 `evaluation_summary` 只有 11 条 warnings。数量太少，会带来两个问题：

- P@10 看起来高，但样本太小
- baseline 很容易和 BindDrift 选到同一批 warning，导致 ablation 没有区分度

### 解决方案

把输出分成三层：

- `drift_facts`：所有版本变化事实，例如 17k/49k 级别
- `promoted_warnings`：通过 Rust-impact gate 的 warning，例如 200-1000 条
- `paper_topk`：排名前 100 条，用于人工 review 与 paper 主表

当前 gate 可能过严，导致 promoted warnings 只有 11。建议调成：

- Tier A：`oracle_confirmed`
- Tier B：`c_source_diff + direct Rust unsafe use`
- Tier C：`c_behavior_indicator change + contract mapping`
- Tier D：`c_behavior_indicator change + safe API + safety comment`

paper 主评估使用：

```text
Tier A + Tier B + Tier C + Tier D 的 top-100
```

不要只保留 oracle-confirmed，因为那会让结果变成“wrapper-fix lookup”，创新性不足。

### 验收标准

建议目标：

- `drift_facts >= 10,000`
- `promoted_warnings` between 100 and 2,000
- `paper_topk = 100`
- `manual_review_rows = 100`

如果真实 promoted warnings 少于 100，也可以接受，但必须解释：

```text
BindDrift intentionally emits sparse high-confidence warnings.
```

但最低不能只有 11 条，除非 11 条全部人工真阳性或高度可信。

硬性目标：

- `paper_topk >= 50`

## 阶段 4：重做人工 review，目标是非零真阳性和可解释负样本

### 问题

当前 112 条人工标注 true labeled warnings 为 0。这对 CCF-B 是致命问题。即使 wrapper-fix oracle precision 很高，人工没有真阳性也无法支撑 semantic precision。

### 解决方案

重新生成 review CSV，只 review 主 replay warnings，不 review single-version warnings。

Review labels 保持：

- `TRUE_BUILD_BREAKAGE`
- `TRUE_WRAPPER_FIX`
- `TRUE_SEMANTIC_DRIFT`
- `BENIGN_DRIFT`
- `FALSE_POSITIVE`
- `UNCLEAR`

但必须新增两个字段：

```text
false_reason,true_reason
```

`true_reason` 枚举：

- `BUILD_LOG_MATCH`
- `WRAPPER_FIX_COMMIT_MATCH`
- `CONTRACT_CHANGE_REACHES_SAFE_API`
- `ERROR_MAPPING_STALE`
- `NULLABILITY_MAPPING_STALE`
- `OWNERSHIP_LIFETIME_STALE`
- `SLEEPABILITY_CONTEXT_STALE`

`false_reason` 枚举：

- `NO_VERSION_CHANGE`
- `NO_RUST_IMPACT`
- `BINDING_ONLY`
- `BENIGN_CONTRACT_CHANGE`
- `WEAK_INDICATOR`
- `MISMATCHED_SYMBOL`
- `EXTRACTOR_ERROR`
- `INSUFFICIENT_EVIDENCE`

人工 review 流程：

1. reviewer1 独立标 top-100
2. reviewer2 独立标 top-100
3. adjudicator 只处理分歧
4. 生成 `adjudicated_label`
5. eval all 只用 `adjudicated_label`

### 验收标准

最低目标：

- `reviewed_warnings >= 50`
- `double_labeled >= 50`
- `agreement_rate >= 0.75`
- `UNCLEAR <= 30%`
- `true_labeled_warnings >= 5`

CCF-B 可投目标：

- `reviewed_warnings = 100`
- `double_labeled = 100`
- `agreement_rate >= 0.80`
- `UNCLEAR <= 20%`
- `true_labeled_warnings >= 10`
- `manual precision >= 0.10`
- `P@10 >= 0.30`
- `P@50 >= 0.15`
- `P@100 >= 0.10`

硬性失败条件：

- `true_labeled_warnings == 0`

只要真阳性仍为 0，就不能投。

## 阶段 5：重构 wrapper-fix oracle，避免被审稿人认为是 symbol-level leakage

### 问题

当前 wrapper-fix prediction 很好：precision 0.7273、P@10 0.7。但它仍是 symbol-level oracle，审稿人会问：

- 是不是只要 symbol 出现在 wrapper-fix commit 里就算命中？
- 这个 fix 是否真的和 warning 的 drift type 相关？

### 解决方案

把 wrapper oracle 从 symbol-level 升级为 typed oracle。

新增字段：

```json
{
  "oracle_type": "wrapper_fix",
  "symbol": "PTR_ERR",
  "commit": "...",
  "fix_kind": "error_mapping | nullability | ownership | layout | signature | allocation | sleepability",
  "matched_warning_type": "ErrorDrift",
  "rust_file": "rust/kernel/...",
  "diff_hunk": "...",
  "evidence_strength": "strong | weak",
  "time_relation": "after_drift | before_drift | same_pair"
}
```

命中规则：

```text
warning.symbol == oracle.symbol
AND warning.type compatible with fix_kind
AND oracle.commit_date after old_version_date
AND oracle.commit_date <= new_version_or_head_date
```

例如：

- `ErrorDrift` 只能匹配 `error_mapping/signature fix`
- `NullabilityDrift` 只能匹配 `nullability/error pointer fix`
- `OwnershipRefcountDrift` 只能匹配 `ownership/refcount/lifetime fix`

### 验收标准

必须报告两套指标：

- symbol-level wrapper oracle
- typed wrapper oracle

最低目标：

- `typed_wrapper_precision_at_10 >= 0.30`
- `typed_wrapper_precision_at_50 >= 0.15`
- `typed_wrapper_recall >= 0.10`

硬性要求：

- paper 主 claim 只能使用 typed oracle
- symbol-level oracle 只能作为辅助/upper-bound

## 阶段 6：重做 baseline / ablation，让它真的能回答“BindDrift 是否有用”

### 问题

当前 baseline 表危险：`BindgenOnly`、`CSignatureDiff`、`NoRanking` 等 baseline 的 wrapper precision 看起来不差，甚至可能高于 BindDrift。这会让审稿人认为你的 ranking 没有贡献。

### 解决方案

重新设计 baseline，使它们各自输出自己的 top-100，而不是在同一批 11 条 promoted warnings 上过滤。

Baseline 应该是：

- B1 `BindingDiffOnly`：所有 binding diff fact，按 diff severity 排
- B2 `CSignatureDiffOnly`：所有 C signature diff，按 change size 排
- B3 `CIndicatorOnly`：所有 behavior indicator change，按 indicator confidence 排
- B4 `RustUseOnly`：所有触达 `rust_binding_uses` 的 symbol，按 use count 排
- B5 `OracleBlindBindDrift`：BindDrift ranking，但去掉 wrapper/build oracle boost
- B6 `NoRanking`：promoted warnings 原始顺序
- B7 `Random`：random sample, run 10 seeds

主比较指标：

- manual P@10 / P@50 / P@100
- typed wrapper P@10 / P@50 / P@100
- MRR
- AUC-style recall@K if possible

### 验收标准

最低目标：

- BindDrift P@10 > every simple baseline P@10
- BindDrift P@50 >= best baseline P@50 + 0.05
- OracleBlindBindDrift < Full BindDrift on typed wrapper P@K
- NoGraph / NoImpactGate 明显下降

硬性失败条件：

- NoRanking >= BindDrift on P@10 and P@50

如果 NoRanking 仍然更好，你的 claim 必须改成：

```text
evidence gate reduces warning volume
```

而不能 claim：

```text
ranking improves prioritization
```

## 阶段 7：补 extractor / indicator audit

### 问题

当前实现仍然包含 regex/heuristic extraction。CCF-B 审稿人一定会问：C function、Rust use、indicator 的 precision 是多少？现在还没看到 extractor audit 表。

### 解决方案

新增：

```text
paper/tables/extractor_audit.json
data/audit/extractor_sample.csv
```

抽样对象：

- `c_functions`: 100
- `rust_binding_uses`: 100
- `c_behavior_indicators`: 100
- `rust_error_mappings`: 50
- `rust_lifetime_facts`: 50
- `promoted_warnings`: 50

CSV 字段：

```text
sample_id,table,symbol,file,line,extracted_fact,is_correct,corrected_fact,error_type,notes
```

`error_type` 枚举：

- `WRONG_SYMBOL`
- `WRONG_SCOPE`
- `WRONG_LINE`
- `FALSE_INDICATOR`
- `MISSING_CONTEXT`
- `REGEX_ARTIFACT`
- `BINDGEN_ARTIFACT`
- `OTHER`

### 验收标准

最低目标：

- c_functions precision >= 0.90
- rust_binding_uses precision >= 0.90
- c_behavior_indicators precision >= 0.75
- rust_error_mappings precision >= 0.80
- rust_lifetime_facts precision >= 0.75
- promoted_warning_evidence precision >= 0.30

CCF-B 可投目标：

- c_functions precision >= 0.95
- rust_binding_uses precision >= 0.95
- c_behavior_indicators precision >= 0.80
- promoted_warning_evidence precision >= 0.40

硬性要求：

- `paper/tables/table_index.json` 必须包含 `extractor_audit`

## 阶段 8：case study 只允许来自真阳性

### 问题

你已经改了 case study selection，只选 TRUE_LABELS 且必须有 C/Rust evidence。这个方向正确。但现在 `manual_review_summary` 的 true labeled warnings 是 0。所以理论上当前不应该生成任何主 case study。

### 解决方案

case generation 加 hard fail：

```python
if main_paper_mode and len(selected_cases) == 0:
    raise RuntimeError("No adjudicated true-positive case studies available")
```

每个 case 必须满足：

- `adjudicated_label in TRUE_LABELS`
- `old_version != null`
- `new_version != null`
- `pair_id != null`
- has C evidence
- has Rust impact evidence
- has contract/oracle evidence

每个 case markdown 必须包含：

1. old version evidence
2. new version evidence
3. C-side diff or indicator change
4. Rust wrapper/safe API dependency
5. reviewer adjudicated label
6. why compiler cannot catch it
7. why this is not merely generated-binding-only

### 验收标准

最低目标：

- case_studies >= 2
- all case labels in TRUE_LABELS
- 0 UNLABELED case
- 0 FALSE_POSITIVE case
- 0 BENIGN_DRIFT case
- 0 single-version case

CCF-B 可投目标：

- case_studies >= 3
- 覆盖至少 2 种 drift type
- 至少 1 个 wrapper-fix-backed case
- 至少 1 个 semantic-review-backed case

## 阶段 9：重新定义最终论文 claim

### 当前可以 claim 的内容

如果阶段 0-8 都完成，可以 claim：

```text
BindDrift separates low-level cross-version drift facts from Rust-impact warnings and prioritizes warnings that reach Rust unsafe calls, safe APIs, or documented contract mappings.
```

可以 claim：

```text
BindDrift reduces the reviewable warning volume by separating low-level drift facts from Rust-impact warnings; the current baseline table does not support a broad ranking-superiority claim.
```

可以 claim：

```text
BindDrift surfaces wrapper-fix-related drift evidence with typed oracle validation.
```

### 仍然不能 claim 的内容

不要 claim：

- proves Rust abstraction unsoundness
- finds all contract drift
- detects real bugs automatically
- guarantees semantic drift

这和现有 scope 一致：项目明确说 Tier2 semantic findings 是 review targets，不是 confirmed bugs。

### 验收标准

论文 introduction / abstract / evaluation 中不得出现：

- bug detector
- soundness proof
- complete detection
- guaranteed stale abstraction

必须出现：

- warning prioritization
- review target
- evidence chain
- cross-version replay
- manual adjudication

## 最终验收矩阵

下面这张表是我建议你作为下一轮冲刺的“总验收标准”。

| 模块 | 最低验收 | CCF-B 可投验收 |
| --- | --- | --- |
| Artifact consistency | 所有 paper tables 来自同一 manifest | paper build 自动检查，不一致直接失败 |
| 主 warnings | >= 50 条 replay warnings | top-100 完整可审 |
| Single-version leakage | 主结果中 0 条 | 主结果和 appendix 分离 |
| Manual review | >= 50 条双人标注 | 100 条双人标注 |
| Agreement | >= 0.75 | >= 0.80 |
| True positives | >= 5 | >= 10 |
| UNCLEAR 占比 | <= 30% | <= 20% |
| Manual P@10 | >= 0.30 | >= 0.40 |
| Manual P@50 | >= 0.15 | >= 0.25 |
| Typed wrapper P@10 | >= 0.30 | >= 0.50 |
| Build oracle | 可为 0，但必须解释 | 若仍为 0，不能作为主指标 |
| Baseline | BindDrift 优于至少 3 个简单 baseline | BindDrift 优于所有主要 baseline |
| Extractor audit | 有表，有人工抽样 | C/Rust extraction precision >= 0.90 |
| Case studies | >= 2 个真阳性 | >= 3 个真阳性，覆盖 >= 2 drift types |

## 推荐执行顺序

严格按这个顺序做，不要跳：

1. `run_manifest` + artifact hard fail
2. `warning_uid` + label join 修复
3. 禁止 single-version warning 进入主实验
4. 重新生成 top-100 replay warning set
5. 双人 manual review + adjudication
6. typed wrapper oracle
7. baseline/ablation 重算
8. extractor audit
9. case study 生成
10. paper claim 收窄与重写

## 下一轮评分目标

如果只完成阶段 0-2：

```text
56 -> 60
```

如果完成阶段 0-5，并拿到非零人工真阳性：

```text
56 -> 65
```

如果完成阶段 0-8，且 baseline 证明 BindDrift 优于简单方法：

```text
56 -> 70+
```

现在最关键的不是再加 detector，而是让审稿人相信：

1. 这些 warnings 是同一个 run 的结果
2. 人工 review 确实评估了这些 warnings
3. 真阳性不是 0
4. BindDrift 比简单 baseline 更会排序
5. case study 不是自动包装出来的 false positive

这五点解决后，BindDrift 才真正进入 CCF-B 可投区间。
