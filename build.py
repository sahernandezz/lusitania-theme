"""
Builds the Lusitania theme variants from a shared template.

Variants:
- Abyssal       — the canonical deep-blue dark theme (the main one).
- Abyssal Deep  — darker, more dramatic. Matches the icon background (#0A0D14).
- Abyssal Light — light variant with the same syntax spirit, tuned for daylight.

The two dark variants share the same syntax palette; only UI backgrounds change.
The light variant has its own UI + syntax palette designed for light backgrounds.
"""

import json
from pathlib import Path

# ── DARK SYNTAX PALETTE (Material Oceanic family) ─────────────────────────────
DARK_SYNTAX = {
    "fg":             "#c3cee3",
    "fg_bright":      "#eeffff",   # enum members, properties, fields
    "fg_dim":         "#546e7a",   # comments, inactive
    "accent":         "#009688",
    "accent_hover":   "#00796b",
    "yellow":         "#ffcb6b",   # classes, JSX components, hooks, free function calls
    "green":          "#c3e88d",   # strings, interfaces, abstract classes, types
    "blue":           "#82aaff",   # method/function declarations and method calls
    "cyan":           "#89ddff",   # operators, punctuation
    "purple":         "#c792ea",   # keywords, decorators, primitives, true/false/null
    "orange":         "#f78c6c",   # numbers, parameters, JSX attrs, annotation arg names
    "red":            "#f07178",   # JSX tags, html tags
    "red_strong":     "#ff5370",   # errors, this/super
    "cursor":         "#ffcc00",
    # SQL accents — derived from the main palette but tuned to read well on SQL.
    "sql_keyword":    "#c792ea",   # SELECT/FROM/WHERE — purple, matches keyword family
    "sql_fn":         "#ffcb6b",   # COUNT/SUM/NOW — yellow, matches free function calls
    "sql_table":      "#ffcb6b",   # table identifiers — yellow (class-like)
    "sql_column":     "#eeffff",   # column identifiers — bright fg (property-like)
    "sql_alias":      "#c3e88d",   # aliases — green (type-like)
}

# ── LIGHT SYNTAX PALETTE (Abyssal Light) ──────────────────────────────────────
# Designed from scratch for light backgrounds. Names match DARK_SYNTAX so the
# same token rules work for both — only color values differ.
LIGHT_SYNTAX = {
    "fg":             "#2c3e50",   # base text, dark slate
    "fg_bright":      "#1a2733",   # enum members, properties (darker for emphasis)
    "fg_dim":         "#90a4ae",   # comments
    "accent":         "#00897b",   # teal, slightly darker for light bg
    "accent_hover":   "#00695c",
    "yellow":         "#c9851a",   # classes — amber, dark enough to read on white
    "green":          "#558b2f",   # strings, interfaces — moss green
    "blue":           "#1976d2",   # methods — strong blue
    "cyan":           "#0288d1",   # operators, punctuation
    "purple":         "#7b1fa2",   # keywords, decorators
    "orange":         "#d84315",   # numbers, params, annotation args — burnt orange
    "red":            "#c62828",   # JSX tags
    "red_strong":     "#b71c1c",   # errors
    "cursor":         "#272727",
    "sql_keyword":    "#7b1fa2",
    "sql_fn":         "#c9851a",
    "sql_table":      "#c9851a",
    "sql_column":     "#1a2733",
    "sql_alias":      "#558b2f",
}

# ── DARK VARIANT BACKGROUNDS ──────────────────────────────────────────────────
DARK_VARIANTS = {
    "abyssal": {
        # The canonical Lusitania theme — deep blue oceanic.
        "name": "Lusitania — Abyssal",
        "bg_deepest":   "#0d1620",
        "bg_panel":     "#0d1620",
        "bg_widget":    "#121d2a",
        "bg_line":      "#11202e",
        "bg_input":     "#121d2a",
        "bg_dropdown":  "#172534",
        "border_soft":  "#172534",
        "border_med":   "#1f3145",
        "border_guide": "#17263a",
        "sel_bg":       "#1f3a55",
        "sel_weak":     "#1f3a5544",
        "list_inactive":"#101d2a",
    },
    "abyssal-deep": {
        # Darker, more dramatic — matches the icon background. For OLED and
        # users who want the deepest possible feel.
        "name": "Lusitania — Abyssal Deep",
        "bg_deepest":   "#0a0d14",
        "bg_panel":     "#0a0d14",
        "bg_widget":    "#0f131c",
        "bg_line":      "#0d1119",
        "bg_input":     "#0f131c",
        "bg_dropdown":  "#141926",
        "border_soft":  "#141926",
        "border_med":   "#1c2333",
        "border_guide": "#13182380",
        "sel_bg":       "#1a2f45",
        "sel_weak":     "#1a2f4544",
        "list_inactive":"#0d111a",
    },
}

