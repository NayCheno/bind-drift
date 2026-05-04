# BindDrift CCF-B 最稳妥版本实施计划表

## 目标

做出一个可投稿 CCF-B 的 BindDrift 原型系统与完整实验。计划不按时间划分，而按“怎么做出来”的依赖顺序划分。

### 最终产物包括

- 可运行工具
- Linux 多版本 drift 数据库
- C-to-Rust dependency graph
- drift detector
- warning ranking
- 历史回放实验
- build breakage / wrapper fix ground truth
- 人工审查结果
- case studies
- 可复现 artifact

## 总体路线

- Step 0: 固定论文 claim 和 scope
- Step 1: 搭建 Rust-for-Linux 可复现构建环境
- Step 2: 构建 Linux 多版本数据集
- Step 3: 抽取 bindgen output
- Step 4: 抽取 Rust wrapper 使用关系
- Step 5: 抽取 C API facts
- Step 6: 构建 C-to-Rust dependency graph
- Step 7: 实现 Tier 1 drift detectors
- Step 8: 实现 Tier 2 contract drift detectors
- Step 9: 实现 warning ranking
- Step 10: 构建 ground truth
- Step 11: 做历史 replay 评估
- Step 12: 做 manual review 和 case study
- Step 13: 做 ablation / baseline / threat analysis
- Step 14: 写论文和整理 artifact

## Phase 0：固定最稳妥 Scope

| 项目       | 决策                                                             |
| ---------- | ---------------------------------------------------------------- |
| 论文目标   | CCF-B 最稳妥版本                                                 |
| 研究对象   | Rust-for-Linux                                                   |
| 主数据集   | Linux mainline                                                   |
| 扩展数据集 | rust-next / staged Rust branches，可选                           |
| 架构       | x86_64                                                           |
| config     | 固定 Rust-enabled config                                         |
| claim      | warning / prioritization，不做 soundness proof                   |
| 核心对象   | rust/bindings/、rust/helpers/、rust/kernel/                      |
| 主贡献     | dependency graph + drift taxonomy + detector + replay evaluation |

### 验收标准

- 能用一句话说明项目不是“bindgen diff”
- 能用一句话说明项目不是“formal verification”
- 能列出必做 detector 和不做 detector
- 能明确所有实验都围绕 C-to-Rust dependency graph 展开

## Phase 1：搭建可复现构建环境

| 子任务               | 做法                                                                      | 产出物                | 验收标准                        |
| -------------------- | ------------------------------------------------------------------------- | --------------------- | ------------------------------- |
| 准备 Linux repo      | clone Linux mainline                                                      | local git repo        | 能 checkout 任意目标版本        |
| 准备 Rust toolchain  | 按 kernel Rust quick-start 安装 rustc、rust-src、bindgen、rustfmt、clippy | toolchain manifest    | 能运行 Rust kernel 构建相关命令 |
| 准备 LLVM / libclang | 安装 LLVM / Clang / libclang                                              | LLVM version record   | bindgen 可运行                  |
| 检查 Rust 可用性     | 运行 make LLVM=1 rustavailable                                            | build environment log | 检查通过或记录失败原因          |
| 固定 config          | 生成 Rust-enabled .config                                                 | config file           | 所有版本尽量使用同一配置策略    |

Linux Rust quick-start 文档说明了 Rust kernel development 所需 toolchain 安装方式，并列出发行版安装 rustc、rust-src、bindgen 等依赖的方式。 Linux kernel 的 minimal requirements 文档也说明 bindgen 用于生成 Rust bindings，且依赖 libclang。

### 工程注意事项

必须记录：

- kernel commit
- config hash
- clang version
- rustc version
- bindgen version
- arch
- build flags。
- 每次抽取结果都要和 environment metadata 绑定。
- 避免把 toolchain 差异误判为 API drift。

## Phase 2：构建 Linux 多版本数据集

