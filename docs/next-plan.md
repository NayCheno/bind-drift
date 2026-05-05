# BindDrift 下一阶段计划：从 Borderline 推进到严格 CCF-B 可接收

## 总目标

当前 BindDrift 已经达到 CCF-B borderline artifact 水平：系统完整、实验规模可用、manual review 和 run manifest 已经成形。但严格 CCF-B 正会仍会卡在四个问题上：

1. top-K ranking 不够强：当前 P@10 = 0.30，低于 P@100 = 0.37，说明排序没有把真阳性稳定推到前面。
2. true positive 来源偏 wrapper-fix：当前 37 个 true positives 中，35 个是 `TRUE_WRAPPER_FIX`，只有 2 个 `TRUE_SEMANTIC_DRIFT`。
3. case studies 类型单一：当前 4 个 case studies 都是 `SignatureDrift`，不能支撑“多类 API/contract drift”的强 claim。
4. baseline/ranking claim 需要重新设计：当前最强 claim 是 evidence gate，而不是 ranking 全面优于简单 baseline。

下一阶段目标不是扩大 warning 数量，而是完成下面的 CCF-B hard gates：

- 主论文 claim 从 “detect drift” 稳定收窄为 “evidence-backed warning prioritization”
- 主 ranking evaluation 不能使用 wrapper-fix oracle 作为 scoring feature
- top-K 结果必须在 locked pooled review set 上优于强 baseline
- 至少补出多类型、非 wrapper-only 的 true semantic case studies
- 所有表格、case、review、baseline、audit 必须从同一个 manifest 可重复生成
- paper build 必须在不满足验收条件时 hard fail

目标分数：从当前约 66/100 提升到 72+/100。

---

## 阶段 0：冻结 claim、manifest、evaluation split

### 当前问题

现在的结果能支持：

> BindDrift reduces many cross-version drift facts into fewer evidence-backed Rust-impact review targets.

但还不能支持：

> BindDrift is a bug detector.
> BindDrift ranking is broadly superior to all simple baselines.
> BindDrift discovers many new semantic bugs.

如果下一阶段继续调 ranking，同时仍用同一批 top-100 labels 汇报结果，会被 CCF-B 评审认为有 overfitting 风险。

### 修改方案

新增一个冻结文件：

```text
data/replay/latest/evaluation_protocol.json
```

内容包括：

```json
{
  "protocol_version": "ccfb-strict-v1",
  "claim_boundary": "evidence-backed warning prioritization",
  "primary_warning_set": "oracle_blind_ranked_warnings",
  "oracle_usage": {
    "wrapper_fix_oracle": "labels_and_auxiliary_validation_only",
    "build_oracle": "labels_and_auxiliary_validation_only",
    "not_allowed_in_primary_score": true
  },
  "splits": {
    "dev_pairs": ["latest-p001", "latest-p002", "..."],
    "validation_pairs": ["latest-p011", "..."],
    "locked_test_pairs": ["latest-p016", "..."]
  },
  "primary_metrics": [
    "P@10",
    "P@20",
    "P@50",
    "P@100",
    "NDCG@20",
    "AUPRC_on_pooled_review_set"
  ],
  "baseline_metrics": [
    "relative_lift_over_best_simple_baseline",
    "absolute_lift_over_random",
    "warning_volume_reduction"
  ],
  "manual_review_policy": {
    "double_review": true,
    "adjudication_required": true,
    "cohen_kappa_required": true,
    "unclear_is_not_true_positive": true
  }
}
```

同时修改 table generation：

binddrift/paper/tables.py
binddrift/evaluation/evaluator.py
binddrift/evaluation/baselines.py
binddrift/run_manifest.py

所有主表必须读取：

run_manifest.json
evaluation_protocol.json
manual_review.csv
pooled_review_set.jsonl
pooled_review_labels.csv

不能直接读临时 warnings 文件。

### 验收标准

必须全部满足：

