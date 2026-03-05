# TESSLATE.md - Project Context

## Framework Configuration

**Framework**: Vite + React
**Version**: React 18
**Port**: 5173

**Tech Stack:**
- React 18 with Vite
- Tailwind CSS
- React Router DOM v6 (pre-configured in `src/App.jsx`)

**Directory Structure:**
- Entry point: `src/main.jsx`
- Root component: `src/App.jsx`
- All source files live under `src/`

---

## IMPORTANT: Framework-specific file locations

### If this is a Next.js project (has `next.config.js` or `"next"` in package.json)

**CRITICAL: File Location Rules — READ BEFORE WRITING ANY FILE**

| File type | Correct location | Example |
|-----------|-----------------|---------|
| Pages / routes | `app/{route}/page.tsx` | `app/dashboard/page.tsx` |
| Root layout | `app/layout.tsx` | — |
| Global styles | `app/globals.css` | — |
| API routes | `app/api/{name}/route.ts` | `app/api/users/route.ts` |
| Shared components | `components/{Name}.tsx` | `components/Button.tsx` |
| React context providers | `contexts/{Name}.tsx` | `contexts/AuthContext.tsx` |
| TypeScript types/interfaces | `types/{name}.ts` | `types/user.ts` |
| Utility / helper functions | `lib/{name}.ts` | `lib/utils.ts` |
| Custom React hooks | `hooks/use{Name}.ts` | `hooks/useAuth.ts` |

- `components/`, `contexts/`, `types/`, `lib/`, `hooks/` are at the **project root**, NOT inside `src/`
- **NEVER create a `src/` directory** — this is not a Vite project

### If this is a Vite + React project (has `vite.config.js`)

- All source files go under `src/`
- Main entry: `src/main.jsx`, root component: `src/App.jsx`
- Components: `src/components/`, utilities: `src/lib/`, hooks: `src/hooks/`

---

## Development Server

**Start Command**:
```bash
npm install
npm run dev -- --host 0.0.0.0 --port 5173
```

**Production Build:**
```bash
npm run build
```
