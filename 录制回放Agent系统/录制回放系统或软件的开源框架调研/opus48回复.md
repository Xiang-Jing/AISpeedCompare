我先调研一下当前这个领域的最新进展，特别是 GUI Agent、屏幕解析、以及 Windows 桌面自动化框架的现状，再给你按优先级整理。UI-TARS 信息很全面。现在我重点查一下「录制探索→固化为脚本」这个范式的工具，以及对原生 Windows 应用更可靠的 UIA 方案。很好，OpenAdapt 正是「录制→学习→执行」范式。现在查一下对原生 Windows 应用更可靠的 Agent S2（用 UIA 树）以及确定性回放层（pywinauto / FlaUI）。核心的 AI 层已经清楚了。现在查确定性回放层 —— 这是「固化脚本」阶段的关键（pywinauto / FlaUI 这类基于 UIA 的库），尤其要确认它们对同花顺/Wind 这类金融终端的适用性。确定性回放层清楚了。还有两个关键点要确认：一是同花顺/Wind 这类终端常常没有规范的 UIA 树（自绘界面），需要视觉定位兜底（OmniParser）；二是「把 AI 探索固化成可自愈的确定性工作流」这个模式有没有现成实现。OmniParser V2 确认。最后查一下「录制一次→生成确定性参数化工作流→批量回放」这个模式最清晰的实现（workflow-use / Skyvern），这正是你架构的核心思路。先说核心结论:**目前没有任何一个开源框架能开箱即用地完成你描述的「原生 Windows 应用上 AI 探索 → 固化 → 参数化 → 无人值守批量回放」全链路。** 你需要把它拆成 3~4 层能力来组装。而对你这个场景(同花顺、Wind),决定整个方案难易和稳定性的**最关键变量**是:这些终端到底暴不暴露规范的 UIA(Windows UI Automation)元素树。这类金融终端很多是 Qt/自绘界面或内嵌行情控件,UIA 树往往残缺,这会直接决定你能用"稳定选择器"还是被迫退回"视觉/坐标"定位。

下面按优先级(从高到低,也是建议你投入精力的顺序)分层列出。

---

## A 层 · 确定性回放引擎(最高优先级 —— 这是"固化+参数化+批量"的地基)

这是回放阶段真正干活、且**不需要 AI** 的部分,也是你脚本"可人工审阅、可修改、稳定"的载体。务必优先选定。

**1. pywinauto(Python,首选)**
Python 原生 Windows GUI 自动化库,底层同时支持 Win32 API(默认 backend)和 MS UI Automation(backend="uia")两套后端。它通过控件的文本/属性做对象级定位(而非坐标),这正是你要的"不写死、可参数化、抗界面微调"。值得注意:pywinauto 官方把可靠的基于文本的「record-replay」生成器列为高优先级开发特性,社区也有 "Pywinauto Recorder" 项目可作录制起点。许可证 BSD 3-clause,商用无忧。