# ── LIGHT VARIANT (Abyssal Light) ─────────────────────────────────────────────
LIGHT_VARIANT = {
    "name": "Lusitania — Abyssal Light",
    "bg_deepest":   "#fafafa",
    "bg_panel":     "#f5f5f5",
    "bg_widget":    "#ffffff",
    "bg_line":      "#f0f4f8",
    "bg_input":     "#ffffff",
    "bg_dropdown":  "#eceff1",
    "border_soft":  "#e0e0e0",
    "border_med":   "#cfd8dc",
    "border_guide": "#e8eaed",
    "sel_bg":       "#b2dfdb",
    "sel_weak":     "#b2dfdb55",
    "list_inactive":"#eceff1",
}


def build_colors(v: dict, syntax: dict, is_light: bool = False) -> dict:
    """Build workbench UI colors. Works for both dark and light variants."""
    bg, bg_p, bg_w = v["bg_deepest"], v["bg_panel"], v["bg_widget"]
    bg_l, bg_i, bg_d = v["bg_line"], v["bg_input"], v["bg_dropdown"]
    bs, bm, bg_g    = v["border_soft"], v["border_med"], v["border_guide"]
    sel, sel_w      = v["sel_bg"], v["sel_weak"]
    list_in         = v["list_inactive"]

    s = syntax
    accent = s["accent"]
    contrast_fg = "#ffffff" if not is_light else "#ffffff"  # buttons always white text
    inactive_alpha = "99" if is_light else "99"

    return {
        "activityBar.activeBackground":   "#00000000",
        "activityBar.activeBorder":       accent,
        "activityBar.background":         bg,
        "activityBar.border":             bs,
        "activityBar.foreground":         s["fg"],
        "activityBar.inactiveForeground": s["fg_dim"],
        "activityBarBadge.background":    accent,
        "activityBarBadge.foreground":    contrast_fg,
        "badge.background":               accent,
        "badge.foreground":               contrast_fg,
        "breadcrumb.activeSelectionForeground": s["fg_bright"] if is_light else "#ffffff",
        "breadcrumb.background":          bg,
        "breadcrumb.focusForeground":     s["fg_bright"] if is_light else "#ffffff",
        "breadcrumb.foreground":          s["fg_dim"],
        "button.background":              accent,
        "button.foreground":              contrast_fg,
        "button.hoverBackground":         s["accent_hover"],
        "button.secondaryBackground":     bs,
        "button.secondaryForeground":     s["fg"],
        "checkbox.background":            bg_i,
        "checkbox.border":                bm,
        "debugToolBar.background":        bg,
        "diffEditor.insertedTextBackground": s["green"]  + "22",
        "diffEditor.removedTextBackground":  s["red"]    + "22",
        "dropdown.background":            bg_d,
        "dropdown.border":                bm,
        "dropdown.foreground":            s["fg"],
        "editor.background":              bg,
        "editor.findMatchBackground":     s["yellow"] + "55",
        "editor.findMatchBorder":         s["yellow"],
        "editor.findMatchHighlightBackground": s["yellow"] + "33",
        "editor.findRangeHighlightBackground": ("#00000008" if is_light else "#ffffff08"),
        "editor.foreground":              s["fg"],
        "editor.hoverHighlightBackground": accent + "18",
        "editor.inactiveSelectionBackground": sel + "44",
        "editor.lineHighlightBackground": bg_l,
        "editor.lineHighlightBorder":     bg_l,
        "editor.rangeHighlightBackground": ("#00000008" if is_light else "#ffffff08"),
        "editor.selectionBackground":     sel,
        "editor.selectionForeground":     s["fg_bright"] if is_light else "#fffbf7",
        "editor.selectionHighlightBackground": sel_w,
        "editor.wordHighlightBackground":     sel + "80",
        "editor.wordHighlightStrongBackground": ("#80deea80" if not is_light else "#80cbc480"),
        "editorBracketMatch.background":  accent + "22",
        "editorBracketMatch.border":      accent,
        "editorCodeLens.foreground":      s["fg_dim"],
        "editorCursor.foreground":        s["cursor"],
        "editorError.foreground":         s["red_strong"],
        "editorGroup.border":             bs,
        "editorGroup.dropBackground":     accent + "20",
        "editorGroupHeader.noTabsBackground": bg,
        "editorGroupHeader.tabsBackground":   bg,
        "editorGroupHeader.tabsBorder":       bs,
        "editorGutter.addedBackground":   s["green"],
        "editorGutter.deletedBackground": s["red"],
        "editorGutter.modifiedBackground": s["yellow"],
        "editorHoverWidget.background":   bg_w,
        "editorHoverWidget.border":       bm,
        "editorIndentGuide.activeBackground": "#37474f" if not is_light else "#90a4ae",
        "editorIndentGuide.background":   bg_g,
        "editorInfo.foreground":          s["blue"],
        "editorLineNumber.activeForeground": s["fg_dim"],
        "editorLineNumber.foreground":    ("#2a3a3a" if not is_light else "#c2c8cc"),
        "editorLink.activeForeground":    s["blue"],
        "editorMarkerNavigation.background": bg_w,
        "editorOverviewRuler.border":     bs,
        "editorRuler.foreground":         bg_g,
        "editorSuggestWidget.background": bg_w,
        "editorSuggestWidget.border":     bm,
        "editorSuggestWidget.foreground": s["fg"],
        "editorSuggestWidget.highlightForeground": accent,
        "editorSuggestWidget.selectedBackground":  sel,
        "editorWarning.foreground":       s["yellow"],
        "editorWhitespace.foreground":    bg_g,
        "editorWidget.background":        bg_w,
        "editorWidget.border":            bm,
        "errorForeground":                s["red_strong"],
        "extensionButton.prominentBackground":      accent,
        "extensionButton.prominentForeground":      contrast_fg,
        "extensionButton.prominentHoverBackground": s["accent_hover"],
        "focusBorder":                    accent,
        "foreground":                     s["fg"],
        "gitDecoration.addedResourceForeground":       s["green"],
        "gitDecoration.conflictingResourceForeground": s["purple"],
        "gitDecoration.deletedResourceForeground":     s["fg_dim"],
        "gitDecoration.ignoredResourceForeground":     s["fg_dim"],
        "gitDecoration.modifiedResourceForeground":    s["accent"],
        "gitDecoration.submoduleResourceForeground":   s["blue"],
        "gitDecoration.untrackedResourceForeground":   s["green"],
        "input.background":                bg_i,
        "input.border":                    bm,
        "input.foreground":                s["fg"],
        "input.placeholderForeground":     s["fg_dim"],
        "inputOption.activeBackground":    accent + "33",
        "inputOption.activeBorder":        accent,
        "list.activeSelectionBackground":   sel,
        "list.activeSelectionForeground":   s["fg_bright"] if is_light else "#ffffff",
        "list.dropBackground":              sel,
        "list.errorForeground":             s["red_strong"],
        "list.focusBackground":             sel,
        "list.highlightForeground":         accent,
        "list.hoverBackground":             bg_w,
        "list.inactiveSelectionBackground": list_in,
        "list.warningForeground":           s["yellow"],
        "menu.background":               bg_w,
        "menu.foreground":               s["fg"],
        "menu.selectionBackground":      sel,
        "menu.selectionForeground":      s["fg_bright"] if is_light else "#ffffff",
        "menu.separatorBackground":      bm,
        "menubar.selectionBackground":   ("#00000011" if is_light else "#ffffff11"),
        "menubar.selectionForeground":   s["fg"],
        "notificationCenterHeader.background": bg_w,
        "notifications.background":      bg_w,
        "notifications.border":          bs,
        "notifications.foreground":      s["fg"],
        "panel.background":              bg_p,
        "panel.border":                  bs,
        "panelTitle.activeBorder":       accent,
        "panelTitle.activeForeground":   s["fg_bright"] if is_light else "#ffffff",
        "panelTitle.inactiveForeground": s["fg_dim"],
        "peekView.border":               accent,
        "peekViewEditor.background":     bg,
        "peekViewEditorGutter.background": bg,
        "peekViewResult.background":     bg_w,
        "peekViewTitle.background":      bg,
        "peekViewTitleLabel.foreground": s["fg_bright"] if is_light else "#ffffff",
        "pickerGroup.border":            bm,
        "pickerGroup.foreground":        accent,
        "progressBar.background":        accent,
        "quickInput.background":         bg_w,
        "quickInput.foreground":         s["fg"],
        "scrollbar.shadow":                       ("#cfd8dc" if is_light else "#000000"),
        "scrollbarSlider.activeBackground":       accent + "aa",
        "scrollbarSlider.background":             bm + "55",
        "scrollbarSlider.hoverBackground":        accent + "aa",
        "selection.background":                   sel,
        "settings.checkboxBackground":  bg_i,
        "settings.checkboxBorder":      bm,
        "settings.dropdownBackground":  bg_i,
        "settings.dropdownBorder":      bm,
        "settings.headerForeground":    s["fg_bright"] if is_light else "#ffffff",
        "settings.modifiedItemIndicator": accent,
        "settings.numberInputBackground": bg_i,
        "settings.textInputBackground":   bg_i,
        "sideBar.background":           bg,
        "sideBar.border":               bs,
        "sideBar.dropBackground":       sel + "33",
        "sideBar.foreground":           s["fg"],
        "sideBarSectionHeader.background": bg,
        "sideBarSectionHeader.border": bs,
        "sideBarSectionHeader.foreground": s["fg_dim"],
        "sideBarTitle.foreground":      s["fg_dim"],
        "statusBar.background":            bg,
        "statusBar.border":                bs,
        "statusBar.debuggingBackground":   s["red"],
        "statusBar.debuggingForeground":   contrast_fg,
        "statusBar.foreground":            s["fg_dim"],
        "statusBar.noFolderBackground":    bg,
        "statusBarItem.hoverBackground":   ("#00000011" if is_light else "#ffffff11"),
        "statusBarItem.remoteBackground":  accent,
        "statusBarItem.remoteForeground":  contrast_fg,
        "tab.activeBackground":            bg,
        "tab.activeBorder":                "#00000000",
        "tab.activeBorderTop":             accent,
        "tab.activeForeground":            s["fg_bright"] if is_light else "#ffffff",
        "tab.border":                      bs,
        "tab.hoverBackground":             bg_w,
        "tab.inactiveBackground":          bg,
        "tab.inactiveForeground":          s["fg_dim"],
        "tab.unfocusedActiveBackground":   bg,
        "tab.unfocusedActiveForeground":   s["fg"] + "80",
        "tab.unfocusedInactiveForeground": s["fg_dim"] + "80",
        "terminal.background":             bg,
        "terminal.foreground":             s["fg"],
        "terminal.ansiBlack":              ("#37474f" if is_light else "#000000"),
        "terminal.ansiBlue":               s["blue"],
        "terminal.ansiBrightBlack":        s["fg_dim"],
        "terminal.ansiBrightBlue":         s["blue"],
        "terminal.ansiBrightCyan":         s["cyan"],
        "terminal.ansiBrightGreen":        s["green"],
        "terminal.ansiBrightMagenta":      s["purple"],
        "terminal.ansiBrightRed":          s["red"],
        "terminal.ansiBrightWhite":        s["fg_bright"] if is_light else "#ffffff",
        "terminal.ansiBrightYellow":       s["yellow"],
        "terminal.ansiCyan":               s["cyan"],
        "terminal.ansiGreen":              s["green"],
        "terminal.ansiMagenta":            s["purple"],
        "terminal.ansiRed":                s["red_strong"],
        "terminal.ansiWhite":              s["fg"],
        "terminal.ansiYellow":             s["yellow"],
        "terminal.selectionBackground":    sel,
        "terminalCursor.foreground":       s["cursor"],
        "textLink.activeForeground":       s["blue"],
        "textLink.foreground":             s["blue"],
        "titleBar.activeBackground":       bg,
        "titleBar.activeForeground":       s["fg"],
        "titleBar.border":                 bs,
        "titleBar.inactiveBackground":     bg,
        "titleBar.inactiveForeground":     s["fg"] + inactive_alpha,
        "toolbar.hoverBackground":         bs,
        "widget.shadow":                   ("#00000022" if is_light else "#00000099"),
    }


