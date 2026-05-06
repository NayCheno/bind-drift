# CCF-B 后续投稿计划

## 总目标

当前状态按 CCF-B 标准估计为 **74/100**，属于弱接收边缘。下一步目标是提升到：

| 目标 | 分数线 | 建议 |
| --- | --- | --- |
| 稳 B 投稿线 | >= 82/100 | 可按 CCF-B regular/full paper 推进 |
| 最低投稿线 | >= 78/100 | 可以投稿，但风险较高 |
| 低于 78 | < 78/100 | 不建议投 CCF-B full/regular paper，只建议投 CCF-C 或 artifact/demo track |

BindDrift 已经有比较强的 artifact 基础：仓库说明它是 Rust-for-Linux safe abstractions 的跨语言 API/contract drift 检测原型，包含 staged CLI workflow、multi-version replay、evaluation、paper table generation 等。

当前 canonical replay 已记录：

- 20 个 adjacent version pairs
- 16,757 drift facts
- 320 promoted warnings
- 500 条 pooled review labels

但要达到稳 B，还需要把实验外部有效性、论文叙事、oracle-blind 论证、LaTeX 论文稿全部补齐。

## 下一步方案与验收标准

## M0：锁定投稿定位与 Claim Boundary

### 目标

明确论文只能主张 **evidence-backed warning prioritization**，不能主张“自动发现真实 bug”或“证明 Rust safe abstraction soundness”。

### 必须完成

论文题目和摘要都使用以下定位：

> BindDrift prioritizes review targets for Rust-for-Linux cross-language API and contract drift.

明确三类贡献：

- C/Rust 跨语言 drift evidence chain
- multi-version replay + warning prioritization
- Rust-for-Linux 真实历史版本上的人工评审与排序评估

明确禁止的 claim：

- 不说 “BindDrift proves safety”
- 不说 “BindDrift automatically detects bugs”
- 不把 `TRUE_WRAPPER_FIX` 混同为 `TRUE_SEMANTIC_DRIFT`
- 不把 Tier-2 semantic warnings 说成 confirmed defects

### 验收标准

| 检查项 | 必须满足 |
| --- | --- |
| 摘要中是否出现 “confirmed bug detector” 类表达 | 不得出现 |
| 摘要中是否写明 warning prioritization / review target | 必须出现 |
| Scope 是否和仓库一致 | 必须一致 |
| Tier-2 semantic finding 是否被写成 review target | 必须 |

仓库当前 scope 已经写得比较正确：BindDrift 不证明 Rust abstraction soundness，Tier 2 semantic findings 是 review targets，评估数字必须来自 replay outputs、build logs、wrapper-fix mining 或 manual review CSV。

这部分要直接转化到论文 Introduction、Threats to Validity 和 Evaluation Protocol。

## M1：补强实验外部有效性

### 目标

解决当前最大弱点：实验集中在 Linux mainline、x86_64、Rust-for-Linux 单一生态。

当前默认 scope 是 Linux mainline、x86_64、Rust-enabled builds，并覆盖 `rust/bindings`、`rust/helpers`、`rust/kernel` surfaces。这对 CCF-B 是够用但偏窄；如果想稳 B，需要至少补一个 external-validity slice。

### 必须完成的最低版本

增加 arm64 external-validity slice。Artifact guide 已经预留了 arm64 小规模 replay 命令，建议直接把它做成正式实验。

arm64 slice 不必和 x86_64 同规模，但必须报告：

- 版本数量
- pair 数量
- drift fact count
- promoted warning count
- 与 x86_64 的 warning overlap
- 不同 architecture 下新增或缺失的 warning 类型
- 失败 pair 和失败原因

如果 arm64 绑定生成失败，必须把失败作为 validity data 报告，而不是静默跳过。现有 artifact guide 已经要求 failed pairs 记录 error，而不是 silently skipped。

### 验收标准

| 指标 | 最低验收线 | 稳 B 目标 |
| --- | --- | --- |
| arm64 replay versions | >= 6 个 release tags | >= 8 个 release tags |
| completed pairs | >= 5 | >= 7 |
| 失败 pair 记录 | 100% 记录 | 100% 记录并分类 |
| warning overlap analysis | 必须有 | 必须有表格 + 解释 |
| external validity section | 必须有 | 独立小节 + threats discussion |

失败条件：如果 arm64 完全无法跑通，论文仍可投，但必须把 external validity 评分从 18/25 降到约 15/25，整体很难稳 B。

