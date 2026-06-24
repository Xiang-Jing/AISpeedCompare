# FlaUI + WinAppDriver

## 项目介绍

FlaUI 是 .NET 生态的 Windows UI Automation 自动化库，支持通过 UIA2/UIA3 操作 Win32、WinForms、WPF、Store Apps 等 Windows 应用。WinAppDriver 是微软开源的 Windows Application Driver，提供类似 Selenium/Appium 的方式自动化 Windows 应用。

这两者不是 AI Agent，也不是面向普通用户的 RPA Studio，但它们代表了 Windows 控件级确定性执行层。对于金融终端、企业客户端、WPF/WinForms 软件，如果控件树可访问，FlaUI/WinAppDriver 通常比坐标点击、图片匹配更稳定。

## 录制方式

- FlaUI 本身不提供完整录制器，主要通过 C#/.NET 编写自动化代码。
- WinAppDriver 生态曾有 Windows Application Driver UI Recorder，可辅助生成定位信息和代码片段，但整体维护活跃度需谨慎评估。
- 它们更适合作为“脚本生成目标”和“控件定位工具”，由 AI 根据观察结果生成或修正代码。
- 不是视频学习，也不具备自然语言自主探索能力。

## 核心能力

| 能力 | 结论 |
| --- | --- |
| AI 语义理解 | 不支持，可由上层 Agent 调用 |
| 框架自动截图 | 可通过代码实现，不是核心定位方式 |
| UIA/原生控件信息 | 支持，是核心价值 |
| 人工录制 | 弱；WinAppDriver 生态有辅助录制工具但不宜作为主方案 |
| 生成回放资产 | 支持 C#/.NET、Appium 风格脚本，需编写或生成 |
| 参数化和批量执行 | 支持，依赖工程封装 |
| 一键回放 | 支持命令行/测试框架方式 |
| 自动探索 App | 不支持 |
| 适用平台 | Windows |
| 开源 | FlaUI 为 MIT；WinAppDriver 为 MIT |

## 优势

- 对标准 Windows 控件比坐标、截图模板更稳定。
- 能读取控件名称、AutomationId、ControlType、层级结构等信息，适合脚本生成器选择定位策略。
- 适合与 UFO、pywinauto、LangGraph 组合：Agent 负责识别目标，FlaUI/WinAppDriver 负责执行确定性动作。
- 对 WPF、WinForms、Win32 等企业客户端有较高价值。

## 局限和风险

- 对自绘控件、远程桌面、游戏式渲染界面、Canvas/Qt 特殊控件可能效果有限。
- 需要 .NET 或 Appium/Selenium 技术栈能力。
- WinAppDriver 维护活跃度和兼容性需要单独 PoC。
- 不提供完整的 AI 录制、参数抽取、脚本发布和回放验证闭环。

## 不符合要求的核心原因

1. **没有 AI 自主探索能力。**
2. **没有成熟面向业务人员的录制转参数化脚本产品体验。**
3. 只能作为确定性执行层或控件定位层。

## 适用结论

FlaUI/WinAppDriver 建议补入 Windows 桌面执行层。最终方案中，优先顺序应为：能走 UIA/控件树就走 FlaUI/pywinauto/WinAppDriver；控件不可见再走 OCR/视觉；最后才用坐标兜底。

## 参考资料

- [FlaUI GitHub](https://github.com/FlaUI/FlaUI)
- [WinAppDriver GitHub](https://github.com/microsoft/WinAppDriver)

