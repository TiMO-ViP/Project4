---
name: Enterprise Prestige Dark
colors:
  primary: "#edd300"
  primary-hover: "#d4bd00"
  secondary: "#1f1f1f"
  surface: "#0a0a0a"
  card: "#141414"
  card-border: "#262626"
  text-main: "#edd300"
  text-muted: "#a3a3a3"
  text-body: "#e5e5e5"
  error: "#ef4444"
  success: "#22c55e"
typography:
  h1:
    fontFamily: "system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: "36px"
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: "-0.02em"
  h2:
    fontFamily: "system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: "20px"
    fontWeight: 600
    lineHeight: 1.3
  body-md:
    fontFamily: "system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: "14px"
    fontWeight: 400
    lineHeight: 1.6
rounded:
  sm: "4px"
  md: "8px"
  lg: "12px"
spacing:
  xs: "4px"
  sm: "8px"
  md: "16px"
  lg: "24px"
  xl: "32px"
components:
  card:
    backgroundColor: "{colors.card}"
    rounded: "{rounded.md}"
    padding: "24px"
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.surface}"
    rounded: "{rounded.sm}"
    padding: "10px 18px"
---

# Enterprise Prestige Dark

## Overview
A high-contrast, function-driven dark design system tailored for enterprise platform applications (Next.js 16, Supabase, Drizzle ORM). Built with WCAG AAA accessibility standards, crisp visual hierarchy, and zero decorative fluff.

## Colors
- **Primary Amber-Gold (`#edd300`)**: Core brand accent for key interactive focus and main titles.
- **Surface Dark (`#0a0a0a`)**: Deep charcoal background providing maximum visual comfort.
- **Card Container (`#141414`)**: Subdued container surface paired with crisp `#262626` structural borders.
- **Muted Text (`#a3a3a3`)**: High legibility secondary copy.

## Typography
- System Sans-Serif font stack with strict line heights and tracking to guarantee instant scanning.

## Do's and Don'ts
- **DO** use exact token references (`var(--primary)`, `var(--card)`) defined in `src/app/globals.css`.
- **DON'T** use purple or violet accents on dark backgrounds (Forbidden Cliché).
- **DON'T** use gradient keywords or headline biscuit pills.
- **DO** keep touch targets > 44px for accessible mobile interaction.