## M2：重做 Oracle-Blind Ranking 叙事

### 目标

消除审稿人对 oracle leakage 的疑虑。

CCF-B 审稿人会非常敏感：ranking 是否偷偷用了 wrapper-fix 或 build oracle。这里必须写清楚。

当前仓库里有两套排序相关逻辑：

- 一套 current scorer 会包含 `build_oracle_hit` 和 `wrapper_fix_hit` 分量。
- 一套 pooled evaluation 的 primary ranker 是 `binddrift_oracle_blind`。

current scorer 中确实有 oracle component。pooled review 代码里 primary ranker 使用 `rank_primary_warnings_oracle_blind`。oracle-blind scorer 明确把 `build_oracle_hit`、`wrapper_fix_hit` 作为 oracle components 排除。

### 必须完成

论文中画一张数据流图，分成三层：

- detection-time features
- primary oracle-blind ranking
- auxiliary validation oracles

在 Evaluation 里明确：

- build-breakage oracle 只用于 labels / auxiliary validation
- wrapper-fix oracle 只用于 labels / auxiliary validation
- primary score 不使用 forbidden oracle features

在 artifact 里保留一个 machine-checkable gate：

- 输出 primary ranker 的 score component keys
- 输出 forbidden feature keys = empty
- 如果非空，artifact reproduction 失败

当前 ranking table 已记录 primary ranker 的 score component keys 与 forbidden oracle feature keys。Artifact reproducibility 也有 `oracle_blind_primary_has_no_forbidden_components` gate。

### 验收标准

| 检查项 | 验收线 |
| --- | --- |
| primary ranker 名称 | 全文统一为 `BindDrift-oracle-blind` |
| forbidden oracle feature keys | `[]` |
| build/wrapper oracle 使用位置 | 只能出现在 evaluation/validation |
| 论文图示 | 至少 1 张 data-flow figure |
| Artifact gate | 必须自动检查并失败退出 |

失败条件：如果论文里没有解释 current scorer 与 oracle-blind scorer 的差异，审稿人很可能给 Weak Reject。

## M3：把实验改成五个 RQ 驱动

### 目标

CCF-B regular paper 不接受单纯 artifact report，需要清晰的 research questions。

建议最终使用 5 个 RQ：

| RQ | 问题 | 核心指标 |
| --- | --- | --- |
| RQ1 | BindDrift 能否可靠抽取 C/Rust drift evidence？ | extractor audit precision、fact counts、失败 taxonomy |
| RQ2 | evidence gating 是否降低 review workload？ | drift facts -> promoted warnings -> top-K warnings |
| RQ3 | oracle-blind ranking 是否优于 baseline？ | P@10/P@20/P@50/P@100、NDCG@20、AUPRC |
| RQ4 | 哪些 semantic drift pattern 对 Rust safe abstractions 有意义？ | semantic target review、case studies |
| RQ5 | artifact 是否可复现并能跨 toolchain/version replay？ | run manifest、sha256、strict gate、runtime |

draft 当前已经有这五个 RQ 的雏形。但需要把每个 RQ 写成完整闭环：

> 问题 -> 方法 -> 数据 -> 结果 -> 解释 -> 威胁

### 验收标准

| RQ | 最低验收线 |
| --- | --- |
| RQ1 | strict extractor audit >= 800 samples，precision gate 通过 |
| RQ2 | 报告 drift facts、promoted warnings、top-K workload reduction |
| RQ3 | primary ranker 必须优于 best simple baseline |
| RQ4 | 至少 3 类 semantic drift，至少 8 个 true semantic drift |
| RQ5 | one-command reproduction + table sha256 provenance |

当前 strict extractor audit 已采样 830 个 facts，overall Cohen’s kappa = 1.0，所有 minimum gates pass。ranking 结果也已经很强：primary ranker P@10 = 1.00、P@20 = 1.00、P@50 = 0.86、P@100 = 0.43、NDCG@20 = 1.00。

## M4：降低 False Positive 风险

### 目标

把论文叙事转成 top-K review prioritization。

当前 500 个 pooled labels 中，450 个是 `FALSE_POSITIVE`，这在普通 detection 论文里很危险。但如果叙事是 top-K prioritization for maintainers，结果反而有说服力，因为 P@10/P@20 很强。

### 必须完成

不报告 overall precision 作为主指标。