def build_token_colors(s: dict) -> list:
    """Token colors (TextMate scopes). Same rules for dark & light, only color values differ."""
    return [
        {"name": "Base text",
         "scope": ["source", "text"],
         "settings": {"foreground": s["fg"]}},

        {"name": "Comments",
         "scope": ["comment", "punctuation.definition.comment"],
         "settings": {"foreground": s["fg_dim"], "fontStyle": "italic"}},

        # KEYWORDS → purple
        {"name": "Keywords",
         "scope": [
            "keyword", "keyword.control", "keyword.control.import",
            "keyword.control.export", "keyword.control.from",
            "keyword.control.as", "keyword.control.default",
            "keyword.control.module", "keyword.control.flow",
            "keyword.control.return", "keyword.control.conditional",
            "keyword.control.loop", "keyword.control.trycatch",
            "keyword.control.switch", "keyword.other.new", "keyword.other",
            "keyword.other.package", "keyword.other.import",
            "storage.type", "storage.type.ts", "storage.type.tsx",
            "storage.type.js", "storage.type.java",
            "storage.type.function.arrow", "storage.type.type",
            "storage.type.type.ts", "storage.type.type.tsx",
            "storage.type.interface", "storage.type.interface.ts",
            "storage.type.interface.tsx", "storage.type.class",
            "storage.type.enum", "storage.modifier",
            "storage.modifier.import", "storage.modifier.package"
         ],
         "settings": {"foreground": s["purple"]}},

        # IMPORT PATHS → yellow
        {"name": "Import paths",
         "scope": [
            "entity.name.namespace", "support.other.namespace",
            "meta.import entity.name.namespace",
            "meta.package.declaration entity.name.namespace",
            "entity.name.module", "meta.import string.quoted",
            "variable.language.wildcard.java",
            "storage.modifier.import.java", "storage.modifier.package.java",
            "meta.import.java", "meta.package.java"
         ],
         "settings": {"foreground": s["yellow"]}},

        {"name": "Imported names in braces",
         "scope": [
            "meta.import variable.other.readwrite",
            "meta.import variable.other.readwrite.alias",
            "meta.import variable.other",
            "meta.export variable.other.readwrite",
            "meta.export variable.other"
         ],
         "settings": {"foreground": s["yellow"]}},

        # OPERATORS / PUNCTUATION → cyan
        {"name": "Operators",
         "scope": [
            "keyword.operator", "keyword.operator.assignment",
            "keyword.operator.comparison", "keyword.operator.logical",
            "keyword.operator.arithmetic", "keyword.operator.type",
            "keyword.operator.spread", "keyword.operator.rest",
            "keyword.operator.expression.typeof",
            "keyword.operator.expression.instanceof",
            "keyword.operator.expression.keyof"
         ],
         "settings": {"foreground": s["cyan"]}},

        {"name": "Punctuation",
         "scope": [
            "punctuation.definition.block",
            "punctuation.definition.parameters",
            "punctuation.definition.typeparameters",
            "punctuation.definition.template-expression",
            "punctuation.section.embedded", "meta.brace.curly",
            "meta.brace.round", "meta.brace.square",
            "punctuation.separator.comma",
            "punctuation.terminator.statement",
            "punctuation.accessor", "punctuation.separator",
            "punctuation.separator.key-value"
         ],
         "settings": {"foreground": s["cyan"]}},

        # VARIABLES / FIELDS
        {"name": "Variables and fields",
         "scope": [
            "variable", "variable.other", "variable.other.readwrite",
            "variable.other.object", "variable.other.constant",
            "variable.other.readwrite.alias",
            "variable.other.object.property",
            "variable.other.property", "variable.other.field"
         ],
         "settings": {"foreground": s["fg_bright"]}},

        {"name": "Parameters",
         "scope": ["variable.parameter"],
         "settings": {"foreground": s["orange"]}},

        {"name": "this / super",
         "scope": ["variable.language.this", "variable.language.super"],
         "settings": {"foreground": s["red_strong"]}},

        # STRINGS → green
        {"name": "Strings",
         "scope": [
            "string", "string.quoted.single", "string.quoted.double",
            "string.quoted.backtick", "string.template"
         ],
         "settings": {"foreground": s["green"]}},

        {"name": "String escapes",
         "scope": ["constant.character.escape"],
         "settings": {"foreground": s["cyan"]}},

        {"name": "Regex",
         "scope": ["string.regexp"],
         "settings": {"foreground": s["green"]}},

        # NUMBERS → orange
        {"name": "Numbers",
         "scope": ["constant.numeric"],
         "settings": {"foreground": s["orange"]}},

        # true / false / null / undefined → purple
        {"name": "Language constants (true/false/null/undefined)",
         "scope": [
            "constant.language",
            "constant.language.boolean",
            "constant.language.null",
            "constant.language.undefined",
            "constant.language.boolean.true",
            "constant.language.boolean.false",
            "constant.language.boolean.true.java",
            "constant.language.boolean.false.java",
            "constant.language.null.java"
         ],
         "settings": {"foreground": s["purple"]}},

        # Enum members → bright fg (white-ish): ElementType.TYPE, RUNTIME...
        {"name": "Enum members",
         "scope": [
            "variable.other.enummember",
            "constant.other.enum",
            "meta.enum variable.other.readwrite"
         ],
         "settings": {"foreground": s["fg_bright"]}},

        # Primitive types → purple italic
        {"name": "Primitive types",
         "scope": [
            "support.type.primitive", "keyword.type",
            "support.type.builtin", "storage.type.primitive",
            "storage.type.numeric.java", "storage.type.boolean.java",
            "storage.type.object.array.java"
         ],
         "settings": {"foreground": s["purple"], "fontStyle": "italic"}},

        # ─── FUNCTIONS vs METHODS ────────────────────────────────────────────
        {"name": "Method declarations",
         "scope": [
            "meta.method entity.name.function",
            "meta.definition.method entity.name.function",
            "entity.name.function.member"
         ],
         "settings": {"foreground": s["blue"]}},

        {"name": "Method calls",
         "scope": [
            "meta.function-call.method entity.name.function",
            "meta.method-call entity.name.function",
            "variable.function.member",
            "support.function.member"
         ],
         "settings": {"foreground": s["blue"]}},

        {"name": "Function declarations",
         "scope": [
            "meta.function entity.name.function",
            "meta.definition.function entity.name.function",
            "entity.name.function"
         ],
         "settings": {"foreground": s["blue"]}},

        {"name": "Free function calls (built-ins, helpers)",
         "scope": [
            "meta.function-call entity.name.function",
            "meta.function-call.generic entity.name.function",
            "support.function",
            "support.function.builtin"
         ],
         "settings": {"foreground": s["yellow"]}},

        # React hooks - placed AFTER function rules so they win
        {"name": "React hooks",
         "scope": [
            "support.function.hook",
            "entity.name.function.hook",
            "variable.other.constant.hook",
            "meta.function-call entity.name.function.hook",
            "support.function.react",
            "entity.name.function.use"
         ],
         "settings": {"foreground": s["yellow"]}},

        # ─── CLASSES ─────────────────────────────────────────────────────────
        {"name": "Class names",
         "scope": [
            "entity.name.class", "entity.name.type.class",
            "support.class", "entity.other.inherited-class"
         ],
         "settings": {"foreground": s["yellow"]}},

        # FIX for `new Date()`, `new FormData()`, `new Promise()` in TS/JS:
        # TS server marks these as support.type / support.class constructors.
        # Force yellow here so the class part stays yellow (not blue).
        {"name": "Constructor classes after new (built-ins like Date, FormData, Promise)",
         "scope": [
            "new.expr entity.name.type",
            "meta.new entity.name.type",
            "meta.instance.constructor entity.name.type",
            "support.class.builtin",
            "support.class.error.ts",
            "support.class.promise.ts",
            "support.class.console.ts",
            "support.class.error.tsx",
            "support.class.promise.tsx",
            "support.class.builtin.ts"
         ],
         "settings": {"foreground": s["yellow"]}},

        # Abstract classes → green
        {"name": "Abstract class declarations",
         "scope": [
            "meta.class.abstract entity.name.class",
            "meta.class.abstract entity.name.type.class",
            "entity.name.type.class.abstract",
            "entity.name.class.abstract"
         ],
         "settings": {"foreground": s["green"]}},

        # Interfaces → green
        {"name": "Interfaces",
         "scope": ["entity.name.type.interface"],
         "settings": {"foreground": s["green"]}},

        # Enums → yellow
        {"name": "Enum type names",
         "scope": ["entity.name.type.enum"],
         "settings": {"foreground": s["yellow"]}},

        # Types & generics → green
        {"name": "Type references and generics",
         "scope": [
            "entity.name.type", "entity.name.type.alias", "support.type"
         ],
         "settings": {"foreground": s["green"]}},

        {"name": "Type parameters",
         "scope": ["entity.name.type.parameter"],
         "settings": {"foreground": s["green"]}},

        # Decorators / Annotations → purple
        {"name": "Decorators and annotations",
         "scope": [
            "entity.name.function.decorator", "meta.decorator",
            "punctuation.decorator", "storage.type.annotation",
            "entity.name.type.annotation",
            "punctuation.definition.annotation",
            "meta.declaration.annotation", "support.type.annotation"
         ],
         "settings": {"foreground": s["purple"]}},

        # FIX for @Column(name = "id"), @RabbitListener(queues = ...):
        # Per the official Java tmLanguage grammar, annotation arg names use
        # the scope "constant.other.key.java". This is the canonical fix.
        # We also include other common scopes as fallback for TS decorators.
        {"name": "Annotation argument names (Java/TS decorators)",
         "scope": [
            "constant.other.key.java",
            "meta.declaration.annotation.java constant.other.key",
            "meta.declaration.annotation constant.other.key",
            "meta.declaration.annotation variable.other.readwrite",
            "meta.declaration.annotation variable.other",
            "meta.declaration.annotation variable.parameter",
            "meta.annotation variable.other.readwrite",
            "meta.annotation variable.other",
            "meta.annotation variable.parameter",
            "meta.annotation.identifier",
            "meta.annotation.parameters variable.other.readwrite",
            "meta.annotation.parameters variable.other",
            "meta.annotation.java variable.other.readwrite",
            "meta.annotation.java variable.other",
            "annotation.identifier",
            "annotation.parameter.name"
         ],
         "settings": {"foreground": s["orange"]}},

        # ─── JSX / HTML ──────────────────────────────────────────────────────
        {"name": "Tag punctuation",
         "scope": [
            "punctuation.definition.tag",
            "punctuation.definition.tag.begin",
            "punctuation.definition.tag.end"
         ],
         "settings": {"foreground": s["cyan"]}},

        # IntelliJ-style: ALL tag names red — both HTML elements AND React components
        {"name": "HTML/JSX tag names (elements and components)",
         "scope": [
            "entity.name.tag", "entity.name.tag.html",
            "entity.name.tag.tsx", "entity.name.tag.jsx",
            "entity.name.tag.js",
            "support.class.component",
            "support.class.component.tsx",
            "support.class.component.jsx"
         ],
         "settings": {"foreground": s["red"]}},

        # JSX/HTML attributes → yellow italic (props)
        {"name": "HTML/JSX attribute names",
         "scope": [
            "entity.other.attribute-name",
            "entity.other.attribute-name.html",
            "entity.other.attribute-name.tsx",
            "entity.other.attribute-name.jsx"
         ],
         "settings": {"foreground": s["yellow"], "fontStyle": "italic"}},

        # ─── CSS ─────────────────────────────────────────────────────────────
        {"name": "CSS tag selectors",
         "scope": ["entity.name.tag.css"],
         "settings": {"foreground": s["red"]}},

        {"name": "CSS class names",
         "scope": ["entity.other.attribute-name.class.css"],
         "settings": {"foreground": s["yellow"]}},

        {"name": "CSS IDs and pseudo selectors",
         "scope": [
            "entity.other.attribute-name.id.css",
            "entity.other.pseudo-class.css",
            "entity.other.pseudo-element.css"
         ],
         "settings": {"foreground": s["purple"]}},

        {"name": "CSS property names",
         "scope": ["support.type.property-name.css"],
         "settings": {"foreground": s["accent"]}},

        {"name": "CSS values",
         "scope": [
            "constant.numeric.css", "keyword.other.unit.css",
            "support.constant.property-value.css"
         ],
         "settings": {"foreground": s["orange"]}},

        # ─── JSON ────────────────────────────────────────────────────────────
        {"name": "JSON keys",
         "scope": ["support.type.property-name.json"],
         "settings": {"foreground": s["purple"]}},

        {"name": "JSON constants",
         "scope": ["constant.language.json"],
         "settings": {"foreground": s["purple"]}},

        # ─── SQL ─────────────────────────────────────────────────────────────
        # SQL grammars vary across extensions (vscode built-in, mssql, pg, etc).
        # We cover the canonical scopes from the built-in grammar plus the most
        # common variants. Rules are ordered specific → general so the SQL ones
        # win over the generic keyword/function rules above.

        # DML/DDL/DCL keywords → purple. SELECT, FROM, WHERE, JOIN, CREATE...
        {"name": "SQL keywords",
         "scope": [
            "keyword.other.DML.sql", "keyword.other.DDL.sql",
            "keyword.other.DCL.sql", "keyword.other.alias.sql",
            "keyword.other.create.sql", "keyword.other.drop.sql",
            "keyword.other.update.sql", "keyword.other.delete.sql",
            "keyword.other.insert.sql", "keyword.other.select.sql",
            "keyword.other.from.sql", "keyword.other.where.sql",
            "keyword.other.join.sql", "keyword.other.order-by.sql",
            "keyword.other.group-by.sql", "keyword.other.having.sql",
            "keyword.other.union.sql", "keyword.other.limit.sql",
            "keyword.other.sql"
         ],
         "settings": {"foreground": s["sql_keyword"]}},

        # SQL operators (AND, OR, NOT, IN, BETWEEN, LIKE, IS NULL...) → cyan
        {"name": "SQL operators",
         "scope": [
            "keyword.operator.logical.sql",
            "keyword.operator.comparison.sql",
            "keyword.operator.assignment.sql",
            "keyword.operator.math.sql",
            "keyword.operator.concatenator.sql",
            "keyword.other.operator.sql"
         ],
         "settings": {"foreground": s["cyan"]}},

        # SQL types (INT, VARCHAR, TEXT, BOOLEAN, TIMESTAMP...) → purple italic
        {"name": "SQL data types",
         "scope": [
            "storage.type.sql",
            "support.type.sql",
            "support.type.builtin.sql"
         ],
         "settings": {"foreground": s["purple"], "fontStyle": "italic"}},

        # SQL functions (COUNT, SUM, AVG, NOW, COALESCE, MAX, MIN...) → yellow
        {"name": "SQL built-in functions",
         "scope": [
            "support.function.aggregate.sql",
            "support.function.scalar.sql",
            "support.function.string.sql",
            "support.function.numeric.sql",
            "support.function.datetime.sql",
            "support.function.window.sql",
            "support.function.sql",
            "meta.function-call.sql entity.name.function",
            "entity.name.function.sql"
         ],
         "settings": {"foreground": s["sql_fn"]}},

        # SQL strings (single-quoted) → green (already covered by string rule,
        # but explicit to win over any grammar that uses string.unquoted)
        {"name": "SQL strings",
         "scope": [
            "string.quoted.single.sql",
            "string.quoted.double.sql"
         ],
         "settings": {"foreground": s["green"]}},

        # SQL numeric literals → orange (already covered, explicit for safety)
        {"name": "SQL numbers",
         "scope": ["constant.numeric.sql"],
         "settings": {"foreground": s["orange"]}},

        # SQL identifiers — schema, table, column. Different grammars expose
        # these differently; we set bright fg as the default for column-like
        # identifiers and yellow for table-like ones.
        {"name": "SQL table / schema names",
         "scope": [
            "entity.name.function.table.sql",
            "entity.name.table.sql",
            "constant.other.table-name.sql",
            "constant.other.database-name.sql",
            "meta.table-name.sql",
            "entity.name.schema.sql"
         ],
         "settings": {"foreground": s["sql_table"]}},

        {"name": "SQL column names",
         "scope": [
            "constant.other.column-name.sql",
            "entity.name.column.sql",
            "meta.column-name.sql",
            "variable.other.column.sql"
         ],
         "settings": {"foreground": s["sql_column"]}},

        # SQL aliases (AS foo) → green (type-ish)
        {"name": "SQL aliases",
         "scope": [
            "entity.name.alias.sql",
            "variable.other.alias.sql"
         ],
         "settings": {"foreground": s["sql_alias"]}},

        # SQL quoted identifiers ("my_table", `users`) — keep readable on
        # backgrounds; treat as table-ish identifier.
        {"name": "SQL quoted identifiers",
         "scope": [
            "string.quoted.other.identifier.sql",
            "entity.name.identifier.sql"
         ],
         "settings": {"foreground": s["sql_table"]}},

        # SQL parameters and bind variables (:id, $1, ?) → orange
        {"name": "SQL parameters",
         "scope": [
            "variable.parameter.sql",
            "variable.other.bind.sql",
            "constant.other.placeholder.sql"
         ],
         "settings": {"foreground": s["orange"]}},

        # SQL punctuation (commas, parens) → cyan, matches the family
        {"name": "SQL punctuation",
         "scope": [
            "punctuation.separator.comma.sql",
            "punctuation.definition.parameters.sql",
            "punctuation.section.scope.sql",
            "punctuation.terminator.statement.sql"
         ],
         "settings": {"foreground": s["cyan"]}},

        # SQL comments — already covered by generic comment, explicit for safety
        {"name": "SQL comments",
         "scope": [
            "comment.line.double-dash.sql",
            "comment.block.sql"
         ],
         "settings": {"foreground": s["fg_dim"], "fontStyle": "italic"}},

        # ─── MARKDOWN ────────────────────────────────────────────────────────
        {"name": "Markdown headings",
         "scope": ["markup.heading", "entity.name.section.markdown"],
         "settings": {"foreground": s["green"]}},

        {"name": "Markdown bold",
         "scope": ["markup.bold"],
         "settings": {"foreground": s["red"], "fontStyle": "bold"}},

        {"name": "Markdown italic",
         "scope": ["markup.italic"],
         "settings": {"foreground": s["red"], "fontStyle": "italic"}},

        {"name": "Markdown code",
         "scope": ["markup.inline.raw"],
         "settings": {"foreground": s["purple"]}},

        {"name": "Markdown links",
         "scope": ["markup.underline.link", "string.other.link"],
         "settings": {"foreground": s["blue"]}},

        {"name": "Invalid",
         "scope": ["invalid", "invalid.illegal"],
         "settings": {"foreground": s["red_strong"], "fontStyle": ""}},
    ]


