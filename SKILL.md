---
name: project-manager
description: 初始化项目的 AI 协作入口和管理目录；在用户要求接入项目管理、补全项目管理结构时使用。提供文本规则、skills 和项目文档的按需管理入口。
---

# Project Manager

## 初始化项目

目前仅支持 Codex。用户要求接入项目管理时，在目标项目根目录运行本 skill 自带的脚本：

```sh
python3 <本 skill 目录>/scripts/init_project.py <目标项目根目录>
```

脚本建立 `.project-manager/rule/`、`document/` 和 `skill/`，复制缺失的规则编写规范、管理 skills 和统一能力地图，并补充根目录入口：

- `AGENTS.md` 是 Codex 的实际项目指令入口，包含文本规则地图、按需加载与退出约定，以及统一能力地图 `.project-manager/skill/index.md` 的入口。规范类和工具类 skills 都按需读取，不在入口展开正文或逐项摘要。
- `agent.md` 按项目约定保留，缺失时创建，存在时补充指向 `AGENTS.md` 的说明。不会将其中的预览示例自动升级为生效规范。
- 已有文件和管理块保持不变；重复运行只补缺失内容。若已有规则与新增规则存在冲突，说明具体冲突，不擅自覆盖。

执行前检查现有根级指令，特别是 `AGENTS.override.md`；若它存在，脚本会将管理块补充到该实际优先入口。初始化后读取实际入口，使当前会话也了解新增规则。首次接入文档时，读取 manage-documents，按浅层概览方式建立文档入口与初步能力概览；脚本只建立目录和分发规范，项目内容由 Agent 根据实际浅读写入。已有文档则沿用入口，不重复初始化或自动深入。

## 按需管理入口

以下路径相对于被管理的项目根目录：

- 添加、调整或首次实际使用未登记的项目 skills，以及管理轻量文本规则及其地图：读取 `.project-manager/skill/manage-skills/SKILL.md`。
- 编写目标、现状、阶段计划：读取 `.project-manager/skill/manage-documents/SKILL.md`。

`manage-skills` 管理轻量文本规则，以及由 Agent 执行的 skill 分类、复制接入、路径登记与维护流程：全局 skill 保留实际绝对路径，非全局 skill 复制到项目统一目录后登记相对路径；尚未提供批量安装脚本、来源可信性校验或自动版本同步；`manage-documents` 已提供浅层概览、指定功能建档、明确范围内完整整理及局部维护的 Agent 工作流。普通业务工作不加载全部管理内容，不把壳子描述成已实现能力。

已有项目升级时，先读取 skill 管理规范，保留用户条目，将旧入口的规范 skill 摘要与旧 `tools.md` 条目合并到 `skill/index.md`，把轻量文本规则按需归入 `rule/` 并维护入口规则地图；确认旧目录无独有内容且引用已更新后再移除。初始化脚本只补缺，不执行此迁移。
