#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qichun tang
# @Date    : 2021-01-14
# @Contact    : qichun.tang@bupt.edu.cn
import warnings
from collections import defaultdict
from pathlib import Path
from typing import Dict
from typing import List
from typing import Tuple


def strip_lines(lines: List[str]):
    if not lines:
        return lines
    s = 0
    while s < len(lines) and lines[s] == '':
        s += 1
    e = len(lines) - 1
    while e >= 0 and lines[e] == '':
        e -= 1
    return lines[s:e + 1]


def get_level_title(str_: str) -> Tuple[int, str]:
    level = 0
    i = 0
    for i, c in enumerate(str_):
        if c == "#":
            level += 1
        else:
            break
    return level, str_[i:].strip()


class Node():
    def __init__(self, level=0, title="notes", lines=None, is_root=False):
        self.level = level
        if lines is None:
            lines = []
        if title is None:
            title = ""
        self.lines = lines
        self.title = title
        self.children = []
        self.is_root = is_root

    def __str__(self):
        return "#" * self.level + " " + self.title

    __repr__ = __str__

    def get_md(self):
        lines = [
            "@[toc]",
            ""
        ]

        def rec(node: Node):
            lines.append(str(node))
            lines.append('')
            # 非叶子结点
            if node.children:
                if node.lines:
                    warnings.warn("有问题， 非叶子结点中也有内容:")
                    # 用于定位问题
                    for line in node.lines:
                        warnings.warn(f"\t{line}")
                for child in node.children:
                    rec(child)
            # 叶子结点
            else:
                lines.extend(node.lines)
            lines.append('')

        rec(self)
        return "\n".join(lines)

    @classmethod
    def from_md(cls, md_txt):
        lines = md_txt.splitlines()
        cur_lines = []
        level2nodes: Dict[int, List[Node]] = defaultdict(list)
        level2nodes.update({
            0: [Node(is_root=True)]  # root
        })

        pre_node = cur_node = None
        code_field = 0
        for line in lines:

            if line.startswith("#") and (not code_field):
                level, title = get_level_title(line)

                cur_node = pre_node
                pre_node = Node(level, title)
                if cur_node:
                    cur_node.lines = strip_lines(cur_lines)
                    cur_lines = []
                    level2nodes[cur_node.level - 1][-1].children.append(cur_node)
                    level2nodes[cur_node.level].append(cur_node)
            else:
                if line.startswith("@[toc]"):
                    continue
                if line.startswith("```"):
                    code_field ^= 1
                cur_lines.append(line)
        pre_node.lines = strip_lines(cur_lines)
        level2nodes[cur_node.level - 1][-1].children.append(pre_node)
        level2nodes[cur_node.level].append(pre_node)
        root: Node = level2nodes[0][0]
        return root

    @classmethod
    def from_md_file(cls, file="notes.md"):
        md_txt = Path(file).read_text()
        return Node.from_md(md_txt)

    def dump_to_dir(self, dir_name="."):
        notes_dir = Path(dir_name)
        notes_dir.mkdir(parents=True, exist_ok=True)

        def rec(node: Node, path: Path):
            # 非叶子结点
            if node.children :
                cur_path = path / node.title
                (cur_path).mkdir(parents=True, exist_ok=True)
                for child in node.children:
                    rec(child, cur_path)
            # 叶子结点
            else:
                cur_path = path / f"{node.title}.md"
                (cur_path).write_text("\n".join(node.lines))

        rec(self, notes_dir)

    def build_toc(self):
        toc_list = []

        def rec(node: Node, level=0, path="."):
            # 非叶子结点
            prefix = " " * ((level) * 4) + "- "
            toc_list.append(f"{prefix}[{node.title}]")
            cur_path = path + "/" + node.title
            # link = f"'{cur_path}'"
            link = cur_path.replace(" ", "%20")
            if node.children:
                toc_list[-1] += f"({link})"
                for child in node.children:
                    rec(child, level + 1, cur_path)
            else:
                toc_list[-1] += f"({link}.md)"

        rec(self)
        return "\n".join(toc_list)


def md2dir():
    node = Node.from_md_file()
    node.dump_to_dir()
    toc = node.build_toc()
    Path("README.md").write_text(toc)


if __name__ == '__main__':
    md2dir()
