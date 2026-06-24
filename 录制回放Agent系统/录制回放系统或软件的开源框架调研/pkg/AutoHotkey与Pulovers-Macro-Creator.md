# AutoHotkey + Pulover's Macro Creator

## 项目介绍

AutoHotkey 是面向 Windows 的开源自动化脚本语言和运行时，常用于热键、文本替换、窗口控制、鼠标键盘模拟、简单 GUI 工具和重复任务自动化。它不是传统意义上的 RPA 平台，而是一个轻量、强大的 Windows 脚本执行层。

Pulover's Macro Creator 是基于 AutoHotkey 的免费自动化工具和脚本生成器，定位是“宏录制器 + 可视化流程编辑器 + AHK 导出工具”。它可以记录键盘、鼠标、窗口相关操作，并把宏导出为可运行的 AutoHotkey 脚本。

因此这两个工具更适合作为一个组合来看：Pulover's Macro Creator 负责降低录制和编辑门槛，AutoHotkey 负责承载最终脚本、运行和维护。组合适合把已经明确的人工操作固化成可重复执行的 Windows 脚本，但不负责理解业务目标、自动探索界面或生成生产级流程。

## 录制方式

- **主要方式：Pulover's Macro Creator 录制键盘鼠标宏，再导出 AutoHotkey 脚本。**
- AutoHotkey 本体通常由开发者手写 `.ahk` 脚本；Pulover 补充可视化录制、步骤编辑和脚本生成能力。
- 可以记录按键、鼠标移动、点击，并支持相对窗口或相对屏幕的坐标。
- 支持在宏中加入循环、条件判断、变量、文件操作、图片/像素搜索、窗口/控件命令等步骤。
- AutoHotkey 回放阶段可通过 `Send`、`Click`、`ControlClick`、`ControlSend`、`WinWait`、`WinActivate`、`ImageSearch`、`PixelSearch`、COM 等命令控制应用。
- **不是视频录制。** 回放依赖宏步骤、AHK 脚本和窗口/控件/图像定位，不会分析录像生成自动化流程。
- **不能只给一段文字描述。** 组合不具备原生 AI 语义理解能力，也不会根据业务目标自主探索桌面软件。

## 核心能力

| 能力 | 结论 |
| --- | --- |
| AI 语义理解 | 不支持 |
| 框架自动截图 | 可通过脚本或外部库实现；Pulover 主要提供图像/像素搜索相关能力 |
| UIA/原生控件信息 | 支持部分窗口/传统控件命令，但不是完整 UIA 自动化框架 |
| 鼠标键盘模拟 | 支持 |
| 鼠标键盘录制 | Pulover's Macro Creator 支持 |
| 图像/像素定位 | 支持 `ImageSearch`、`PixelSearch` |
| 人工录制 | 支持，主要由 Pulover's Macro Creator 提供 |
| 生成回放资产 | 支持 `.ahk` 脚本和可执行文件 |
| 参数化和批量执行 | 支持变量、循环、条件、文件读写、命令行参数，但需要人工设计 |
| 一键回放 | 支持 |
| 自动探索 App | 不支持 |
| 适用平台 | Windows |
| 开源 | AutoHotkey 为 GPL-2.0；Pulover's Macro Creator 为 GPL-3.0 |

## 优势

- 组合门槛低：Pulover 负责录制和可视化编辑，AutoHotkey 负责脚本执行和后续维护。
- AutoHotkey 轻量、成熟、社区大，Windows 桌面自动化资料非常丰富。
- 可以导出 `.ahk` 脚本，比黑盒宏文件更容易审阅、修改和版本管理，也可以编译为 exe 交付。
- 对热键、键鼠模拟、窗口激活、剪贴板、文件处理、批量循环等固定任务非常高效。
- 支持循环、条件、变量、图片搜索、像素搜索、窗口命令、控件命令等常见自动化元素。
- 可以和 Python、PowerShell、命令行工具、数据库导出文件等外围系统组合。
- 适合作为简单 Windows 重复操作、数据录入、文件处理和辅助办公场景的快速 PoC 工具。

## 局限和风险

- Pulover's Macro Creator 最近正式 Release 停留在 2021 年，活跃度弱于 AutoHotkey 本体和当前 AI Agent 项目。
- 录制结果容易包含坐标、窗口状态和人工路径细节，复杂界面变化后维护成本较高。
- 对复杂桌面软件的稳定定位能力弱于 pywinauto/UIA 等专门框架，常退化为窗口标题、控件名、坐标、图像、像素或键盘路径。
- 图像、坐标、窗口标题等方式容易受分辨率、缩放、主题、语言、弹窗和布局变化影响。
- 组合不理解业务目标，也不会自动识别“哪个输入是参数、哪个表格是结果、哪个弹窗是异常”。
- 不具备任务级日志、报告、任务队列、失败重跑、参数批量管理等生产化 RPA 能力，需要自行建设。
- 对金融终端、自绘控件、复杂表格、远程桌面等场景，仍需大量 PoC 验证和兜底逻辑。

## 不符合要求的核心原因

1. **不具备 AI 语义理解和自主探索 App 能力。**
2. **录制以键鼠宏为主，难以天然生成稳定、语义化、参数化的业务流程。**
3. **复杂桌面软件、金融终端、自绘控件和异常分支需要大量人工维护。**
4. 参数化和批量执行可以实现，但不是开箱即用的业务流程管理能力。
5. Pulover 项目活跃度偏低，不适合作为长期主方案依赖。

## 适用结论

AutoHotkey + Pulover's Macro Creator 适合作为 Windows 固定流程的轻量录制和执行组合：Pulover 用于快速录制、编辑和导出 AHK；AutoHotkey 用于脚本运行、维护和集成。它可以承担热键触发、窗口切换、键鼠模拟、简单数据录入、文件整理等边缘自动化任务。

对于本次目标，它更适合作为“示教录制参考工具”或“AHK 脚本生成/执行层”，不建议作为主方案。若需要生产化，应把录制得到的 AHK 步骤重构到 Python/Robot Framework 等可参数化、可测试、可调度的执行层中；AutoHotkey 只负责少量难以用主框架处理的键鼠动作或本地快捷操作。

## 参考资料

- [AutoHotkey 官网](https://www.autohotkey.com/)
- [AutoHotkey GitHub](https://github.com/AutoHotkey/AutoHotkey)
- [AutoHotkey 文档](https://www.autohotkey.com/docs/v2/)
- [Pulover's Macro Creator 官网](https://www.macrocreator.com/)
- [Pulover's Macro Creator GitHub](https://github.com/Pulover/PuloversMacroCreator)
