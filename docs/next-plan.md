# BindDrift 下一阶段计划

目标是把 BindDrift 平推到多数审稿人倾向 accept / weak accept，少数可能 borderline，但很难直接 reject 的状态。

BindDrift 的最终论文定位为：

> 一个面向 Rust-for-Linux 的跨语言 API / contract drift review-target prioritization 系统。核心贡献是 C-to-Rust evidence graph、跨版本 drift taxonomy、oracle-blind ranking、历史 replay 评估和可复现 artifact。

这个定位必须坚持：不要声称自动发现 bug 或证明 Rust safe abstraction soundness。仓库当前 scope 已经写得比较稳：BindDrift 是 warning/prioritization artifact，不证明 soundness，不自动确认 bug，Tier 2 semantic finding 只是 review target，`TRUE_WRAPPER_FIX` 与 `TRUE_SEMANTIC_DRIFT` 分开报告。

## 一、最终目标线

### 稳定 CCF-B Accept 的硬目标

最终提交前，项目应达到：

| 方面 | 稳定 accept 目标 |
| --- | --- |
| 问题定义 | 清楚说明 Rust-for-Linux C/Rust drift 是真实维护问题，不是普通 bindgen diff |
| 方法贡献 | 至少有一个审稿人认可的“非平凡方法核心”：C-to-Rust evidence graph + drift taxonomy + oracle-blind prioritization |
| 工程完整性 | 可从 Linux 多版本 replay 到 warnings、labels、tables、cases 一键复现 |
| 实验规模 | 主实验覆盖 >=20 个 Linux adjacent version pairs，至少一个外部架构或外部分支验证 |
| 人工评审 | >=800 个 pooled review items，双人独立标注 + adjudication，kappa >=0.75 |
| 排序效果 | primary ranker 显著优于最强 simple baseline，不允许 oracle leakage |
| 抽取可靠性 | precision 和 recall 都有 audit，而不只报告 precision |
| 复现性 | artifact evaluator 可在文档指导下复现实验，strict gate 失败时返回非 0 |
| 写作安全性 | 不夸大为 bug detector / soundness verifier / complete static analyzer |

## 二、总体里程碑

建议分成 8 个阶段：

- M0：锁定论文 claim 和审稿口径
- M1：补强核心技术，不再像纯 regex heuristic
- M2：补 extractor precision + recall audit
- M3：重做/扩充人工评审协议
- M4：重构评价口径，消除指标冲突
- M5：强化 baseline、ablation、significance
- M6：补外部有效性、scalability、failure taxonomy
- M7：整理论文、artifact 和 rebuttal-ready 材料

## 三、M0：锁定论文 Claim 和一票否决边界

### 目标

把论文主张固定为：

> BindDrift prioritizes review targets for Rust-for-Linux cross-language API and contract drift.

不要写成：

- BindDrift detects bugs.
- BindDrift verifies Rust safe abstraction soundness.
- BindDrift completely detects all C/Rust contract drift.

仓库当前文档已经明确了这一点：默认范围是 Linux mainline、x86_64、Rust-enabled builds，以及 `rust/bindings`、`rust/helpers`、`rust/kernel` surface。

### 必做任务

| 任务 | 说明 |
| --- | --- |
| 统一论文 terminology | 全文统一使用 “review target / warning prioritization / evidence-backed warning” |
| 删除过强 claim | 删除 “bug finding”、“soundness”、“complete detection”、“guarantee” 等表述 |
| 明确输出层次 | drift facts != promoted warnings != true semantic drift != wrapper fix |
| 明确 oracle 使用 | build/wrapper oracle 只用于 label 和 auxiliary validation，不能进入 primary score |
| 固定 threat boundary | regex/AST 不完整、Linux-specific、Rust-for-Linux-specific、semantic label 主观性都要主动承认 |

### 验收标准

| 验收项 | 通过标准 |
| --- | --- |
| Claim boundary | Abstract、Introduction、Conclusion 中都只声称 prioritization，不声称 bug detection |
| Label boundary | `TRUE_WRAPPER_FIX` 与 `TRUE_SEMANTIC_DRIFT` 分表或分列报告 |
| Oracle boundary | paper 中有一张 data-flow figure，明确 oracle 不进入 primary ranking |
| Scope consistency | README、scope、paper、artifact guide 的 claim 完全一致 |
| 一票否决 | 任何地方出现 “proves soundness”、“detects bugs automatically”、“complete detection” 之类表述，直接不通过 |

