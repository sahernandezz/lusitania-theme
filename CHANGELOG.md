# Changelog

All notable changes to **Lusitania Theme** are documented here.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.1.0] — 2026-05-17

### Changed
- **Curated variants**: now ships 3 focused variants instead of 6.
  - **Abyssal** (`#0d1620`) — the canonical deep-blue oceanic theme.
  - **Abyssal Deep** (`#0a0d14`) — darker, dramatic, matches the new icon.
  - **Abyssal Light** (`#f4f7f9`) — light variant with the same deep-sea palette spirit.
- **New icon** — modern brand mark (Lusitania mono) replacing the previous Tide Brackets logo.
- **Brand teal** (`#7fd4d4`) is now the single accent across UI: cursor, focus ring,
  active line numbers, button background, status bar accents.
- README rewritten as a visual showcase with code previews (TS/React, Java, SQL).
- Gallery banner color updated to match the new icon background.

### Added
- **SQL syntax tuning** — dedicated rules for SQL grammars:
  - DML/DDL keywords (`SELECT`, `FROM`, `WHERE`, `CREATE`...) → purple.
  - Built-in functions (`COUNT`, `SUM`, `NOW`, `COALESCE`...) → yellow.
  - Table / schema identifiers → yellow.
  - Column identifiers → bright foreground.
  - Aliases → green.
  - Logical / comparison operators (`AND`, `OR`, `IN`, `BETWEEN`...) → cyan.
  - Data types (`INT`, `VARCHAR`, `TIMESTAMP`...) → purple italic.
  - Bind variables (`:id`, `$1`, `?`) → orange.

### Removed
- Trench, Midnight, Steel, Oceanic, and Surface variants — replaced by the focused
  Abyssal trio. If you need them, install v1.0.0.

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