存在 data/replay/latest/evaluation_protocol.json
paper/tables/evaluation_summary.json 中包含：
protocol_version
claim_boundary
primary_warning_set
oracle_blind_primary_result
主 paper result 默认使用 oracle-blind ranking。
wrapper-fix/build oracle 不得作为 primary ranking score 的输入。
如果代码检测到 primary score 使用 oracle label 或 wrapper-fix label，paper build hard fail。
pytest tests/test_evaluation_protocol.py tests/test_paper_tables.py 通过。
论文中不得出现以下未被结果支持的强 claim：
bug detector
automatically detects bugs
proves unsoundness
outperforms all baselines
complete detection
paper/draft.md 必须明确写出：
warnings are review targets
not every warning is a confirmed bug
wrapper-fix oracle is auxiliary validation
ranking improvement is evaluated separately from evidence gating

**通过标准：**claim consistency 100%。

## 阶段 1：重做 fair ranking evaluation，避免 top-100 自证

### 当前问题

当前 top-100 manual review 只能说明现有排名下有 37 个 true positives。它不能公平比较不同 ranker，因为 baseline 的 top warnings 可能没有被标注。

严格 CCF-B 评审会问：

你的 baseline top-20 如果没被人工标注，怎么知道 BindDrift 排名真的更好？

### 修改方案

新增 pooled review evaluation。

生成一个固定 review pool：

data/replay/latest/pooled_review_set.jsonl
data/replay/latest/pooled_review_labels.csv
data/replay/latest/pooled_review_manifest.json

pool 构成：

union(
top100(BindDrift-oracle-blind),
top100(BindDrift-current),
top100(BindingDiffOnly),
top100(CSignatureDiffOnly),
top100(CIndicatorOnly),
top100(RustUseOnly),
top100(NoImpactGate),
top100(NoGraph),
top100(NoRanking),
stratified_sample_by_warning_type(120),
stratified_sample_by_version_pair(80)
)

去重后，如果 pool 超过 500 条，按下面规则压缩到 400–500 条：

保留所有 ranker top-20 union
保留所有 non-SignatureDrift candidates
保留所有 candidate with safe API exposure
保留每个 warning type 至少 30 条
其余按 pair/type 分层采样

新增命令：

```bash
python -m binddrift.evaluation.pooled_review \
  --run latest \
  --rankers binddrift_oracle_blind,binddrift_current,binding_diff,c_signature,c_indicator,rust_use,no_graph,no_impact_gate,no_ranking,random \
  --output data/replay/latest/pooled_review_set.jsonl
```

新增评估：

```bash
python -m binddrift.evaluation.evaluate_rankers \
  --pool data/replay/latest/pooled_review_set.jsonl \
  --labels data/replay/latest/pooled_review_labels.csv \
  --protocol data/replay/latest/evaluation_protocol.json \
  --output paper/tables/ranking_pooled_evaluation.json
```

### 验收标准

主结果必须满足最低线：

| 指标                     | 当前参考   | CCF-B 最低验收 | CCF-B 目标 |
| ------------------------ | ---------- | -------------- | ---------- |
| P@10                     | 0.30       | ≥ 0.50         | ≥ 0.60     |
| P@20                     | 未稳定报告 | ≥ 0.45         | ≥ 0.55     |
| P@50                     | 0.36       | ≥ 0.42         | ≥ 0.50     |
| P@100                    | 0.37       | ≥ 0.40         | ≥ 0.45     |
| NDCG@20                  | 未稳定报告 | ≥ 0.55         | ≥ 0.65     |
| unclear rate             | 1%         | ≤ 5%           | ≤ 3%       |
| false positive rate @100 | 27%        | ≤ 25%          | ≤ 20%      |

### Baseline 验收

BindDrift-oracle-blind 在 pooled review set 上必须优于 best simple baseline。
至少满足以下两个条件：
P@20 比 best simple baseline 高 ≥ 0.10
P@50 比 best simple baseline 高 ≥ 0.07
NDCG@20 比 best simple baseline 高 ≥ 0.10
如果不满足，则论文必须降级 claim：
可以说 evidence gate reduces review volume
不可以说 ranking significantly improves prioritization
ranking_pooled_evaluation.json 必须包含每个 ranker 的：
P@10/P@20/P@50/P@100
NDCG@20
true label distribution
warning volume
confidence interval by bootstrap
paired randomization test 或 bootstrap significance against best baseline
bootstrap 95% CI 必须生成并写入表格。
所有 ranker 必须在同一 pooled labels 上评估，不能用各自单独 top-100 labels。
如果 pooled labels 覆盖率低于 95%，paper build hard fail。