def build_semantic_tokens(s: dict) -> dict:
    """Semantic tokens. These override TextMate scopes and are reported by the language server."""
    return {
        "variable":                       s["fg_bright"],
        "variable.readonly":              s["fg_bright"],
        "variable.readonly.defaultLibrary": s["cyan"],
        "parameter":                      s["orange"],

        # Functions: by default yellow (free function calls, hooks, built-ins).
        # Explicit declarations get blue via "function.declaration".
        # This matches the "free function calls → yellow" TextMate rule and
        # automatically catches React hooks (useState, useEffect) since the
        # TS server reports them as plain "function" semantic tokens.
        "function":                       s["yellow"],
        "function.declaration":           s["blue"],
        "function.defaultLibrary":        s["yellow"],

        # Methods always blue (declarations AND calls)
        "method":                         s["blue"],
        "method.defaultLibrary":          s["blue"],
        "method.declaration":             s["blue"],
        "method.static":                  s["blue"],

        # Classes
        "class":                          s["yellow"],
        "class.defaultLibrary":           s["yellow"],

        # Abstract classes → green via modifier
        # IMPORTANT: We use "class.abstract:LANG" instead of "*.abstract:LANG"
        # because in Java, methods declared inside interfaces are technically
        # "abstract" too, and *.abstract would turn them all green.
        "class.abstract":                 s["green"],
        "class.abstract:java":            s["green"],
        "class.abstract:typescript":      s["green"],
        "class.abstract:typescriptreact": s["green"],
        "class.abstract:javascript":      s["green"],

        # ─── Java annotation member overrides ────────────────────────────────
        # The JDT language server doesn't expose a single canonical token for
        # annotation argument names (queues, name, nullable, value...).
        # Depending on the version it may use property, member, enumMember,
        # annotationMember, or method.declaration with various modifiers.
        # We cover all the plausible scopes to maximize chances of catching it.
        "annotationMember":               s["orange"],
        "annotationMember:java":          s["orange"],
        "member:java":                    s["orange"],
        "property.annotation:java":       s["orange"],
        "method.annotation:java":         s["orange"],
        "function.annotation:java":       s["orange"],
        "*.annotation:java":              s["orange"],

        # Interfaces & types
        "interface":                      s["green"],
        "type":                           s["green"],
        "type.defaultLibrary":            s["purple"],
        "typeParameter":                  s["green"],

        # Enums
        "enum":                           s["yellow"],
        "enumMember":                     s["fg_bright"],

        "namespace":                      s["yellow"],
        "property":                       s["fg_bright"],

        "keyword":                        s["purple"],
        "number":                         s["orange"],
        "string":                         s["green"],
        "regexp":                         s["green"],
        "operator":                       s["cyan"],

        "decorator":                      s["purple"],
        "annotation":                     s["purple"],
        "macro":                          s["purple"],

        "comment":                        {"foreground": s["fg_dim"], "italic": True},
        "selfKeyword":                    s["red_strong"],
    }


