<div align="center">

<img src="icon.png" alt="Lusitania" width="160" height="160" />

# Lusitania Theme

**A deep-sea theme for VS Code & Cursor.**
Abyssal blue. Teal currents. Eight depths.

[![Version](https://img.shields.io/badge/version-1.1.0-7fd4d4?style=flat-square)](https://github.com/sahernandezz/lusitania-theme)
[![License](https://img.shields.io/badge/license-MIT-7fd4d4?style=flat-square)](LICENSE.txt)
[![VS Code](https://img.shields.io/badge/VS%20Code-1.70+-7fd4d4?style=flat-square&logo=visualstudiocode&logoColor=white)](https://code.visualstudio.com/)

</div>

---

## The theme

Named after the RMS Lusitania, the ocean liner that disappeared into the Atlantic depths in 1915. Built on a deep oceanic palette — abyssal blue backgrounds, teal accents, syntax tuned for long sessions.

### Variants

Six dark depths and two lights. **Abyssal** is the canonical one.

| | Name | Background | Use it when |
|---|---|---|---|
| ![#0a0a0a](https://img.shields.io/badge/-%20-0a0a0a?style=flat-square) | **Trench** | `#0a0a0a` | Maximum contrast, OLED screens. |
| ![#15171c](https://img.shields.io/badge/-%20-15171c?style=flat-square) | **Midnight** | `#15171c` | Soft black, long sessions, less eye strain. |
| ![#0d1620](https://img.shields.io/badge/-%20-0d1620?style=flat-square) | **Abyssal** ★ | `#0d1620` | The canonical theme. Deep oceanic blue. |
| ![#0a0d14](https://img.shields.io/badge/-%20-0a0d14?style=flat-square) | **Abyssal Deep** *(new)* | `#0a0d14` | Darker, dramatic. Matches the icon. |
| ![#1c1f26](https://img.shields.io/badge/-%20-1c1f26?style=flat-square) | **Steel** | `#1c1f26` | Mid depth, grey-blue like a ship's hull. |
| ![#263238](https://img.shields.io/badge/-%20-263238?style=flat-square) | **Oceanic** | `#263238` | Classic Material Oceanic. |
| ![#fafafa](https://img.shields.io/badge/-%20-fafafa?style=flat-square) | **Surface** | `#fafafa` | Light, neutral. Bright environments. |
| ![#f4f7f9](https://img.shields.io/badge/-%20-f4f7f9?style=flat-square) | **Abyssal Light** *(new)* | `#f4f7f9` | Light with a subtle blue-green tint. |

Switch with `Cmd/Ctrl+K Cmd/Ctrl+T`.

---

## See it in action

Each language is shown in a different variant so you can compare the three.

### TypeScript / React — *Abyssal*

<p align="center"><img src="previews/typescript.png" alt="TypeScript & React in Abyssal" width="720" /></p>

### Java + Spring annotations — *Abyssal Deep*

<p align="center"><img src="previews/java.png" alt="Java with Spring annotations in Abyssal Deep" width="720" /></p>

### SQL — *Abyssal Light*

<p align="center"><img src="previews/sql.png" alt="SQL in Abyssal Light" width="720" /></p>

---

## Syntax rules at a glance

| Element | Color | Example |
|---|---|---|
| Keywords | purple | `const`, `import`, `class`, `SELECT` |
| Strings | green | `'hello'`, `"world"` |
| Numbers | orange | `42`, `3.14` |
| Methods | blue | `.toString()`, `onMessage()` |
| Free functions / hooks | yellow | `console.log`, `useState`, `COUNT()` |
| Classes / enums | yellow | `ChatInput`, `Status` |
| Interfaces / types / abstract | green | `User`, `Promise<T>`, `abstract class` |
| JSX tags | red | `<div>`, `<ChatInput>` |
| JSX attrs | yellow italic | `value`, `onChange` |
| Parameters | orange | function args |
| Annotations | purple | `@Service`, `@RabbitListener` |
| Annotation arg names | orange | `queues = ...` |
| SQL tables | yellow | `customers`, `orders` |
| SQL columns | bright | `customer_id`, `total` |
| Comments | dim italic | `// ...`, `-- ...` |