**通过标准：**ranking evaluation 可以经受 CCF-B reviewer 复查。

## 阶段 2：修复 ranking 本身，而不是只改表述

### 当前问题

当前 P@10 低说明 score 函数没有把最可靠 warning 放前面。下一阶段要优化 ranker，但必须避免 oracle leakage。

### 修改方案

新增 oracle-blind ranker：

binddrift/ranking/oracle_blind_scorer.py

主 ranking feature 只能使用 detection-time 可获得信息：

允许：

C source diff evidence
binding diff evidence
direct Rust unsafe call evidence
safe API exposure
safety comment proximity
error mapping evidence
lifetime/ownership evidence
type/layout dependency
cross-version stability
warning type reliability prior learned from dev split
symbol-specific fanout
generated-binding-only demotion
multi-evidence agreement

禁止：

wrapper-fix commit label
manual review label
build breakage oracle label
adjudicated label
future commit message indicating fix
post-hoc case-study selection signal

新增 score explanation：

每条 warning 输出：

```json
{
  "score": 12.4,
  "score_components": {
    "c_source_diff": 2.0,
    "rust_direct_use": 2.0,
    "safe_api_exposure": 2.0,
    "contract_evidence": 2.0,
    "multi_evidence_bonus": 1.5,
    "generated_binding_only_penalty": -3.0
  },
  "oracle_blind": true
}
```

新增 ranker audit：

paper/tables/ranking_score_audit.json

它必须报告 top false positives 的主要 score 来源，避免某个 spurious feature 支配排序。

### 排序规则建议

把 score 从简单加权改成两阶段：

第一阶段：eligibility tier
Tier A: C source diff + direct Rust use + safe API/contract evidence
Tier B: C source diff + direct Rust use
Tier C: binding diff + direct Rust use + contract evidence
Tier D: generated-binding-only or weak graph-only

主 top-50 禁止出现 Tier D。

第二阶段：within-tier ranking

按以下顺序打分：

evidence diversity：C diff、Rust use、safe API、safety comment、error mapping、lifetime fact 是否同时出现
Rust abstraction reachability：是否到 public safe API
contract sensitivity：nullability/error/ownership/allocation/sleepability 高于纯 signature churn
historical recurrence：同一 symbol 是否跨版本反复影响 Rust wrapper
fanout penalty：过高 fanout 的 common helper 降权
generated-binding-only penalty：只有 bindgen edge 的强降权

### 验收标准

paper/tables/ranking_score_audit.json 存在。
top-50 中 generated_binding_only warning 数量 = 0。
top-50 中每条 warning 至少满足：
C source evidence 或 semantic indicator evidence
direct Rust use 或 safe API exposure
非空 score_components
primary ranker 的 oracle_blind == true。
primary ranker 结果达到阶段 1 的最低 top-K 指标。
top-20 false positives 必须生成 failure analysis：
paper/analysis/top20_false_positive_analysis.md
如果 P@10 仍低于 0.50，论文不得声称 ranking improvement，只能保留 evidence gate claim。

**通过标准：**ranking 不再是 CCF-B 最大弱点。

## 阶段 3：增加非 wrapper-only、非 SignatureDrift 的 semantic true positives

### 当前问题

当前 37 个 true positives 中，35 个是 wrapper-fix-backed，只有 2 个 semantic-review-backed。case studies 也集中在 SignatureDrift。这会让审稿人认为 BindDrift 主要是在找历史 wrapper fixes，而不是发现 cross-language semantic contract drift。

### 修改方案

新增 semantic drift mining pass：

binddrift/detectors/semantic_review_targets.py

重点挖掘以下类别：

