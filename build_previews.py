"""
Generates SVG previews of code rendered with the Lusitania Abyssal palette.
Each preview looks like a small editor window — title bar, traffic lights,
line numbers, tokenized code. SVGs render natively on GitHub & the VS Code
marketplace, so the README always shows the real theme colors.

Run: python3 build_previews.py
Output: previews/typescript.svg, previews/java.svg, previews/sql.svg
"""

from pathlib import Path

# ── Abyssal palette (must stay in sync with build.py DARK_SYNTAX) ─────────────
P = {
    "bg":          "#0d1620",
    "bg_chrome":   "#121d2a",
    "border":      "#1f3145",
    "fg":          "#c3cee3",
    "fg_bright":   "#eeffff",
    "fg_dim":      "#546e7a",
    "accent":      "#7fd4d4",
    "yellow":      "#ffcb6b",
    "green":       "#c3e88d",
    "blue":        "#82aaff",
    "cyan":        "#89ddff",
    "purple":      "#c792ea",
    "orange":      "#f78c6c",
    "red":         "#f07178",
    "red_strong":  "#ff5370",
}

# Token shorthand helpers — each returns (text, color, italic).
def t(s):    return (s, P["fg"], False)         # base text / whitespace
def k(s):    return (s, P["purple"], False)     # keyword
def K(s):    return (s, P["purple"], True)      # primitive / italic keyword
def st(s):   return (s, P["green"], False)      # string
def n(s):    return (s, P["orange"], False)     # number
def c(s):    return (s, P["fg_dim"], True)      # comment
def fn(s):   return (s, P["yellow"], False)     # free function / hook / built-in
def m(s):    return (s, P["blue"], False)       # method / function declaration
def cls(s):  return (s, P["yellow"], False)     # class / enum name
def ty(s):   return (s, P["green"], False)      # type / interface / generic
def p(s):    return (s, P["orange"], False)     # parameter
def f(s):    return (s, P["fg_bright"], False)  # field / property / enum member
def op(s):   return (s, P["cyan"], False)       # operator / punctuation
def tag(s):  return (s, P["red"], False)        # jsx/html tag
def at(s):   return (s, P["yellow"], True)      # jsx attribute (italic)
def an(s):   return (s, P["purple"], False)     # annotation / decorator
def ak(s):   return (s, P["orange"], False)     # annotation arg name
def th(s):   return (s, P["red_strong"], False) # this / super
def b(s):    return (s, P["purple"], False)     # true / false / null

def esc(s):
    return s.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')