| 子任务                    | 做法                                                | 产出物          | 验收标准                              |
| ------------------------- | --------------------------------------------------- | --------------- | ------------------------------------- |
| 选择版本粒度              | 先按 release tag，后按 commit window                | version list    | 至少覆盖 Rust mainline 后多个版本     |
| 选择 commit window        | 针对 rust/、include/、相关 subsystem 路径取 commits | commit list     | 能定位 C 变更与 Rust 变更             |
| 提取 metadata             | commit hash、author、date、subject、changed files   | metadata DB     | 可查询任意 symbol 的演化历史          |
| 标记 Rust-related commits | 修改 rust/ 或 Rust-enabled build 相关文件           | labeled commits | 能区分 C-side change 和 Rust-side fix |
| 标记 C API commits        | 修改 header、helper、subsystem C 文件               | labeled commits | 能为 drift detector 提供输入          |

### 推荐数据表

```text
KernelVersion(
version_id,
git_commit,
tag,
date,
arch,
config_hash,
rustc_version,
clang_version,
bindgen_version
)
```

```text
Commit(
commit_id,
parent_id,
date,
author,
subject,
message,
changed_files,
is_rust_related,
is_c_api_related
)
```

### 验收标准

可以回答：“某个 C symbol 在哪些版本变了？”
可以回答：“某个 Rust wrapper 在哪些 commits 被修改？”
可以回答：“某次 C API drift 后，是否出现 Rust build failure 或 wrapper fix？”

## Phase 3：抽取 bindgen output

| 子任务                  | 做法                                        | 产出物                | 验收标准                            |
| ----------------------- | ------------------------------------------- | --------------------- | ----------------------------------- |
| 定位 generated bindings | 找到 `rust/bindings/*_generated.rs`         | generated file list   | 每个版本有 bindings snapshot        |
| 解析 extern functions   | 用 Rust parser / regex 抽取 extern "C" 函数 | BindingFunction facts | 能查询函数名、参数、返回值          |
| 解析 structs            | 抽取 generated struct 定义                  | BindingStruct facts   | 能查询字段、类型                    |
| 解析 constants          | 抽取 generated constants / enums            | BindingConst facts    | 能查询值变化                        |
| 解析 layout tests       | 抽取 bindgen layout test 信息               | Layout facts          | 能查询 size、align、offset          |
| 对比版本                | diff adjacent versions                      | BindingDrift records  | 能输出 signature/layout/const drift |

### 数据结构

```text
BindingFunction(
version_id,
rust_symbol,
c_symbol,
params,
return_type,
is_unsafe,
source_file
)
```

```text
BindingStruct(
version_id,
rust_type,
c_type,
fields,
size,
align,
source_file
)
```

```text
BindingConst(
version_id,
rust_name,
c_name,
value,
source_file
)
```

### 验收标准

输入两个 kernel versions，能输出：

- 新增 / 删除 binding function
- 函数签名变化
- struct 字段变化
- layout 变化
- const / enum value 变化

## Phase 4：抽取 Rust wrapper 使用关系

| 子任务                    | 做法                                         | 产出物               | 验收标准                         |
| ------------------------- | -------------------------------------------- | -------------------- | -------------------------------- |
| 扫描 Rust files           | 遍历 `rust/kernel/**/*.rs`                   | Rust source list     | 覆盖所有 abstraction 文件        |
| 识别 bindings 调用        | 搜索 bindings::foo、crate::bindings::foo     | BindingUse facts     | 能定位 call site                 |
| 识别 unsafe block         | AST 或轻量 parser 定位 unsafe scope          | UnsafeBlock facts    | 能知道调用是否在 unsafe 中       |
| 识别 safe public API      | 提取 pub fn、impl、trait impl                | SafeAPI facts        | 能知道 wrapper 暴露了什么        |
| 识别 Drop / Clone         | 提取 impl Drop、Clone、refcount wrapper      | Lifetime facts       | 支持 ownership/refcount detector |
| 识别 Result / Option 映射 | 查找 to_result、from_err_ptr、Option、Result | ErrorMapping facts   | 支持 NULL/error detector         |
| 识别 safety comments      | 提取 // SAFETY:、doc comments                | SafetyContract facts | 支持 warning explanation         |

### 推荐实现顺序

- 第一版用 regex + line mapping
- 第二版引入 tree-sitter-rust 或 rust-analyzer AST
- 不把 MIR 作为第一版核心
- 不依赖完整 rustdoc JSON
- unsafe call graph 先做 intra-file / direct call，后续再扩展

### 数据结构