## 四、M1：补强核心技术，不再像纯正则系统

当前最大弱点是审稿人可能认为：

> 这只是 regex extractor + hand-written ranking。

要稳定 CCF-B，必须让方法部分更像“有设计的程序分析系统”，而不是若干正则拼接。

### M1.1 C Extractor 升级

当前 C extractor 主要依赖 `FUNC_RE`、`STRUCT_RE`、`MACRO_RE` 和行为指标正则。这对 prototype 可以，但稳定 accept 不够。

#### 方案

增加两级 C extraction：

| 层级 | 方法 | 用途 |
| --- | --- | --- |
| C-L0 | 当前 regex fast path | 快速扫描、fallback、宏/文本 indicator |
| C-L1 | Clang AST / libclang parser | 函数签名、参数、返回值、struct fields、typedef、enum |
| C-L2 | Coccinelle / semantic grep 可选规则 | error path、refcount、allocation/free、sleepability evidence |

重点不是完全替换 regex，而是把 regex 从“主解析器”降级为 fallback / indicator scanner。

#### 必做能力

| 能力 | 验收要求 |
| --- | --- |
| 函数签名 | 对 header 和 helper C 文件，Clang AST 抽取函数名、return type、params |
| struct fields | 支持 nested struct、anonymous field、bitfield 的可解释处理 |
| typedef/enum | 支持 typedef alias normalization |
| function pointer | 至少不误识别为普通函数 |
| macro | 宏仍可用 text/preprocessor 处理，但要标注 limitation |
| C indicator | NULL、ERR_PTR、ERROR_CODE、REFCOUNT、ALLOC/FREE、MAY_SLEEP、ATOMIC_CONTEXT 至少 7 类 |

### M1.2 Rust Extractor 升级

当前 Rust extractor 主要依赖 `BINDING_RE`、`PUB_FN_RE`、`ERROR_MAPPING_PATTERNS`、`LIFETIME_PATTERNS` 等模式。

#### 方案

增加 tree-sitter-rust 或 rust-analyzer-based parsing。

| 层级 | 方法 | 用途 |
| --- | --- | --- |
| R-L0 | 当前 regex fast path | fallback |
| R-L1 | tree-sitter-rust | function/item boundary、unsafe block、impl、trait impl、method receiver |
| R-L2 | rustdoc JSON / cargo metadata 可选 | public API surface、doc comment、type exposure |

#### 必做能力

| 能力 | 验收要求 |
| --- | --- |
| unsafe block 定位 | unsafe call 是否在 unsafe block 内，line mapping 准确 |
| binding use | `bindings::foo`、`crate::bindings::foo`、helper wrapper 调用都覆盖 |
| safe API | `pub fn`、`pub unsafe fn`、`impl Type { pub fn }`、trait impl 中 public surface |
| safety comment | `SAFETY` comment 与最近 unsafe call / binding use 关联 |
| error mapping | `Result`、`Option`、`from_err_ptr`、`to_result`、`PTR_ERR`、`IS_ERR` |
| lifetime/ownership | `Drop`、`Clone`、`ARef`、`Opaque`、`from_raw`、`into_raw`、refcount-like wrapper |

### M1.3 Bindgen Parser 升级

当前 bindgen parser 用正则解析 generated functions、structs、consts、layout assert。

#### 方案

增加 Rust AST parser，例如 syn 或 tree-sitter-rust，用于 generated Rust bindings。

| 能力 | 验收要求 |
| --- | --- |
| extern function | 支持 `extern "C"` block 中函数 |
| struct | 支持 `repr(C)` struct、field、visibility |
| const | 支持 const / enum-like constant |
| layout | 支持 size、align、offset assertion |
| missing binding | 缺失 generated file 必须作为 artifact warning，不可静默成功 |

仓库 artifact guide 已经说明 generated bindings 是 build artifacts，完整抽取前需要 kernel object tree 和 Rust availability check。稳定 CCF-B 版本必须把这个路径作为主实验，而不是只跑 pilot。

### M1 验收标准

