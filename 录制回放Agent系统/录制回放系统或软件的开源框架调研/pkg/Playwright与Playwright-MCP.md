# Playwright + Playwright MCP

## 项目介绍

Playwright 是微软开源的浏览器自动化框架，支持 Chromium、Firefox 和 WebKit，常用于 Web 测试、数据抓取和流程自动化。Playwright Codegen 可以通过人工操作录制生成测试代码，Playwright MCP 则把浏览器自动化能力暴露给 AI Agent。

它不解决 Windows CS 客户端问题，但对“竞品数据”非常重要：如果数据来源包含 Web 站点、后台系统、研报平台、行情网页或下载页面，Playwright 是稳定回放和参数化执行的优先目标。

## 录制方式

- **Web：Playwright Codegen 支持人工操作录制并生成代码。**
- **AI：Playwright MCP 可让 Agent 通过浏览器可访问性树和快照操作页面。**
- 生成脚本后可以用 TypeScript、JavaScript、Python、Java、.NET 等语言维护。
- 不是桌面应用录制器，也不能直接操作非浏览器 CS 客户端。
- AI 探索成功后，应把路径固化为确定性 Playwright 脚本，而不是每次让 Agent 重新点击。

## 核心能力

| 能力 | 结论 |
| --- | --- |
| AI 语义理解 | Playwright 本身不支持；Playwright MCP 可接入 Agent |
| 框架自动截图 | 支持 |
| 可访问性树/DOM 定位 | 支持，是 Web 稳定性核心 |
| 人工录制 | Codegen 支持 |
| 生成回放资产 | 支持，多语言脚本 |
| 参数化和批量执行 | 支持，工程化能力强 |
| 一键回放 | 支持 CLI、测试框架、CI |
| 自动探索页面 | 通过 MCP/Agent 可实现 |
| 桌面应用 | 不支持，除非目标是浏览器内页面 |
| 开源 | 是，Apache-2.0 |

## 优势

- Web 场景确定性强，定位方式比纯视觉点击稳定。
- 生成脚本可审阅、可维护、可参数化、可进 CI。
- 与 Midscene 的 AI 视觉步骤可互补：AI 负责找路径，Playwright 负责沉淀稳定脚本。
- MCP 让 AI 可以先探索页面，再把成功操作转成脚本。
- 对批量竞品数据采集、下载、分页、表格提取和断言非常实用。

## 局限和风险

- 只能覆盖 Web，不覆盖原生桌面客户端。
- 动态页面、验证码、登录风控和反自动化策略需要合规处理。
- Codegen 生成的初版脚本通常要人工或 AI 二次整理，抽参数、加等待、加断言和异常处理。
- MCP 探索不等同于稳定脚本，仍要固化。

## 不符合要求的核心原因

1. **不支持桌面 CS 客户端。**
2. **AI 能力来自 MCP/上层 Agent，不是 Playwright 核心。**
3. 只适合作为 Web 数据源的确定性执行层。

## 适用结论

只要竞品数据来源包含 Web，Playwright 应进入最终方案的确定性执行层。建议与 Midscene 或 Playwright MCP 组合：Agent 探索页面路径，脚本生成层把成功路径固化为 Playwright 参数化脚本，生产阶段按数据集批量回放。

## 参考资料

- [Playwright GitHub](https://github.com/microsoft/playwright)
- [Playwright Codegen](https://playwright.dev/docs/codegen)
- [Playwright MCP GitHub](https://github.com/microsoft/playwright-mcp)