```text
RustBindingUse(
version_id,
rust_file,
line,
binding_symbol,
enclosing_unsafe_block,
enclosing_function,
enclosing_impl,
enclosing_type
)
```

```text
RustSafeAPI(
version_id,
rust_file,
api_name,
receiver_type,
visibility,
return_type,
params,
uses_bindings
)
```

```text
RustSafetyComment(
version_id,
rust_file,
line,
text,
nearby_binding_symbol,
nearby_api
)
```

### 验收标准

- 输入 bindings::foo，能列出所有 Rust call sites
- 输入 Rust safe API，能列出它依赖的 C symbols
- 输入 C symbol，能追踪到 Rust wrapper 和 safe API

## Phase 5：抽取 C API facts

| 子任务                    | 做法                               | 产出物                   | 验收标准                     |
| ------------------------- | ---------------------------------- | ------------------------ | ---------------------------- |
| 抽取 C 函数签名           | Clang AST / libclang               | CFunction facts          | 能与 binding function 对齐   |
| 抽取 struct 定义          | Clang AST                          | CStruct facts            | 能和 bindgen struct 对齐     |
| 抽取 enum / typedef       | Clang AST                          | CType facts              | 支持 signature normalization |
| 抽取 macro / const        | preprocessor dump / sparse parsing | CMacro facts             | 支持 flag/error drift        |
| 抽取 inline functions     | header AST + grep                  | CInline facts            | 支持 helper drift            |
| 抽取 call body indicators | grep / Coccinelle / AST traversal  | CBehaviorIndicator facts | 支持 contract drift          |
| 抽取 commit message       | git log                            | CommitText facts         | 支持 evidence ranking        |

### 重点 C behavior indicators

| Indicator           | 关键词 / API                                |
| ------------------- | ------------------------------------------- |
| NULL return         | return NULL                                 |
| ERR_PTR return      | ERR_PTR、IS_ERR、PTR_ERR                    |
| error code          | -ENOMEM、-EINVAL、-EAGAIN、-EBUSY           |
| refcount get        | kref_get、refcount_inc、get_device、`*_get` |
| refcount put        | kref_put、refcount_dec、put_device、`*_put` |
| free/release        | kfree、`*_free`、`*_release`                |
| sleepability        | might_sleep、mutex_lock、wait_event         |
| atomic context      | spin_lock、rcu_read_lock、GFP_ATOMIC        |
| blocking allocation | GFP_KERNEL                                  |
| lock requirement    | comments with must hold、caller holds       |

### 数据结构

```text
CFunction(
version_id,
c_symbol,
return_type,
params,
header_file,
definition_file
)
```

```text
CStruct(
version_id,
c_type,
fields,
size,
align,
header_file
)
```

```text
CBehaviorIndicator(
version_id,
c_symbol,
indicator_type,
evidence_file,
evidence_line,
evidence_text,
confidence
)
```

### 验收标准

- 输入 C symbol，能知道它的 signature、body indicators、commit history
- 输入两个版本，能知道哪些 indicators 新增 / 删除
- 能识别至少 NULL、ERR_PTR、error code、refcount、sleepability 五类 indicators

## Phase 6：构建 C-to-Rust Dependency Graph

| 子任务                | 做法                                     | 产出物             | 验收标准                           |
| --------------------- | ---------------------------------------- | ------------------ | ---------------------------------- |
| symbol normalization  | C symbol 与 binding symbol 对齐          | symbol map         | foo_bar 能映射到 bindings::foo_bar |
| 建图                  | 节点和边写入 graph DB                    | dependency graph   | 可双向查询                         |
| 关联 unsafe call      | binding use → unsafe block → wrapper API | unsafe path        | 能定位 risk boundary               |
| 关联 safe abstraction | wrapper API → public safe method         | safe API path      | 能知道是否暴露给 safe users        |
| 关联 helper           | C inline / macro → rust/helper wrapper   | helper path        | 能检测 helper drift                |
| 关联 drift records    | drift → affected graph nodes             | warning candidates | 能生成候选 warning                 |

### 节点类型

CFunction
CStruct
CMacro
CEnum
CInlineFunction
RustBindingFunction
RustBindingStruct
RustHelper
RustUnsafeCall
RustSafeAPI
RustType
RustDriverUser

