# Changelog

All notable changes to **Lusitania Theme** are documented here.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.1.1] — 2026-05-20

### Changed
- Re-framed the theme as language-agnostic in `package.json` description,
  marketplace keywords and README. The previous wording said it was *"tuned
  for TypeScript, Java, React and SQL"* — those grammars receive dedicated
  syntax rules, but every language VS Code knows about is themed. The
  preview screenshots are now labelled as *illustrative, not prescriptive*.
- Repository hygiene: dropped `.claude/`, `.DS_Store` and intermediate
  preview SVGs from the tree; hardened `.gitignore` / `.vscodeignore` with
  patterns for secrets, lockfiles and editor metadata. README gained
  Install, Pairs-well-with, Security, Build and License sections so it
  stands alone on the marketplace.
- Pairs with the new [Lusitania Icon Theme](https://github.com/sahernandezz/lusitania-icon-theme)
  for matching file & folder icons.

### Notes
- No colour or syntax-rule changes. Existing setups upgrade transparently.

## [1.1.0] — 2026-05-17

### Added
- **Two new variants** added alongside the existing six:
  - **Abyssal Deep** (`#0a0d14`) — darker, more dramatic. Matches the new icon
    background. For OLED screens and the deepest possible feel.
  - **Abyssal Light** (`#f4f7f9`) — light variant with a subtle blue-green
    tinted chrome that ties it back to the Abyssal family. Uses the same
    light syntax palette as Surface.
- **New icon** — modern brand mark (Lusitania mono) replacing the previous
  Tide Brackets logo.
- **SQL syntax tuning** — dedicated rules for SQL grammars:
  - DML/DDL keywords (`SELECT`, `FROM`, `WHERE`, `CREATE`...) → purple.
  - Built-in functions (`COUNT`, `SUM`, `NOW`, `COALESCE`...) → yellow.
  - Table / schema identifiers → yellow.
  - Column identifiers → bright foreground.
  - Aliases → green.
  - Logical / comparison operators (`AND`, `OR`, `IN`, `BETWEEN`...) → cyan.
  - Data types (`INT`, `VARCHAR`, `TIMESTAMP`...) → purple italic.
  - Bind variables (`:id`, `$1`, `?`) → orange.
- **Visual README** — rewritten as a showcase with PNG previews of TS/React
  (in Abyssal), Java + Spring (in Abyssal Deep), and SQL (in Abyssal Light).
- `build_previews.py` — generates the SVG mockups and PNGs from a shared
  palette, kept in sync with `build.py` via direct imports.

### Notes
- All existing variants (Trench, Midnight, Abyssal, Steel, Oceanic, Surface)
  and all existing syntax colors are preserved unchanged.

## [1.0.0] — 2026-05-12

### Added
- Six variants:
  - **Trench** (`#0a0a0a`) — deep black
  - **Midnight** (`#15171c`) — soft black
  - **Abyssal** (`#0d1620`) — deep blue
  - **Steel** (`#1c1f26`) — grey-blue
  - **Oceanic** (`#263238`) — classic Material Oceanic
  - **Surface** (`#fafafa`) — light mode
- Tide Brackets logo.
- Semantic highlighting for JS/TS/Java/React:
  - Concrete classes → yellow
  - Abstract classes → green (same as interfaces)
  - Interfaces, types, generics → green
  - Enum type names → yellow
  - Enum members → bright foreground
  - Method declarations & calls → blue (including inside interfaces)
  - Free function calls and React hooks (useState, useEffect...) → yellow
  - Function declarations → blue
  - JSX/HTML tags (elements AND components) → red, IntelliJ-style
  - JSX/HTML attributes → yellow italic
  - Keywords → purple
  - Primitives (string, number, boolean, void...) → purple italic
  - true / false / null / undefined → purple
  - Numbers, parameters → orange
  - Java annotation argument names (@Column(name = "id")) → orange
  - Strings → green
  - Operators, punctuation → cyan
  - Constructors after `new` keep class color (yellow)
- MIT license.
