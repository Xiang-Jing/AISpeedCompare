# Open Computer Use / Coasty

## 项目介绍

Open Computer Use 是 Coasty AI 开源的 computer-use agent 项目，官方仓库为 `coasty-ai/open-computer-use`。项目目标是让 AI Agent 能控制真实电脑，覆盖浏览器、桌面应用和终端场景，并支持多 Agent 编排。

仓库 README 将其描述为开源的云端 computer-use 平台，具备浏览器控制、桌面控制、终端命令执行、任务执行和多 Agent 工作流编排能力。项目还提供 Desktop App、本地环境、远程环境、SDK 和任务/工作流相关能力。License 为 Apache-2.0。

## 录制方式

- **主要方式不是人工录制，而是自然语言任务驱动。** 用户输入任务后，由 Agent 控制浏览器、桌面或终端完成动作。
- 支持浏览器控制、桌面 UI 控制和终端命令执行，适合桌面 + 浏览器 + 命令行混合任务。
- 支持多 Agent 编排和工作流式任务执行，但这不等同于传统 RPA 的“录制一次后生成确定性脚本”。
- **不是视频录制。** 即使系统记录运行轨迹，也主要用于任务执行、调试或审计，不是从录像生成可回放脚本。
- 若要沉淀生产资产，需要额外把成功轨迹转写成 Python、Robot Framework、AHK、Playwright、YAML 或自定义 DSL。

## 核心能力

| 能力 | 结论 |
| --- | --- |
| AI 语义理解 | 支持，依赖接入的 LLM/VLM |
| 框架自动截图 | 支持，桌面/browser computer-use 的基础能力 |
| UIA/原生控件信息 | 未见其作为核心能力强调，需实测 |
| 鼠标键盘控制 | 支持 |
| 浏览器控制 | 支持 |
| 命令行/终端操作 | 支持 |
| 多 Agent 编排 | 支持 |
| 人工录制 | 不是核心能力 |
| 生成确定性脚本 | 暂无成熟通用闭环 |
| 参数化和批量执行 | 可通过任务/工作流层设计，但需要工程化验证 |
| 一键回放 | 可重新运行任务/工作流，但不等同固定脚本回放 |
| 自动探索 App | 支持方向明确，实际成功率需 PoC |
| 适用平台 | 官方强调本地/远程环境和 Desktop App，具体 Windows 金融客户端适配需实测 |
| 开源 | 是，Apache-2.0 |

## 优势

- 方向接近“AI 直接操作电脑”，覆盖浏览器、桌面、终端和工作流编排。
- 不是单纯浏览器 Agent，对桌面任务和命令行任务也有覆盖。
- 支持多 Agent 工作流，适合探索复杂任务拆解和协同执行。
- 提供 Desktop App、本地环境和远程环境，便于搭建 computer-use agent PoC。
- Apache-2.0 许可证相对友好，适合技术团队二次验证。

## 局限和风险

- 核心范式是 Agent 实时决策，不是传统录制回放器。
- 缺少成熟的“探索轨迹 -> 可审阅参数化脚本 -> 批量稳定回放”闭环。
- 对模型能力、环境权限、运行沙箱和网络可用性依赖较强。
- 如果允许 Agent 操作桌面、终端和文件系统，必须严格设计权限边界、凭据保护和审计日志。
- 对 Windows 专业客户端、金融终端、自绘控件、复杂弹窗和长流程任务的稳定性需要实际 PoC。

## 不符合要求的核心原因

1. **偏 AI 自主执行，不是传统录制回放工具。**
2. **暂未看到成熟的录制后自动生成独立、参数化、确定性脚本的能力。**
3. 生产化所需的权限隔离、日志审计、失败重跑、参数批量管理和结果校验需要额外建设。
4. 对 Wind 等专业金融客户端的控件识别和异常恢复能力必须实测。

## 适用结论

Open Computer Use / Coasty 适合放在 AI computer-use agent 探索层，用于验证“自然语言任务 -> 浏览器/桌面/终端混合执行 -> 多 Agent 编排”的能力。

如果目标是稳定采集或批量回放，不建议单独作为主执行层。更合理的方式是：Open Computer Use 负责试跑、探索和发现路径；人工或脚本生成层把成功路径固化到 Robot Framework、Python、pywinauto/FlaUI、AutoHotkey 或 Playwright 等确定性执行层中。

## 参考资料

- [Open Computer Use GitHub](https://github.com/coasty-ai/open-computer-use)
- [Coasty AI](https://github.com/coasty-ai)