| 类别 | 稳定 accept 验收线 |
| --- | --- |
| C 函数签名 precision | >=0.98 |
| C 函数签名 recall | >=0.90 |
| C behavior indicator precision | >=0.90 |
| C behavior indicator recall | >=0.75 |
| Rust binding use precision | >=0.95 |
| Rust binding use recall | >=0.90 |
| unsafe block precision | >=0.95 |
| safe API exposure precision | >=0.90 |
| safe API exposure recall | >=0.85 |
| generated binding fact precision | >=0.98 |
| generated binding fact recall | >=0.95 |
| Parser limitation | 每类 extractor 至少 5 个 documented limitation examples |
| 一票否决 | 仍然只用 regex 做主 parser 且没有 recall audit，不通过 |

## 五、M2：补 Extractor Precision + Recall Audit

当前仓库已有 strict extractor audit，报告 830 个样本、overall pass、kappa 1.0 等结果。这很好，但更偏 precision audit。稳定 accept 需要补 recall。

### 方案

设计一个新的 Extractor Reliability Audit，分成两部分：

- Precision audit：抽到的事实是否正确。
- Recall audit：人工 gold set 中应该抽到的事实是否被抽到。

### Gold Set 设计

| Gold set | 来源 | 数量 |
| --- | --- | --- |
| C function signature gold | 随机抽 header/helper C 文件 | >=300 |
| C struct field gold | 随机抽 struct definitions | >=200 |
| C behavior indicator gold | 人工标注 C function body / helper | >=300 |
| Rust binding use gold | 随机抽 Rust unsafe wrapper 文件 | >=300 |
| Rust safe API gold | `rust/kernel/**/*.rs` public APIs | >=250 |
| Safety comment gold | `SAFETY` comments + nearby unsafe use | >=200 |
| Error/lifetime mapping gold | wrapper code focused sample | >=200 |
| Generated binding gold | generated bindings AST sample | >=300 |

总 gold facts 建议 >=2,000。

### 抽样策略

必须 stratified，不要只随机：

| 维度 | 要求 |
| --- | --- |
| version | 覆盖至少 8 个 Linux versions |
| pair | 覆盖 dev / validation / locked-test pairs |
| file type | `.h`、`.c`、generated `.rs`、hand-written `.rs` |
| warning type | Signature、Field/Layout、MacroConst、Nullability、Error、Refcount、Sleepability |
| difficulty | 简单函数、inline、macro-like、function pointer、nested struct、unsafe wrapper |

### 验收标准

| 指标 | 通过线 | 稳定 accept 线 |
| --- | --- | --- |
| Overall extractor precision | >=0.90 | >=0.95 |
| Overall extractor recall | >=0.80 | >=0.88 |
| C signature recall | >=0.88 | >=0.92 |
| Rust binding-use recall | >=0.88 | >=0.93 |
| Safe API exposure recall | >=0.80 | >=0.88 |
| Behavior indicator recall | >=0.70 | >=0.78 |
| Double review kappa | >=0.70 | >=0.80 |
| Disagreement examples | >=10 | >=20 |
| Negative controls | 每类 extractor >=20 | 每类 extractor >=30 |

### 产出物

| 文件 | 内容 |
| --- | --- |
| `paper/tables/extractor_precision_recall.json` | 每类 extractor precision/recall |
| `paper/tables/extractor_confusion_matrix.json` | TP/FP/FN 分类 |
| `paper/analysis/extractor_limitations.md` | 每类 parser limitation |
| `paper/analysis/extractor_false_negatives.md` | 漏报样例和原因 |
| `data/audit/extractor_gold_labels.csv` | gold labels |
| `data/audit/extractor_audit_manifest.json` | 抽样方法、hash、reviewer 信息 |

## 六、M3：扩充人工评审协议

当前 pooled review 已经不错：500 条 double-labeled，agreement rate 0.922，Cohen’s kappa 0.8118。但稳定 accept 建议扩充到 >=800 或 1,000 条，并解决不同 evaluation summary 指标口径不一致的问题。

### 方案

建立三层 label set：

