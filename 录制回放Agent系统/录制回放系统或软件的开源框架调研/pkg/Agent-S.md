# Agent S

## 项目介绍

Agent S 是 Simular AI 开源的 GUI Agent / Computer Use Agent 框架，目标是让智能体像人一样通过图形界面操作电脑。它围绕 Agent-Computer Interface（ACI）构建，利用多模态大模型观察屏幕、规划步骤、定位界面元素并执行鼠标键盘动作。

项目最初以 Agent S 论文和代码发布，后续演进到 Agent S2、Agent S2.5、Agent S3。官方仓库介绍其支持 Linux、macOS 和 Windows，并提供 `gui-agents` 包、CLI 和 SDK 用于运行 GUI Agent。它更偏 AI Agent 研究和 computer-use 能力验证，不是传统 RPA 录制回放产品。

## 录制方式

- **主要方式不是人工录制，而是自然语言任务驱动。** 用户给出任务目标后，Agent 根据屏幕观察和历史经验规划操作。
- 执行过程中会持续获取屏幕状态，并使用 grounding 模型把高层动作映射到具体坐标或界面操作。
- 支持经验检索、层级规划、反思等 Agent 机制，用于处理长步骤和动态界面。
- 可选启用本地代码执行环境，让 Agent 通过 Python/Bash 处理文件、数据和系统任务。
- **不是视频录制。** 它不会从录屏中自动生成固定脚本。
- **不是传统示教录制器。** 它的核心是智能体自主执行，不是记录人工操作后稳定重放。

## 核心能力

| 能力 | 结论 |
| --- | --- |
| AI 语义理解 | 支持，依赖 LLM/MLLM |
| 框架自动截图 | 支持，是 GUI Agent 的核心观察方式 |
| Grounding/坐标定位 | 支持，需要专门的 grounding 模型或服务 |
| UIA/原生控件信息 | 不是核心公开定位方式，主要依赖 ACI、截图和模型 grounding |
| 鼠标键盘控制 | 支持 |
| 命令行/本地代码执行 | 可选支持，需谨慎开启 |
| 人工录制 | 不是核心能力 |
| 生成确定性脚本 | 暂无成熟通用闭环 |
| 参数化和批量执行 | 需要外部封装 |
| 一键回放 | 可重新运行任务，但不等同固定脚本回放 |
| 自动探索 App | 支持，是其核心方向 |
| 适用平台 | Linux、macOS、Windows |
| 开源 | 是，Apache-2.0 |

## 优势

- 方向非常接近“AI 看屏幕并自主操作电脑”。
- 支持多操作系统，不局限浏览器，适合桌面 GUI Agent 研究。
- 层级规划、经验检索、反思和 grounding 组合，比简单截图点击 Agent 更完整。
- 在 OSWorld、WindowsAgentArena、AndroidWorld 等 computer-use benchmark 上持续迭代。
- 可作为自研 AI 桌面 Agent 的参考框架，学习其 ACI、规划、grounding 和经验机制。

## 局限和风险

- 不是传统 RPA 产品，没有成熟录制、参数抽取、流程设计器和稳定回放闭环。
- 生产执行依赖模型实时推理，同一任务多次运行可能路径不同，可复现性弱于固定脚本。
- 部署门槛较高，需要主模型、grounding 模型、API Key 或本地推理服务。
- 本地代码执行能力有较高安全风险，必须在可信、隔离环境中使用。
- 对具体 Windows 金融客户端、企业客户端、自绘控件和长流程异常恢复，需要单独 PoC。

## 不符合要求的核心原因

1. **缺少“探索或录制一次 -> 生成可审阅参数化脚本 -> 批量稳定回放”的成熟闭环。**
2. **执行范式是 Agent 实时决策，不是确定性流程脚本。**
3. 参数化、日志审计、失败重跑、权限隔离和结果校验需要外部工程化补齐。
4. 更适合研究和探索层，不适合直接作为生产回放主执行层。

## 适用结论

Agent S 适合放在 AI 探索层，用来验证“给出自然语言任务后，Agent 能否自己理解界面并找到操作路径”。它对构建自研 GUI Agent、比较模型能力、探索 ACI 和 grounding 方案很有参考价值。

如果目标是稳定采集或批量执行，不建议单独依赖 Agent S。更合理的方式是：Agent S 负责探索和生成候选路径；人工或脚本生成层把成功路径固化为 Python、Robot Framework、pywinauto/FlaUI、AutoHotkey 或 Playwright 脚本；生产阶段由确定性脚本负责参数化、日志、重试和结果校验。

## 参考资料

- [Agent S GitHub](https://github.com/simular-ai/Agent-S)
- [Agent S 论文](https://arxiv.org/abs/2410.08164)
- [Agent S2 论文](https://arxiv.org/abs/2504.00906)
- [Simular AI](https://www.simular.ai/)
