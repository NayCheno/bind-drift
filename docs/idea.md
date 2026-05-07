# BindDrift CCF-B 最稳妥版本 Idea

## 题目

BindDrift: Prioritizing Cross-Language API and Contract Drift Review Targets in Rust-for-Linux

### 中文题目

BindDrift：面向 Rust-for-Linux Safe Abstraction 的跨语言 API 与契约漂移审查目标排序

## 一句话 Idea

Linux C 侧 API 在演化时，可能改变函数签名、结构体布局、返回值约定、NULL / ERR_PTR 语义、ownership / refcount 语义、sleepability 或锁上下文要求，从而使 Rust-for-Linux 中由 bindgen 生成的 bindings 或人工编写的 safe abstractions 过期。BindDrift 自动构建 C symbol → generated binding → unsafe call → safe abstraction 的跨语言依赖图，筛选高风险 API / contract drift evidence，给出可解释 review-target warning 和优先级排序。

## 最稳妥版本的核心定位

本项目不宣称：

自动证明 Rust safe abstraction soundness。

本项目宣称：

优先排序 Linux C API 演化中可能导致 Rust bindings / safe abstractions 过期的 API drift 和 contract drift review-target warning，并通过历史回放、build breakage、wrapper fix mining 和人工审查验证 warning 的审查价值。

这是 CCF-B 最稳妥版本。它把目标从“完整证明安全性”降到“高价值漂移检测与预警”，工程可做，评价可复现，论文 claim 也更容易被审稿人接受。

## 背景与动机

Rust-for-Linux 的结构天然存在跨语言依赖。Linux 官方文档明确区分了 bindings 和 abstractions：bindings 是 Rust 侧对 C 函数和类型的声明，abstractions 是包装 C 侧 kernel functionality 的 Rust 代码；文档还说明 leaf modules，例如 drivers，不应直接使用 C bindings，而应通过尽可能安全的 abstractions。

官方文档还明确指出，Rust kernel 的目标是把直接接触 C API 的 unsafe 操作封装到经过审查和文档化的 abstractions 中；这些 abstractions 的用户只要 abstraction 本身 sound，并且 unsafe block 遵守 safety contract，就不能引入 UB。

这意味着 Rust safe abstraction 的安全性并不只由 Rust 类型系统决定，还依赖 C API 的语义长期稳定。如果 C API 演化改变了返回值、引用计数、锁上下文或 lifetime 约定，而 Rust wrapper 没有同步更新，就可能出现 stale safe abstraction。

Rust-for-Linux 官方文档也说明，C header 被加入 rust/bindings/bindings_helper.h 后会由 bindgen 自动生成 bindings；对于 bindgen 不能自动生成的 C inline functions 或复杂 macros，可以通过 rust/helpers/ 添加小 wrapper 暴露给 Rust 侧。 这给 BindDrift 提供了非常清晰的工程入口：rust/bindings/、rust/helpers/ 和 rust/kernel/ 正好构成跨语言漂移链路。

Rust-for-Linux policy 也承认了 C 侧变更可能破坏 Rust-enabled build 的现实：默认情况下不应引入已知会破坏包括 Rust 在内的构建的变更，但某些 subsystem 可以临时允许 Rust code breakage，并应尽快修复，最好在进入 Linus tree 之前修复。 这说明“C API 演化影响 Rust 侧”不是假想问题，而是已经被工程政策显式讨论的问题。

USENIX ATC 2024 的 Rust-for-Linux 实证研究也支持这个研究方向：该研究指出 RFL 基础设施逐渐成熟后，safe abstraction 和 drivers 成为后续重点；研究还报告了 merged 和 staged RFL 代码中的 bug，其中包括 safe abstraction 相关问题。

## 研究问题

### RQ1：暴露给 Rust 的 Linux C API 演化有多频繁？

### 统计对象包括

- 被 rust/bindings/bindings_helper.h 引入的 C symbols
- 被 rust/helpers/ 包装的 C helpers
- 被 rust/kernel/ safe abstractions 实际调用的 `bindings::*`
- 这些 C symbols 在历史版本中的 signature、layout、macro、constant、helper drift

### 目标是证明：Rust 所依赖的 C API surface 确实在持续演化，且并非所有变化都能被 Rust compiler 直接发现。

### RQ2：哪些 C API drift 会传播到 Rust bindings / safe abstractions？

构建跨语言依赖图：

