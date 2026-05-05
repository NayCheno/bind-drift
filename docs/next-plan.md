# BindDrift 下一阶段整改计划

## 当前最大问题排序

### 1. Ranking 目标失败

当前 high score / top warnings 大量是 false positive 或 benign drift。manual review 前几十条几乎都是 generated-binding-only、缺 source diff、缺 Rust contract evidence。

对 warning / prioritization paper 来说，top-K precision 比 total recall 更关键；现在 top-K 表现不能支撑 claim。

### 2. Exposure gate 太弱

Tier1 会对 generated bindings / C facts 的新增、删除、签名、字段、macro 变化直接出 warning，再用 graph exposure 加分。

但 review 反复说明：generated binding edge alone 不足以说明 Rust safe abstraction 受到影响。应该把 generated-binding-only warning 降级为 fact report，而不是 high-risk warning。

### 3. 提取器仍偏启发式

C parser 是正则；C behavior indicator 是 keyword list；Rust extractor 也是正则扫描 `bindings::`、`pub fn`、`SAFETY` comments、`Result` / `Option` / lifetime patterns。

这可以作为 pilot，但 CCF-B 主实验需要更强的 validation，至少要证明这些 heuristic 的误差不会主导结果。

### 4. Ground truth 不够强

build breakage events 为 0，wrapper-fix precision 极低，人工真阳性只有 2。

目前系统更像“发现大量 candidate drift facts”，而不是“有效发现 Rust-facing contract drift”。

## 总体策略

当前系统的问题本质是：drift fact 层和 warning 层混在了一起。

现在 Tier1 发现 binding / C facts 变化后会直接生成 warning。例如 `SignatureDrift` 对 binding function 的新增、删除、签名变化都会直接 `_add_warning`，只附上 graph exposure。`FieldDrift`、`LayoutDrift`、`MacroConstDrift` 也类似。而 graph exposure 当前又使用 `LIKE` 做模糊匹配，容易把不相关名字连上。

整改核心：

> 先产出 drift facts；只有通过 Rust-impact evidence gate 的 facts 才能升级成 paper warning。

整改后应该形成两层输出：

| 输出层 | 定义 | 论文用途 |
| --- | --- | --- |
| Drift Facts | 低门槛、完整记录 C / bindgen / API / layout / macro / indicator 的版本变化 | 可作为 appendix / reporting，不参与 precision 主指标 |
| Rust-Impact Warnings | 高门槛，只保留确实触达 Rust unsafe call、safe API、safety comment、error / lifetime mapping、wrapper fix 或 build oracle 的 warning | 论文主指标只评估这一层 |

## 方案一：把 Tier1 改成 fact producer

### 当前问题

Tier1 会把 binding function 新增/删除直接作为 `SignatureDrift` warning，例如 `old = absent`、`new = added` 也进入 warning。

这正是 `up`、`down`、`force_sig` 这类 false positive 的来源：它们很多只是 generated binding 覆盖变化，而不是 Rust safe abstraction contract drift。

### 修改方法

新增一个中间结构：`drift_fact`。

建议 warning dict 增加字段：

```json
{
  "record_kind": "fact",
  "promotion_status": "unpromoted",
  "fact_source": "binding_diff | c_api_diff | layout_diff | macro_diff | behavior_indicator_diff",
  "c_evidence_level": "binding_only | c_source_diff | c_behavior_indicator | build_oracle | wrapper_fix",
  "rust_impact_level": "none | generated_binding | direct_unsafe_call | safe_api | contract_mapping | oracle_confirmed",
  "promotion_reasons": [],
  "demotion_reasons": []
}
```

Tier1 改动原则：

