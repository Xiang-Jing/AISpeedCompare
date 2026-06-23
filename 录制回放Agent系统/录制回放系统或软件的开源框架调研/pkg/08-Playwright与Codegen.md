# Playwright + Playwright Codegen

## 项目介绍

Playwright 是 Microsoft 开源的浏览器自动化框架。`playwright codegen` 能记录用户在网页上的点击、输入和选择行为，并实时生成 JavaScript、TypeScript、Python、Java 或 .NET 代码。

## 录制方式

- **主要方式：浏览器操作事件录制。**
- Codegen 监听点击、输入、选择等事件，同时读取 DOM 和定位器，实时生成代码。
- **不是录制视频后识别操作。** Playwright 可以录制视频，但视频主要用于调试和留证，不能直接作为回放脚本。
- 不需要人工截图；截图、Trace 和视频均可由框架自动生成。
- **不能只给一段文字描述。** 原生 Playwright 不会根据业务目标自主探索页面。

## 核心能力

| 能力 | 结论 |
| --- | --- |
| AI 语义理解 | 不原生支持 |
| 框架自动截图 | 支持 |
| 人工录制 | 支持操作事件录制并生成代码；视频仅用于留证 |
| 生成回放资产 | 支持多语言源代码 |
| 一键回放 | 支持 |
| 自动探索页面 | 不支持 |
| 适用平台 | Web |

## 优势

- 录制、生成脚本和重复回放非常成熟。
- 支持自动等待、登录态、下载、网络拦截、并发、截图、视频和 Trace。
- 脚本可审阅、可测试、可进入 Git。
- 适合生产级竞品网页采集。

## 局限和风险

- 只支持浏览器，不支持普通 Windows 桌面应用。
- Codegen 只是记录操作，不理解“我要什么数据”。
- 页面结构变化后，生成的定位器仍可能需要维护。

## 不符合要求的核心原因

1. **没有原生 AI 语义理解。**
2. **不能根据数据目标自主探索页面。**
3. 只能录制或执行人类已经明确给出的操作路径。

## 适用结论

它是最可靠的 Web 回放执行层。推荐与 Midscene、Skyvern 或其他 AI Agent 组合，由 AI 探索后生成或整理为 Playwright 脚本。

## 参考资料

- [Playwright GitHub](https://github.com/microsoft/playwright)
- [Playwright Codegen](https://playwright.dev/docs/codegen)

