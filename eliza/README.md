# Eliza

An AI-powered movie recommendation chatbot built with Next.js 16, React 19, and Tailwind CSS 4.

## Stack

- **Framework**: Next.js 16 (App Router, Turbopack)
- **UI**: React 19, Tailwind CSS 4, Radix UI, Remixicon
- **Package manager**: Bun
- **Language**: TypeScript

## Dependencies

### Production
| Package | Version | Usage |
|---|---|---|
| `next` | 16.2.2 | React framework (App Router, SSR, routing) |
| `react` | 19.2.4 | UI library |
| `react-dom` | 19.2.4 | DOM rendering for React |
| `@radix-ui/react-avatar` | ^1.1.11 | Accessible avatar component (profile page) |
| `@radix-ui/react-tooltip` | ^1.2.8 | Accessible tooltip component |
| `@remixicon/react` | ^4.9.0 | Icon library |

### Dev / Build
| Package | Usage |
|---|---|
| `tailwindcss` ^4 | Utility-first CSS framework |
| `@tailwindcss/postcss` ^4 | PostCSS plugin for Tailwind |
| `typescript` ^5 | Static typing |
| `@types/node`, `@types/react`, `@types/react-dom` | TypeScript type definitions |
| `eslint` ^9 + `eslint-config-next` | Linting |

## Project structure

```
app/
  page.tsx            # Landing page
  chatbot/page.tsx    # Chatbot interface
  profile/page.tsx    # User profile
  layout.tsx          # Root layout
  globals.css         # Global styles (Tailwind)

components/
  landing/            # Landing page sections
    Header.tsx
    Features.tsx
    HowItWorks.tsx
    Demo.tsx
    Results.tsx
    Footer.tsx
    Divider.tsx
  chatbot/            # Chat UI
    ChatBubble.tsx
    ChatHeader.tsx
    FilmCard.tsx
  profile/
    Profile.tsx
  Navbar.tsx
```

## Setup from scratch (how this project was initialised)

If you want to recreate this stack from zero:

```bash
# Create a Next.js project (includes React, TypeScript, ESLint, Tailwind, App Router)
bunx create-next-app@latest eliza \
  --typescript \
  --tailwind \
  --eslint \
  --app \
  --turbopack \
  --src-dir=false \
  --import-alias "@/*"

cd eliza

# Add Radix UI components
bun add @radix-ui/react-avatar @radix-ui/react-tooltip

# Add icon library
bun add @remixicon/react
```

> `create-next-app` automatically installs `react`, `react-dom`, `next`, `tailwindcss`, `typescript` and their type definitions.

---

## Prerequisites

Install [Bun](https://bun.sh) if you don't have it:

```bash
curl -fsSL https://bun.sh/install | bash
```

> Node.js (>=18) also works as an alternative with `npm` or `yarn`, but this project is optimised for Bun.

## Getting started

```bash
# 1. Clone the repo
git clone <repo-url>
cd eliza

# 2. Install dependencies
bun install

# 3. Start the dev server (Turbopack)
bun dev
```

Open [http://localhost:3000](http://localhost:3000).

## All commands

```bash
bun dev           # Start development server with Turbopack (hot reload)
bun run build     # Build for production
bun run start     # Start the production server (run build first)
bun run lint      # Run ESLint across the project
```

### With npm (alternative)

```bash
npm install
npm run dev
npm run build
npm run start
npm run lint
```