| Drift 类型 | 仍然记录 fact | 直接升级 warning 条件 |
| --- | --- | --- |
| `SignatureDrift` from `binding_functions` | 是 | 需要 C source signature diff 或 build / wrapper oracle；仅 binding absent / added 不升级 |
| `SignatureDrift` from `c_functions` | 是 | 需要 direct Rust use 或 safe API exposure |
| `FieldDrift` | 是 | 需要 Rust 侧字段 / layout 依赖证据；否则 fact only |
| `LayoutDrift` | 是 | 需要 Rust 侧 type / layout / safety dependency；否则 fact only |
| `MacroConstDrift` | 是 | 需要 Rust 侧 const use 或 safe API / safety comment；否则 fact only |
| `HelperDrift` | 是 | helper symbol 被 Rust wrapper 使用时升级 |

具体改法：

在 `binddrift/detectors/tier1.py` 中，不要在 `_add_warning` 里直接写入最终 warnings。把 `_make_warning` 拆成两个函数：

```python
def _make_drift_fact(...):
    return {
        "record_kind": "fact",
        "type": drift_type,
        "c_side": {...},
        "rust_side": {...},
        "promotion_status": "unpromoted",
        ...
    }


def _promote_fact_if_impactful(conn, fact, version):
    impact = compute_rust_impact(conn, fact, version)
    if impact["eligible"]:
        return make_warning_from_fact(fact, impact)
    return fact
```

然后 Tier1 输出两份：

```text
data/drift_facts.jsonl
data/warnings.jsonl
```

论文主实验只用 `warnings.jsonl`。`drift_facts.jsonl` 可以作为 appendix / reporting，不参与 precision 主指标。

### 接受标准

这一步完成后，top warnings 中不应该再出现下面这种 warning：

```text
old = absent
new = added
rust_side 只有 graph_edges / generation edge
```

它们应该降级为 `fact_only`。

## 方案二：重写 Rust-impact gate

### 当前问题

Tier2 已经比 Tier1 严一点：它要求 symbol 在 `rust_binding_uses` 中有 exposure；对 `Nullability` / `Error` 还要求 Rust mapping，对 `Ownership` / `Allocation` 要求 lifetime evidence。

这个方向是对的，但 Tier1 没有类似 gate；ranking 还会把 graph edge count 当 Rust exposure 加分。

### 修改方法

新增统一模块：

```text
binddrift/evidence/impact.py
```

核心函数：

```python
def compute_rust_impact(conn, version: str, symbol: str, drift_type: str) -> dict:
    ...
```

输出：

```json
{
  "eligible": true,
  "impact_level": "safe_api",
  "direct_uses": [],
  "safe_apis": [],
  "safety_comments": [],
  "error_mappings": [],
  "lifetime_facts": [],
  "oracle_hits": [],
  "reasons": [
    "direct_binding_use",
    "exposes_safe_api",
    "has_safety_comment"
  ]
}
```

### 统一 promotion rule

一个 drift fact 只有满足下面至少一类证据，才能进入 warnings：

- direct Rust unsafe call：`rust_binding_uses.binding_symbol == symbol`，并且不是 generated binding 文件本身。
- safe API exposure：graph 中存在 `RustUnsafeCall -> RustSafeAPI`。
- contract evidence：存在 safety comment、error mapping、lifetime fact。
- oracle evidence：命中 build breakage 或 wrapper fix。
- helper evidence：`rust/helpers` 改动且被 Rust wrapper 或 safe API 间接使用。

不能作为 promotion 条件的证据：

```text
CFunction -> RustBindingFunction GENERATED_FROM
```

这个只能说明 bindgen 生成了 binding，不能说明 Rust safe abstraction 受影响。当前 graph builder 会为 binding functions 建 `GENERATED_FROM` 边。这类边应记为 background edge，而不是 Rust-impact evidence。

### 分类型 gate

#### `SignatureDrift`

升级 warning 需要：

```text
C source signature changed
AND
Rust direct use OR safe API OR build / wrapper oracle
```

如果只是：

```text
binding absent -> added
binding present -> removed
```

则默认 fact only。只有命中 build breakage 或 wrapper fix 才升级。

