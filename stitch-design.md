---
name: High-Trust Multi-Category Rental System
colors:
  surface: '#faf8ff'
  surface-dim: '#d2d9f4'
  surface-bright: '#faf8ff'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f2f3ff'
  surface-container: '#eaedff'
  surface-container-high: '#e2e7ff'
  surface-container-highest: '#dae2fd'
  on-surface: '#131b2e'
  on-surface-variant: '#434653'
  inverse-surface: '#283044'
  inverse-on-surface: '#eef0ff'
  outline: '#737784'
  outline-variant: '#c3c6d5'
  surface-tint: '#1d59c1'
  primary: '#003c90'
  on-primary: '#ffffff'
  primary-container: '#0f52ba'
  on-primary-container: '#bcceff'
  inverse-primary: '#b0c6ff'
  secondary: '#00677d'
  on-secondary: '#ffffff'
  secondary-container: '#50d9fe'
  on-secondary-container: '#005c70'
  tertiary: '#2c16c6'
  on-tertiary: '#ffffff'
  tertiary-container: '#463cdd'
  on-tertiary-container: '#ccc9ff'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#d9e2ff'
  primary-fixed-dim: '#b0c6ff'
  on-primary-fixed: '#001945'
  on-primary-fixed-variant: '#00419c'
  secondary-fixed: '#b3ebff'
  secondary-fixed-dim: '#4cd6fb'
  on-secondary-fixed: '#001f27'
  on-secondary-fixed-variant: '#004e5f'
  tertiary-fixed: '#e2dfff'
  tertiary-fixed-dim: '#c3c0ff'
  on-tertiary-fixed: '#0f0069'
  on-tertiary-fixed-variant: '#3323cc'
  background: '#faf8ff'
  on-background: '#131b2e'
  surface-variant: '#dae2fd'
  brand-primary-hover: '#0B3C8A'
  brand-primary-light: '#EBF3FF'
  trust-verified: '#059669'
  trust-verified-bg: '#ECFDF5'
  trust-warning: '#D97706'
  trust-warning-bg: '#FFFBEB'
  trust-danger: '#DC2626'
  trust-danger-bg: '#FEF2F2'
  canvas-slate: '#F8FAFC'
  surface-card: '#FFFFFF'
  surface-subtle: '#F1F5F9'
  border-default: '#E2E8F0'
  border-focus: '#3B82F6'
  text-secondary: '#475569'
  text-muted: '#94A3B8'
typography:
  display-hero:
    fontFamily: Inter
    fontSize: 40px
    fontWeight: '800'
    lineHeight: 48px
    letterSpacing: -0.02em
  display-hero-mobile:
    fontFamily: Inter
    fontSize: 30px
    fontWeight: '800'
    lineHeight: 38px
    letterSpacing: -0.015em
  headline-lg:
    fontFamily: Inter
    fontSize: 32px
    fontWeight: '700'
    lineHeight: 40px
    letterSpacing: -0.01em
  headline-lg-mobile:
    fontFamily: Inter
    fontSize: 24px
    fontWeight: '700'
    lineHeight: 32px
    letterSpacing: -0.01em
  headline-md:
    fontFamily: Inter
    fontSize: 24px
    fontWeight: '700'
    lineHeight: 32px
  headline-sm:
    fontFamily: Inter
    fontSize: 20px
    fontWeight: '600'
    lineHeight: 28px
  body-lg:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '500'
    lineHeight: 24px
  body-base:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '400'
    lineHeight: 20px
  body-base-medium:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '500'
    lineHeight: 20px
  caption:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '400'
    lineHeight: 16px
  caption-bold:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '600'
    lineHeight: 16px
  code-mono:
    fontFamily: JetBrains Mono
    fontSize: 14px
    fontWeight: '600'
    lineHeight: 20px
    letterSpacing: 0.05em
  code-mono-sm:
    fontFamily: JetBrains Mono
    fontSize: 12px
    fontWeight: '500'
    lineHeight: 16px
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  gutter: 1rem
  gutter-tablet: 1.5rem
  gutter-desktop: 2rem
  margin: 1rem
  margin-tablet: 2rem
  margin-desktop: 3rem
  space-xs: 0.25rem
  space-sm: 0.5rem
  space-md: 1rem
  space-lg: 1.5rem
  space-xl: 2rem
---

## Brand & Style

This design system establishes an institutional, defensive, and rigorously transparent visual language tailored for high-value peer-to-peer and B2C equipment, mobility, and property rentals. The overarching brand identity balances technical authority with seamless transactional ease. Every interface element communicates fiscal protection, mechanical condition guarantees, and legal accountability.