| Label set | 用途 | 数量 |
| --- | --- | --- |
| L1 Top-K review set | 评价实际 top-100/top-200 warning quality | >=200 |
| L2 Pooled ranking set | 比较 rankers 的共享评价池 | >=800 |
| L3 Semantic-focused set | 深挖 Tier 2 semantic drift 类型 | >=400 |

三者可以有重叠，但必须在 paper 中明确区分。

### Label 定义

最终 label 必须固定为：

| Label | 定义 |
| --- | --- |
| `TRUE_SEMANTIC_DRIFT` | C-side contract drift + Rust exposure + plausible stale abstraction assumption |
| `TRUE_WRAPPER_FIX` | 后续 Rust wrapper/helper/binding 修复支持，但不计入 semantic drift |
| `TRUE_BUILD_BREAKAGE` | replay/build oracle 证明 build failure |
| `BENIGN_DRIFT` | drift 存在但对 Rust contract 无实质风险 |
| `FALSE_POSITIVE` | evidence chain 错误、弱匹配、无 Rust impact |
| `UNCLEAR` | 证据不足，不计为 true positive |

### Blind Review 协议

| 角色 | 要求 |
| --- | --- |
| Evidence collector | 只整理 evidence packet，不给 label |
| Reviewer 1 | 看 evidence，不看 rank、score、ranker name |
| Reviewer 2 | 独立看 evidence，不看 Reviewer 1 |
| Adjudicator | 看两个 reviewer 输出后给最终 label |
| Leakage checker | 检查 evidence packet 是否泄漏 score/rank/ranker |

当前 manual review quality 中已经有 reviewer independence、rank/score blindness、adjudication、oracle visibility declaration 等字段。稳定版本要继续保留，并把协议写进论文正文。

### 验收标准

| 项目 | 通过线 | 稳定 accept 线 |
| --- | --- | --- |
| Pooled review size | >=500 | >=800，最好 1,000 |
| Double-labeled coverage | 100% | 100% |
| Adjudication coverage | 100% | 100% |
| Cohen’s kappa | >=0.70 | >=0.78 |
| Agreement rate | >=0.80 | >=0.88 |
| UNCLEAR rate | <=5% | <=3% |
| Leakage findings | 0 | 0 |
| Disagreement examples | >=10 | >=20 |
| Label source | 只用 adjudicated label | 只用 adjudicated label |
| 一票否决 | Reviewer 看到 rank/score/ranker name，不通过 | Reviewer 看到 rank/score/ranker name，不通过 |

## 七、M4：重构评价口径，消除指标冲突

这是当前最需要立刻解决的问题。

现在仓库里可能出现多套指标：pooled ranking evaluation 很强，但 canonical/manual review summary 中 top-K 指标较弱。严格审稿人会问：

> 为什么 P@10 有不同结果？你是不是选择性报告？

### 方案

把所有评价拆成 4 个互不混淆的 RQ。

### RQ1：Extractor Reliability

回答：

> 抽取的 C/Rust/binding facts 是否可靠？

指标：

| 指标 | 要求 |
| --- | --- |
| Precision / Recall | 每类 extractor 报告 |
| Kappa | 双人 audit |
| False positive taxonomy | 报告 |
| False negative taxonomy | 报告 |

### RQ2：Workload Reduction

回答：

> 从 raw drift facts 到 promoted warnings，是否显著减少维护者工作量？

当前 run manifest 已经记录 16,757 drift facts、320 promoted warnings、500 pooled labels 等信息。这个可以保留。

指标：

| 指标 | 稳定线 |
| --- | --- |
| Drift facts | >=10,000 |
| Promoted warnings | >=200 |
| Warning volume reduction | >=95% |
| Top-100 占 raw facts | <=1% |
| Promoted warning traceability | 100% 有 evidence chain |

### RQ3：Ranking Effectiveness

回答：

> Oracle-blind ranker 是否优于 simple baselines？

当前 artifact guide 已经要求 strict gate 检查 BindDrift-oracle-blind，并要求 forbidden oracle feature key list 为 `[]`，build/wrapper oracle 只能用于 label 或 auxiliary validation。这个必须作为 RQ3 的核心防线。

指标建议：

