# Open Computer Use / Coasty

## 项目介绍

Open Computer Use / Coasty 在现有清单中被归为 AI computer-use agent 方向：目标是让 AI Agent 通过截图、鼠标、键盘、终端和系统命令操作真实电脑，完成浏览器、桌面应用和命令行混合任务。

需要特别说明：截至本次补充时，未检索到稳定、可确认的官方仓库或文档入口。这里先按“待核实的 AI 电脑操作框架”记录其可能定位和评估口径，不能像 UI-TARS、UFO、OpenAdapt 那样作为已确认资料充分的候选项。后续如果能确认准确 GitHub 地址，应补充 License、Stars、最近更新时间、安装方式和实际能力边界。

## 录制方式

- **主要方式不是人工录制，而是自然语言任务驱动。** 用户描述目标后，由 Agent 观察屏幕或系统状态并规划动作。
- 可能通过截图、可访问性信息、鼠标键盘控制、Shell/PowerShell 命令、文件系统工具等方式执行任务。
- **不是传统录制回放器。** 它的重点是 AI 实时决策和电脑控制，而不是把人工操作录成稳定脚本。
- **不是视频录制。** 即使支持轨迹记录，也通常用于调试、审计或评估，不等同于从视频生成可回放脚本。
- 若要沉淀生产资产，需要额外把成功轨迹转写成 Python、Robot Framework、AHK、Playwright 或自定义 DSL。

## 核心能力

| 能力 | 结论 |
| --- | --- |
| AI 语义理解 | 理论上支持，依赖接入的 LLM/VLM |
| 框架自动截图 | 可能支持，是 computer-use agent 的基础能力 |
| UIA/原生控件信息 | 待核实 |
| 鼠标键盘控制 | 可能支持 |
| 命令行/文件系统操作 | 可能支持 |
| 人工录制 | 不是核心能力 |
| 生成确定性脚本 | 暂无可确认成熟闭环 |
| 参数化和批量执行 | 需要外部设计 |
| 一键回放 | 可重新运行任务，但不等同固定脚本回放 |
| 自动探索 App | 理论方向支持，实际能力待验证 |
| 适用平台 | 清单中描述为 Windows、macOS、Linux，需核实 |
| 开源 | 待核实 |

## 优势

- 方向接近“AI 直接操作电脑”，能覆盖桌面、浏览器、终端和文件系统混合任务。
- 如果工具链完整，适合用自然语言探索未知界面和长步骤任务。
- 对“先让 AI 试着完成一次，再由人固化流程”的研发路线有参考价值。
- 可作为 GUI Agent PoC 平台，用于比较不同模型在电脑操作任务上的表现。

## 局限和风险

- 项目信息待核实，不能直接作为正式选型依据。
- computer-use agent 通常依赖模型实时判断，确定性、可复现性和错误恢复弱于固定脚本。
- 缺少成熟录制、参数抽取、批量回放、日志报告和审计闭环。
- 权限风险较高：Agent 如果能操作桌面、命令行和文件系统，必须严格限制账号、目录、网络和凭据访问。
- 对 Windows 专业客户端、金融终端、复杂弹窗和长流程任务的成功率需要实际 PoC。

## 不符合要求的核心原因

1. **资料来源尚未确认，不适合直接进入主方案。**
2. **偏 AI 自主执行，不是传统录制回放工具。**
3. **缺少可确认的“探索轨迹 -> 可审阅参数化脚本 -> 批量稳定回放”闭环。**
4. 生产化所需的权限隔离、日志审计、失败重跑和结果校验需要额外建设。

## 适用结论

Open Computer Use / Coasty 可以暂时放入“AI computer-use agent 待核实候选”类别，不建议作为近期落地主方案。若后续确认项目真实可用，推荐把它作为探索层：让 AI 试跑和发现路径，再把成功路径固化到 Robot Framework、Python、pywinauto/FlaUI、AutoHotkey 或 Playwright 等确定性执行层。

当前更稳的替代选择是：Windows 桌面 Agent 用 Microsoft UFO 或 UI-TARS Desktop；演示学习方向用 OpenAdapt；computer-use 基础设施方向用 CUA / trycua；生产回放仍由 Robot Framework、OpenRPA、pywinauto/FlaUI 或 AutoHotkey 承担。

## 参考资料

- 当前未检索到可确认的 Open Computer Use / Coasty 官方仓库或文档入口。
- 相关方向参考：[Microsoft UFO GitHub](https://github.com/microsoft/UFO)
- 相关方向参考：[OpenAdapt GitHub](https://github.com/OpenAdaptAI/OpenAdapt)
- 相关方向参考：[trycua/cua GitHub](https://github.com/trycua/cua)
