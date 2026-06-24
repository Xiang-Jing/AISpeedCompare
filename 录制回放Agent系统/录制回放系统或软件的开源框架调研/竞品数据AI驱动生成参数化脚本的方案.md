# 竞品数据 AI 驱动生成参数化脚本的方案

## 一、结论

当前痛点不是“没有能回放的 RPA”，而是**稳定脚本仍然靠人录制、靠人参数化、靠人调试**。如果直接让 AI Agent 每次去操作软件，短期看很智能，长期看会遇到成功率、可复现、审计、异常恢复和批量执行问题。

更稳的方案是：

> **AI 负责探索、归纳和生成脚本；生产阶段由确定性脚本负责回放。**

也就是把“录制”从人工点击录制升级为：

1. 用户只描述数据目标和参数范围。
2. AI Agent 在沙箱或受控环境里探索 App / Web 页面。
3. 系统记录截图、控件树、动作、输入输出、异常和结果校验。
4. 将成功轨迹抽象为参数化技能图。
5. 编译成 Python、Robot Framework、Playwright、FlaUI、OpenRPA XAML、AHK 等稳定脚本。
6. 自动用多组参数回放验证，通过后进入脚本库。

因此推荐架构不是单一框架，而是分层组合。

## 二、推荐组合

| 层级 | 推荐框架 | 作用 | 选择理由 |
| --- | --- | --- | --- |
| Agent 编排层 | [LangGraph](pkg/LangGraph.md) | 管理探索、生成、验证、人审和发布流程 | 长流程、有状态、可恢复，适合把 AI 产脚本拆成多个可控节点 |
| AI 探索层 | [Midscene](pkg/Midscene.md)、[Microsoft UFO](pkg/Microsoft-UFO.md)、[UI-TARS Desktop](pkg/UI-TARS-Desktop.md)、[Agent S](pkg/Agent-S.md) | 根据自然语言目标观察界面、寻找路径、试运行 | 它们解决“人不再手工找路径”的问题 |
| 沙箱/Driver 层 | [CUA / trycua](pkg/CUA-trycua.md) | 隔离桌面、记录状态、评估 Agent 操作 | 避免 Agent 直接在真实生产环境试错 |
| 技能中间层 | [CUA-Skill](pkg/CUA-Skill.md) 思路 + 自研 DSL | 把成功轨迹抽象成参数化技能图 | 这是从 AI 轨迹到稳定脚本的关键桥梁 |
| Web 执行层 | [Playwright + Playwright MCP](pkg/Playwright与Playwright-MCP.md)、Midscene | 稳定操作竞品网站、下载页面、后台页面 | Web 侧比视觉点击更适合用 DOM/可访问性树稳定定位 |
| Windows 控件执行层 | [Python + pywinauto + OCR](pkg/Python桌面自动化组合.md)、[FlaUI + WinAppDriver](pkg/FlaUI与WinAppDriver.md) | 操作 Windows 客户端、WPF/WinForms/Win32 控件 | 控件树可见时比坐标和截图模板稳定 |
| 流程/RPA 执行层 | [Robot Framework + RPA Framework](pkg/Robot-Framework与RPA-Framework.md)、[OpenRPA](pkg/OpenRPA.md) | 批量执行、日志、报告、调度、审计 | 适合长期维护和生产化 |
| 视觉兜底层 | [SikuliX / Oculix](pkg/SikuliX.md)、PyAutoGUI、OCR | 自绘界面、远程桌面、控件不可见场景 | 作为最后兜底，不建议作为主定位方式 |
| 轻量脚本层 | [AutoHotkey + Pulover's Macro Creator](pkg/AutoHotkey与Pulovers-Macro-Creator.md) | Windows 轻量固定流程 | 适合小工具和快捷键密集任务 |

## 三、总体架构

```text
自然语言数据目标
例如：采集 A/B/C 三家竞品近 3 年产品价格、更新日期、导出 CSV
        │
        ▼
任务解析与参数建模
参数：竞品名称、证券代码、日期区间、指标、导出路径、账号环境
        │
        ▼
LangGraph 编排
        │
        ├─ 探索 Agent：Midscene / UFO / UI-TARS / Agent S
        │
        ├─ 沙箱环境：CUA / trycua / 测试机 / RDP
        │
        ├─ 状态观察：截图 + UIA/控件树 + OCR + DOM + 日志
        │
        ▼
轨迹记录
动作、定位方式、输入值、等待条件、页面状态、异常弹窗、输出结果
        │
        ▼
参数化技能图 IR
状态节点 + 动作节点 + 参数绑定 + 断言 + 异常恢复
        │
        ▼
脚本生成器
        ├─ Web：Playwright / Midscene YAML
        ├─ Windows 控件：Python + pywinauto / FlaUI
        ├─ RPA：Robot Framework / OpenRPA XAML
        └─ 兜底：SikuliX / PyAutoGUI / AHK
        │
        ▼
自动回放验证
多参数、多次运行、截图对比、结果断言、失败归因
        │
        ▼
人工审核发布
脚本库 + 参数模板 + 运行报告 + 版本管理
        │
        ▼
生产批量执行
调度、日志、重试、数据落库、质量校验
```

## 四、关键设计：不要直接保存 Agent 操作，要保存参数化技能图

如果只保存 Agent 的鼠标点击轨迹，本质还是坐标录制，稳定性不会好。建议定义一层自研 IR，例如：

```yaml
skill_id: competitor_data_export.wind.financial_indicator.v1
name: 导出竞品财务指标
target:
  app: Wind金融终端
  platform: windows
parameters:
  competitor_code:
    type: string
    examples: ["000001.SZ", "600519.SH"]
  start_date:
    type: date
  end_date:
    type: date
  indicator:
    type: enum
    values: ["营业收入", "毛利率", "净利润"]
  output_path:
    type: path
preconditions:
  - app_running: Wind金融终端
  - logged_in: true
steps:
  - id: open_query
    intent: 打开指标查询页面
    locator:
      preferred: uia
      uia:
        name: 指标查询
        control_type: Button
      fallback:
        ocr_text: 指标查询
    action: click
    assert:
      visible_text: 证券代码
  - id: input_code
    intent: 输入竞品代码
    locator:
      preferred: uia
      uia:
        automation_id: txtSecurityCode
      fallback:
        ocr_near_text: 证券代码
    action: type
    value: "{{ competitor_code }}"
  - id: export_csv
    intent: 导出结果
    locator:
      preferred: uia
      uia:
        name: 导出
        control_type: Button
      fallback:
        image: assets/export_button.png
    action: click
    assert:
      file_exists: "{{ output_path }}"
recovery:
  - when: popup_contains("登录过期")
    action: stop_and_require_login
  - when: popup_contains("无数据")
    action: mark_empty_result
```

这个 IR 的价值是：

- 让 AI 生成的是“可审阅结构”，不是一坨难维护代码。
- 参数、定位、断言、异常恢复分开存，后续可以单独优化。
- 同一个技能可以编译成不同执行器脚本。
- 失败时能定位是参数问题、定位问题、环境问题还是业务数据问题。

## 五、脚本生成流程

### 1. 任务解析

输入不应只是“帮我采集竞品数据”，而要转成结构化任务：

| 字段 | 示例 |
| --- | --- |
| 数据对象 | 竞品公司、产品、证券代码、店铺、平台 |
| 数据指标 | 价格、销量、财务指标、发布时间、库存、评级 |
| 时间范围 | 2024-01-01 到 2026-06-25 |
| 来源系统 | Web、Wind、同花顺、Excel、内部系统 |
| 输出格式 | CSV、Excel、数据库表 |
| 成功标准 | 行数、字段完整率、文件存在、字段校验 |
| 合规约束 | 只访问授权账号、遵守站点规则、不得绕过风控 |

### 2. AI 探索

按场景选择探索工具：

| 场景 | 首选 |
| --- | --- |
| Web 页面和后台系统 | Midscene + Playwright MCP |
| Windows 标准客户端 | Microsoft UFO + pywinauto/FlaUI |
| 跨平台桌面/动态界面 | UI-TARS Desktop / Agent S |
| 人工已有示教样本 | OpenAdapt |
| 需要隔离试错 | CUA / trycua |

探索阶段的目标不是直接生产，而是产出：

- 成功路径。
- 页面/窗口状态变化。
- 控件定位候选。
- 参数出现的位置。
- 可验证的输出结果。
- 异常弹窗和恢复策略。

### 3. 轨迹归纳和参数抽取

把探索轨迹里的固定值抽成参数：

| 固定值 | 参数 |
| --- | --- |
| 某个竞品名称 | `competitor_name` |
| 股票代码 | `security_code` |
| 日期区间 | `start_date` / `end_date` |
| 下载目录 | `output_path` |
| 指标名称 | `indicator` |
| 登录账号 | 环境变量或凭据引用，不写入脚本 |

同时把定位方式排序：

1. DOM / Accessibility / UIA / AutomationId。
2. 稳定文本、label、role、control type。
3. OCR 文本定位。
4. 图像模板。
5. 相对坐标。
6. 绝对坐标。

### 4. 生成脚本

按目标系统编译：

| 目标 | 生成脚本 |
| --- | --- |
| Web 竞品页面 | Playwright TypeScript/Python |
| AI 视觉 Web/PC | Midscene YAML/JS |
| Windows 标准控件 | Python + pywinauto 或 C# + FlaUI |
| 流程化批量执行 | Robot Framework |
| OpenRPA 生态 | XAML 工作流 |
| 自绘/远程界面 | SikuliX/PyAutoGUI + OCR |
| Windows 轻量宏 | AutoHotkey |

生成后的脚本必须包含：

- 参数入口。
- 显式等待。
- 控件定位解释。
- 输入输出日志。
- 每个关键步骤的断言。
- 失败截图。
- 异常弹窗处理。
- 幂等检查，例如目标文件已存在时如何处理。

### 5. 自动回放验证

脚本不能生成后直接发布。至少跑三类验证：

| 验证类型 | 要求 |
| --- | --- |
| 单参数重复 | 同一参数连续跑 3 次，确认路径稳定 |
| 多参数泛化 | 至少 5 组竞品/日期/指标参数，确认参数化有效 |
| 异常场景 | 无数据、登录过期、弹窗、导出失败、网络慢 |

通过标准建议：

- 成功率 >= 95% 才能进入生产候选。
- 关键字段完整率 >= 99%。
- 每次运行必须有日志、截图、输入参数、输出校验。
- 失败能自动归因到定位、环境、权限、业务无数据或模型生成错误。

## 六、推荐落地路线

### 阶段 0：先定边界

先选 2 类代表场景：

1. **Web 竞品数据**：登录网站、搜索竞品、筛选日期、导出 CSV。
2. **Windows 客户端数据**：打开金融/行业客户端、输入代码、导出指标。

不要一开始覆盖所有软件。先把闭环跑通。

### 阶段 1：Web PoC

推荐组合：

```text
LangGraph + Midscene + Playwright MCP + Playwright
```

目标：

- AI 能根据目标找到页面路径。
- 成功轨迹能转成 Playwright 脚本。
- 脚本能用 CSV/JSON 参数批量执行。
- 有结果断言和失败截图。

这是最快见效的一条线，因为 Web 有 DOM、可访问性树和成熟脚本生态。

### 阶段 2：Windows 控件 PoC

推荐组合：

```text
LangGraph + Microsoft UFO / Midscene Computer + pywinauto / FlaUI + Robot Framework
```

目标：

- AI 能探索客户端菜单和页面。
- 控件可见时生成 pywinauto/FlaUI 脚本。
- 控件不可见时自动降级到 OCR/视觉。
- Robot Framework 负责参数化批量执行和报告。

### 阶段 3：技能库和脚本库

建立两个资产库：

| 资产 | 内容 |
| --- | --- |
| 技能库 | 参数化技能图、定位策略、断言、恢复策略、适用环境 |
| 脚本库 | Playwright/Python/Robot/FlaUI/OpenRPA/AHK 等可执行脚本 |

技能库是上层稳定语义，脚本库是下层执行产物。未来 App 改版时，优先修技能图或定位策略，再重新生成脚本。

### 阶段 4：生产化

补齐：

- 调度器。
- 运行队列。
- 凭据管理。
- 沙箱/测试环境。
- 权限审批。
- 数据落库。
- 回放报告。
- 失败工单。
- 脚本版本回滚。

## 七、和现有 pkg 的组合关系

### 推荐主线

1. **Web 主线**：Midscene / Playwright MCP 探索，Playwright 稳定回放。
2. **Windows 主线**：UFO / Midscene Computer 探索，pywinauto/FlaUI 稳定回放。
3. **流程主线**：Robot Framework 统一参数化、日志、报告、调度。
4. **视觉兜底**：OCR + SikuliX/PyAutoGUI 处理自绘界面。
5. **低代码备选**：OpenRPA 承接需要可视化工作流的流程。
6. **研究增强**：Agent S / UI-TARS / CUA/trycua 做更强的探索和沙箱验证。

### 不建议的主线

| 路线 | 原因 |
| --- | --- |
| 只用传统 RPA | 稳定但仍然靠人录制和参数化，不能解决根因 |
| 只用 GUI Agent | 能探索但生产回放不确定，审计和重跑困难 |
| 只用图像模板 | 易受分辨率、主题、遮挡影响，维护成本高 |
| 只让 LLM 直接写脚本 | 缺少真实轨迹验证，容易生成看似正确但无法执行的代码 |

## 八、最小可行系统

MVP 可以只做 6 个模块：

| 模块 | 说明 |
| --- | --- |
| 任务入口 | 输入数据目标、参数、来源系统、输出格式 |
| 探索执行器 | 调用 Midscene/UFO/Playwright MCP 等执行探索 |
| 轨迹记录器 | 保存截图、控件树、DOM、动作、输入输出 |
| 技能图生成器 | 把轨迹抽象成参数化 IR |
| 脚本编译器 | 生成 Playwright 或 Python/pywinauto 脚本 |
| 回放验证器 | 多参数运行、断言结果、生成报告 |

MVP 成功标准：

- 输入一个自然语言数据目标后，系统能生成第一版脚本。
- 用户只需审核和少量修订，不再从零录制。
- 同一脚本能换参数批量执行。
- 失败时能给出可定位原因，而不是只报“执行失败”。

## 九、实施优先级

| 优先级 | 工作项 | 说明 |
| ---: | --- | --- |
| P0 | 定义技能图 IR | 没有 IR，AI 轨迹无法稳定沉淀 |
| P0 | Web Playwright 生成链路 | 最容易先跑通闭环 |
| P0 | Windows pywinauto/FlaUI 生成链路 | 覆盖核心 CS 客户端 |
| P1 | LangGraph 编排 | 把流程从一次性 Prompt 变成可恢复流水线 |
| P1 | 自动回放验证器 | 决定脚本能否进生产 |
| P1 | OCR/视觉兜底 | 处理控件不可见场景 |
| P2 | CUA/trycua 沙箱 | 降低 Agent 试错风险 |
| P2 | OpenRPA/Robot 发布适配 | 适配不同团队维护习惯 |
| P3 | UI 可视化审核台 | 给业务/测试人员审核技能和脚本 |

## 十、风险和规避

| 风险 | 规避 |
| --- | --- |
| Agent 路径不稳定 | 只把 Agent 用于探索，生产阶段运行固定脚本 |
| 脚本泛化差 | 多参数回放验证，失败样本回灌技能图 |
| 坐标化严重 | 强制定位优先级：UIA/DOM > OCR > 图像 > 相对坐标 > 绝对坐标 |
| 业务系统弹窗多 | 建立异常弹窗库和恢复策略 |
| 登录和凭据泄露 | 凭据只走密钥管理，不写入脚本和日志 |
| 数据源合规问题 | 只访问授权系统和允许采集的数据，保留访问审计 |
| AI 生成代码有误 | 生成脚本必须经过沙箱回放和人工审核 |
| App 改版导致失败 | 失败截图和控件树入库，触发技能图修复和脚本再生成 |

## 十一、最终建议

建议把目标产品定义为：

> **AI 驱动的参数化自动化脚本生成平台，而不是 AI 直接执行平台。**

推荐第一版技术选型：

```text
编排：LangGraph
Web 探索：Midscene + Playwright MCP
Web 回放：Playwright
Windows 探索：Microsoft UFO / Midscene Computer
Windows 回放：Python + pywinauto + FlaUI
流程执行与报告：Robot Framework
视觉兜底：OCR + SikuliX / PyAutoGUI
技能 IR：参考 CUA-Skill 自研参数化技能图
沙箱候选：CUA / trycua
```

一句话落地策略：

> **先让 AI 帮你“找到怎么做”，再让系统把“怎么做”变成可审阅、可参数化、可重复验证的脚本。**

## 参考资料

- [Midscene](pkg/Midscene.md)
- [Microsoft UFO/UFO²](pkg/Microsoft-UFO.md)
- [UI-TARS Desktop](pkg/UI-TARS-Desktop.md)
- [Agent S](pkg/Agent-S.md)
- [OpenAdapt](pkg/OpenAdapt.md)
- [Python + pywinauto + pyautogui + OCR](pkg/Python桌面自动化组合.md)
- [FlaUI + WinAppDriver](pkg/FlaUI与WinAppDriver.md)
- [Playwright + Playwright MCP](pkg/Playwright与Playwright-MCP.md)
- [LangGraph](pkg/LangGraph.md)
- [CUA-Skill](pkg/CUA-Skill.md)
- [CUA / trycua](pkg/CUA-trycua.md)
- [Robot Framework + RPA Framework](pkg/Robot-Framework与RPA-Framework.md)
- [OpenRPA](pkg/OpenRPA.md)
- [SikuliX / Oculix](pkg/SikuliX.md)