| 指标 | 稳定 accept 线 |
| --- | --- |
| P@10 | >=0.70 |
| P@20 | >=0.65 |
| P@50 | >=0.50 |
| P@100 | >=0.35 |
| NDCG@20 | >=0.75 |
| AUPRC pooled | >= best baseline + 0.10 |
| P@20 lift over best baseline | >=0.15 |
| P@50 lift over best baseline | >=0.10 |
| NDCG@20 lift | >=0.10 |
| Bootstrap p-value | <0.05 |
| Bootstrap CI lower bound | >0 for primary metrics |

注意：不建议把 “P@20 = 1.0” 作为唯一主结论，太容易被质疑。可以报告，但核心 claim 应写成：

> BindDrift significantly improves top-K review yield over the strongest simple baseline on a shared pooled review set.

### RQ4：Semantic Drift Cases

回答：

> 发现了哪些真实有意义的 semantic review targets？

当前 case summary 有 8 个 positive case、2 个 negative case，覆盖 AllocationFree、LayoutField、Nullability、OwnershipRefcount、SleepabilityContext 等 drift type。稳定 accept 建议扩到 10-12 个 case。

验收：

| 项目 | 稳定 accept 线 |
| --- | --- |
| Positive case studies | >=10 |
| Negative case studies | >=3 |
| `TRUE_SEMANTIC_DRIFT` cases | >=6 |
| `TRUE_WRAPPER_FIX`-backed cases | <=50% |
| Drift type coverage | >=5 types |
| 每个 case evidence chain | 100% 完整 |
| 每个 case 有 C evidence + Rust exposure + review rationale | 100% |

### RQ5：External Validity and Scalability

回答：

> 是否只对一个 replay run 有效？

当前 artifact guide 已经要求主 replay 使用 official release tags，并记录失败 pair；还提供 arm64 外部有效性 slice 的命令，以及 arm64 replay 路径。稳定 accept 需要把这个做成正式 RQ。

验收：

| 项目 | 稳定 accept 线 |
| --- | --- |
| x86_64 main run | >=20 adjacent pairs |
| arm64 run | >=8 versions / >=7 pairs |
| optional rust-next/staging slice | >=5 pairs |
| failed pair handling | 100% 记录，不允许 silent skip |
| runtime report | 每阶段 runtime + peak memory |
| scalability plot/table | facts、warnings、time 随版本数变化 |
| warning overlap analysis | x86_64 vs arm64 或 mainline vs rust-next |

## 八、M5：强化 Baseline、Ablation、Significance

### Baseline 设计

至少需要 6 类 baseline。

| Baseline | 说明 |
| --- | --- |
| Random | sanity check |
| No ranking | 原始顺序 |
| Binding diff only | 只看 bindgen signature/layout/const diff |
| C signature diff only | 只看 C API signature |
| C indicator only | 只看 NULL/ERR/refcount/sleep 等 indicator |
| Rust use count | 按 Rust binding use / safe API exposure 排序 |
| Graph reachability only | 只用 C-to-Rust graph reachability |
| Contract keyword baseline | ERR/NULL/refcount/free/sleep keyword heuristic |
| Prior-score ablation | 去掉 graph、去掉 impact gate、去掉 contract evidence |

当前仓库已经有 best simple baseline、random baseline、ablation 和 bootstrap significance 结构。例如 baseline comparison 中有 best simple baseline、paired bootstrap、p-value 等字段。稳定版本应把这些结果整理得更清楚。

### Ablation 设计

| Ablation | 目的 |
| --- | --- |
| `no_graph` | 证明 C-to-Rust graph 有用 |
| `no_impact_gate` | 证明 Rust-impact filtering 有用 |
| `no_contract_evidence` | 证明 safety/error/lifetime evidence 有用 |
| `no_c_source` | 证明 C-side source evidence 有用 |
| `no_binding_diff` | 证明 generated binding diff 的作用 |
| `no_penalty` | 证明 macro/layout/binding-only penalties 有用 |
| `no_cross_version` | 证明 repeated drift stability 有用 |

### 验收标准

| 指标 | 稳定 accept 线 |
| --- | --- |
| Primary beats best simple baseline | 必须 |
| P@20 lift | >=0.15 |
| P@50 lift | >=0.10 |
| NDCG@20 lift | >=0.10 |
| AUPRC lift | >=0.10 |
| p-value | <0.05 |
| At least 3 ablations support design | 必须 |
| Random baseline sanity | Primary 显著优于 random |
| Same pooled set | 所有 ranker 在同一 pool 上评估 |
| 一票否决 | primary score 使用 build/wrapper oracle，不通过 |