### 边类型

GENERATED_FROM
CALLS_BINDING
WRAPS
EXPOSES_SAFE_API
USES_TYPE
DEPENDS_ON_LAYOUT
DEPENDS_ON_CONST
HAS_SAFETY_COMMENT
MODIFIED_AFTER

### 验收标准

- 输入 C API drift，能输出受影响 Rust wrapper
- 输入 Rust safe API，能输出底层 C dependency
- 输入 warning，能生成完整 evidence chain

## Phase 7：实现 Tier 1 Drift Detectors

Tier 1 是最稳妥、最客观的部分，必须优先做完。

### 7.1 SignatureDrift Detector

| 检测项               | 规则                               |
| -------------------- | ---------------------------------- |
| return type change   | old.return_type != new.return_type |
| param count change   | len(old.params) != len(new.params) |
| param type change    | normalized type diff               |
| pointer depth change | `T*` → `T**`                       |
| constness change     | T* → const T*                      |
| callback type change | function pointer signature diff    |

输出 warning：

```text
SignatureDrift:
c_symbol
old_signature
new_signature
affected_binding
affected_rust_api
build_breakage_likelihood
```

### 7.2 FieldDrift Detector

| 检测项               | 规则                                   |
| -------------------- | -------------------------------------- |
| field added          | field in new not old                   |
| field removed        | field in old not new                   |
| field renamed        | type/position similar but name changed |
| field type changed   | same name, different type              |
| nested field changed | recursively compare nested struct      |

### 7.3 LayoutDrift Detector

| 检测项                      | 规则                                   |
| --------------------------- | -------------------------------------- |
| size change                 | sizeof(old) != sizeof(new)             |
| alignment change            | alignof(old) != alignof(new)           |
| offset change               | offset(old.field) != offset(new.field) |
| bitfield change             | bitfield width / order change          |
| union representation change | union field set changed                |

### 7.4 MacroConstDrift Detector

| 检测项                     | 规则                        |
| -------------------------- | --------------------------- |
| const value changed        | old value != new value      |
| flag added/removed         | bitmask set changed         |
| enum variant changed       | enum value diff             |
| error code mapping changed | error-related macro changed |

### 7.5 HelperDrift Detector

检测 rust/helpers/ 中暴露给 Rust 的 C helper 是否与底层 C inline / macro 语义同步。

规则：

if C inline function changed
and corresponding rust/helper wrapper unchanged
and Rust wrapper uses helper
then emit HelperDrift warning

官方文档明确说明，bindgen 不能自动生成的 C inline functions 或复杂 macros 可通过 rust/helpers/ 小 wrapper 暴露给 Rust 侧，因此 helper 是非常重要的 drift 监控对象。

### Tier 1 验收标准

- 对任意相邻版本，能生成客观 drift records
- detector 结果可人工复查
- 能和 build failure 对齐
- 能作为 baseline 参与论文评估

## Phase 8：实现 Tier 2 Contract Drift Detectors

Tier 2 是论文亮点，但要做成“indicator-based warning”，不做 soundness proof。

### 8.1 NullabilityDrift Detector

#### 检测目标

发现 C API failure convention 变化：

return NULL
return ERR_PTR(...)
return non-NULL pointer
return int error code

#### 规则

old indicators:
returns NULL on failure

new indicators:
returns ERR_PTR on failure

Rust wrapper:
maps return to Option<T>

=> High-risk NullabilityDrift

或：

old:
returns ERR_PTR

new:
returns NULL

Rust wrapper:
uses from_err_ptr / to_result

=> High-risk ErrorRepresentationDrift

#### Rust 侧证据

搜索：

Option<...>
Result<...>
from_err_ptr(...)
to_result(...)
IS_ERR(...)
PTR_ERR(...)
NonNull::new(...)

#### 输出

```text
NullabilityDrift:
c_symbol
old_failure_convention
new_failure_convention
rust_mapping
affected_safe_api
risk = high
```

### 8.2 ErrorDrift Detector

#### 检测目标

发现 C 函数新增 / 删除错误码路径，而 Rust wrapper 文档或类型假设没有同步更新。

#### C 侧规则

比较函数 body 中的 error code indicators：