#### `FieldDrift` / `LayoutDrift`

升级 warning 需要：

- Rust side depends on struct layout / field。
- safe abstraction mentions the type。
- wrapper fix / build failure references the type。

否则就是 C / bindgen fact，不是 warning。

#### `MacroConstDrift`

升级 warning 需要：

- Rust code actually uses the const / macro binding。
- safe abstraction / safety comment / error mapping references it。

否则 fact only。

#### `NullabilityDrift` / `ErrorDrift`

保留 Tier2 当前思路，但再加一条：

```text
C indicator changed across versions
```

不要只因为新版本扫描到了 `NULL_RETURN` / `ERROR_CODE` 就出 warning。当前 Tier2 使用 `changed = indicators - old_set`，方向是对的。但要排除 old version 缺失导致的伪变化，并把 indicator confidence 纳入 gate。

#### `OwnershipRefcountDrift` / `AllocationFreePairingDrift`

保留 lifetime evidence gate，但禁止只靠函数名模式。当前 `_rust_lifetime` 会在没有 facts 时回退到函数名包含 `drop`、`clone`、`get`、`put`、`new`、`free`、`release` 等模式。

这个 fallback 可以保留，但只能作为 weak evidence，不能单独 promotion；必须搭配 direct use 或 safety comment。

## 方案三：修复 symbol matching，禁止 substring 误连

### 当前问题

两个地方风险最大：

- Tier1 `_graph_exposure` 用 `src LIKE ? OR dst LIKE ?`。
- graph query 也用 `node_id LIKE "%:{target}%"`。

其中 `dst LIKE "%:{symbol}%"` 会导致 substring 误连。这会导致 `d_alloc` 与 `dealloc` 这类名字相近但语义无关的误连。

### 修改方法

引入 canonical symbol key：

```python
@dataclass(frozen=True)
class SymbolKey:
    kind: Literal[
        "c_function",
        "c_struct",
        "c_macro",
        "rust_binding_fn",
        "rust_binding_struct",
        "rust_binding_const",
    ]
    name: str
    namespace: str | None = None
```

统一编码：

```text
c_function:foo
c_struct:struct foo
c_macro:FOO
rust_binding_fn:foo
rust_binding_struct:foo
rust_binding_const:FOO
```

graph `node_id` 不再直接拼 `node_type:label`，而是使用 canonical key：

```python
def canonical_node_id(node_type, label):
    return f"{node_type}:{normalize_exact(label)}"
```

查询时只允许 exact match：

```sql
SELECT *
FROM graph_nodes
WHERE version_id = ?
  AND node_id = ?
```

如果需要模糊搜索，只能在 CLI `query_graph` 中作为人工检索功能使用，不能进入 detector / ranking。

### 具体替换

把 Tier1 里的：

```python
_graph_exposure(conn, selected_new, symbol)
```

改成：

```python
_exact_graph_exposure(conn, selected_new, canonical_symbol_id(symbol))
```

把：

```sql
src LIKE ? OR dst LIKE ?
```

改成：

```sql
src = ? OR dst = ?
```

如果要找从 `CFunction` 到 `RustBindingFunction` 的路径，就显式查：

```sql
src = 'CFunction:<symbol>'
OR dst = 'RustBindingFunction:<symbol>'
```

不要用 `%symbol%`。

### 接受标准

新增单元测试：

```python
def test_no_substring_symbol_match():
    # d_alloc should not match dealloc
    ...
```

测试里构造：

```text
CFunction:d_alloc
RustSafeAPI:dealloc
```

期望：

```python
compute_rust_impact("d_alloc").eligible == False
```

## 方案四：重写 ranking，让 top-K 优先真实 Rust-impact

### 当前问题

当前 ranking 的公式会把 drift severity、edge count、unsafe、contract、helper、historical、build 等简单加权。问题是：