NullabilityDrift
NULL / ERR*PTR / IS_ERR / PTR_ERR / nullable pointer convention
Rust side Option, Result, to_result, from_err_ptr
OwnershipRefcountDrift
get_device, put_device, kref_get, kref_put, refcount_inc, refcount_dec
Rust side Drop, ARef, lifetime wrapper
AllocationFreeDrift
kmalloc, kzalloc, devm*\*, kfree, release callback
Rust side allocator wrapper, Drop, Box, ownership transfer
SleepabilityContextDrift
might_sleep, GFP_KERNEL, lock context, atomic context
Rust side safety comment or wrapper function marked usable in context
LayoutFieldDrift
C struct field addition/removal/retype
Rust side field access, offset assumption, wrapper invariant

新增 targeted review set：

data/replay/latest/semantic_target_review_set.jsonl
data/replay/latest/semantic_target_review.csv
paper/tables/semantic_drift_review_summary.json

采样策略：

top50 semantic candidates by oracle-blind score

- 20 NullabilityDrift
- 20 OwnershipRefcountDrift
- 20 AllocationFreeDrift
- 20 SleepabilityContextDrift
- 20 LayoutFieldDrift

每类不足则全部纳入，并在表格中报告不足原因。

### 验收标准

最低 CCF-B 验收：

至少找到 8 个 TRUE_SEMANTIC_DRIFT。
其中至少 5 个不是 wrapper-fix-backed。
至少覆盖 3 个 drift types。
每个 true semantic drift 必须有：
old/new C evidence
Rust side usage evidence
contract mapping evidence
reviewer adjudication notes
semantic_drift_review_summary.json 必须报告：
candidates reviewed
true semantic drift count
type distribution
false positive taxonomy
examples not used as case studies
如果 true semantic drift < 5，则论文必须把 semantic drift claim 降级为 exploratory。
如果 true semantic drift ≥ 8，论文可以把 semantic review targets 作为次要贡献。
不允许把 TRUE_WRAPPER_FIX 计入 TRUE_SEMANTIC_DRIFT。

目标 CCF-B 验收：

≥ 12 个 TRUE_SEMANTIC_DRIFT
≥ 4 个 drift types
≥ 3 个非-wrapper case studies

**通过标准：**BindDrift 不再只像 wrapper-fix recovery 工具。

## 阶段 4：重做 case studies，满足 CCF-B 说服力

### 当前问题

当前 case studies 已经绑定 true positives，这是正确的；但类型全部集中在 SignatureDrift，不足以支撑论文广度。

### 修改方案

生成新的 case suite：

paper/cases/case-01-...
paper/cases/case-02-...
...
paper/cases/case-08-...
paper/tables/case_study_summary.json

case 选择规则：

must be adjudicated true positive
must be eligible_for_main_warning
must have old_version and new_version
must have pair_id
must not be generated-binding-only
must include C-side evidence
must include Rust-side dependency evidence
must include reviewer adjudication note

case suite 至少包括：

2 SignatureDrift
1 NullabilityDrift
1 OwnershipRefcountDrift
1 AllocationFreeDrift
1 LayoutFieldDrift or FieldDrift
1 SleepabilityContextDrift if available
1 failure case or benign drift analysis

如果某类没有 true positive，必须写入：

paper/analysis/missing_case_types.md

并解释为什么没有。

case 文件必须包含

每个 case 必须有固定模板：

```markdown
# Case Title

## Summary

## Old Version Evidence

## New Version Evidence

## C-Side Diff

## Rust-Side Dependency

## Safe API / Contract Assumption

## Manual Review Label

## Why This Is Not Generated-Binding-Only

## Why Compiler Alone Does Not Catch It

## Alternative Explanation Considered

## Maintainer Review Implication

## Reproduction Pointers
```

额外修复

当前 case 输出中不应出现本机绝对路径，例如：

/home/...
/Users/...
/tmp/...

所有路径必须转为 repo-relative 或 kernel-tree-relative。

### 验收标准

