# Lusitania Theme

[![Version](https://img.shields.io/badge/version-1.0.0-009688.svg)](https://github.com/sahernandezz/lusitania-theme)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

A deep-sea inspired theme for VS Code & Cursor. Named after the RMS Lusitania, the ocean liner that disappeared into the Atlantic depths in 1915.

**Six variants** — five depths of dark plus a light mode. Carefully tuned syntax highlighting for **TypeScript, JavaScript, Java, React** and beyond.

![Lusitania](icon.png)

## Variants

| Variant | Background | Best for |
|---------|-----------|----------|
| **Trench** | `#0a0a0a` (deep black) | Maximum contrast, OLED screens |
| **Midnight** | `#15171c` (soft black) | Long sessions, less eye strain |
| **Abyssal** | `#0d1620` (deep blue) | True oceanic feel |
| **Steel** | `#1c1f26` (grey-blue) | Mid depth, like a ship's hull |
| **Oceanic** | `#263238` (teal charcoal) | Classic Material Oceanic |
| **Surface** | `#fafafa` (light) | Bright environments, daytime work |

Switch via `Cmd/Ctrl+K Cmd/Ctrl+T`.

## Syntax color rules

| Element | Color | Notes |
|---------|-------|-------|
| Concrete classes | yellow | `ChatInput`, `ElementType` |
| **Abstract classes** | green | Same as interfaces — flags abstraction |
| Interfaces | green | |
| Types & generics | green | `Promise<T>`, `HTMLDivElement` |
| Enum type names | yellow | `enum Status` |
| **Enum members** | bright fg | `Status.ACTIVE`, `ElementType.TYPE` |
| **Method declarations & calls** | blue | Always blue, including inside interfaces |
| Function declarations | blue | |
| Free function calls | yellow | `console.log`, helpers |
| **React hooks** | yellow | `useState`, `useEffect`, `useMemo`... always |
| Keywords | purple | `const`, `import`, `new`, `return` |
| **Primitives** | purple italic | `string`, `number`, `boolean`, `int` |
| **`true` / `false` / `null` / `undefined`** | purple | Grouped with keywords |
| Numbers | orange | `42`, `3.14` |
| Parameters | orange | Function parameters |
| Decorators / annotations | purple | `@Builder`, `@Service` |
| **Annotation arg names** | orange | `@Column(name = "id")` → `name` orange |
| Strings | green | |
| Operators / punctuation | cyan | |
| JSX tags | red | `<div>`, `<nav>` |
| JSX components | yellow | `<ChatInput>` |
| **JSX attributes** | orange italic | `value`, `onChange` — distinct from component |

## Install

### From a `.vsix` file

```bash
# VS Code
code --install-extension lusitania-theme-1.0.0.vsix

# Cursor
cursor --install-extension lusitania-theme-1.0.0.vsix
```

Then pick a variant from `Cmd/Ctrl+K Cmd/Ctrl+T`.

### From the marketplace

Once published:

```bash
code --install-extension sahernandezz.lusitania-theme
```

## Building from source

```bash
git clone https://github.com/sahernandezz/lusitania-theme.git
cd lusitania-theme
python3 build.py   # regenerates the JSON theme files
```

## Publishing to the VS Code Marketplace

If you fork this and want to publish your own version, see the [publishing guide](PUBLISHING.md).

## Contributing

Issues and PRs welcome. If a token highlights weirdly in your language, open an issue with a screenshot and the language; the scope rules are easy to extend.

## License

MIT — see [LICENSE](LICENSE).

## Credits

Inspired by Material Theme's Oceanic palette and the Cursor Dark UI. Built and maintained by [@sahernandezz](https://github.com/sahernandezz).