- `SignatureDrift` 基础 severity 很高。
- edge count 也能加 exposure 分。
- `SignatureDrift` / `LayoutDrift` / `FieldDrift` 还有 build 分。
- generated-binding-only 也可能被排到很前。

这解释了为什么 top warnings 中大量 `old = absent`、`new = added` 被高排。

### 修改方法

改为 “gate first, score second”。

第一层：eligibility。

```python
if not warning["promotion_status"] == "promoted":
    continue
```

第二层：重新设计 score。

```text
score =
    4.0 * direct_rust_use
  + 4.0 * safe_api_exposure
  + 3.0 * contract_mapping
  + 3.0 * safety_comment
  + 3.0 * c_source_diff_strength
  + 5.0 * build_oracle_hit
  + 4.0 * wrapper_fix_hit
  + 2.0 * multi_version_consistency
  + 1.0 * indicator_confidence
  - 5.0 * binding_only_penalty
  - 3.0 * added_symbol_without_old_c_evidence_penalty
  - 3.0 * weak_name_match_penalty
  - 2.0 * no_evidence_chain_penalty
```

风险等级：

```text
High:
  score >= 12
  and safe_api_exposure or contract_mapping or oracle_hit

Medium:
  score >= 8
  and direct_rust_use

Low:
  promoted but only weak Rust evidence
```

重点惩罚项：

```text
binding_only_penalty = 1
```

当 warning 只有 `GENERATED_FROM` graph edge，没有 `rust_binding_uses`、safe API、safety comment、mapping、oracle 时，直接降级，不参与主 ranking。

```text
added_symbol_without_old_c_evidence_penalty = 1
```

对 `old = absent`、`new = added` 的 binding diff，如果没有 C source diff 或 Rust wrapper change，直接降级。

### 接受标准

重排后，manual review 的 top-50 应该满足：

| 指标 | 目标 |
| --- | --- |
| P@10 | `>= 0.3` |
| P@50 | `>= 0.15` |
| P@100 | `>= 0.1` |

这是比较保守的 CCF-B 最低线。现在 P@10 / P@50 / P@100 对 wrapper oracle 是 0，必须显著改善。

## 方案五：把已有人工标注转成 hard negatives

### 当前问题

manual review 已经暴露了大量 false positives，但目前没有被反馈回系统。metrics 只是读 label、算 precision / precision@k。

### 修改方法

新增：

```text
data/manual/hard_negatives.csv
data/manual/true_positives.csv
```

字段：

```csv
warning_id,symbol,type,pair_id,label,false_reason,required_fix
```

`false_reason` 建议标准化为：

```text
BINDING_ONLY
NO_RUST_USE
SUBSTRING_MISMATCH
ADDED_SYMBOL_NO_OLD_EVIDENCE
PLACEHOLDER_STRUCT_FIELDS
NO_C_SOURCE_DIFF
BENIGN_CONTRACT_CHANGE
WEAK_INDICATOR
```

增加一个开发阶段命令：

```bash
uv run binddrift eval diagnose-false-positives \
  --manual-review data/replay/.../manual_review.csv \
  --warnings data/replay/.../warnings.jsonl
```

输出：

```json
{
  "false_positive_reasons": {
    "BINDING_ONLY": 42,
    "NO_RUST_USE": 31,
    "SUBSTRING_MISMATCH": 7
  },
  "recommended_gate_changes": []
}
```

### 数据划分

不要用全部人工标签直接调参后再报告同一批结果。建议：

```text
dev labels: 70%
test labels: 30%
```

dev 用于调 gate / ranking，test 用于报告 final precision。

如果样本太少，至少做 leave-one-pair-out：按 replay pair 留一组做 test。

### 接受标准

论文中能说清楚：

> We used historical manual labels only to tune gates on the development split; all reported P@K numbers are from held-out pairs.

这能显著提高 CCF-B 可信度。

## 方案六：修复 case study 选择逻辑

