# CCF-B Strict Accept 后续方案

目标不是“把分数写好看”，而是让仓库内置 strict gate、论文主 claim、人工复核、baseline 对比、case studies 和 artifact 复现全部闭环。当前最重要的事实是：项目已经有完整 pipeline 和 20-pair replay 基础，但 `artifact_reproducibility.json` 明确显示 `ccfb_submission_ready=false`、`status=failed`。

我建议把后续工作拆成 8 个强制里程碑。每个里程碑都有 hard acceptance gate，不通过就不能进入下一阶段，也不能写入论文主结果。

## 总目标与不可变 Claim

主 claim 必须固定为：

> BindDrift provides evidence-backed warning prioritization for Rust-for-Linux cross-language API/contract drift.

不能 claim：

- automatic bug detector；
- proves Rust abstraction soundness；
- ranking outperforms all baselines；
- detects many semantic bugs。

仓库 scope 已经明确：BindDrift 是 warning/prioritization artifact，Tier-2 semantic findings 是 review targets，不是 confirmed bugs。

最终 CCF-B strict accept 的目标状态：

| Gate | 当前状态 | Accept 目标 |
| --- | --- | --- |
| `ccfb_submission_ready` | `false` | `true` |
| primary oracle-blind P@10 | 0.20 | >= 0.60，最低 >= 0.50 |
| primary oracle-blind P@20 | 0.10 | >= 0.55，最低 >= 0.45 |
| primary oracle-blind P@50 | 0.04 | >= 0.50，最低 >= 0.42 |
| primary oracle-blind P@100 | 0.02 | >= 0.45，最低 >= 0.40 |
| NDCG@20 | 0.1848 | >= 0.65，最低 >= 0.55 |
| 与 best simple baseline 差距 | 显著落后 | P@20 +0.10、P@50 +0.07、NDCG@20 +0.10 |
| true semantic drift | 2 | >= 8 |
| non-wrapper semantic TP | 2 | >= 5 |
| semantic drift type count | 2 | >= 3 |
| case-study drift type count | 1 | >= 4 |
| manual-review Cohen's kappa | 0.1195 | >= 0.60，目标 >= 0.70 |
| local absolute paths | 存在 | 0 |
| paper/table 数字一致性 | 不一致风险 | 100% generated from manifest/tables |

这些阈值要进入 `strict_validator.py` 和 paper build，不能只作为人工目标。

## 里程碑 0：冻结 Claim、协议和数据边界

### 目的

先防止后续优化变成 p-hacking。当前已经有 `evaluation_protocol.json`，它规定 wrapper-fix/build oracle 只能作为 auxiliary validation，不能进入 primary score。这一点必须继续保留。

### 实施方案

- 冻结 `data/replay/latest/evaluation_protocol.json`。
- 明确三类 split：
  - dev pairs：只允许调参；
  - validation pairs：只允许选择模型；
  - locked test pairs：只允许最终运行一次。
- 将所有主表强制读取：
  - `run_manifest.json`
  - `evaluation_protocol.json`
  - `pooled_review_set.jsonl`
  - `pooled_review_labels.csv`
  - `manual_review.csv`
- 论文所有数字必须来自 `paper/tables/*.json`，禁止手填。
- 修改 paper build：当前 CLI 的 `cmd_paper_build` 只生成 cases 和 tables，不做 strict fail。必须改成调用 strict validator，并在未通过时返回非零 exit code。

### 验收标准

| 检查项 | 必须满足 |
| --- | --- |
| `evaluation_protocol.json` | 存在，`protocol_version=ccfb-strict-v2` |
| oracle policy | wrapper-fix/build oracle 不进入 primary score |
| paper build | 任一 strict gate 失败则 hard fail |
| locked split | locked test 结果只能生成一次，manifest 记录 hash |
| paper 数字 | 与 `paper/tables/*.json` 逐项一致 |
| forbidden claims | draft 不含 “bug detector / proves soundness / outperforms all baselines / complete detection” |
| CI | `uv run pytest` + strict validator 全部通过 |

## 里程碑 1：清理 Canonical Replay 与 Reproducibility

### 当前问题

当前 canonical run 有不错规模：20 pairs、21 versions、16,757 drift facts、320 promoted warnings、100 reviewed warnings、276 pooled labels。但复现层面仍有 local absolute path 问题，`summary.json` 中出现 `/home/nya/...` 路径。strict artifact check 也因为 `no_local_absolute_paths` 失败。

### 实施方案