主指标固定为：

- P@10
- P@20
- P@50
- P@100
- NDCG@20
- AUPRC on pooled review set

单独做 false-positive taxonomy：

- binding-only/generated surface
- weak rust reachability
- real C drift but no Rust contract impact
- macro/constant over-prioritization
- layout ambiguity

在 Threats 里承认：

- overall warning set precision 不高
- 方法目标是 prioritization 而非 exhaustive bug finding
- semantic labels 有主观性

当前 semantic review summary 已经报告 false-positive taxonomy，其中 `binding_only_or_generated_surface` 占 255。这应该成为论文中 “why ranking matters” 的证据。

### 验收标准

| 指标 | 最低线 | 稳 B 目标 |
| --- | --- | --- |
| P@10 | >= 0.70 | >= 0.90 |
| P@20 | >= 0.60 | >= 0.80 |
| P@50 | >= 0.40 | >= 0.70 |
| NDCG@20 | >= 0.70 | >= 0.90 |
| best baseline delta P@20 | >= 0.10 | >= 0.30 |
| false-positive taxonomy | 必须有 | 必须有 examples |

当前结果已经超过稳 B 目标：P@20 = 1.00，P@50 = 0.86，且对 best simple baseline 的 delta P@20 = 0.60、P@50 = 0.64、NDCG@20 = 0.5394。

## M5：补强人工评审可信度

### 目标

让审稿人相信 manual labels 不是 cherry-picking，也不是模型自评。

当前 manual review guide 已经要求两个独立 reviewer 和 adjudicator。当前 pooled review 质量也不错：500 条 double-labeled，agreement rate 0.922，Cohen’s kappa 0.8118，label coverage 1.0。

### 必须补充

在论文中写清 review protocol：

- reviewer 是否 blind to ranker
- reviewer 是否 blind to oracle
- adjudication 如何进行
- unclear 如何处理
- `TRUE_WRAPPER_FIX` 与 `TRUE_SEMANTIC_DRIFT` 如何区分

说明 “LLM-assisted” 的边界。现在 artifact reproducibility 里写了 “LLM-assisted independent double review with adjudication”，这很容易被审稿人追问。建议写成：

- LLM 只用于 evidence packet summarization / formatting
- 最终 label 由人工 reviewer 决定
- adjudication 由人工完成
- LLM 不参与 primary score
- LLM 不看 ground-truth labels

增加 10 个 disagreement examples 的 appendix 或 artifact 文件引用。

### 验收标准

| 检查项 | 验收线 |
| --- | --- |
| double review | 100% pooled rows |
| adjudication | 100% pooled rows |
| Cohen’s kappa | >= 0.70 |
| agreement rate | >= 0.80 |
| unclear rate | <= 5% |
| label leakage check | pass |
| reviewer disagreement examples | >= 10 |

当前指标已满足。

## M6：补强 Case Studies

### 目标

让贡献“可读”。CCF-B 审稿人需要看到具体例子，不然这类工具论文会显得抽象。

当前 draft 已列出 8 个 positive warning-backed case studies 和 2 个 negative/failure-analysis cases。case summary 也显示 8 个 positive case、2 个 negative case、覆盖 5 类 drift type。

建议论文正文保留 3 个主案例：

| 案例 | 例子 | 说明 |
| --- | --- | --- |
| Nullability/Error Drift | `errname` 或 `security_secid_to_secctx` | 解释 C error/null contract 如何影响 Rust wrapper |
| Sleepability/Context Drift | `__mutex_init` 或 `init_wait` | 说明 semantic contract 不一定体现在类型签名中 |
| Allocation/Free or Lifetime Drift | `dma_free_attrs` 或 `security_release_secctx` | 说明 Drop path / ownership abstraction 的风险 |

### 验收标准

| 项目 | 验收线 |
| --- | --- |
| 正文 case studies | 3 个 |
| Artifact appendix cases | >= 8 positive + >= 2 negative |
| 每个 case 是否有 evidence chain | 必须 |
| 每个 positive case 是否有 adjudicated true label | 必须 |
| 是否包含 false-positive negative case | 必须 |
| 是否避免 confirmed bug 过度表述 | 必须 |

当前 case study summary 已显示 positive cases 中 `TRUE_SEMANTIC_DRIFT` 4 个、`TRUE_WRAPPER_FIX` 4 个，negative cases 为 2 个 false positives。