### 当前问题

case study 生成器现在按类型从 warnings 中选第一条，不检查 label 是否为真阳性。模板还会固定写 “C-side contract evidence reaches Rust-for-Linux wrapper code”，即使没有 Rust-side evidence。

这会把 false positive 自动包装成 case study。

### 修改方法

修改 `_select_cases`：

```python
TRUE_LABELS = {
    "TRUE_BUILD_BREAKAGE",
    "TRUE_WRAPPER_FIX",
    "TRUE_SEMANTIC_DRIFT",
}


def _select_cases(warnings, labels):
    candidates = [
        w for w in warnings
        if labels.get(str(w.get("warning_id"))) in TRUE_LABELS
        and has_strong_evidence(w)
    ]
    ...
```

如果真阳性不足，不要强行凑满 8 个 case。宁可输出：

```yaml
cases: 2
note: only adjudicated true positives are used
```

这比自动生成 8 个假 case 更可信。

### Case 必须包含的证据

每个 case study 至少包含：

- C-side diff 或 behavior indicator evidence。
- Rust direct call 或 safe API。
- safety comment / mapping / lifetime fact / wrapper fix / build log 之一。
- manual adjudicated label。
- 为什么 compiler 不会捕获。

没有这些证据的 warning 不能做 case study。

### 接受标准

生成 case 前先跑 validation：

```python
assert label in TRUE_LABELS
assert has_c_evidence(warning)
assert has_rust_impact(warning)
```

否则 fail fast，不生成 case。

## 方案七：增加 parser 与 indicator 的抽样验证

### 当前问题

当前 C / Rust extractors 主要是 regex / heuristic。这个可以作为 artifact prototype，但 CCF-B 审稿会问：你扫出来的 facts 准吗？如果事实层错误很多，后面的 warning / ranking 都不可信。

### 修改方法

新增一个 validation workflow：

```bash
uv run binddrift eval audit-sample \
  --sample c_functions:100 \
  --sample rust_binding_uses:100 \
  --sample c_behavior_indicators:100 \
  --sample promoted_warnings:100
```

输出人工审查 CSV：

```csv
row_id,table,symbol,file,line,extracted_fact,is_correct,corrected_fact,notes
```

然后生成：

```text
paper/tables/extractor_audit.json
```

指标：

```json
{
  "c_function_signature_precision": 0.93,
  "rust_binding_use_precision": 0.90,
  "indicator_precision": 0.78,
  "promoted_warning_evidence_precision": 0.35
}
```

这里的数字只是目标格式，不要伪造；真实跑完再填。

### 最低接受线

建议 CCF-B 前最低达到：

| 指标 | 最低线 |
| --- | --- |
| C function extraction precision | `>= 0.90` |
| Rust binding use precision | `>= 0.90` |
| C behavior indicator precision | `>= 0.75` |
| Promoted warning evidence precision | `>= 0.30` |

如果 indicator precision 不高，就不要把 indicator 作为强证据，只能作为 weak signal。

## 方案八：增强 oracle，而不是只靠 symbol-level wrapper fix

### 当前问题

当前 `oracle_summary` 是 symbol-level：warning 的 `c_side.symbol` 命中 oracle symbols 就算 matched。

这个粒度太粗，既可能误伤，也很难支撑 semantic drift claim。build breakage 当前为 0，wrapper-fix precision 又很低。

### 修改方法

把 oracle 分成三类：

```text
build_oracle:
  build log error references bindings::foo or Rust wrapper API

wrapper_fix_oracle:
  commit changes Rust wrapper/helper around bindings::foo
  AND commit/diff mentions semantic adjustment, signature adjustment, null/error/ownership/layout fix

semantic_review_oracle:
  manual adjudicated TRUE_SEMANTIC_DRIFT
```

不要只记录 symbol。新增 oracle row：

