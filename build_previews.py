"""
Generates PNG previews of code rendered with each Lusitania variant.
- TypeScript / React  → Abyssal       (the canonical deep-blue)
- Java + Spring       → Abyssal Deep  (the darker variant)
- SQL                 → Abyssal Light (the light variant)

Each preview looks like a small editor window — title bar, traffic lights,
line numbers, tokenized code. We render to SVG (source of truth) and then
convert to PNG via `npx svgexport`, because the VS Code Marketplace strips
SVGs from README.

Palettes are imported from build.py so they stay in sync automatically.

Run: python3 build_previews.py
Output: previews/typescript.png, previews/java.png, previews/sql.png
        (and the .svg sources alongside them)
"""

from pathlib import Path

from build import DARK_SYNTAX, LIGHT_SYNTAX, DARK_VARIANTS, LIGHT_VARIANTS


def palette_for(variant: dict, syntax: dict) -> dict:
    """Merge a variant's UI backgrounds with a syntax palette into a single
    flat dict the renderer can consume."""
    return {
        "bg":          variant["bg_deepest"],
        "bg_chrome":   variant["bg_widget"],
        "border":      variant["border_med"],
        "fg":          syntax["fg"],
        "fg_bright":   syntax["fg_bright"],
        "fg_dim":      syntax["fg_dim"],
        "yellow":      syntax["yellow"],
        "green":       syntax["green"],
        "blue":        syntax["blue"],
        "cyan":        syntax["cyan"],
        "purple":      syntax["purple"],
        "orange":      syntax["orange"],
        "red":         syntax["red"],
        "red_strong":  syntax["red_strong"],
    }


# Per-preview palette assignments.
ABYSSAL       = palette_for(DARK_VARIANTS["abyssal"],      DARK_SYNTAX)
ABYSSAL_DEEP  = palette_for(DARK_VARIANTS["abyssal-deep"], DARK_SYNTAX)
ABYSSAL_LIGHT = palette_for(LIGHT_VARIANTS["abyssal-light"], LIGHT_SYNTAX)


# Token shorthand — each returns a (text, palette_key, italic) tuple. We pass
# the palette in at render time and resolve the key then, so the same token
# list can render in any variant.
def t(s):    return (s, "fg",          False)
def k(s):    return (s, "purple",      False)
def K(s):    return (s, "purple",      True)
def st(s):   return (s, "green",       False)
def n(s):    return (s, "orange",      False)
def c(s):    return (s, "fg_dim",      True)
def fn(s):   return (s, "yellow",      False)
def m(s):    return (s, "blue",        False)
def cls(s):  return (s, "yellow",      False)
def ty(s):   return (s, "green",       False)
def p(s):    return (s, "orange",      False)
def f(s):    return (s, "fg_bright",   False)
def op(s):   return (s, "cyan",        False)
def tag(s):  return (s, "red",         False)
def at(s):   return (s, "yellow",      True)
def an(s):   return (s, "purple",      False)
def ak(s):   return (s, "orange",      False)
def th(s):   return (s, "red_strong",  False)


def esc(s):
    return s.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')


def render_svg(filename: str, lines: list, palette: dict, output: Path) -> None:
    """Render a list of token lines as an editor-window SVG using the given palette."""
    P = palette
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
        out.append(
            f'<text x="{pad + line_num_w}" y="{y}" font-size="{font_size}" fill="{P["fg_dim"]}" text-anchor="end">{i+1}</text>'
        )
        tspans = []
        for text, color_key, italic in line:
            style = ' font-style="italic"' if italic else ''
            tspans.append(f'<tspan fill="{P[color_key]}"{style}>{esc(text)}</tspan>')
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
# tables → yellow (cls), table aliases → green (ty), columns → bright (f),
# keywords → purple (k), functions → yellow (fn).
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
    # One language per variant — each variant gets its own showcase.
    previews = [
        ("ChatInput.tsx",       TS,   ABYSSAL,       out_dir / "typescript.svg"),
        ("MessageHandler.java", JAVA, ABYSSAL_DEEP,  out_dir / "java.svg"),
        ("top_customers.sql",   SQL,  ABYSSAL_LIGHT, out_dir / "sql.svg"),
    ]
    for filename, lines, palette, path in previews:
        render_svg(filename, lines, palette, path)
    for _, _, _, path in previews:
        svg_to_png(path)


if __name__ == "__main__":
    main()