## M7：启动 LaTeX 论文写作

### 结论

现在可以开始写 LaTeX 论文，但不能直接写 final submission。

正确顺序是：

1. 先写 LaTeX skeleton + method + evaluation protocol。
2. 同步补 arm64 external-validity slice。
3. arm64 结果出来后再定稿 Evaluation 和 Threats。
4. 最后做 camera-ready 风格 polish。

### 推荐主投方向

| 目标 | 建议 |
| --- | --- |
| 首选 | SANER / ICSME |
| 次选 | SAS，如果强调 static analysis |
| 系统角度备选 | HotOS，但需要更强 vision/problem framing |
| 不建议 | 直接冲 CCF-A，当前 novelty 不够稳 |

CCF 软件工程/系统软件/程序设计语言 B 类列表中确实包含 SANER、ICSME、SAS、HotOS。

### LaTeX 模板策略

| 目标会议 | LaTeX 模板 |
| --- | --- |
| SANER / ICSME / ESEM / ISSRE | IEEE conference LaTeX |
| SAS / VMCAI / ETAPS 子会 | Springer LNCS LaTeX |
| HotOS | USENIX LaTeX |

由于当前最匹配的是 SANER/ICSME，建议先用 IEEE conference LaTeX 写主稿，后续如果转 SAS 再迁移到 LNCS。

### LaTeX 论文结构建议

建议建立如下目录：

```text
paper-latex/
  main.tex
  sections/
    00-abstract.tex
    01-introduction.tex
    02-background.tex
    03-problem.tex
    04-design.tex
    05-implementation.tex
    06-evaluation.tex
    07-case-studies.tex
    08-discussion.tex
    09-related-work.tex
    10-conclusion.tex
  figures/
    architecture.pdf
    evidence-chain.pdf
    ranking-dataflow.pdf
    warning-volume.pdf
  tables/
    rq1-extractor-audit.tex
    rq2-warning-volume.tex
    rq3-ranking.tex
    rq4-semantic-review.tex
    rq5-reproducibility.tex
  refs.bib
```

建议论文标题暂定：

```tex
\title{BindDrift: Prioritizing Cross-Language API and Contract Drift in Rust-for-Linux}
```

摘要的核心句式建议是：

> BindDrift is a static-analysis and cross-version replay framework that prioritizes evidence-backed review targets for Rust-for-Linux API and contract drift. It does not prove Rust abstraction soundness or automatically confirm runtime bugs.

这句话必须保留，能显著降低审稿人对 claim 过强的攻击。

## 最终投稿前硬性 Gate

下面这些是 CCF-B 投稿前必须全部通过的验收标准。

| Gate | 验收标准 | 当前状态 |
| --- | --- | --- |
| G1 Claim Boundary | 只主张 warning prioritization，不主张 bug confirmation | 基本通过 |
| G2 Full Paper Readiness | LaTeX regular paper 完整，不是 artifact report | 未完成 |
| G3 External Validity | 至少补 arm64 或等价外部验证 | 未完成 |
| G4 Oracle Blindness | primary ranker 无 forbidden oracle features | 基本通过 |
| G5 Manual Review | 500 pooled labels，double review + adjudication | 已通过 |
| G6 Ranking Superiority | 显著优于 best simple baseline | 已通过 |
| G7 False Positive Taxonomy | 有 taxonomy + examples | 基本通过 |
| G8 Case Studies | >= 3 正文案例，>= 8 artifact 案例 | 基本通过 |
| G9 Reproducibility | 一键复现 + sha256 table provenance | 已通过 |
| G10 Writing Quality | Introduction / RQ / Threats / Related Work 达 regular paper 水平 | 未完成 |

## 评分提升预期

| 当前问题 | 解决后加分 |
| --- | --- |
| LaTeX full paper 未成稿 | +4 |
| external validity 不足 | +3 |
| oracle-blind 叙事不够清楚 | +2 |
| false positive 风险未转化为 ranking story | +2 |
| case studies 没有进入强叙事 | +1 |
| related work / threats 不够成熟 | +2 |

完成 M0-M7 后，预期评分：**82-85/100**。

这时可以按 CCF-B regular paper 标准投稿。当前最优路线是：先写 IEEE LaTeX 主稿，目标 SANER/ICSME；同时补 arm64 external-validity slice，并把 oracle-blind ranking 和 false-positive taxonomy 写成论文主线。