The style operates at the intersection of **Corporate Modern** and **Tactile Utility**. High-contrast slate neutrals paired with crisp white surfaces eliminate decorative ambiguity, while dedicated chromatic signifiers (Sapphire Blue for commerce, Emerald for physical verification, and Escrow Indigo for financial custody) ensure immediate cognitive clarity. The aesthetic emphasizes high-density clarity over minimalism, prioritizing visible evidence: clear price breakdowns, side-by-side condition records, live telemetry status, and overt security guarantees.

## Colors

The color architecture is built around functional trust zones. Chromatic colors are strictly reserved for state identification, brand CTAs, and ledger transparency, avoiding aesthetic overuse.

### Role Assignments
- **Primary (`#0F52BA` - Sapphire / Royal Blue)**: Powers primary transactional calls to action, active navigation tabs, active calendar selections, and core system accents.
- **Secondary (`#00B4D8` - Teal Accent)**: Reserved for real-time telemetry indicators, live availability badges, live tracker pins, and visual highlights.
- **Tertiary (`#4F46E5` - Escrow Indigo)**: Exclusively governs the financial architecture—vault holds, security deposit guarantees, automated releases, and insurance protection tiers.
- **Neutral (`#0F172A` - Slate 900)**: Serves as the high-contrast baseline for typography, iconography, and deep ambient elevations.

### Surface and Semantic Usage
- Use canvas background `canvas-slate` (`#F8FAFC`) to ground interfaces, reserving pure white (`#FFFFFF`) for structural cards and dialog containers.
- Statuses must pair their solid stroke/icon tokens (`trust-verified`, `trust-warning`, `trust-danger`) with corresponding 50-tint backgrounds (`trust-verified-bg`, `trust-warning-bg`, `trust-danger-bg`) to maintain accessible 4.5:1 text-to-background ratios.
- Avoid using arbitrary gray scales; all sub-elements, dividers, and disabled states must map directly to the defined Slate family tokens (`#E2E8F0`, `#F1F5F9`, `#94A3B8`, `#475569`).

## Typography

The typographic hierarchy enforces structural legibility and auditability across complex legal, financial, and product data:

- **Primary Stack (`Inter`)**: Drives display, headline, and regular body copy. Negative letter tracking is applied strictly to display sizes (`-0.02em` on `display-hero`) to condense punchy headings without sacrificing clarity.
- **Monospace Stack (`JetBrains Mono`)**: Mandated for all legally binding identifiers, cryptographic validation tokens, OTP entry fields, asset serial numbers, geo-coordinate readouts, and currency breakdown amounts in the checkout engine. This prevents glyph confusion (e.g., zero vs. capital O).
- **Scale Applications**: Tabular data cells and standard field values default to `body-base` (`14px/20px`). `caption-bold` (`12px/16px`) is applied to pill indicators, guarantee labels, and metadata markers.

## Layout & Spacing

The layout model operates on an 8-point structural framework with a 4-point micro-scale for component internals.

### Grid & Viewport Transitions
- **Desktop (1024px and above)**: 12-column fluid grid, `2rem` (32px) gutters, and `3rem` (48px) margins. Used to host side-by-side inspector canvases, split escrow workflows, and fixed right-hand rental calculators. Max canvas containment sits at 1280px.
- **Tablet (640px to 1023px)**: 8-column fluid grid, `1.5rem` (24px) gutters, and `2rem` (32px) margins. Rental items collapse to a 2-column matrix; filters move into full-height sliding drawer surfaces.
- **Mobile (< 640px)**: 4-column grid, `1rem` (16px) gutters, and `1rem` (16px) margins. Booking breakdown panels become persistent bottom fixed bars (with safe-area insets). Inspection comparisons adapt to vertical stacked cards.

### Spacing Application
- Use `space-xs` (4px) and `space-sm` (8px) for badge internals, inline rating lockups, and compact cell groupings.
- Use `space-md` (16px) for form group gaps, standard card interior padding, and listing spec listings.
- Use `space-lg` (24px) and `space-xl` (32px) for card container separations, modal interior paddings, and verification section transitions.

## Elevation & Depth

Visual hierarchy uses slate-tinted ambient shadows and crisp perimeter boundaries to convey durability and transactional confidence. Blur radiuses are kept restrained, paired with explicit 1px outline definitions.

### Depth Hierarchy
1. **Canvas Baseline (0dp)**: Rendered in `canvas-slate` (`#F8FAFC`). Flat background with zero elevation.
2. **Resting Cards & Interactive Elements (Level 1)**: Pure white background enclosed by a `1px solid #E2E8F0` frame, supported by `0 1px 3px rgba(15, 23, 42, 0.05), 0 1px 2px rgba(15, 23, 42, 0.02)`. Used for listing cards, inactive filters, and data tables.
3. **Interactive Hover & Selectable Modules (Level 2)**: Elevated to `0 4px 6px -1px rgba(15, 23, 42, 0.08), 0 2px 4px -2px rgba(15, 23, 42, 0.04)`. Applied to active date pickers, hovered asset cards, and expanded escrow line items.
4. **Modals, Floating Checkouts, and Overlays (Level 3)**: Structured with `0 12px 24px -4px rgba(15, 23, 42, 0.12), 0 4px 6px -2px rgba(15, 23, 42, 0.05)`. Applied to inspection photo sliders, floating summary drawers, dispute resolution sidebars, and critical verification prompts.