- 所有 replay/paper/audit 输出统一经过 `sanitize_local_paths`。
- 重新生成：
  - `data/replay/latest/summary.json`
  - `data/replay/latest/run_manifest.json`
  - `paper/tables/artifact_reproducibility.json`
  - `paper/tables/table_index.json`
- 所有 path 字段只允许：
  - repo-relative path；
  - artifact-relative path；
  - `<repo-root>` placeholder。
- 删除或隔离 stale replay runs，避免 table generator 扫到历史失败 run。
- `run_manifest.json` 记录所有主输入文件 sha256。

### 验收标准

| 检查项 | 必须满足 |
| --- | --- |
| local absolute path | 0 个 |
| stale run contamination | 0 个 |
| replay pairs | 20/20 completed |
| failed pairs | 0 |
| canonical run id | exactly one：`latest` 或明确命名的 frozen run |
| manifest hash | 所有主输入文件有 sha256 |
| artifact reproducibility | `passes=true` |
| paper build | 不因路径、缺表、stale run 失败 |

## 里程碑 2：重做 Oracle-Blind Ranking

### 当前问题

这是最大硬伤。当前 strict ranking gate 要求 P@10 >= 0.50、P@20 >= 0.45、P@50 >= 0.42、P@100 >= 0.40、NDCG@20 >= 0.55。但当前 primary oracle-blind ranker 只有：

- P@10 = 0.20；
- P@20 = 0.10；
- P@50 = 0.04；
- P@100 = 0.02；
- NDCG@20 = 0.1848。

更严重的是，它输给 best simple baseline `no_ranking`。当前 delta 是 P@20 -0.40、P@50 -0.22、NDCG@20 -0.3335。

### 根因判断

当前 primary oracle-blind ranker 过度过滤。它只剩 29 个 primary candidates，导致 pooled denominator 下 P@100 必然很差。

同时，旧的 scorer 里存在 `build_oracle_hit` 和 `wrapper_fix_hit` scoring components。这些只能保留为 auxiliary/current ranker，绝不能进入 primary oracle-blind ranker。

### 实施方案

#### 2.1 扩大 Primary Oracle-Blind 候选集

当前 29 个太少。新的 primary ranker 必须输出完整 top-100。

候选条件改为：

```text
Eligible if:
  has C source diff OR binding diff OR semantic indicator
AND
  has direct Rust use OR safe API exposure OR contract evidence OR safety comment proximity
AND
  not oracle-only
AND
  not manual-label-dependent
```

不再因为缺少 safe API 就直接丢弃；safe API 应该提高 rank，而不是决定候选是否存在。

#### 2.2 两阶段 Ranking

第一阶段：eligibility tier。

| Tier | 条件 | 进入 top-100 |
| --- | --- | --- |
| A | C source diff + direct Rust use + safe API/contract evidence | 必须优先 |
| B | C source diff + direct Rust use | 可进入 |
| C | binding diff + direct Rust use + contract evidence | 可进入 |
| D | generated-binding-only / weak graph-only | top-50 禁止，top-100 限制 <= 10% |

第二阶段：within-tier score。

允许特征：

- C source diff strength；
- binding diff strength；
- direct Rust unsafe call；
- safe API exposure；
- safety comment proximity；
- error mapping；
- lifetime/ownership/refcount evidence；
- allocation/free pairing evidence；
- sleepability indicator；
- fanout penalty；
- repeated cross-version occurrence；
- evidence diversity；
- confidence from extractor audit。

禁止特征：

- wrapper-fix label；
- build-breakage oracle；
- manual review label；
- adjudicated label；
- future commit message；
- case-study selection signal。

#### 2.3 从反例 Ranker 学习

当前 `no_graph` ablation 反而 P@10=0.8、NDCG@20=0.5616。这说明 graph gate 可能在误杀好候选。必须做 top-50 error audit：

- primary false positives 为什么排前？
- `no_graph` true positives 为什么 primary 排后或被过滤？
- `binding_diff` 和 `c_signature` 哪些 feature 有用？
- wrapper-fix true positives 中哪些 evidence 在 detection-time 已经可见？

### 验收标准

