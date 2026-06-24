# UI.Vision RPA

## 项目介绍

UI.Vision RPA 是 A9T9 维护的开源 RPA 工具，核心形态是浏览器扩展，支持 Chrome、Edge 和 Firefox。它继承了 Selenium IDE / iMacros 类工具的 Web 宏录制和回放能力，同时通过图像识别、OCR 和 XModules 扩展到桌面自动化。

项目仓库显示其核心代码开源，GitHub 介绍中也明确提到 Computer Vision、OCR、Anthropic Computer Use/LLM 和 Selenium IDE 导入导出能力。需要注意的是，AI 能力属于较新的增强项，更多是给宏命令增加视觉定位和 LLM 辅助，而不是完整的自主探索型桌面 Agent。

## 录制方式

- **Web 自动化主要方式：浏览器宏录制。** 可以记录点击、输入、选择等 Selenium IDE 风格命令，并保存为可回放的宏。
- **桌面自动化主要方式：视觉命令手工构建。** 官方文档说明桌面模式下通常用 `XClick`、`XMove`、`XType`、OCR 等命令逐步搭建宏。
- **桌面模式不支持完整操作录制。** 官方文档明确说明 `Record` 按钮只用于 Selenium IDE 类型的浏览器宏，不能录制 `XClick`、`XMove` 和 `XType` 桌面命令。
- 可以通过截图模板、图像匹配、OCR 文本识别、坐标和键盘输入组合回放桌面流程。
- **不是录制视频后自动理解。** 它依赖宏命令、图像模板、OCR 和脚本逻辑，而不是分析录像生成流程。
- **不能只给一段文字描述。** 新增 AI 命令可调用 Anthropic Claude API 做提示词、屏幕坐标或 Computer Use 辅助，但整体仍需要用户设计宏流程，不能稳定地从业务目标自主探索并沉淀生产级脚本。

## 核心能力

| 能力 | 结论 |
| --- | --- |
| AI 语义理解 | 部分支持，依赖 Anthropic API 的新 AI 命令，能力仍偏辅助和 Beta |
| 框架自动截图 | 支持，包含网页截图和桌面截图命令 |
| 图像识别/OCR | 支持，是其桌面自动化核心能力 |
| UIA/原生控件信息 | 不作为核心定位方式，主要依赖视觉、OCR、坐标和键盘鼠标模拟 |
| 人工录制 | Web 支持 Selenium IDE 风格录制；桌面视觉命令不支持完整录制 |
| 生成回放资产 | 支持，宏命令/JSON/HTML/Selenium IDE 风格脚本 |
| 参数化和批量执行 | 支持变量、CSV 读写、循环、命令行参数和测试套件 |
| 一键回放 | 支持 |
| 自动探索 App | 不成熟，不适合作为核心能力 |
| 适用平台 | Web、Windows/Mac/Linux 桌面视觉自动化 |
| 开源 | 核心开源，GNU/AGPL 相关许可证；部分 XModules/企业能力需单独确认 |

## 优势

- Web 录制回放链路成熟，适合替代 Selenium IDE、iMacros 一类宏工具。
- 同一套工具可覆盖 Web、桌面、OCR、视觉点击和屏幕抓取。
- 支持 CSV 数据驱动、循环、流程控制、命令行启动、测试套件和日志报告。
- 对 Citrix、SAP GUI、自绘界面、远程桌面这类控件树不可访问场景，视觉/OCR 方案比纯 UIA 更容易起步。
- 宏资产可保存、导入导出、版本管理，并能和外部脚本通过命令行 API 集成。

## 局限和风险

- 桌面自动化主要依赖截图模板、OCR、坐标区域和键鼠模拟，稳定性受分辨率、缩放、主题、字体、窗口布局影响。
- 桌面命令不能像浏览器宏一样完整录制，需要人工逐步选择截图区域、配置 `XClick`/`XType` 等命令。
- AI 功能依赖 Anthropic Claude API，存在云端依赖、费用、合规和网络可用性问题；本地 LLM 支持仍需关注实际可用程度。
- 不以 Windows UIA 控件树为核心，面对复杂金融客户端时，无法天然获得控件属性、表格结构和语义层级。
- 适合固定流程和视觉自动化补位，但不适合直接承担高频、强可追溯、强确定性的批量生产执行主链路。

## 不符合要求的核心原因

1. **桌面端缺少完整“人工录制 -> 自动生成稳定脚本”的能力。**
2. **AI 能力仍偏命令级辅助，不等同于能根据业务目标自主探索 App 并固化流程。**
3. **桌面定位以视觉/OCR 为主，参数变化、窗口变化和界面细节变化后维护成本较高。**
4. **缺少面向 Windows 原生控件树的结构化理解，不适合作为复杂桌面客户端的唯一执行层。**

## 适用结论

UI.Vision RPA 适合作为 Web 宏录制、视觉/OCR 桌面自动化和屏幕抓取的辅助方案。对于控件树不可见的老旧客户端、Citrix、远程桌面、SAP GUI 或少量固定桌面流程，它可以快速做 PoC。

如果目标是“AI 探索 Windows 桌面软件 -> 生成可审阅、可参数化、可批量稳定回放脚本”，不建议单独作为主方案。更适合与 pywinauto、Robot Framework、Playwright 或 AI GUI Agent 组合：UI.Vision 负责视觉/OCR 兜底和宏原型，结构化执行与批量回放由 Python/Robot 层固化。

## 参考资料

- [UI.Vision RPA 官网](https://ui.vision/rpa)
- [UI.Vision RPA 文档](https://ui.vision/rpa/docs/)
- [UI.Vision Desktop Automation](https://ui.vision/rpa/x/desktop-automation)
- [UI.Vision AI](https://ui.vision/ai)
- [A9T9/RPA GitHub](https://github.com/A9T9/RPA)
