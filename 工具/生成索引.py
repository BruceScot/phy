"""根据 灵感库/条目/ 下每个条目开头的字段表，重新生成 灵感库/索引.md。

用法：python3 工具/生成索引.py
"""
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parent.parent
ENTRIES = ROOT / "灵感库" / "条目"
INDEX = ROOT / "灵感库" / "索引.md"
FIELDS = ["类型", "状态", "来源", "置信度", "可参考性", "标签"]


def parse(path: pathlib.Path) -> dict:
    text = path.read_text(encoding="utf-8")
    title = text.split("\n", 1)[0].lstrip("# ").strip()
    code, _, name = title.partition(" ")
    info = {"编号": code, "名称": name, "文件": path.name}
    for m in re.finditer(r"^\|\s*([^|]+?)\s*\|\s*([^|]*?)\s*\|$", text, re.M):
        k, v = m.group(1), m.group(2)
        if k in FIELDS and k not in info:
            info[k] = v
    missing = [k for k in FIELDS if k not in info]
    if missing:
        raise SystemExit(f"{path.name} 缺少字段：{'、'.join(missing)}")
    return info


def main() -> None:
    rows = [parse(p) for p in sorted(ENTRIES.glob("L*.md"))]
    lines = [
        "# 灵感库索引",
        "",
        "> 本文件由 `工具/生成索引.py` 自动生成，请勿手工编辑。",
        "",
        f"共 {len(rows)} 条。",
        "",
        "| 编号 | 名称 | 类型 | 状态 | 来源 | 置信度 | 可参考性 | 标签 |",
        "|---|---|---|---|---|---|---|---|",
    ]
    for r in rows:
        lines.append(
            f"| {r['编号']} | [{r['名称']}](条目/{r['文件']}) | {r['类型']} | {r['状态']} | "
            f"{r['来源']} | {r['置信度']} | {r['可参考性']} | {r['标签']} |"
        )
    INDEX.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"已生成索引：{len(rows)} 条")


if __name__ == "__main__":
    main()