| 检查项 | 最低线 | 目标线 |
| --- | --- | --- |
| primary candidate count | >= 150 | >= 250 |
| reported top-K | top-100 完整 | top-100 完整 |
| P@10 | >= 0.50 | >= 0.60 |
| P@20 | >= 0.45 | >= 0.55 |
| P@50 | >= 0.42 | >= 0.50 |
| P@100 | >= 0.40 | >= 0.45 |
| NDCG@20 | >= 0.55 | >= 0.65 |
| AUPRC | >= best baseline | best baseline + 0.05 |
| P@20 lift over best baseline | >= +0.10 | >= +0.15 |
| P@50 lift over best baseline | >= +0.07 | >= +0.12 |
| NDCG@20 lift over best baseline | >= +0.10 | >= +0.15 |
| bootstrap CI | delta 下界 > 0 | delta 下界 > 0 |
| significance | p < 0.05 | p < 0.01 |
| oracle leakage | 0 | 0 |
| top-50 generated-binding-only | 0 | 0 |
| top-100 generated-binding-only | <= 10 | <= 5 |
| top-50 score explanations | 100% 非空 | 100% 非空 |

未达到这些标准，论文只能写：

> evidence gate reduces review volume.

不能写：

> BindDrift improves ranking/prioritization.

## 里程碑 3：重建 Pooled Review Evaluation

### 当前问题

当前 pooled review 有 276 条，coverage=1.0，这是好的；但 reviewer agreement 很低：agreement rate=0.2609，Cohen's kappa=0.1195，276 条里 204 个 disagreement。这会让审稿人质疑 label schema。

### 实施方案

- 重新生成 pooled review set，规模提高到 450-600。
- pool 由以下集合 union：
  - top-100 new oracle-blind ranker；
  - top-100 old current ranker；
  - top-100 no-ranking；
  - top-100 binding-diff；
  - top-100 c-signature；
  - top-100 no-graph；
  - top-100 no-impact-gate；
  - semantic-target stratified sample；
  - warning-type stratified sample；
  - pair-level stratified sample。
- 每条 review item 附 evidence packet，但不暴露 ranker 名称。
- 两名 reviewer 独立标注。
- 第三方 adjudication。
- reviewer rubric 必须包含 decision tree，特别区分：
  - `TRUE_SEMANTIC_DRIFT`
  - `TRUE_WRAPPER_FIX`
  - `TRUE_BUILD_BREAKAGE`
  - `BENIGN_DRIFT`
  - `FALSE_POSITIVE`
  - `UNCLEAR`

### 验收标准

| 检查项 | 必须满足 |
| --- | --- |
| pooled review size | 450-600 |
| label coverage | 100% |
| double review | 100% |
| adjudication | 100% |
| blind-to-ranker | `true` |
| Cohen's kappa | >= 0.60，目标 >= 0.70 |
| agreement rate | >= 0.75 |
| adjudication notes missing rate | 0 |
| unclear rate | <= 5%，目标 <= 3% |
| label leakage check | passed |
| ranker top-100 coverage | 每个 ranker >= 95%，目标 100% |
| reviewer disagreement examples | >= 10 个，正文/附录解释 |

如果 kappa 仍低于 0.60，不能把 manual labels 作为强 precision 证据，只能作为 exploratory review。

## 里程碑 4：补强 Semantic Drift 结果

### 当前问题

semantic gate 当前失败。acceptance 要求 true semantic drift、non-wrapper semantic true positives 和 semantic drift type 都过线，但当前只有：

- `true_semantic_drift_count = 2`
- `non_wrapper_semantic_true_positives = 2`
- `semantic_drift_type_count = 2`

### 实施方案

#### 4.1 扩大 Semantic Target Generation

必须覆盖至少 5 类：

- Nullability / error convention drift
- Ownership / refcount drift
- Allocation / free pairing drift
- Sleepability / context drift
- Layout / field semantic drift

每类生成至少 80 个 candidate，优先选 Rust-impact evidence 完整的项。

#### 4.2 加强 Semantic Detectors

新增或加强 detector：

| Detector | 证据来源 |
| --- | --- |
| NullabilityDrift | `NULL_RETURN`、`ERR_PTR_RETURN`、`IS_ERR`、`PTR_ERR`、Option/Result mapping |
| OwnershipRefcountDrift | `REFCOUNT_GET`、`REFCOUNT_PUT`、Clone/Drop/lifetime facts |
| AllocationFreeDrift | `ALLOC`、`FREE`、Drop impl、owned pointer wrapper |
| SleepabilityContextDrift | `MAY_SLEEP`、atomic context comments、unsafe wrapper notes |
| LayoutFieldDrift | struct field add/remove/type change + Rust safe abstraction reachability |

#### 4.3 Review Policy

`TRUE_WRAPPER_FIX` 不能计入 `TRUE_SEMANTIC_DRIFT`。这一点当前表格已经明确区分。

### 验收标准

