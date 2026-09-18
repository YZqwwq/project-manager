# project-manager
为项目建立轻量的 AI 协作入口，按责任范围选择规范和自动化 skills，并提供项目文档管理入口。目前仅面向 Codex。

## 初始化

在本仓库中运行：

```sh
python3 scripts/init_project.py /目标项目根目录
```

初始化会补全 `AGENTS.md`、`agent.md` 和以下结构，保留已有内容，重复运行只补缺失项：

```text
.project-manager/
├── document/
└── skill/
    ├── tools.md
    ├── document-rules/SKILL.md
    └── skill-rules/SKILL.md
```

`AGENTS.md` 是 Codex 的实际规则入口；存在 `AGENTS.override.md` 时也向其补充管理块。`agent.md` 保留为项目约定入口并指向实际规则。当前会话需读取新增入口，后续由 Codex 在启动时发现项目指令。

根目录 `SKILL.md` 定义 project-manager 初始化能力，`assets/` 提供分发模板。规范类 skills 的摘要直接写入 `AGENTS.md`，根据当前任务匹配后读取全文；按需工具只登记在 `.project-manager/skill/tools.md`，需要自动化能力时才检索目录。

`skill-rules` 已提供基础分类与登记约定，自动安装、校验和同步流程尚未实现；`document-rules` 已提供由 Agent 执行的文档建立与维护流程。初始化脚本只建立结构，不分析源码或生成项目事实。

初始化会保留已有管理块和 skills，不自动升级已接入项目的规则。已有项目调整结构时，需按 skill 管理规范同步入口和目录，保留用户登记内容。

## 项目文档能力

通过 project-manager 首次接入时，Agent 按文档规范浅读项目，建立 `.project-manager/document/index.md` 和 `current/index.md`，不会自行逐层读完整个项目。单独运行初始化脚本只准备目录和规范，不执行此阅读流程。

- “建立项目文档”：默认只做初步能力概览，记录实际依据和未确认范围。
- “为某个功能建立文档”：只深入该功能及理解它必需的依赖，按功能组织文档。
- “完整整理项目（或某子系统）的文档”：在明确范围内分批整理，保留真实覆盖进度。
- 日常实现变化或用户纠正：按当前授权同步修订已有相关文档，不顺带为其他功能建档。

文档说明与阅读进度分开：`index.md` 负责导航和覆盖情况，`current/` 保存当前能力和功能知识；目标与计划有明确内容时再建立或沿用现有文件。计划不构成执行授权，阅读待办不属于产品阶段计划。