def build_theme(name: str, variant: dict, syntax: dict, ui_type: str, is_light: bool) -> dict:
    return {
        "$schema": "vscode://schemas/color-theme",
        "name":    name,
        "type":    ui_type,
        "colors":  build_colors(variant, syntax, is_light),
        "tokenColors":          build_token_colors(syntax),
        "semanticHighlighting": True,
        "semanticTokenColors":  build_semantic_tokens(syntax),
    }


def main():
    out_dir = Path(__file__).parent / "themes"
    out_dir.mkdir(exist_ok=True)

    # Build all dark variants
    for key, variant in DARK_VARIANTS.items():
        theme = build_theme(variant["name"], variant, DARK_SYNTAX, "dark", False)
        path = out_dir / f"lusitania-{key}-color-theme.json"
        path.write_text(json.dumps(theme, indent=2, ensure_ascii=False))
        print(f"Wrote {path}")

    # Build the light variant
    theme = build_theme(LIGHT_VARIANT["name"], LIGHT_VARIANT, LIGHT_SYNTAX, "light", True)
    path = out_dir / "lusitania-abyssal-light-color-theme.json"
    path.write_text(json.dumps(theme, indent=2, ensure_ascii=False))
    print(f"Wrote {path}")


if __name__ == "__main__":
    main()