```json
{
  "oracle_type": "wrapper_fix",
  "symbol": "foo",
  "rust_file": "rust/kernel/...",
  "commit": "...",
  "fix_kind": "signature | nullability | ownership | layout | error | sleepability",
  "evidence_text": "...",
  "confidence": "strong | weak"
}
```

评价时分开报告：

- Build breakage recall。
- Wrapper-fix recall。
- Manual semantic precision。
- Top-K promoted warning precision。

不要把所有指标混在一起。

### 接受标准

至少报告：

- P@10 / P@50 / P@100 on adjudicated manual labels。
- Recall on wrapper-fix oracle。
- Number of build-breakage events, even if zero。

并明确：

> Build breakage oracle is sparse; semantic precision is measured by manual review.

这与项目 scope 保持一致：BindDrift 是 warning / prioritization artifact，不证明 soundness。scope 文档本来就已经这么写了。

## 方案九：baseline / ablation 要围绕 ranking 改写

### 当前问题

目前最关键的主张应该是：

> BindDrift ranks Rust-impactful drift warnings better than simple heuristics.

所以 baseline 不能只是形式上存在，必须针对 ranking 失败点设计。

### 建议 baseline

至少保留四个：

| Baseline | 定义 |
| --- | --- |
| `BindingDiffOnly` | 所有 binding diff 都作为 warning，按 severity 排 |
| `CIndicatorOnly` | 只用 C behavior indicator，不看 Rust exposure |
| `RustUseOnly` | 只要 Rust binding use 命中就排前，不看 contract evidence |
| `NoRanking` / `Random` / `Chronological` | 作为下界 |

BindDrift 应该证明：

```text
BindDrift P@K > BindingDiffOnly P@K
BindDrift P@K > CIndicatorOnly P@K
BindDrift P@K > RustUseOnly P@K
```

如果做不到，论文主张必须收窄。

### Ablation

建议做：

- Full BindDrift。
- no Rust-impact gate。
- no exact symbol matching。
- no contract evidence。
- no oracle boost。
- no binding-only penalty。

重点证明两件事：

- Rust-impact gate 显著提高 precision。
- exact symbol matching 显著减少 false positives。

## 方案十：论文 claim 边界也要相应改写

当前 scope 已经比较稳：不声称证明 Rust abstraction soundness，只声称检测 C API change 可能 stale Rust binding / helper / unsafe wrapper / safe abstraction。

但实验结果目前不支持“高精度检测”。整改后论文 claim 建议写成：

> BindDrift is a replay-based warning prioritization system for Rust-for-Linux cross-language API and contract drift. It separates low-level drift facts from Rust-impact warnings and ranks warnings by evidence that a C-side change reaches Rust unsafe calls, safe abstractions, or documented safety/error/lifetime contracts.

不要写：

- detects bugs
- proves soundness violations
- finds all contract drift
- guarantees safe abstraction stale

应该写：

- prioritizes review targets
- surfaces Rust-impactful drift evidence
- improves top-K precision over binding-only and indicator-only baselines

## 推荐实施顺序

### 第 1 阶段：先止血，减少明显误报

改动文件：

```text
binddrift/detectors/tier1.py
binddrift/graph/builder.py
binddrift/ranking/scorer.py
tests/
```

任务：

- Tier1 输出 drift facts，不直接输出 high-risk warnings。
- `GENERATED_FROM` 不算 Rust-impact evidence。
- 替换 `LIKE` symbol matching 为 exact matching。
- generated-binding-only 降级。
- 新增 substring mismatch 测试。

完成标准：

```text
top-20 不再出现无 Rust-side evidence 的 old absent / new added SignatureDrift
```

### 第 2 阶段：建立 Rust-impact gate

新增：

```text
binddrift/evidence/impact.py
```

修改：

```text
binddrift/detectors/tier1.py
binddrift/detectors/tier2.py
```

任务：