至少 6 个 case studies。
至少 3 个 drift types。
至少 2 个 TRUE_SEMANTIC_DRIFT case。
至少 2 个 wrapper-fix-backed case。
至少 1 个 negative/failure-analysis case，用来解释 false positive 或 benign drift。
所有 case 必须来自 adjudicated labels。
case_study_summary.json 中：
case_studies >= 6
drift_type_count >= 3
semantic_true_cases >= 2
false_positive_cases == 0 for positive cases
benign_drift_cases == 0 for positive cases
unlabeled_cases == 0
absolute_local_paths == 0
如果 case type count < 3，paper build hard fail。
如果没有 negative/failure case，paper build warning；主论文必须至少在 threats/failure analysis 中补充。

**通过标准：**case studies 能支撑“cross-language contract drift”而不只是 signature change。

## 阶段 5：baseline 和 ablation 改成审稿人无法轻易反驳的版本

### 当前问题

简单 baseline 如果没有公平评估，会让 reviewer 质疑：

是不是 grep Rust use + C signature diff 就够了？

### 修改方案

保留并强化以下 baseline：

BindingDiffOnly
CSignatureDiffOnly
CIndicatorOnly
RustUseOnly
CSignaturePlusRustUse
NoGraph
NoImpactGate
NoTier2
NoRanking
Random
OracleBlindBindDrift
FullBindDriftWithOracleAuxiliary

注意：

FullBindDriftWithOracleAuxiliary 只能放 appendix 或 auxiliary validation。
OracleBlindBindDrift 是主表默认。
baseline 和 BindDrift 必须在同一 pooled review set 上评估。

新增表：

paper/tables/baseline_strict_comparison.json
paper/tables/ablation_strict_comparison.json
paper/tables/warning_volume_reduction.json

每个 baseline 必须报告：

```json
{
  "ranker": "CSignaturePlusRustUse",
  "candidate_count": 1234,
  "review_pool_covered": 0.98,
  "p_at_10": 0.4,
  "p_at_20": 0.35,
  "p_at_50": 0.32,
  "p_at_100": 0.3,
  "ndcg_at_20": 0.5,
  "bootstrap_ci": {
    "p_at_20": [0.25, 0.45]
  },
  "relative_lift_against_binddrift": -0.1
}
```

### 验收标准

所有 baseline 使用同一个 pooled label set。
best simple baseline 必须明确标出。
BindDrift-oracle-blind 至少在 P@20 或 NDCG@20 上显著优于 best simple baseline。
如果显著性不足，论文必须改写为：
evidence gate improves candidate quality / volume
ranking remains future work
NoImpactGate 应该显著恶化 precision 或显著扩大 warning volume。
NoGraph 应该显著降低 Rust-impact precision 或 recall proxy。
NoTier2 应该降低 semantic drift coverage。
所有 baseline 表必须由脚本生成，禁止手写。
tests/test_baselines_strict.py 必须检查：
baseline 列表完整
metric 字段完整
pooled labels 一致
no oracle leakage in primary baseline comparison

**通过标准：**baseline 不再是论文软肋。

## 阶段 6：extractor audit 从“有样本”升级为“可信测量”

### 当前问题

C/Rust extractor 仍偏 heuristic。CCF-B 评审会问：

如果 extractor 是 regex，那么结果是不是由 extractor error 主导？

### 修改方案

扩展 extractor audit：

data/audit/strict_extractor_sample.csv
data/audit/strict_extractor_review.csv
paper/tables/strict_extractor_audit.json

采样至少 600 条：

100 C functions
100 C behavior indicators
100 Rust binding uses
100 Rust safe API exposures
75 Rust error mappings
75 Rust lifetime/ownership facts
50 promoted warning evidence chains

每条 audit row 包含：

sample_id
extractor_name
version
file
line
symbol
extracted_fact
raw_context
reviewer1_label
reviewer2_label
adjudicated_label
error_category
notes

错误类别：

PARSE_ERROR
SYMBOL_MISMATCH
LINE_MISMATCH
GENERATED_BINDING_CONFUSION
COMMENT_ASSOCIATION_ERROR
FALSE_USAGE_EDGE
FALSE_CONTRACT_MAPPING
MISSING_CONTEXT
OTHER

### 验收标准

最低 CCF-B 验收：