old: {-ENOMEM, -EINVAL}
new: {-ENOMEM, -EINVAL, -EAGAIN}

#### Rust 侧规则

检查 wrapper 是否：

- 只处理固定错误码
- 将所有负数简单转成 Error
- 文档中枚举了错误条件
- safe API 名称暗示不可失败
- 返回 Result<T> 但没有文档更新
  Warning
  ErrorDrift:
  c_symbol
  added_error_codes
  removed_error_codes
  affected_result_mapping
  affected_doc_comment

### 8.3 Ownership / Refcount Drift Detector

#### 检测目标

发现 C API ownership transfer 或 refcount 约定变化。

#### C 侧 indicators

`*_get`
`*_put`
get_device
put_device
kref_get
kref_put
refcount_inc
refcount_dec
atomic_inc
atomic_dec
kfree
`*_release`

#### Rust 侧 indicators

impl Drop
impl Clone
ARef
Arc
ForeignOwnable
Opaque
from_raw
into_raw
as_ptr
NonNull
ManuallyDrop

#### 规则示例

if C function newly calls get_device()/kref_get()
and Rust wrapper already increments refcount
then possible double get / leak
if C function stops returning owned reference
and Rust wrapper Drop still calls put/free
then possible use-after-free / double put
if C function newly transfers ownership
and Rust wrapper does not implement Drop or release
then possible leak
Warning

```text
OwnershipDrift:
c_symbol
old_ownership_indicators
new_ownership_indicators
rust_lifetime_pattern
affected_drop_or_clone_impl
risk
```

### 8.4 Allocation / Free Pairing Drift Detector

#### 检测目标

发现 C allocation / release API 对变化，而 Rust constructor / destructor 没有同步变化。

#### C 侧

alloc: kmalloc, kzalloc, vmalloc, `*_alloc`, `*_create`, `*_new`
free: kfree, vfree, `*_free`, `*_destroy`, `*_release`

#### Rust 侧

pub fn new(...)
impl Drop for ...

#### 规则

if constructor uses C alloc function A
and destructor uses C free function B
and A/B pairing changes in C history
then emit pairing drift warning

### 8.5 SleepabilityDrift Detector

#### 检测目标

发现 C API 从 non-sleeping 变成 may-sleep，或新增 blocking path。

#### C 侧 indicators

might_sleep()
mutex_lock()
wait_event()
schedule()
GFP_KERNEL
down_read()
down_write()

#### Rust 侧 indicators

spinlock guard
irqsave
preempt disabled context
atomic context comments

#### 规则

if C function newly includes might_sleep/mutex_lock/GFP_KERNEL
and Rust safe API is callable under spinlock/atomic context
then emit SleepabilityDrift

#### 注意

这类 warning 误报可能高，所以作为重点 case study，而不是唯一主线指标。

### Tier 2 验收标准

至少实现 4 类：

- NullabilityDrift
- ErrorDrift
- Ownership / Refcount Drift
- SleepabilityDrift 或 Allocation / Free Pairing Drift
- 每类至少找到真实或可人工确认 case
- 每类 warning 能给出 C evidence + Rust evidence
- 不把 warning 直接等同于 bug

## Phase 9：实现 Warning Ranking

| 特征                     | 含义                              | 分数方向                  |
| ------------------------ | --------------------------------- | ------------------------- |
| drift severity           | drift 本身严重程度                | 越严重越高                |
| Rust exposure            | 是否被 Rust 使用                  | 未使用低，safe API 暴露高 |
| unsafe proximity         | 是否穿过 unsafe block             | 越近越高                  |
| safe API visibility      | 是否 public                       | public 越高               |
| contract relevance       | 是否涉及 ownership / error / NULL | 越相关越高                |
| helper involvement       | 是否经过 rust/helpers/            | 是则更高                  |
| historical confidence    | 历史上该 pattern 是否常导致 fix   | 越高越高                  |
| build failure likelihood | 是否可能直接编译失败              | 越高越高                  |

#### 简单 scoring

```text
risk_score =
  2.0 * drift_severity
+ 2.0 * rust_exposure
+ 1.5 * unsafe_proximity
+ 1.5 * contract_relevance
+ 1.0 * helper_involvement
+ 1.0 * historical_confidence
+ 1.0 * build_failure_likelihood
```

