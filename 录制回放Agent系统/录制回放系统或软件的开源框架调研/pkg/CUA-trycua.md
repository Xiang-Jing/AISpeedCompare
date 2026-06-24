# CUA / trycua

## 项目介绍

trycua/cua 是开源的 Computer Use Agent 基础设施项目，目标是为 AI Agent 提供可控的桌面运行环境、Computer-Use Driver、SDK 和评估能力。它覆盖 macOS、Linux 和 Windows，强调让 Agent 能点击、输入、滚动、读取可访问性树、捕获窗口状态，并在隔离环境里执行桌面任务。

与 Open Computer Use / Coasty 相比，CUA 更偏底层 driver、沙箱、训练和评估基础设施；与 OpenRPA 相比，它更接近 AI computer-use 平台，而不是确定性 RPA。

## 录制方式

- 主要不是人工录制，而是提供 Agent 操作桌面的 driver 和环境。
- 可捕获桌面状态、窗口状态、可访问性树和操作结果，为轨迹记录和脚本生成提供基础。
- 不直接提供成熟的“录制一次 -> 生成参数化 RPA 脚本”产品闭环。
- 可以作为自研 Agent 探索层的运行环境，让 AI 在沙箱里试错并生成轨迹。

## 核心能力

| 能力 | 结论 |
| --- | --- |
| AI 语义理解 | 依赖接入的 Agent/模型 |
| 框架自动截图 | 支持方向明确 |
| 可访问性树/窗口状态 | 支持方向明确 |
| 鼠标键盘控制 | 支持 |
| 人工录制 | 不是核心产品能力 |
| 生成确定性脚本 | 暂无成熟通用闭环 |
| 参数化和批量执行 | 需要上层设计 |
| 一键回放 | 可运行任务/评估，不等同固定脚本回放 |
| 自动探索 App | 支持 Agent 运行环境 |
| 开源 | 是，MIT |

## 优势

- 适合构建安全、隔离、可观测的 AI 桌面操作环境。
- 能把 Agent 操作桌面的输入输出统一成 driver 接口，便于记录轨迹和评估成功率。
- 对训练、评测、沙箱化执行和多平台探索有价值。
- 可作为“AI 探索区”，把成功轨迹再转到确定性脚本层。

## 局限和风险

- 不是完整 RPA 平台。
- 生产化需要补齐权限控制、凭据保护、审计、失败恢复、脚本生成和脚本验证。
- Windows 专业客户端、金融终端、自绘控件需要实际 PoC。
- 如果直接让 Agent 在真实生产环境操作，风险高，必须先沙箱化。

## 不符合要求的核心原因

1. **偏 computer-use 基础设施，不是录制回放产品。**
2. **不直接生成可审阅、参数化、确定性的 RPA 脚本。**
3. 需要和 LangGraph、CUA-Skill IR、Python/FlaUI/Playwright 执行层组合使用。

## 适用结论

CUA/trycua 建议作为“隔离探索环境和 driver 层”候选。如果团队要自研 AI 录制器，让 Agent 在沙箱桌面里探索竞品软件，CUA 比直接操作真实桌面更适合做安全边界和评估基座。

## 参考资料

- [CUA / trycua GitHub](https://github.com/trycua/cua)
- [trycua Docs](https://docs.trycua.com/)