| extractor                        | precision 最低要求 |
| -------------------------------- | ------------------ |
| C functions                      | ≥ 0.95             |
| Rust binding uses                | ≥ 0.90             |
| C behavior indicators            | ≥ 0.85             |
| Rust error mappings              | ≥ 0.85             |
| Rust lifetime facts              | ≥ 0.80             |
| promoted warning evidence chains | ≥ 0.85             |

其他要求：

总样本数 ≥ 600。
每个 extractor 至少 50 条样本。
Cohen’s kappa ≥ 0.70。
如果 agreement rate = 1.0，必须同时报告 kappa；不能只报告 agreement。
promoted warning evidence chain precision < 0.85 时，paper build hard fail。
每类 extractor 的主要错误类别必须写入 paper/analysis/extractor_error_taxonomy.md。
如果某 extractor precision < 阈值，主论文中对应 detector claim 必须降级。

**通过标准：**heuristic extractor 的威胁被量化，而不是口头承认。

## 阶段 7：manual review 质量控制升级

### 当前问题

当前 review 有 double labels 和 adjudication，但严格 CCF-B 还会关心：

reviewer 是否独立
label guide 是否固定
disagreement 如何处理
unclear 是否算 true positive
是否存在 label leakage

### 修改方案

新增 review guide：

docs/manual-review-guide.md

必须定义：

TRUE_SEMANTIC_DRIFT
TRUE_WRAPPER_FIX
BENIGN_DRIFT
FALSE_POSITIVE
UNCLEAR

并明确：

UNCLEAR is not counted as true positive
TRUE_WRAPPER_FIX and TRUE_SEMANTIC_DRIFT are reported separately
wrapper-fix-backed labels are auxiliary validation
semantic true positives require human contract reasoning

新增 review quality summary：

paper/tables/manual_review_quality.json

包含：

```json
{
  "reviewed_warnings": 100,
  "reviewers": 2,
  "adjudicated": true,
  "agreement_rate": 0.82,
  "cohen_kappa": 0.74,
  "disagreements": 18,
  "unclear_count": 3,
  "label_leakage_check": "passed"
}
```

### 验收标准

所有主结果 labels 必须有 adjudicated label。
UNCLEAR 不计入 TP。
TRUE_WRAPPER_FIX 和 TRUE_SEMANTIC_DRIFT 分开报告。
Cohen’s kappa 必须报告。
reviewer disagreement examples 至少写 5 个。
review guide 必须随 artifact 提交。
review CSV 必须包含：
warning_uid
pair_id
warning_id
ranker_source
type
symbol
reviewer1_label
reviewer2_label
adjudicated_label
adjudication_notes
如果 adjudication_notes 缺失率 > 20%，paper build hard fail。
如果 pooled review set 的 label coverage < 95%，paper build hard fail。

**通过标准：**manual review 能经受审稿人质疑。

## 阶段 8：复现性和 artifact packaging 达到 CCF-B artifact evaluation 标准

### 当前问题

当前 manifest 已经有进展，但 CCF-B artifact 需要“一键重建主表”和“失败时可解释”。

### 修改方案

新增顶层命令：

make reproduce-paper
make check-artifact
make build-paper-tables
make validate-ccfb

或等价 Python 命令：

python -m binddrift.artifact reproduce
python -m binddrift.artifact validate --strict-ccfb

新增 strict validator：

binddrift/artifact/strict_validator.py

它检查：

run_manifest exists
evaluation_protocol exists
all canonical files exist
all sha256 match
paper tables regenerate byte-for-byte
manual labels cover warning set
pooled labels cover ranker outputs
case studies match adjudicated labels
no absolute local paths
no oracle leakage in primary ranking
all tests pass
all required paper tables exist

新增 artifact report：

paper/tables/artifact_reproducibility.json

### 验收标准