#### Warning 输出格式

```text
warning_id: W-000123
type: OwnershipDrift
risk: High
score: 8.7

c_side:
symbol: foo_get()
old_version: v6.x
new_version: v6.y
evidence:
- removed kref_get()
- changed return path

rust_side:
binding: bindings::foo_get
unsafe_call: rust/kernel/foo.rs:123
safe_api: Foo::get()
safety_comment: "SAFETY: foo_get returns a valid owned reference"

explanation:
The C function no longer appears to return an owned reference,
but the Rust safe abstraction still treats the pointer as owned.

suggested_action:
Check whether Foo::get() should stop constructing an owning wrapper,
or whether Drop should be adjusted.
```

### 验收标准

- top warnings 明显比随机 warnings 更有价值
- warning 可以被 reviewer 快速理解
- 每个 warning 有完整证据链
- 支持 precision@10 / precision@50 / precision@100 评估

## Phase 10：构建 Ground Truth

### 10.1 Build Breakage Ground Truth

| 子任务                            | 做法                                                   |
| --------------------------------- | ------------------------------------------------------ |
| 对目标版本运行 Rust-enabled build | make LLVM=1 with Rust config                           |
| 收集 build logs                   | stderr/stdout                                          |
| 解析 Rust-related errors          | bindings::、type mismatch、missing field、layout error |
| 映射到 C symbol                   | 通过 error line 和 dependency graph                    |
| 标记 true breakage                | human confirm                                          |

### 10.2 Wrapper Fix Ground Truth

| 子任务                     | 做法                                             |
| -------------------------- | ------------------------------------------------ |
| 搜索 Rust-side fix commits | 修改 rust/kernel/、rust/helpers/、rust/bindings/ |
| 找前置 C-side change       | 同 symbol / same subsystem / nearby commits      |
| 分析 commit message        | 是否提到 API change / fix / build break          |
| diff wrapper               | 是否修改 Result、Drop、helper、signature         |
| 标注 relation              | confirmed / likely / unrelated                   |

### 10.3 Manual Review Ground Truth

| 子任务             | 做法                            |
| ------------------ | ------------------------------- |
| 采样 top-K warning | 按 risk rank 取样               |
| 分层采样           | 每类 drift 都有样本             |
| 双人标注           | true drift / benign / unclear   |
| 解决分歧           | discussion                      |
| 统计 precision     | precision@K、per-type precision |

#### Ground Truth 标签

```text
TRUE_BUILD_BREAKAGE
TRUE_WRAPPER_FIX
TRUE_SEMANTIC_DRIFT
BENIGN_DRIFT
FALSE_POSITIVE
UNCLEAR
```

### 验收标准

- 有强 oracle：build breakage
- 有中强 oracle：wrapper fix
- 有人工 oracle：semantic drift
- 不依赖单一人工 top-100

## Phase 11：历史 Replay 评估

评估任务 1：API drift 规模

| 指标                       | 含义                             |
| -------------------------- | -------------------------------- |
| #C symbols exposed to Rust | Rust 依赖的 C API 数量           |
| #binding functions         | generated binding 函数数量       |
| #binding structs           | generated binding 类型数量       |
| #Rust wrappers             | safe abstraction 数量            |
| #drift events              | 漂移事件数量                     |
| #drift reaching Rust       | 实际影响 Rust wrapper 的漂移数量 |

评估任务 2：Build breakage prediction

| 指标      | 含义                                |
| --------- | ----------------------------------- |
| Precision | warning 中多少导致 build breakage   |
| Recall    | build breakage 中多少被提前 warning |
| F1        | 综合指标                            |
| Lead time | warning 比修复早多少 commit / days  |

评估任务 3：Wrapper fix prediction

| 指标        | 含义                                       |
| ----------- | ------------------------------------------ |
| Precision@K | top-K warning 中有多少对应后续 wrapper fix |
| Recall      | wrapper fix 中多少能追溯到 warning         |
| MRR         | fix commit 对应 warning 排名               |
| Lead time   | drift warning 与 fix 之间距离              |

评估任务 4：Semantic warning quality