| 检查项 | 最低线 | 目标线 |
| --- | --- | --- |
| semantic review candidates | >= 400 | >= 600 |
| reviewed semantic targets | >= 200 | >= 300 |
| true semantic drift | >= 8 | >= 12 |
| non-wrapper semantic TP | >= 5 | >= 8 |
| semantic drift types | >= 3 | >= 4 |
| wrapper-fix-only not counted as semantic | 100% | 100% |
| unclear rate | <= 5% | <= 3% |
| false-positive taxonomy | 必须生成 | 必须进入论文 |
| examples per semantic type | >= 2 | >= 3 |
| semantic gate | `passes=true` | `passes=true` |

如果找不到足够 true semantic drift，应主动降级 claim：

> BindDrift supports evidence-backed review prioritization; semantic-drift discovery remains exploratory.

但要冲 strict accept，最好还是达到 semantic gate。

## 里程碑 5：重做 Case Studies

### 当前问题

case-study gate 失败。当前 6 个 case studies 只有 SignatureDrift 一类，positive cases 中 5 个是 `TRUE_WRAPPER_FIX`，只有 1 个 `TRUE_SEMANTIC_DRIFT`。

### 实施方案

重建 case-study selection policy：

- 只能从 locked/adjudicated labels 中选。
- 每个 case 必须有完整 evidence chain：

  ```text
  C API / helper / macro / struct change
  -> generated binding or Rust helper
  -> unsafe Rust use
  -> wrapper / safe API / safety comment / contract mapping
  -> why review is needed
  ```

- positive cases 不允许 unlabeled、unclear、false positive、single-version-only。
- 至少包含一个 negative/failure-analysis case，解释 false positive 来源。
- case artifacts 不能包含 local absolute paths。

### 验收标准

| 检查项 | 必须满足 |
| --- | --- |
| positive case studies | >= 8 |
| negative/failure cases | >= 2 |
| true semantic cases | >= 3 |
| non-wrapper semantic cases | >= 2 |
| wrapper-fix-backed cases | 可以有，但 <= 50% |
| drift target categories | >= 4 |
| raw warning types | >= 3 |
| each case has evidence chain | 100% |
| each case has adjudicated label | 100% |
| false/benign/unclear positive cases | 0 |
| local absolute paths | 0 |
| case-study gate | `passes=true` |

建议 case 组合：

| Case 类型 | 数量 |
| --- | --- |
| Nullability/error convention | 2 |
| Ownership/refcount | 2 |
| Allocation/free | 2 |
| Sleepability/context | 1 |
| Layout/field | 1 |
| Negative/failure analysis | 2 |

## 里程碑 6：Baseline、Ablation 与统计检验重做

### 当前问题

当前 primary ranker 不仅没有超过 baseline，而且显著落后 best simple baseline。所以必须重做 fair baseline evaluation，而不是只修文字。

### 实施方案

所有 ranker 在同一个 pooled label set 上评估：

| Ranker | 用途 |
| --- | --- |
| BindDrift oracle-blind | primary |
| BindDrift current/oracle-assisted | auxiliary only |
| no-ranking | 强 baseline |
| binding-diff | simple baseline |
| c-signature | simple baseline |
| c-indicator | simple baseline |
| rust-use | simple baseline |
| no-graph | ablation |
| no-impact-gate | ablation |
| random | sanity baseline |

必须报告：

- P@10/P@20/P@50/P@100；
- NDCG@20；
- AUPRC；
- label distribution；
- warning volume；
- 95% bootstrap CI；
- paired bootstrap / randomization test against best simple baseline；
- top false-positive taxonomy；
- top false-negative taxonomy。

### 验收标准

| 检查项 | 必须满足 |
| --- | --- |
| all rankers same pool | `true` |
| pool label coverage | >= 95%，目标 100% |
| primary beats best simple baseline | `true` |
| P@20 delta | >= +0.10 |
| P@50 delta | >= +0.07 |
| NDCG@20 delta | >= +0.10 |
| bootstrap CI lower bound | > 0 |
| p-value | < 0.05 |
| random baseline sanity | primary 显著优于 random |
| ablation story | 至少 2 个 ablation 支持设计选择 |
| no oracle leakage | 0 |
| no self-evaluation top-100 only | `true` |

如果不能超过 `no_ranking`，论文必须放弃 ranking claim。

## 里程碑 7：强化 Extractor Audit，但不要过度依赖

### 当前优势

strict extractor audit 是当前最强正面结果。它有 600 samples，overall Cohen's kappa=1.0，并且各类 extractor precision 都通过 gate。

### 后续方案