def render_svg(filename: str, lines: list, output: Path) -> None:
    """Render a list of token lines as an editor-window SVG."""
    pad         = 22
    title_h     = 38
    line_h      = 22
    font_size   = 14
    char_w      = font_size * 0.6   # monospace approximation
    line_num_w  = 30

    n_lines = len(lines)
    max_chars = max((sum(len(tok[0]) for tok in line) for line in lines), default=0)
    code_w = int(max_chars * char_w)
    code_x = pad + line_num_w + 14

    w = max(720, code_x + code_w + pad)
    h = title_h + pad + n_lines * line_h + pad

    out = []
    out.append(f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" font-family="Menlo, Consolas, &quot;Courier New&quot;, monospace">')

    # Drop shadow (subtle)
    out.append('<defs><filter id="shadow" x="-5%" y="-5%" width="110%" height="115%"><feDropShadow dx="0" dy="2" stdDeviation="3" flood-color="#000000" flood-opacity="0.4"/></filter></defs>')

    # Window with rounded corners
    out.append(f'<rect x="0.5" y="0.5" width="{w-1}" height="{h-1}" rx="10" ry="10" fill="{P["bg"]}" stroke="{P["border"]}" stroke-width="1" filter="url(#shadow)"/>')

    # Title bar
    out.append(f'<path d="M 10 0.5 L {w-10} 0.5 Q {w-0.5} 0.5 {w-0.5} 10 L {w-0.5} {title_h} L 0.5 {title_h} L 0.5 10 Q 0.5 0.5 10 0.5 Z" fill="{P["bg_chrome"]}"/>')
    out.append(f'<line x1="0" y1="{title_h}" x2="{w}" y2="{title_h}" stroke="{P["border"]}" stroke-width="1"/>')

    # Traffic lights
    cy = title_h // 2
    out.append(f'<circle cx="20" cy="{cy}" r="6" fill="#ff5f57"/>')
    out.append(f'<circle cx="40" cy="{cy}" r="6" fill="#febc2e"/>')
    out.append(f'<circle cx="60" cy="{cy}" r="6" fill="#28c840"/>')

    # Filename centered
    out.append(
        f'<text x="{w//2}" y="{cy + 4}" font-size="12" fill="{P["fg_dim"]}" text-anchor="middle">{esc(filename)}</text>'
    )

    # Code lines
    y0 = title_h + pad + font_size - 4
    for i, line in enumerate(lines):
        y = y0 + i * line_h
        # line number
        out.append(
            f'<text x="{pad + line_num_w}" y="{y}" font-size="{font_size}" fill="{P["fg_dim"]}" text-anchor="end">{i+1}</text>'
        )
        # tokens
        tspans = []
        for text, color, italic in line:
            style = ' font-style="italic"' if italic else ''
            tspans.append(f'<tspan fill="{color}"{style}>{esc(text)}</tspan>')
        out.append(
            f'<text x="{code_x}" y="{y}" font-size="{font_size}" xml:space="preserve">' + ''.join(tspans) + '</text>'
        )

    out.append('</svg>')
    output.write_text('\n'.join(out))
    print(f"Wrote {output}")


# ─── TypeScript / React snippet ───────────────────────────────────────────────
TS = [
    [k("import"), t(" "), op("{"), t(" "), fn("useState"), op(","), t(" "), fn("useEffect"), t(" "), op("}"), t(" "), k("from"), t(" "), st("'react'"), op(";")],
    [],
    [k("interface"), t(" "), ty("ChatInputProps"), t(" "), op("{")],
    [t("  "), f("onSend"), op(":"), t(" "), op("("), p("message"), op(":"), t(" "), K("string"), op(")"), t(" "), op("=>"), t(" "), K("void"), op(";")],
    [t("  "), f("placeholder"), op("?:"), t(" "), K("string"), op(";")],
    [op("}")],
    [],
    [k("export"), t(" "), k("const"), t(" "), cls("ChatInput"), op(":"), t(" "), ty("FC"), op("<"), ty("ChatInputProps"), op(">"), t(" "), op("="), t(" "), op("("), op("{"), t(" "), p("onSend"), t(" "), op("}"), op(")"), t(" "), op("=>"), t(" "), op("{")],
    [t("  "), k("const"), t(" "), op("["), f("value"), op(","), t(" "), f("setValue"), op("]"), t(" "), op("="), t(" "), fn("useState"), op("<"), K("string"), op(">"), op("("), st("''"), op(")"), op(";")],
    [],
    [t("  "), fn("useEffect"), op("("), op("("), op(")"), t(" "), op("=>"), t(" "), op("{")],
    [t("    "), fn("fetch"), op("("), st("'/api/users'"), op(")"), op("."), m("then"), op("("), p("setUsers"), op(")"), op(";")],
    [t("  "), op("}"), op(","), t(" "), op("["), op("]"), op(")"), op(";")],
    [],
    [t("  "), k("return"), t(" "), op("(")],
    [t("    "), op("<"), tag("div"), t(" "), at("className"), op("="), st('"chat-input"'), op(">")],
    [t("      "), op("<"), tag("input"), t(" "), at("value"), op("="), op("{"), f("value"), op("}"), t(" "), at("onChange"), op("="), op("{"), p("e"), t(" "), op("=>"), t(" "), fn("setValue"), op("("), p("e"), op("."), f("target"), op("."), f("value"), op(")"), op("}"), t(" "), op("/>")],
    [t("      "), op("<"), tag("button"), t(" "), at("onClick"), op("="), op("{"), op("("), op(")"), t(" "), op("=>"), t(" "), fn("onSend"), op("("), f("value"), op(")"), op("}"), op(">"), t("Send"), op("</"), tag("button"), op(">")],
    [t("    "), op("</"), tag("div"), op(">")],
    [t("  "), op(")"), op(";")],
    [op("}"), op(";")],
]

# ─── Java + Spring snippet ────────────────────────────────────────────────────
JAVA = [
    [k("package"), t(" "), fn("com"), op("."), fn("lusitania"), op("."), fn("service"), op(";")],
    [],
    [k("import"), t(" "), fn("org.springframework.stereotype"), op("."), cls("Service"), op(";")],
    [k("import"), t(" "), fn("org.springframework.amqp.rabbit.annotation"), op("."), cls("RabbitListener"), op(";")],
    [k("import"), t(" "), fn("lombok"), op("."), cls("Builder"), op(";")],
    [],
    [an("@Service")],
    [k("public"), t(" "), k("abstract"), t(" "), k("class"), t(" "), ty("MessageHandler"), t(" "), op("{")],
    [],
    [t("    "), an("@Builder")],
    [t("    "), k("public"), t(" "), k("static"), t(" "), k("class"), t(" "), cls("Message"), t(" "), op("{")],
    [t("        "), k("private"), t(" "), K("String"), t(" "), f("id"), op(";")],
    [t("        "), k("private"), t(" "), K("boolean"), t(" "), f("processed"), op(";")],
    [t("    "), op("}")],
    [],
    [t("    "), an("@RabbitListener"), op("(")],
    [t("        "), ak("queues"), t(" "), op("="), t(" "), st('"incoming.messages"'), op(",")],
    [t("        "), ak("containerFactory"), t(" "), op("="), t(" "), st('"rabbitFactory"')],
    [t("    "), op(")")],
    [t("    "), k("public"), t(" "), K("void"), t(" "), m("onMessage"), op("("), ty("Message"), t(" "), p("message"), op(")"), t(" "), op("{")],
    [t("        "), k("if"), t(" "), op("("), p("message"), op("."), m("isProcessed"), op("("), op(")"), op(")"), t(" "), op("{")],
    [t("            "), k("return"), op(";")],
    [t("        "), op("}")],
    [t("        "), m("process"), op("("), p("message"), op(")"), op(";")],
    [t("    "), op("}")],
    [],
    [t("    "), k("protected"), t(" "), k("abstract"), t(" "), K("void"), t(" "), m("process"), op("("), ty("Message"), t(" "), p("message"), op(")"), op(";")],
    [op("}")],
]

# ─── SQL snippet ──────────────────────────────────────────────────────────────
# Color choices (match build.py SQL palette):
#   tables (`customers`, `orders`) → yellow via cls()
#   table aliases (`c`, `o`)       → green  via ty()
#   columns (`id`, `total`)        → bright via f()
#   keywords (SELECT, FROM, AS)    → purple via k()
#   functions (COUNT, SUM, NOW)    → yellow via fn()
SQL = [
    [c("-- Top 10 customers by revenue in the last 30 days")],
    [k("SELECT")],
    [t("    "), ty("c"), op("."), f("id"),         t("            "), k("AS"), t(" "), ty("customer_id"),     op(",")],
    [t("    "), ty("c"), op("."), f("name"),       t("          "), k("AS"), t(" "), ty("customer_name"),   op(",")],
    [t("    "), fn("COUNT"), op("("), ty("o"), op("."), f("id"),    op(")"), t("     "), k("AS"), t(" "), ty("order_count"),      op(",")],
    [t("    "), fn("SUM"),   op("("), ty("o"), op("."), f("total"), op(")"), t("    "), k("AS"), t(" "), ty("revenue"),          op(",")],
    [t("    "), fn("AVG"),   op("("), ty("o"), op("."), f("total"), op(")"), t("    "), k("AS"), t(" "), ty("avg_order_value")],
    [k("FROM"), t(" "), cls("customers"), t(" "), ty("c")],
    [k("INNER JOIN"), t(" "), cls("orders"), t(" "), ty("o"), t(" "), k("ON"), t(" "), ty("o"), op("."), f("customer_id"), t(" "), op("="), t(" "), ty("c"), op("."), f("id")],
    [k("WHERE"), t(" "), ty("o"), op("."), f("created_at"), t(" "), op(">="), t(" "), fn("NOW"), op("("), op(")"), t(" "), op("-"), t(" "), K("INTERVAL"), t(" "), st("'30 days'")],
    [t("  "), k("AND"), t(" "), ty("o"), op("."), f("status"), t(" "), k("NOT IN"), t(" "), op("("), st("'cancelled'"), op(","), t(" "), st("'refunded'"), op(")")],
    [k("GROUP BY"), t(" "), ty("c"), op("."), f("id"), op(","), t(" "), ty("c"), op("."), f("name")],
    [k("HAVING"), t(" "), fn("SUM"), op("("), ty("o"), op("."), f("total"), op(")"), t(" "), op(">"), t(" "), n("1000")],
    [k("ORDER BY"), t(" "), ty("revenue"), t(" "), k("DESC")],
    [k("LIMIT"), t(" "), n("10"), op(";")],
]


def svg_to_png(svg_path: Path) -> None:
    """Convert SVG → PNG at 2x via `npx svgexport`. The marketplace strips
    SVGs from README, so we ship PNGs and keep SVGs as source artifacts."""
    import shutil, subprocess
    png_path = svg_path.with_suffix(".png")
    if not shutil.which("npx"):
        print(f"[warn] npx not found; skipping {png_path.name}. "
              f"Install Node.js to enable PNG generation.")
        return
    subprocess.run(
        ["npx", "--yes", "svgexport", str(svg_path), str(png_path), "2x"],
        check=True,
    )
    print(f"Wrote {png_path}")


def main():
    out_dir = Path(__file__).parent / "previews"
    out_dir.mkdir(exist_ok=True)
    svgs = [
        ("ChatInput.tsx",       TS,   out_dir / "typescript.svg"),
        ("MessageHandler.java", JAVA, out_dir / "java.svg"),
        ("top_customers.sql",   SQL,  out_dir / "sql.svg"),
    ]
    for filename, lines, path in svgs:
        render_svg(filename, lines, path)
    for _, _, path in svgs:
        svg_to_png(path)


if __name__ == "__main__":
    main()