## 九、M6：实验规模与数据集标准

### 主实验标准

| 项目 | 当前基础 | 稳定 accept 标准 |
| --- | --- | --- |
| Linux snapshots | 21 | >=21 |
| Adjacent pairs | 20 | >=20 |
| Drift facts | 16,757 | >=15,000 |
| Promoted warnings | 320 | >=300 |
| Pooled labels | 500 | >=800 |
| Reviewed semantic targets | 304 | >=400 |
| Case studies | 8 positive + 2 negative | >=10 positive + >=3 negative |
| Architectures | x86_64 + arm64 slice | x86_64 main + arm64 external |
| Toolchain matrix | 已有 | 必须固定 hash + version metadata |

### Replay 要求

主实验必须走 full binding extraction，而不是 pilot。artifact guide 里已经说明 CCF-B-strength experiment 应使用 Linux mirror、official release tags、kernel build dependencies、Rust-for-Linux toolchain，并运行 `replay versions --build-bindings --configure --toolchain auto`。

### 验收标准

| 验收项 | 通过标准 |
| --- | --- |
| Official release tags | 所有 replay versions 来自 official Linux tags 或明确 HEAD commit |
| Toolchain matrix | 每个 version 有 rustc、rust-src、bindgen、LLVM/libclang 记录 |
| Generated bindings | 每个成功 pair 必须生成 binding snapshot |
| Failed pairs | 失败必须记录原因，不允许跳过 |
| Config hash | 每个 version 记录 config hash |
| Environment metadata | kernel commit、arch、compiler、bindgen、LLVM、host info |
| Replay determinism | 同一 artifact snapshot 复跑 sha256 一致或差异解释清楚 |
| 一票否决 | replay 中 silent skip failed version/pair，不通过 |

## 十、M7：论文结构方案

### 推荐论文标题

> BindDrift: Prioritizing Review Targets for Rust-for-Linux Cross-Language API and Contract Drift

这个标题比 “Detecting Bugs” 稳得多。

### 论文结构

#### Abstract

必须包含：

- Rust-for-Linux safe abstractions depend on evolving C APIs.
- BindDrift prioritizes review targets, not confirmed bugs.
- C-to-Rust evidence graph + cross-version replay.
- 数据规模：versions、pairs、facts、warnings、labels。
- 排序结果：P@K / NDCG / baseline lift。
- artifact reproducibility。

#### Introduction

结构：

- Rust-for-Linux 背景。
- C API contract drift 问题。
- 为什么 Rust type system 看不到全部 drift。
- 为什么不是简单 bindgen diff。
- BindDrift 的 evidence chain：

```text
C API -> generated binding/helper -> unsafe call -> safe abstraction
```

- contributions。

#### Contributions

建议写 4 个：

- Taxonomy：Rust-for-Linux cross-language API/contract drift taxonomy。
- System：C-to-Rust evidence graph and detector pipeline。
- Oracle-blind prioritization：ranker uses detection-time features only。
- Evaluation/artifact：multi-version replay, labels, baselines, case studies, reproducibility。

#### Design

必须有图：

- Pipeline figure。
- C-to-Rust evidence graph figure。
- Oracle-blind ranking data-flow figure。

#### Evaluation

按 RQ1-RQ5 写，不要混合指标。

#### Threats

必须主动写：

| Threat | 应对 |
| --- | --- |
| Parser incompleteness | precision + recall audit，limitation taxonomy |
| Label subjectivity | double review + adjudication + kappa |
| Oracle leakage | data-flow gate + forbidden feature keys |
| Linux-specific | arm64/rust-next external slice |
| Toolchain noise | versioned toolchain matrix |
| Build failures | failure taxonomy |
| Generalization | 不声称其他 OS / Rust FFI 全覆盖 |

## 十一、Artifact 验收方案

当前 artifact guide 已经有 pilot workflow、multi-version replay、strict reproduction command 和 strict gate；`python -m binddrift.artifact reproduce` 会重写 tables/cases/analysis，并在 strict gate 失败时返回非 0。稳定 CCF-B 版本要把它扩成“审稿人友好 artifact”。

