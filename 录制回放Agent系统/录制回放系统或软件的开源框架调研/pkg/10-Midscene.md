# Midscene

## 项目介绍

Midscene 是开源的视觉驱动 UI 自动化框架。它通过多模态模型理解截图和自然语言，支持 Web、Windows/macOS/Linux PC、Android、iOS、HarmonyOS 和自定义界面。

用户可以描述操作目标或待提取的数据，由 Midscene 规划步骤、定位元素、点击、输入、查询和断言，并将流程写成 JavaScript 或 YAML 后重复执行。

## 录制方式

Midscene 不同平台的“录制”方式不同：

- **Web：操作事件录制。** Chrome Recorder 记录点击、输入、滚动等操作，并生成或整理为自动化步骤。
- **PC：当前主要是文字描述或编写 JS/YAML。** 用户描述目标后，框架运行时自动截图，模型理解界面并执行。
- **不是视频录制学习。** HTML 报告可以回看执行过程，但报告回放不等于通过视频生成脚本。
- Web 和 PC 都不要求用户手工截取按钮模板。
- PC Studio 完整的“人工操作录制 → 自动生成结构化脚本 → 导出”仍在完善。

## 核心能力

| 能力 | 结论 |
| --- | --- |
| AI 语义理解 | 支持 |
| 框架自动截图 | 支持 |
| 人工录制 | Web 支持事件录制；PC 以文字描述/JS/YAML 为主 |
| 生成回放资产 | 支持 JavaScript、YAML、测试代码和工作流 |
| 一键回放 | 支持 CLI、SDK、测试框架和 MCP |
| 自动探索 App/页面 | 支持，`aiAct` 可根据目标自主规划 |
| 开源 | 是，MIT |

## Web 能力

- Chrome 扩展 Recorder 可记录点击、输入和滚动。
- 可与 Playwright、Puppeteer、Vitest 集成。
- 支持页面数据查询、断言、下载和执行报告。
- 可以把 AI 步骤与确定性浏览器代码混合使用。

## PC 官方能力

官方包 [`@midscene/computer`](https://www.npmjs.com/package/@midscene/computer) 支持：

- Windows、macOS、Linux。
- 本地桌面和远程 Windows RDP。
- 自动截图、多显示器、鼠标、键盘、右键、拖动和滚动。
- Computer Playground、JavaScript SDK、YAML、CLI、MCP 和 HTML 报告。
- Electron、Qt、WPF 和原生桌面程序。

## 第三方 PC 包

- [Mofangbao/midscene-pc](https://github.com/Mofangbao/midscene-pc)：支持 Windows、macOS、Linux 的本地和远程桌面 Connector/Agent。
- [Mofangbao/midscene-pc-docker](https://github.com/Mofangbao/midscene-pc-docker)：提供 Ubuntu、GNOME 和 VNC 容器化桌面环境。

目前官方 PC 能力已经较完整，新项目应优先评估官方 `@midscene/computer`，第三方包可作为特定远程部署方案或实现参考。

## 自动探索潜力

Midscene 与需求中“告诉系统要什么数据，让它自己去 App 里探索”最接近：

1. AI 根据自然语言理解目标。
2. 框架自动截图并把界面交给视觉模型。
3. `aiAct` 规划并执行多步操作。
4. `aiQuery` 从当前界面提取结构化数据。
5. 探索成功后可把步骤整理为 JS/YAML，后续重复回放。

生产使用时，建议把成功探索出的路径固化为脚本，不要每次都从头自由探索。

## 局限和风险

- AI 操作不是完全确定性，复杂长流程需要重试、断言和人工审核。
- PC 端完整的 Studio“录制 → 自动生成脚本 → 导出 → 回放”闭环截至 2026-06-23 仍在完善。
- 纯视觉方式可能受分辨率、遮挡、弹窗和模型能力影响。
- 需要控制截图数据、账号凭据和模型服务的安全边界。

## 不符合要求的核心原因

Midscene 基本符合主要目标，但仍有以下缺口：

1. **PC 端完整录制自动转脚本闭环尚未完全成熟。**
2. 自动探索存在概率性，不能直接保证生产级成功率。
3. 长流程需要加入断言、失败恢复和确定性步骤。

## 适用结论

综合 AI 语义理解、自动截图、脚本回放、跨平台和自主探索能力，Midscene 是当前最匹配的候选。建议作为第一优先 PoC，并以 Playwright 或 JS/YAML 固化探索结果。

## 参考资料

- [Midscene GitHub](https://github.com/web-infra-dev/midscene)
- [PC Desktop Automation](https://midscenejs.com/computer-introduction)
- [PC Desktop Getting Started](https://midscenejs.com/computer-getting-started)
- [Midscene Changelog](https://midscenejs.com/changelog)