| 指标                      | 含义                   |
| ------------------------- | ---------------------- |
| Precision@10              | top 10 人工确认比例    |
| Precision@50              | top 50 人工确认比例    |
| Precision@100             | top 100 人工确认比例   |
| Per-type precision        | 每类 detector 的准确率 |
| False positive categories | 误报类型分析           |

评估任务 5：Baseline comparison

#### Baseline

| Baseline       | 说明                                        |
| -------------- | ------------------------------------------- |
| BindgenDiff    | 只比较 generated bindings                   |
| CSignatureDiff | 只比较 C signature                          |
| BuildOnly      | 只依赖 compiler error                       |
| GrepUsage      | 只检查 bindings::foo 是否被调用             |
| NoRanking      | 有 detector 但不排序                        |
| Tier1Only      | 只做 signature/layout/helper，不做 contract |

BindDrift 应证明：

- 比 BindgenDiff 更能定位 safe abstraction 风险
- 比 BuildOnly 更早发现问题
- 比 CSignatureDiff 误报更少
- Tier2 detector 能发现 compiler 不会报错的 high-risk drift
- ranking 能提高 top-K precision

## Phase 12：Case Studies

每个 case study 按统一模板写。

#### Case 模板

```text
Case title:
One-line summary
```

C-side change:
What changed in C API?

Rust-side dependency:
Which binding / helper / wrapper depends on it?

Why compiler cannot fully catch it:
Type still matches? Signature unchanged? Semantic only?

BindDrift warning:
What warning was emitted?

Evidence:
C evidence + Rust evidence + commit evidence

Impact:
Build breakage / possible stale contract / wrapper fix

Lesson:
What general drift pattern does this represent?

#### 推荐 case 类型

| Case 类型         | 目标                                       |
| ----------------- | ------------------------------------------ |
| SignatureDrift    | 展示工具能预测 build breakage              |
| LayoutDrift       | 展示 bindgen output drift 传播到 Rust type |
| HelperDrift       | 展示 inline / macro helper 是高风险点      |
| NullabilityDrift  | 展示 Option / Result 映射过期              |
| OwnershipDrift    | 展示 Drop / refcount wrapper 可能过期      |
| SleepabilityDrift | 展示 compiler 无法发现上下文语义变化       |

### 验收标准

- 至少 5 个高质量 case
- 至少 2 个 case 是 compiler 不容易发现的 semantic drift
- 每个 case 有完整 evidence chain
- case 能支撑论文核心 claim

## Phase 13：Ablation Study

#### Ablation 设计

| Variant         | 去掉什么                | 目的                                |
| --------------- | ----------------------- | ----------------------------------- |
| Full BindDrift  | 无                      | 主结果                              |
| NoGraph         | 不用 C-to-Rust graph    | 证明 graph 必要                     |
| NoTier2         | 不用 semantic detectors | 证明 contract drift detector 有价值 |
| NoRanking       | 不排序                  | 证明 ranking 有价值                 |
| NoSafetyComment | 不用 safety comments    | 证明文档/注释 signal 有帮助         |
| NoCommitText    | 不用 commit message     | 证明历史文本 signal 有帮助          |
| BindgenOnly     | 只看 bindgen output     | 证明不是简单 diff                   |

#### 预期结论

- NoGraph 会导致大量无关 C drift warning
- NoTier2 会漏掉语义 drift
- NoRanking 会降低 top-K precision
- BindgenOnly 无法解释 safe abstraction risk
- BuildOnly 无法提前发现非编译错误的 contract drift

## Phase 14：Threats to Validity

论文必须主动承认这些威胁。

Internal Validity

| 威胁                        | 缓解                                        |
| --------------------------- | ------------------------------------------- |
| toolchain 差异导致假 drift  | 固定 rustc / clang / bindgen，记录 metadata |
| config 差异导致 symbol 差异 | 固定 config，标记 config-dependent symbols  |
| regex 解析不完整            | 对关键结果人工抽查，引入 AST parser         |
| warning 不等于 bug          | 明确 claim 是 warning / prioritization      |
| commit relation 误配        | 使用多信号匹配 + manual validation          |

External Validity