- 统一 direct use / safe API / safety comment / error mapping / lifetime fact / oracle evidence。
- 所有 warning 必须经过 `promote_fact_if_impactful`。
- Tier2 的 weak lifetime naming pattern 不能单独 promotion。

完成标准：

- warnings 数量大幅下降。
- 每条 warning 都能解释“为什么触达 Rust”。

### 第 3 阶段：重写 ranking

修改：

```text
binddrift/ranking/scorer.py
```

任务：

- gate first, score second。
- 加 binding-only penalty。
- 加 oracle boost。
- 加 source-diff / evidence-chain boost。
- 输出 score breakdown。

warning 中建议增加：

```json
{
  "score_breakdown": {
    "direct_rust_use": 4.0,
    "safe_api": 4.0,
    "contract_mapping": 3.0,
    "binding_only_penalty": -5.0
  }
}
```

完成标准：

```text
每个 top warning 的高分原因可解释
```

### 第 4 阶段：用人工标签闭环

新增：

```text
binddrift/evaluation/diagnostics.py
data/manual/hard_negatives.csv
```

任务：

- 把已有 false positives 归因。
- 用 hard negatives 调 gate。
- dev / test split 或 leave-one-pair-out。
- 重新报告 P@K。

完成标准：

```text
报告 held-out P@10 / P@50 / P@100
```

### 第 5 阶段：修 case study

修改：

```text
binddrift/paper/cases.py
```

任务：

- 只选 adjudicated TRUE labels。
- 每个 case 必须通过 evidence validation。
- 真阳性不够时少生成，不硬凑。
- 模板不要默认写 “contract evidence reaches wrapper code”，而要根据 evidence 实际生成。

完成标准：

```text
case study 中没有 UNLABELED / FALSE_POSITIVE / BENIGN_DRIFT
```

### 第 6 阶段：补 extractor audit

新增：

```text
binddrift/evaluation/audit.py
paper/tables/extractor_audit.json
```

任务：

- 抽样 C signatures。
- 抽样 Rust binding uses。
- 抽样 C indicators。
- 抽样 promoted warnings。
- 报 precision。

完成标准：

```text
论文能回答“regex extractor 准不准”
```

## 最终应该追求的指标

整改后，不要再以 “warnings 总数很多” 作为亮点。CCF-B 更看重：

- Top-K precision。
- False-positive reduction。
- Ablation improvement。
- Case-study credibility。
- Reproducible evidence chain。

建议最低目标：

| 指标 | 最低目标 |
| --- | --- |
| promoted warning 数量 | 比当前 17k 大幅下降，最好 `< 2k` |
| P@10 manual review | `>= 0.30` |
| P@50 manual review | `>= 0.15` |
| P@100 manual review | `>= 0.10` |
| generated-binding-only in top-50 | `0` |
| substring mismatch false positives | reviewed top-100 中为 `0` |
| case study true / adjudicated | `100%` |
| extractor audit precision | C / Rust uses `>= 0.90`，indicator `>= 0.75` |

如果这些达不到，论文主张要继续收缩为：

> fact extraction and exploratory review aid

如果这些达到了，才可以比较有底气地写成：

> Rust-for-Linux cross-language drift warning prioritization system

## 最小可执行版本

最小版本不用大改全部 pipeline，只需要做这 5 件事：

1. Tier1 generated-binding-only 不进 warnings，只进 `drift_facts`。
2. 所有 warnings 必须有 direct Rust use / safe API / safety comment / mapping / oracle 之一。
3. 所有 symbol matching 改成 exact match，禁止 detector / ranking 用 `LIKE "%symbol%"`。
4. ranking 加 binding-only penalty 和 score breakdown。
5. case study 只选 adjudicated true labels。

这五件做完，当前最大 CCF-B 风险会明显下降。现在的问题不是系统缺模块，而是证据门槛太低；把门槛加上，BindDrift 才会从“噪声很大的 drift scanner”变成“可以投稿的 warning prioritization artifact”。