**2. FlaUI(C#/.NET,如果你团队在 .NET 栈)**
FlaUI 干净地封装了微软的 UI Automation(UIA2/UIA3),在 GitHub 上活跃维护,对 Win32、WinForms、WPF 这类原生应用的对象级定位非常稳。MIT 许可。如果是纯 Python 团队选 pywinauto,纯 .NET 团队选 FlaUI。

**兜底定位手段(当 UIA 树缺失时,这是你大概率会碰到的)**
- **SikuliX / Airtest+Poco**:图像识别定位,当 UI 缺少可访问的控件树、或界面是 canvas/自绘时使用。
- **AutoHotkey(v2)/ AutoIt**:轻量级键鼠脚本,做"相对窗口的坐标"操作或快捷键兜底。这些都应作为补充,不要作为主力——它们对分辨率/DPI/布局变化很脆弱。

---

## B 层 · AI 探索 Agent(把自然语言变成一次成功执行)

这是你"先 AI 探索"阶段的大脑+手。这里有个**关键取舍**:对你的固化流程而言,**用 UIA 树的 Agent 比纯视觉 Agent 更有优势**,因为它探索时定位到的元素标识(AutomationId/Name/控件路径)可以直接迁移到 A 层的 pywinauto/FlaUI 脚本里,固化时几乎是"原样翻译";纯视觉 Agent 输出的是坐标,固化成稳定选择器要多做一步。

**1. Windows-Use(CursorTouch)/ Agent-S(Simular)—— UIA 优先,首选这两个**
- Windows-Use:通过 Windows UI Automation API 读屏,用任意 LLM 决定点击/输入/滚动,不需要计算机视觉模型;可配置 `use_accessibility=True` 直接吃 UIA 树,且官方推荐配合 claude-haiku/sonnet/opus 系列效果最好。和你的固化目标最契合。
- Agent-S(gui-agents 库):2025/01 起就支持 Windows,可在 WindowsAgentArena 上部署;提供视觉信息+可访问性树双输入,把动作 grounding 到具体 GUI 元素;并有情景记忆机制,会保留过往任务经验、参考历史成败来优化后续策略——这点对"多次探索直到成功"很有用。

**2. UI-TARS-desktop(字节,纯视觉,当 UIA 不可用时的主力)**
ByteDance 出品、Apache 2.0 开源的视觉原生 GUI Agent,纯靠截图感知,不解析 HTML/可访问性树/元素 ID,跨 Windows/macOS/Linux。在 2026 年 4 月的横评里,UI-TARS 被评为 Windows 桌面自动化最强的开源选项(若你有 GPU 做本地推理)。它还提供 Python / TypeScript SDK 和可作为 MCP server 运行,方便集成。同花顺/Wind 里那些没有 UIA 的自绘区域,基本要靠它或 OmniParser 这类视觉方案。

> **大脑(VLM)是可换的**:上面这些 Agent 框架大多解耦了"框架"和"模型",你可以插 Anthropic Claude Computer Use、UI-TARS 模型、GPT、或 Qwen2.5-VL 等。Claude 的 Computer Use 在 Agent-S、OmniTool 等里都是开箱支持的可选大脑之一,做探索和后面的"轨迹→脚本"代码生成都合适。

---

## C 层 · 视觉定位兜底(针对 Wind/同花顺 自绘界面 —— 因你的目标应用而优先级上调)

**OmniParser V2(微软)**
把 UI 截图解析成结构化、带边界框和语义描述的元素,显著增强 VLM 在界面上精确 grounding 动作的能力,关键是它不依赖 DOM 或可访问性树。V1.5 起能更细粒度检测小图标、并预测每个元素是否可交互;微软还配套了 OmniTool,用 OmniParser + 你选的视觉模型控制一台 Windows 11 VM,并支持本地记录轨迹来给你自有领域的 Agent 构建训练/数据管线。对 Wind 这种 UIA 残缺的终端,OmniParser 几乎是必备的"看图找控件"层。注意其模型权重许可证不统一,商用前逐个确认。

---

## D 层 · "录制→固化→参数化→批量"范式参考(你最该照抄架构思路的部分)

你描述的核心流程,**最成熟的现成实现是浏览器领域的 workflow-use,虽然它不能直接用于桌面,但它的架构就是你要的蓝图**:

**workflow-use(browser-use 团队,自称 "RPA 2.0")—— 架构范本**
它的流程和你一字不差:你录一次操作 → LLM 把录制转成带变量的确定性脚本(脚本里也可保留 AI 步骤)→ 回放比纯 Agent 快约 10 倍、便宜约 90%。而且它把表单字段自动变成参数(识别你输入的名字/日期等,标记为每次可变),一次录制就能跑多种取值——这正是你要的 `stockCode`/`reportDate` 抽象;失败时还会回退到 Browser Use 的柔性 Agent 自愈完成该步,无需人工。**直接价值:照搬它的"录制 schema → LLM 转确定性脚本+自动抽参 → 自愈兜底"三段式设计到你的桌面方案。** 缺点:仅限浏览器,且项目处于很早期、不建议直接上生产。

**OpenAdapt(OpenAdaptAI)—— 桌面侧最接近的现成框架**
这是桌面版的 record→learn→execute。它在 Windows 上录制时会同时捕获截图、鼠标、键盘和可访问性树快照,回放引擎再用 LLM 把录制的工作流适配到新数据;架构上明确有 "Abstraction Ladder":从字面回放逐级泛化到目标级自动化,以及动作执行前的安全校验层(高风险动作需确认)。MIT 许可。可作为你"录制器 + 轨迹存储"组件的起点。注意新版模块化架构仍是 alpha/pre-alpha,稳定度不如 pywinauto/FlaUI。

> 补充佐证范式可行:OpenAI 刚在 2026/6/18 给 Codex 桌面端上了 Record & Replay,把一次演示转成可复用、可编辑的"skill",且生成的是自然语言 SKILL.md 而非像素坐标,从而能在应用新实例、新输入值上执行,而不是回放某天有效的固定点击序列——但它闭源、目前仅 macOS,只能当作"这条路走得通"的旁证。

---

## 给你这个场景的推荐组合(直接可落地)

假设你用 Python 栈:

1. **探索层**:Windows-Use 或 Agent-S(吃 UIA 树)为主 + UI-TARS/OmniParser(视觉)兜底;大脑用 Claude Computer Use 或 UI-TARS 模型。
2. **轨迹记录**:让探索 Agent 把每步的(UIA 元素路径 / 控件属性 / 截图 / 动作 / 输入值)结构化落盘(可参考 OpenAdapt 的捕获 schema)。
3. **固化(AI 参与一次)**:用一个 LLM 步骤把成功轨迹翻译成一段 **pywinauto 脚本**,把业务输入位置替换成 `{stockCode}`、`{reportDate}`、`{outputFileName}` 占位符 —— 这一步抄 workflow-use 的"录制→确定性脚本+自动抽参"思路。
4. **人工审阅**:pywinauto 脚本是纯 Python,可直接 review/改。
5. **批量回放(无 AI)**:写一个几十行的 runner,读你那份 JSON/CSV/DB 任务列表,遍历 `params` 注入占位符,逐条执行+每步后做断言校验+截图存证+失败重试。

---

## 三个必须提前想清楚的风险

- **UIA 残缺**是头号风险。建议**动手前先用 inspect.exe / Accessibility Insights 把同花顺、Wind 的目标页面挨个验一遍**:能拿到稳定 AutomationId/Name 的,走 pywinauto 选择器;拿不到的,提前规划 OmniParser/图像锚点方案。这一步基本决定方案形态。
- **回放稳定性≠录制时能跑通**。金融终端有登录态、行情加载延迟、弹窗、报告期下拉异步刷新等。每步必须有显式等待+完成校验(而非固定 sleep),否则批量跑必崩。这也是为什么纯坐标方案在这类应用上不可取。
- **合规与风控**:导出/下载/下单类操作要有权限边界和不可逆动作的人工确认位;同花顺/Wind 的许可协议是否允许自动化采集,需自行确认。

如果你告诉我你们更倾向 Python 还是 .NET、是否已确认过这两个终端的 UIA 可见性、以及大脑模型的预算约束,我可以帮你把上面第 2~5 步的轨迹 schema 和 runner 骨架具体写出来。