clean checkout 后能生成全部 paper tables。
paper/tables/table_index.json 包含所有主表。
所有主表都有 provenance：
source files
sha256
generation command
protocol version
make validate-ccfb 或等价命令通过。
output 中不得包含本机绝对路径。
不允许 paper 表格中的数字与 manifest 不一致。
不允许 case study label 与 manual review label 不一致。
不允许 runtime scalability 的 warning count 与 evaluation summary 口径混淆。
CI 至少运行：
unit tests
table generation tests
manifest validation tests
claim-boundary tests
no-local-path tests
如果没有 CI，README 必须提供本地可执行的 exact commands，并附最新运行日志摘要。

**通过标准：**artifact 进入 CCF-B 可审查状态。

## 阶段 9：论文重写为“结果驱动”，避免过度承诺

### 当前问题

当前论文已经收窄 claim，这是对的。下一步要把弱点主动写清楚，否则 reviewer 会替我们写。

### 修改方案

论文核心叙事改为：

Problem:
Rust safe abstractions depend on evolving C APIs/contracts.

Challenge:
Most C/bindgen changes are irrelevant to Rust safe abstractions.

Contribution:
BindDrift separates drift facts from Rust-impact warnings using evidence chains.

Main result:
Evidence gate reduces 17,867 drift facts to 331 promoted warnings and yields useful review targets.

Ranking result:
Oracle-blind ranking improves or does not improve over baselines depending on strict pooled evaluation.
Only claim improvement if strict metrics pass.

Semantic result:
Report true semantic drift separately from wrapper-fix-backed validation.

Limitations:
Warnings are not bugs.
Extractor is heuristic.
Linux/Rust-for-Linux only.
Case coverage is limited unless phase 4 passes.

必须新增/重写以下章节：

3. Claim Boundary
   5.1 Evaluation Protocol
   5.2 Pooled Manual Review
   5.3 Oracle-Blind Ranking
   5.4 Evidence Gate Ablation
   5.5 Semantic Drift Review
   5.6 Extractor Audit
4. Case Studies
5. Failure Analysis
6. Threats to Validity

### 验收标准

Abstract 不得声称 automatic bug detection。
Introduction 必须定义 review target。
Evaluation 必须区分：
drift facts
promoted warnings
paper top-k
pooled review set
Results 必须单独报告：
wrapper-fix TP
semantic TP
benign drift
false positive
unclear
Baseline section 必须写明 best simple baseline。
Ranking section 不得使用 oracle-backed score 作为主结果。
Failure analysis 至少包括：
top false positives
benign drifts
missed semantic cases
extractor errors
Threats to validity 必须包括：
oracle bias
manual review subjectivity
extractor heuristic error
Linux-only external validity
overfitting risk
tests/test_paper_claims.py 必须检查 forbidden phrases。
如果 strict ranking metrics 没过，论文必须降级 ranking claim。

**通过标准：**论文 claim 和实验证据完全对齐。

## 最终 CCF-B Gate

只有全部通过时，才建议投 CCF-B 正会。

### Hard Gate A：主结果

必须满足：

drift_facts >= 15000
promoted_warnings between 200 and 600
paper_topk >= 100
pooled_review_labels >= 400 or justified >= 300
P@10 >= 0.50
P@20 >= 0.45
P@50 >= 0.42
P@100 >= 0.40
NDCG@20 >= 0.55
false_positive_rate@100 <= 0.25
unclear_rate <= 0.05

### Hard Gate B：baseline

必须满足至少两个：

BindDrift P@20 - best_simple_baseline P@20 >= 0.10
BindDrift P@50 - best_simple_baseline P@50 >= 0.07
BindDrift NDCG@20 - best_simple_baseline NDCG@20 >= 0.10
NoImpactGate warning volume >= 3x BindDrift warning volume
NoImpactGate precision <= BindDrift precision - 0.10

如果不满足，仍可投稿，但必须降级为 artifact/workshop 风格，不建议按 CCF-B 正会主 claim 投稿。

### Hard Gate C：semantic evidence

必须满足：

TRUE_SEMANTIC_DRIFT >= 8
non_wrapper_semantic_true_positives >= 5
semantic_drift_types >= 3

如果不满足，semantic drift 只能作为 exploratory result。

### Hard Gate D：case studies

必须满足：

