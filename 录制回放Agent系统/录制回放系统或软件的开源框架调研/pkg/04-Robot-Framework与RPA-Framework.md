# Robot Framework + RPA Framework

## 项目介绍

Robot Framework 是通用的关键字驱动自动化框架，RPA Framework 为其补充浏览器、桌面、OCR、文件、邮件、Excel、PDF 等 RPA 库。自动化流程通常写成 `.robot` 或 Python 文件。

该组合更偏工程化执行框架，而不是录制器。

## 录制方式

- **主要方式：编写文本脚本或 Python 代码。**
- Robot Framework 本身没有统一的桌面 AI 录制器；部分 Web 生态工具可辅助记录浏览器操作，但不是框架的通用录制模式。
- 执行时可以自动截图和生成报告，但截图主要用于定位、验证和失败留证。
- 不支持把操作视频直接转换为 Robot/Python 回放脚本。

## 核心能力

| 能力 | 结论 |
| --- | --- |
| AI 语义理解 | 非原生，可调用外部 LLM/VLM |
| 框架自动截图 | 支持 |
| 人工录制 | 整体较弱，通常编写 Robot/Python；不是视频学习 |
| 生成回放资产 | 支持，Robot/Python |
| 一键回放 | 支持命令行、CI 和调度执行 |
| 自动探索 App | 非原生，可自行扩展 Agent |
| 开源 | 是，主要采用 Apache-2.0 |

## 优势

- 日志、报告、断言、失败截图和测试组织能力成熟。
- 脚本容易进入 Git，便于审计和版本管理。
- 适合把竞品抓取、库内查询、数据比对和质量报告串成完整任务。
- 可以灵活调用 Python、OCR、浏览器和外部 AI 服务。

## 局限和风险

- 不属于“录一下自动生成完整流程”的工具。
- AI 语义层和自主探索层需要额外开发。
- 复杂 Windows GUI 需要组合其他桌面库。

## 不符合要求的核心原因

1. **没有原生 AI 语义录制能力。**
2. **没有原生的 App 自主探索 Agent。**
3. 自动化脚本主要由开发者编写，首次建设效率低于录制型产品。

## 适用结论

适合作为最终工程化执行和数据质量校验框架，不适合单独承担 AI 探索与录制。

## 参考资料

- [Robot Framework GitHub](https://github.com/robotframework/robotframework)
- [RPA Framework GitHub](https://github.com/robocorp/rpaframework)