Avoid pure-black drop shadows (`rgba(0, 0, 0, ...)`); always tint ambient drop-offs with Slate 900 (`rgba(15, 23, 42, ...)`).

## Shapes

The design system implements a **Rounded (Level 2)** shape strategy. Curves are engineered to soften high-density data without losing the structured appearance of an authoritative financial and operational platform.

- **Base Corner Radius (`0.5rem` / 8px - 10px)**: Applied to all primary interactive elements: inputs, standard action buttons, selector dropdowns, and tabular action cells.
- **Large Corner Radius (`rounded-lg`, `1rem` / 16px)**: Applied to product presentation cards, modal containers, interactive calendars, condition report panels, and escrow breakdown summaries.
- **Full Radius (`9999px`)**: Reserved exclusively for pill verification badges, category filter chips, avatar crops, and live status beacon dots.

## Components

### Verification Badges & Pill Chips
- **Physical Verification**: Constructed with a solid `trust-verified` (`#059669`) shield icon, `12px` semibold Inter label, encased in `trust-verified-bg` (`#ECFDF5`) with a `1px solid rgba(5, 150, 105, 0.2)` border. Full pill radius (`9999px`).
- **KYC Identity Badges**: Sapphire primary fill tint (`#EBF3FF`), `#0F52BA` icon, and text with `1px solid rgba(15, 82, 186, 0.2)`.
- **Category Filter Chips**: Height 36px, `0.5rem` roundedness or pill-shaped, base background `#FFFFFF` with `1px solid #E2E8F0`. When active: `#0F52BA` background, white text, and zero outline blur.

### Trust Score Gauge (0–100)
- Segmented radial or horizontal progress track with a 4-tier visual boundary:
  - `85–100` (Tier 1): `#059669` (Platinum Green)
  - `70–84` (Tier 2): `#0F52BA` (Gold Blue)
  - `50–69` (Tier 3): `#D97706` (Neutral Amber)
  - `<50` (Tier 4): `#DC2626` (Critical Red)
- Score number rendered in `JetBrains Mono` bold; sub-caption explains dispute-free rental history.

### Escrow & Deposit Breakdown Module
- Inset card with `surface-subtle` (`#F1F5F9`) header detailing "Escrow Shield Protected." 
- Features an `#4F46E5` icon flag.
- Line items (Rental Rate, Deposit Hold, Insurance, Platform Fee) formatted in `body-base`. All monetary figures aligned right and typeset in `JetBrains Mono`.
- Explicit legal note detailing automatic fund release timeline placed at the base in `caption` with a subdued lock icon.

### Form Inputs & OTP Verification Cells
- Standard inputs: 44px minimum touch height, `radius-md` (10px), filled with `#FFFFFF`, bordered by `1px solid #E2E8F0`. Focus state replaces border with `2px solid #3B82F6` and adds an ambient focus ring (`0 0 0 3px rgba(59, 130, 246, 0.15)`).
- OTP Matrix: 6 discrete single-character input boxes (48px x 56px), centered typography using `code-mono` (`14px/20px`), auto-advancing on input, shifting to `#0F52BA` border on active focus.

### Buttons & Interactive CTAs
- **Primary CTA**: Solid Sapphire Blue (`#0F52BA`), white text, `radius-md` (10px), padding `12px 24px`. Hover shifts to `#0B3C8A`. Active states depress by 1px.
- **Escrow / Secure Action**: Solid Indigo (`#4F46E5`), used for instant reserve and deposit confirmation triggers.
- **Secondary / Outline**: Pure white background, `1px solid #E2E8F0`, slate 900 text. Hover activates `#F8FAFC`.

### Checkboxes, Radios, and Toggles
- Checkboxes: 18px x 18px, `4px` radius. Active state filled with `#0F52BA` displaying a crisp white check vector.
- Radios: 18px circular, with a centered 8px solid sapphire dot when selected.
- Switches: 44px track with a 20px sliding pill, transitioning from `#E2E8F0` (inactive) to `#059669` (active/verified features).

### Side-by-Side Condition Inspection Slider
- Split container divided by a draggable 2px `#FFFFFF` vertical rule with a central circular grip handle (`32px`, elevated with `shadow-card`).
- Pre-rental check-in photo locked to left canvas; check-out condition locked to right canvas.
- Integrated `2x` loupe magnifying tool anchored to cursor hover for immediate micro-scratch and damage validation.