### Artifact 分层

| 层级 | 目的 | 时间预算 |
| --- | --- | --- |
| A0 Smoke test | 验证安装和 CLI | 5-10 分钟 |
| A1 Pilot run | 小规模 extraction + graph + detection | 30-60 分钟 |
| A2 Table reproduction | 用 checked-in canonical artifacts 复现 paper tables | 5-20 分钟 |
| A3 Full replay | 从 Linux versions 重新跑 full binding replay | 长时间，可选 |
| A4 External slice | arm64 或小规模 external validity | 可选 |

### 必须提供的命令

| 命令 | 作用 |
| --- | --- |
| `uv run pytest` | 单元测试 |
| `uv run binddrift --help` | CLI 可用性 |
| `uv run python -m binddrift.artifact reproduce` | 复现 paper tables 和 strict validation |
| `uv run binddrift replay versions ...` | full replay |
| `uv run binddrift --data-dir data/replay/latest eval all --top-k 100 --run-id latest` | 复现 evaluation |
| `uv run binddrift paper build --stage final` | 生成 tables/cases |

README 目前已经列出了 quick start、multi-version evaluation path 和 reproduce entrypoint，这部分可以保留，但需要按 artifact evaluator 视角重写一版“最短路径”。

### Artifact 验收标准

| 项目 | 稳定 accept 标准 |
| --- | --- |
| Fresh clone smoke test | 100% 通过 |
| Unit tests | >=95% 通过；核心 tests 100% |
| Checked-in tables reproduction | sha256 一致或差异有 manifest |
| Strict gate | 所有 required checks pass |
| Failure message | 缺依赖时给明确错误和安装建议 |
| No absolute local paths | paper artifacts 中不得出现本机路径 |
| Runtime metadata | 每个 stage 记录 runtime |
| Artifact guide | 新用户可以按文档跑出 warnings 和 tables |
| 一票否决 | reproduce 命令不能跑通，不通过 |

## 十二、最终总体验收表

下面是提交 CCF-B 前的总验收表。建议把它做成 `paper/tables/ccfb_stable_accept_gate.json`。

### A. Claim Gate

| 项目 | 标准 |
| --- | --- |
| Claim 是 prioritization | 必须 |
| 不声称 bug detector | 必须 |
| 不声称 soundness proof | 必须 |
| Wrapper fix 与 semantic drift 分开 | 必须 |
| Oracle 只进 labels / auxiliary validation | 必须 |

### B. Method Gate

| 项目 | 标准 |
| --- | --- |
| C-to-Rust evidence graph | 必须有正式定义 |
| Drift taxonomy | >=6 类 |
| Detector layers | Tier 1 + Tier 2 |
| Oracle-blind ranker | 必须 |
| Forbidden oracle feature keys | `[]` |
| AST/parser enhancement | 至少 C 或 Rust 侧有强 parser，不只 regex |
| Evidence chain completeness | top-100 warnings 100% 有 evidence chain |

### C. Extraction Reliability Gate

| 项目 | 稳定线 |
| --- | --- |
| Extractor total gold sample | >=2,000 |
| Overall precision | >=0.95 |
| Overall recall | >=0.88 |
| C signature precision | >=0.98 |
| C signature recall | >=0.92 |
| Rust use precision | >=0.95 |
| Rust use recall | >=0.93 |
| Generated binding recall | >=0.95 |
| Behavior indicator precision | >=0.90 |
| Behavior indicator recall | >=0.78 |
| Audit kappa | >=0.80 |

### D. Replay Gate

| 项目 | 稳定线 |
| --- | --- |
| Linux snapshots | >=21 |
| Adjacent pairs | >=20 |
| Drift facts | >=15,000 |
| Promoted warnings | >=300 |
| Generated bindings built | 成功 pair 100% |
| Failed pairs recorded | 100% |
| Toolchain metadata | 100% |
| Config hash | 100% |
| x86_64 main run | 必须 |
| arm64 external run | >=7 pairs |

### E. Review Gate