| 威胁                 | 缓解                                          |
| -------------------- | --------------------------------------------- |
| 只研究 Linux/RFL     | 明确 CCF-B 版本聚焦 RFL，未来扩展跨生态       |
| 只研究 x86_64        | 把多架构作为 future work                      |
| Rust 代码量仍在增长  | 加入 rust-next / staged branches 作为扩展数据 |
| 结果依赖 kernel 版本 | 覆盖多个 releases / commits                   |

Construct Validity

| 威胁                       | 缓解                                      |
| -------------------------- | ----------------------------------------- |
| semantic drift 难以定义    | 使用 drift taxonomy 和 reviewer guideline |
| false positive 较多        | 使用 ranking 和 precision@K               |
| safety contract 难自动抽取 | 只抽取 indicators，不宣称完整 proof       |
| manual review 主观         | 双人标注 + disagreement resolution        |

## Phase 15：论文写作结构

### 推荐论文结构

## Introduction

## Background: Rust-for-Linux bindings and abstractions

## Motivating Examples

## Problem Definition

## BindDrift Design

### 5.1 Data Extraction

### 5.2 C-to-Rust Dependency Graph

### 5.3 Drift Taxonomy

### 5.4 Contract Drift Detectors

### 5.5 Warning Ranking

## Implementation

## Evaluation

### RQ1: Drift prevalence

### RQ2: Build breakage prediction

### RQ3: Wrapper fix prediction

### RQ4: Semantic warning precision

### RQ5: Ablation and baseline comparison

## Case Studies

## Discussion

## Threats to Validity

## Related Work

## Conclusion

## Phase 16：Artifact 组织

目录结构
binddrift/
README.md
Dockerfile
scripts/
prepare_kernel.sh
build_rust_kernel.sh
extract_bindings.sh
extract_c_api.sh
extract_rust_usage.sh
run_detectors.sh
run_evaluation.sh
binddrift/
extractors/
c_api.py
bindgen.py
rust_usage.py
commit.py
graph/
schema.py
builder.py
queries.py
detectors/
signature.py
layout.py
field.py
macro_const.py
helper.py
nullability.py
error.py
ownership.py
sleepability.py
ranking/
scorer.py
evaluation/
build_breakage.py
wrapper_fix.py
manual_review.py
baselines.py
data/
versions.csv
commits.csv
warnings.jsonl
ground_truth.csv
paper/
cases/
figures/
tables/

## Phase 17：最终完成标准

工具完成标准

- 能对两个 Linux versions 输出 drift
- 能对多个 Linux versions 做 batch replay
- 能构建 C-to-Rust dependency graph
- 能输出 ranked warnings
- 能生成 evaluation tables
- 能复现实验结果
  实验完成标准

| 实验                      | 完成标准                                      |
| ------------------------- | --------------------------------------------- |
| Drift prevalence          | 有完整统计表                                  |
| Build breakage prediction | 有 precision / recall                         |
| Wrapper fix prediction    | 有 precision@K / lead time                    |
| Semantic warning review   | 有人工标注结果                                |
| Baseline comparison       | 至少 4 个 baseline                            |
| Ablation                  | 至少 4 个 ablation variants                   |
| Case study                | 至少 5 个高质量案例                           |
| Threats                   | 覆盖 internal / external / construct validity |

论文完成标准

- Introduction 能讲清楚“为什么 Rust safe abstraction 会被 C API 演化影响”
- Background 能讲清楚 bindings / helpers / abstractions
- Method 能讲清楚 graph 和 detector
- Evaluation 不只靠人工审查
- Case studies 能展示 compiler catch 不到的 semantic drift
- Claim 不过度
- Artifact 可复现
  最终执行路线总结

最稳妥实现顺序是：

- 先做可复现构建和数据集
- 再做 bindgen output diff
- 再做 Rust `bindings::*` 使用抽取
- 再做 C-to-Rust dependency graph
- 先完成 Signature / Layout / Field / Helper 这些硬 drift
- 再加 NULL / ERR_PTR、Error、Ownership / Refcount 这些 contract drift indicators
- 最后做 ranking、ground truth、case study 和 ablation

这个顺序保证即使 Tier 2 semantic detector 部分效果一般，项目仍然有一个稳固的 CCF-B 主干：跨语言 API drift + dependency graph + historical replay。