```text
C function / struct / macro / enum
↓
bindgen-generated Rust binding
↓
unsafe call site in rust/kernel/
↓
safe abstraction API
↓
Rust driver / filesystem / subsystem user
```

目标是区分：

- C API 变了，但 Rust 没用
- C API 变了，binding 变了，但 wrapper 未受影响
- C API 变了，Rust unsafe wrapper 直接依赖
- C API 变了，safe abstraction 的 safety contract 可能过期

### RQ3：哪些 drift pattern 最可能导致 stale safe abstraction？

优先检测最稳妥、最容易验证的 pattern：

| Drift Pattern                            | 检测难度 | 论文价值   | 是否作为主线  |
| ---------------------------------------- | -------- | ---------- | ------------- |
| 函数签名变化                             | 低       | 中         | 是            |
| struct 字段变化                          | 低       | 中         | 是            |
| struct layout 变化                       | 中       | 高         | 是            |
| macro / const / enum value 变化          | 中       | 中         | 是            |
| helper wrapper 变化                      | 中       | 高         | 是            |
| NULL / ERR_PTR 语义变化                  | 中       | 高         | 是            |
| error code set 变化                      | 中       | 高         | 是            |
| ownership / refcount 变化                | 中高     | 高         | 是            |
| allocation / free pairing 变化           | 中高     | 高         | 是            |
| sleepability / atomic-context 变化       | 高       | 高         | 作为重点 case |
| 完整 lifetime / RCU / lock ordering 变化 | 很高     | 高但风险大 | 不作为主线    |

最稳妥策略是：Tier 1 全做，Tier 2 做规则化子集，Tier 3 只做 case study。

## 本文核心贡献

### Contribution 1：问题定义

提出 Cross-Language API and Contract Drift in Rust-for-Linux 问题。

传统 API evolution 研究通常关注单语言 client migration；BindDrift 关注的是：

```text
Linux C API evolution
↓
bindgen-generated Rust bindings
↓
unsafe Rust wrapper
↓
safe abstraction safety contract
```

这个问题的特殊性在于：Rust safe API 表面上可能没有变化，但底层 C contract 已经变化。

### Contribution 2：跨语言依赖图

提出 C-to-Rust Dependency Graph，节点包括：

- C function
- C struct
- C enum / macro / constant
- C inline helper
- generated Rust binding
- Rust unsafe call site
- Rust abstraction type
- Rust public safe method
- Rust driver / subsystem user

边包括：

- generated_from
- calls_binding
- wraps_c_symbol
- exposes_safe_api
- depends_on_layout
- depends_on_error_semantics
- depends_on_ownership
- depends_on_sleepability

### Contribution 3：drift taxonomy

定义面向 Rust-for-Linux 的 drift taxonomy：

| 类别              | 含义                               | 例子                                         |
| ----------------- | ---------------------------------- | -------------------------------------------- |
| SignatureDrift    | C 函数签名变化                     | 参数个数、返回类型、pointer depth、constness |
| LayoutDrift       | C 类型布局变化                     | sizeof、alignof、field offset                |
| FieldDrift        | struct 字段变化                    | 字段新增、删除、重命名、类型变化             |
| MacroConstDrift   | macro / const / enum value 变化    | error code、flag、bitmask 变化               |
| HelperDrift       | rust/helpers/ 包装对象变化         | C inline helper 变化但 Rust helper 未更新    |
| NullabilityDrift  | NULL / non-NULL / ERR_PTR 语义变化 | NULL failure → ERR_PTR failure               |
| ErrorDrift        | 错误码集合变化                     | 新增 -EAGAIN、-ENOMEM 路径                   |
| OwnershipDrift    | ownership transfer 变化            | borrowed ref → owned ref                     |
| RefcountDrift     | refcount 语义变化                  | 新增 / 删除 get、put、kref_get               |
| SleepabilityDrift | sleepability 变化                  | 新增 might_sleep()、mutex_lock()、GFP_KERNEL |
| LockContextDrift  | lock precondition 变化             | 需要 caller hold lock                        |

### Contribution 4：可解释 warning 与排序

BindDrift 不只输出“变了”，而是输出：

```text
Warning:
C symbol: foo_get_device()
Drift type: OwnershipDrift + RefcountDrift
C-side evidence:
- return path now calls get_device()
- old version returned borrowed pointer
Rust-side exposure:
- rust/kernel/device.rs wraps it in Device::from_raw()
- safe API exposes &Device without refcount increment
Risk:
High
Suggested action:
Check whether Rust wrapper must call put_device() in Drop
```