- 保持这个优势，但增加 failure analysis。
- 为每类 extractor 增加 negative samples。
- 增加 cross-version sampled pairs。
- 对 `promoted_warning_evidence` 单独抽样 100 条，而不是当前 50 条。
- 报告 parser limitations，不要假装 completeness。

### 验收标准

| 检查项 | 最低线 | 目标线 |
| --- | --- | --- |
| total samples | >= 600 | >= 800 |
| promoted warning evidence samples | >= 100 | >= 150 |
| C function precision | >= 0.95 | >= 0.98 |
| C behavior indicator precision | >= 0.85 | >= 0.90 |
| Rust binding use precision | >= 0.90 | >= 0.95 |
| Safe API exposure precision | >= 0.85 | >= 0.90 |
| Error/lifetime fact precision | >= 0.85 | >= 0.90 |
| kappa | >= 0.70 | >= 0.80 |
| failure taxonomy | 必须有 | 进入论文 |

## 里程碑 8：论文重写与 Pre-Submission Red Team

### 当前问题

draft 中存在 stale 数字风险。例如 draft 写 17,867 drift facts、331 promoted warnings，但当前 manifest 是 16,757 drift facts、320 promoted warnings。这种不一致会直接伤害可信度。

### 论文结构建议

#### Abstract

只写最终 strict-passed 数字：

```text
BindDrift replays N Linux release pairs, extracts M drift facts,
promotes K Rust-impact review targets, and improves oracle-blind
top-K prioritization over the strongest simple baseline by ...
```

#### Evaluation 主线

- RQ1：Can BindDrift extract reliable cross-language drift facts?
- RQ2：Does evidence gating reduce review volume while preserving useful targets?
- RQ3：Does oracle-blind ranking improve top-K review yield over strong baselines?
- RQ4：What semantic drift patterns appear in adjudicated cases?
- RQ5：How reproducible is the artifact across versioned toolchains?

#### 必须删除或降级

- “detects bugs”
- “proves soundness”
- “ranking improves prioritization” unless gate passes
- “many semantic bugs” unless semantic gate passes
- “complete detection”

### 验收标准

| 检查项 | 必须满足 |
| --- | --- |
| abstract 数字 | 全部来自 generated tables |
| main tables | 全部有 sha256 provenance |
| RQ 与结果一致 | 100% |
| claims 与 gates 一致 | 100% |
| threats to validity | 明确写 parser incompleteness、label ambiguity、x86_64/Linux-only、oracle limitations |
| artifact guide | 一条命令可复现 main tables |
| README quickstart | 与实际 CLI 一致 |
| paper build | strict gates fail 时 hard fail |
| red-team review | 至少 2 轮，问题清单全部关闭 |

## 最终 Accept 前的硬门槛总表

只有全部满足，才建议以 CCF-B strict accept 标准投稿。

| 类别 | Gate |
| --- | --- |
| Claim | 主 claim 只保留 evidence-backed warning prioritization |
| Ranking | P@10 >= 0.50、P@20 >= 0.45、P@50 >= 0.42、P@100 >= 0.40、NDCG@20 >= 0.55 |
| Baseline | primary oracle-blind 显著优于 best simple baseline |
| Semantic | true semantic drift >= 8，non-wrapper >= 5，types >= 3 |
| Case studies | >= 8 positive，>= 2 negative，>= 4 drift categories |
| Manual review | pooled labels 100% coverage，kappa >= 0.60，adjudication 100% |
| Reproducibility | local absolute paths = 0，manifest/table/draft 一致 |
| Artifact | `ccfb_submission_ready=true` |
| Paper | 无 unsupported claim，无 stale number |
| CI | tests + strict validator + paper build 全通过 |

## 预期评分提升路径

| 阶段 | 预计分数 |
| --- | --- |
| 当前状态 | 64/100 |
| 完成 reproducibility + paper consistency | 67/100 |
| primary oracle-blind ranking 过线 | 72/100 |
| semantic gate 过线 | 75/100 |
| case studies 多样化 + manual review kappa 提升 | 78/100 |
| red-team 后正文/Artifact 全闭环 | 80-82/100 |

最低投稿线：72/100。

严格 CCF-B accept 目标线：78+/100。

当前最关键的两件事是：

1. 让 oracle-blind primary ranker 真正赢过 `no_ranking` / `binding_diff` / `c_signature`。
2. 补出足够多、非 wrapper-only、多类型的 semantic drift evidence 和 case studies。

这两点不过线，其他工程改得再完整，也只能是 borderline artifact，难以 strict accept。
