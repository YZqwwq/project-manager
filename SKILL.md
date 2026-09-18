---
name: project-manager
description: 初始化项目的 AI 协作入口和管理目录；在用户要求接入项目管理、补全项目管理结构时使用。提供文档规则和 skill 管理规则的按需入口。
---

# Project Manager

## 初始化项目

目前仅支持 Codex。用户要求接入项目管理时，在目标项目根目录运行本 skill 自带的脚本：

```sh
python3 <本 skill 目录>/scripts/init_project.py <目标项目根目录>
```

脚本建立 `.project-manager/document/` 和 `.project-manager/skill/`，复制缺失的管理 skills 和工具目录，并补充根目录入口：

- `AGENTS.md` 是 Codex 的实际项目指令入口，包含轻量责任划分、仅规范类 skills 的摘要表与管理导航。按需工具只登记在 `.project-manager/skill/tools.md`，入口仅指向该目录。
- `agent.md` 按项目约定保留，缺失时创建，存在时补充指向 `AGENTS.md` 的说明。不会将其中的预览示例自动升级为生效规范。
- 已有文件和管理块保持不变；重复运行只补缺失内容。若已有规则与新增规则存在冲突，说明具体冲突，不擅自覆盖。

执行前检查现有根级指令，特别是 `AGENTS.override.md`；若它存在，脚本会将管理块补充到该实际优先入口。初始化后读取实际入口，使当前会话也了解新增规则。首次接入文档时，读取 document-rules，按浅层概览方式建立文档入口与初步能力概览；脚本只建立目录和分发规范，项目内容由 Agent 根据实际浅读写入。已有文档则沿用入口，不重复初始化或自动深入。

## 按需管理入口

以下路径相对于被管理的项目根目录：

- 添加或调整项目 skills：读取 `.project-manager/skill/skill-rules/SKILL.md`。
- 编写目标、现状、阶段计划：读取 `.project-manager/skill/document-rules/SKILL.md`。

`skill-rules` 已提供基础分类与登记约定，自动安装、校验和同步流程尚未实现；`document-rules` 已提供浅层概览、指定功能建档、明确范围内完整整理及局部维护的 Agent 工作流。普通业务工作不加载全部管理内容，不把壳子描述成已实现能力。

已有项目升级时，先读取 skill 管理规范，保留用户条目，将旧索引中的规范移入入口摘要表、工具移入 `tools.md`；确认无剩余引用和独有内容后再移除旧索引。初始化脚本只补缺，不执行此迁移。
