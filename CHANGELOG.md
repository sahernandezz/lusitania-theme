# Changelog

All notable changes to **Lusitania Theme** are documented here.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

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