### 排序依据

```text
RiskScore =
C drift severity
× Rust exposure level
× unsafe boundary proximity
× contract keyword confidence
× historical pattern confidence
```

### Contribution 5：历史回放与实证评估

评估不只依赖人工审查，而是组合多个 oracle：

| Oracle                                      | 用途                                    | 强度       |
| ------------------------------------------- | --------------------------------------- | ---------- |
| Rust-enabled build breakage                 | 验证 signature / layout / binding drift | 强         |
| 后续 Rust wrapper fix commit                | 验证 warning 是否提前发现真实修复       | 中强       |
| commit message / mailing list evidence      | 辅助确认语义漂移                        | 中         |
| manual review top-N warning                 | 验证 semantic drift precision           | 中         |
| generated compile tests / KUnit / kselftest | 验证少量具体 case                       | 强但覆盖低 |

## 最小可发表版本范围

### 必做范围

- Linux mainline
- Rust-enabled build
- x86_64
- 固定 config
- 固定 toolchain
- rust/bindings/
- rust/helpers/
- rust/kernel/
- Tier 1 drift 全覆盖
- Tier 2 drift 选择 3–4 类重点做
- 历史 replay
- build breakage prediction
- wrapper fix mining
- 人工审查 top warning
- case studies。

### 暂不做范围

- 不做完整 Rust MIR soundness proof
- 不做全局 lifetime / RCU 自动证明
- 不做 lock ordering 全自动验证
- 不做跨所有架构 / 所有 config
- 不做自动 patch generation 作为主贡献
- 不把所有 warning 都宣称为 bug
- 不承诺发现所有 semantic drift。

## 为什么适合 CCF-B

这个版本适合 SANER / ICSME / ISSRE / ESEM 这类 CCF-B 软件工程会议，原因是：

- 问题新：Rust-for-Linux 使 Linux C API evolution 影响 Rust safe abstraction soundness，跨语言软件演化问题明确
- 对象重要：Linux kernel + Rust-for-Linux 是高影响力系统软件
- 方法可做：不需要完整 formal verification，主要依赖 AST extraction、binding diff、dependency graph、历史挖掘和规则化 contract indicators
- 评估可复现：Linux git history、Rust build、bindgen output、wrapper commit 都可以公开复现
- 结果可解释：warning 可以映射到具体 C symbol、Rust wrapper、unsafe block 和 safe API
- 工程现实强：Rust-for-Linux policy 已经明确讨论 C 变更破坏 Rust build 的责任问题

## 论文主张

### 推荐论文 claim

BindDrift prioritizes review targets for Rust-for-Linux cross-language API and contract drift. It builds a C-to-Rust dependency graph and ranks high-risk drifts that may stale Rust safety assumptions.

### 不推荐 claim

A claim that every C API change is fully checked for Rust abstraction correctness is out of scope.

## 预期实验结果形式

最终论文中最好呈现以下结果：

| 实验结果                                     | 目的                                 |
| -------------------------------------------- | ------------------------------------ |
| 暴露给 Rust 的 C API surface 规模            | 证明研究对象存在                     |
| 历史版本中 API drift 数量                    | 证明问题频繁                         |
| drift 中实际传播到 Rust wrapper 的比例       | 证明跨语言图必要                     |
| build breakage prediction precision / recall | 证明工具客观有效                     |
| wrapper fix prediction precision / recall    | 证明能提前发现真实维护需求           |
| semantic warning precision@K                 | 证明 warning 有审查价值              |
| false positive taxonomy                      | 展示工具边界                         |
| case studies                                 | 展示 compiler 发现不了的高价值 drift |
| ablation study                               | 证明每类 detector 的贡献             |

## 最终版本摘要

BindDrift 的 CCF-B 最稳妥版本是：

一个面向 Rust-for-Linux 的跨语言 API / contract drift review-target prioritization 框架。它追踪 Linux C API 从 header / helper / bindgen output 到 Rust unsafe wrapper 和 safe abstraction 的传播路径，筛选 signature、layout、helper、macro、NULL / ERR_PTR、error code、ownership / refcount、sleepability 等高风险漂移 evidence，并通过历史回放、build breakage、wrapper fix mining 和人工审查验证其审查价值。

一句话卖点：

Rust safe abstraction 的安全性依赖 C API contract；BindDrift 系统化排序这种跨语言 contract drift 的审查目标。
