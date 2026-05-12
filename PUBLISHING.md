# Publishing to the VS Code Marketplace

This guide covers how to publish `lusitania-theme` to the VS Code Marketplace using `vsce`.

## Prerequisites

- Node.js 18+
- A Microsoft account
- An Azure DevOps organization (free)
- A Personal Access Token (PAT) with **Marketplace > Manage** scope

## One-time setup

### 1. Install `vsce`

```bash
npm install -g @vscode/vsce
```

### 2. Create a publisher

A publisher is your marketplace identity. The `publisher` field in `package.json` must match the publisher ID you create here.

1. Go to https://marketplace.visualstudio.com/manage
2. Sign in with your Microsoft account
3. Click **Create publisher**
4. Use `sahernandezz` as the ID (this must match `package.json`)
5. Fill in the display name and (optionally) website

### 3. Get a Personal Access Token

1. Go to https://dev.azure.com/
2. Click your avatar → **Personal Access Tokens**
3. **New Token**:
   - Organization: **All accessible organizations**
   - Expiration: choose what fits you
   - Scopes: **Custom defined** → check **Marketplace > Manage**
4. Copy the token (it's only shown once)

### 4. Login

```bash
vsce login sahernandezz
# paste the PAT when prompted
```

## Publishing

### First publish

```bash
# from the repo root
vsce publish
```

Or specify the version explicitly:

```bash
vsce publish 1.0.0
```

### Publishing a new version

Bump the version in `package.json`, then:

```bash
vsce publish patch    # 1.0.0 -> 1.0.1
vsce publish minor    # 1.0.0 -> 1.1.0
vsce publish major    # 1.0.0 -> 2.0.0
```

After publishing, the extension is live at:
`https://marketplace.visualstudio.com/items?itemName=sahernandezz.lusitania-theme`

## Packaging without publishing

To build the `.vsix` file locally (for testing or distribution outside the marketplace):

```bash
vsce package
```

This produces `lusitania-theme-<version>.vsix` which can be installed with:

```bash
code --install-extension lusitania-theme-1.0.0.vsix
```

## Notes on the Open VSX Registry

If you also want Cursor / VSCodium / Gitpod users to find the theme through their default marketplace, publish to [Open VSX](https://open-vsx.org/) as well.

```bash
npm install -g ovsx
ovsx create-namespace sahernandezz -p <openvsx-token>
ovsx publish lusitania-theme-1.0.0.vsix -p <openvsx-token>
```

Get an Open VSX token at https://open-vsx.org/user-settings/tokens.

## Common issues

**"ERROR Make sure to edit the README.md file before you package"** — Open `README.md` and remove any leftover placeholder text from the template. We've already done this, but `vsce` is strict.

**"Missing publisher name"** — `package.json` is missing the `publisher` field. Should be `sahernandezz`.

**"Make sure to edit the LICENSE"** — same family of error. Ensure `LICENSE` exists and is the MIT text (it is).

**Icon too small** — VS Code wants at least 128x128 PNG. Our `icon.png` is 256x256.