| 项目 | 稳定线 |
| --- | --- |
| Pooled review set | >=800 |
| Double review | 100% |
| Adjudication | 100% |
| Cohen’s kappa | >=0.78 |
| Agreement rate | >=0.88 |
| UNCLEAR rate | <=3% |
| Label leakage findings | 0 |
| Reviewer blind to rank/score/ranker | 必须 |
| Adjudicated label as only metric source | 必须 |

### F. Ranking Gate

| 项目 | 稳定线 |
| --- | --- |
| P@10 | >=0.70 |
| P@20 | >=0.65 |
| P@50 | >=0.50 |
| P@100 | >=0.35 |
| NDCG@20 | >=0.75 |
| AUPRC | >= best baseline + 0.10 |
| P@20 lift over best baseline | >=0.15 |
| P@50 lift over best baseline | >=0.10 |
| NDCG@20 lift | >=0.10 |
| Bootstrap p-value | <0.05 |
| Bootstrap CI lower bound | >0 |
| Same pooled set for all rankers | 必须 |

### G. Baseline / Ablation Gate

| 项目 | 标准 |
| --- | --- |
| Random baseline | 必须 |
| No-ranking baseline | 必须 |
| Binding-diff baseline | 必须 |
| C-signature baseline | 必须 |
| C-indicator baseline | 必须 |
| Rust-use baseline | 必须 |
| Graph-only baseline | 必须 |
| >=3 supporting ablations | 必须 |
| `no_graph` ablation | 必须 |
| `no_impact_gate` ablation | 必须 |
| `no_contract_evidence` ablation | 建议必须 |

### H. Case Study Gate

| 项目 | 稳定线 |
| --- | --- |
| Positive cases | >=10 |
| Negative cases | >=3 |
| `TRUE_SEMANTIC_DRIFT` cases | >=6 |
| Drift type coverage | >=5 |
| Wrapper-fix-backed cases | <=50% |
| Full evidence chain | 100% |
| Maintainer-actionable explanation | 100% |

### I. Artifact Gate

| 项目 | 标准 |
| --- | --- |
| `uv run pytest` | 通过 |
| artifact reproduce | 通过 |
| Strict validation | 通过 |
| Required tables | 全部生成 |
| No local absolute paths | 0 |
| README quick start | 可执行 |
| Artifact guide | 可复现 pilot + table + full replay |
| sha256 provenance | 必须 |
| Failure taxonomy | 必须 |

## 十三、优先级排序

如果时间有限，按这个顺序做。

### 第一优先级：必须做，否则不稳

- 统一评价口径：把 pooled ranking、canonical top-100、semantic review 三套指标分开。
- 补 recall audit：当前只有 precision 很容易被打。
- 强化 parser 方法：至少 C 侧 Clang AST 或 Rust 侧 tree-sitter 二选一，最好都做。
- 扩充 pooled review 到 >=800。
- 明确 oracle-blind data flow：paper、figure、strict gate 三处一致。
- 重写 abstract 和 contributions：只说 prioritization，不说 bug detection。

### 第二优先级：强烈建议做

- arm64 external validity 正式纳入 RQ。
- 增加 rust-next / staging branch 小实验。
- 增加 false negative taxonomy。
- 增加 runtime/scalability table。
- case studies 扩到 10-12 个。

### 第三优先级：锦上添花

- 对比 CodeQL / Coccinelle-style baseline。
- 做 maintainer-style qualitative feedback。
- 加一个小型 cross-project FFI sanity experiment。
- 做 interactive warning browser 或 HTML report。

## 十四、最终目标分数

如果按上面方案完成，我对项目的重新评分预期是：

| 维度 | 当前估计 | 完成后目标 |
| --- | --- | --- |
| 选题重要性 | 17/20 | 18/20 |
| 创新性 | 14/20 | 16/20 |
| 技术深度 | 15/25 | 20/25 |
| 实验设计 | 22/25 | 24/25 |
| 人工评审 | 7/10 | 9/10 |
| baseline/ablation | 8/10 | 9/10 |
| artifact | 9/10 | 10/10 |
| 写作与 claim 控制 | 6/10 | 9/10 |

目标总分：

> 85-88 / 100

这基本就是 CCF-B 的稳定 accept 区间。其中最关键的分水岭是：

> 把系统从“regex-heavy prototype”升级成“有 AST/parser audit、recall audit、严格 oracle-blind evaluation 的跨版本程序分析系统”。
