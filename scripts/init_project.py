#!/usr/bin/env python3
"""补全项目管理目录和入口，保留所有已有内容。"""

import argparse
from pathlib import Path


BEGIN = "<!-- project-manager:begin -->"
END = "<!-- project-manager:end -->"
ASSETS = Path(__file__).resolve().parent.parent / "assets"


def add_block(path, block):
    existing = path.read_text(encoding="utf-8") if path.exists() else ""
    if BEGIN in existing or END in existing:
        if existing.count(BEGIN) != 1 or existing.count(END) != 1 or existing.index(BEGIN) > existing.index(END):
            raise ValueError(f"管理块标记不完整或重复，请先检查：{path}")
        print(f"保留已有管理块：{path}")
        return
    separator = "\n\n" if existing and not existing.endswith("\n") else "\n" if existing else ""
    with path.open("a", encoding="utf-8") as stream:
        stream.write(separator + block.rstrip() + "\n")
    print(f"补充入口：{path}")


def initialize(root):
    if not root.is_dir():
        raise ValueError(f"目标项目目录不存在：{root}")
    managed = root / ".project-manager"
    (managed / "document").mkdir(parents=True, exist_ok=True)
    # 空文档目录也随 Git 保存；不预设项目目标或生成虚构现状。
    (managed / "document" / ".gitkeep").touch(exist_ok=True)
    skill_dir = managed / "skill"
    skill_dir.mkdir(parents=True, exist_ok=True)
    for source in sorted((ASSETS / "skills").rglob("*")):
        if not source.is_file():
            continue
        target = skill_dir / source.relative_to(ASSETS / "skills")
        target.parent.mkdir(parents=True, exist_ok=True)
        if not target.exists():
            target.write_bytes(source.read_bytes())
            print(f"创建：{target}")
    entry = (ASSETS / "entry.md").read_text(encoding="utf-8")
    add_block(root / "AGENTS.md", entry)
    if (root / "AGENTS.override.md").exists():
        add_block(root / "AGENTS.override.md", entry)
    add_block(root / "agent.md", f"{BEGIN}\n## 实际项目管理入口\n\nCodex 协作规则见根目录 `AGENTS.md`（若有 `AGENTS.override.md` 则以其为实际入口）。管理目录为 `.project-manager/`。本文件原有预览内容仅供讨论，不作为已登记的 skills 或实际路径。\n{END}")
    print(f"初始化完成：{root}")
    if (skill_dir / "index.md").exists():
        print("发现旧 index.md：已保留。请按 skill-rules 将规范登记到 AGENTS.md、工具登记到 tools.md；初始化不会自动迁移或覆盖已有条目。")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("project_root", type=Path)
    args = parser.parse_args()
    try:
        initialize(args.project_root.resolve())
    except (OSError, ValueError) as error:
        parser.exit(1, f"初始化失败：{error}\n")