positive_case_studies >= 6
case_drift_types >= 3
semantic_true_cases >= 2
wrapper_fix_backed_cases >= 2
unlabeled_positive_cases == 0
false_positive_positive_cases == 0
benign_positive_cases == 0
absolute_local_paths == 0

### Hard Gate E：artifact

必须满足：

run_manifest valid
evaluation_protocol valid
paper tables regenerate
manual labels joined by warning_uid
pooled review coverage >= 95%
case labels match manual review
no oracle leakage in primary ranking
no local absolute paths
all tests pass

### Hard Gate F：paper claim

必须满足：

No automatic bug detection claim
No soundness proof claim
No complete detection claim
No ranking superiority claim unless strict baseline gate passes
All limitations explicitly discussed
All numbers generated from artifact

## 推荐提交顺序

### PR 1：protocol + oracle-blind primary result

文件：

data/replay/latest/evaluation_protocol.json
binddrift/evaluation/protocol.py
binddrift/ranking/oracle_blind_scorer.py
tests/test_evaluation_protocol.py
tests/test_oracle_blind_ranking.py

验收：primary ranking 不使用 wrapper-fix/manual/build oracle。

### PR 2：pooled review set + fair baseline evaluation

文件：

binddrift/evaluation/pooled_review.py
binddrift/evaluation/evaluate_rankers.py
data/replay/latest/pooled_review_set.jsonl
data/replay/latest/pooled_review_labels.csv
paper/tables/ranking_pooled_evaluation.json
paper/tables/baseline_strict_comparison.json
tests/test_pooled_review.py
tests/test_baselines_strict.py

验收：所有 ranker 在同一 label pool 上比较。

### PR 3：ranking repair + score audit

文件：

binddrift/ranking/oracle_blind_scorer.py
paper/tables/ranking_score_audit.json
paper/analysis/top20_false_positive_analysis.md
tests/test_ranking_score_audit.py

验收：top-50 无 generated-binding-only，P@10 达到最低标准或降级 claim。

### PR 4：semantic target review

文件：

binddrift/detectors/semantic_review_targets.py
data/replay/latest/semantic_target_review_set.jsonl
data/replay/latest/semantic_target_review.csv
paper/tables/semantic_drift_review_summary.json
tests/test_semantic_review_targets.py

验收：至少 8 个 TRUE_SEMANTIC_DRIFT，否则降级 semantic claim。

### PR 5：case suite rebuild

文件：

binddrift/paper/cases.py
paper/cases/\*.md
paper/tables/case_study_summary.json
paper/analysis/missing_case_types.md
tests/test_cases.py

验收：至少 6 个 positive cases，至少 3 个 drift types，无本机绝对路径。

### PR 6：strict extractor audit

文件：

binddrift/paper/audit.py
data/audit/strict_extractor_sample.csv
data/audit/strict_extractor_review.csv
paper/tables/strict_extractor_audit.json
paper/analysis/extractor_error_taxonomy.md
tests/test_extractor_audit.py

验收：promoted warning evidence chain precision ≥ 0.85。

### PR 7：artifact validator + paper rewrite

文件：

binddrift/artifact/strict_validator.py
paper/draft.md
paper/tables/artifact_reproducibility.json
tests/test_paper_claims.py
tests/test_artifact_validator.py

验收：validate-ccfb 全通过，论文 claim 与结果一致。

## 最终判断规则

完成后重新评分：

< 68: 不建议投 CCF-B 正会，只适合 workshop/artifact/demo
68–71: CCF-B borderline，可投但风险高
72–75: CCF-B weak accept 区间，可认真投
76+: CCF-B strong borderline / accept 区间

如果所有 hard gates 通过，目标评分应为：

问题重要性: 8/10
创新性: 10/15
方法完整性: 15/20
实验设计: 17/20
结果强度: 12/15
复现性: 9/10
论文表达: 8/10
总分: 79/100 上限

如果只完成 protocol、pooled review、artifact validator，但 ranking 和 semantic case 没过，预期评分：

约 69–71/100

如果 ranking P@10 提升到 ≥ 0.50，semantic true positives ≥ 8，case types ≥ 3，预期评分：

约 72–75/100
