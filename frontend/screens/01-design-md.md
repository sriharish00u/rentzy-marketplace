# UI/UX Design Specification & Architecture (`design.md`)
**Project:** All-in-One Multi-Category Rental Marketplace  
**Version:** 1.0.0  
**Target Platform:** Web Application (Responsive Desktop, Tablet, and Mobile-first layouts)  
**Document Purpose:** Complete, exhaustive design specification covering Design System Tokens, Information Architecture, Wireframe Layouts, Component States, User Flows, and Page-by-Page UI/UX specs across all 44 Platform Pages (Customer, Owner, Admin, and Common).

---

## 1. Design System & Visual Foundation

### 1.1 Color Palette & Token Architecture
The visual system projects **trust, security, clarity, and modern utility**.

```scss
// Primary Brand & Identity (Trust & Action)
$color-brand-primary:      #0F52BA; // Sapphire / Royal Blue (Primary CTA, links, brand active)
$color-brand-primary-hover:#0B3C8A;
$color-brand-primary-light:#EBF3FF; // Tints for badges, selection backgrounds
$color-brand-accent:       #00B4D8; // Teal highlight (Accents, live indicators)

// Verification & Trust Badges (Crucial Marketplace Signals)
$color-trust-verified:     #059669; // Emerald Green (Product Verified, KYC Approved)
$color-trust-verified-bg:  #ECFDF5;
$color-trust-shield:       #4F46E5; // Indigo (Platform Protection / Escrow badge)
$color-trust-warning:      #D97706; // Amber (Pending Verification, Uninspected)
$color-trust-warning-bg:   #FFFBEB;
$color-trust-danger:       #DC2626; // Crimson (Dispute, Damage, Flagged)
$color-trust-danger-bg:    #FEF2F2;

// Neutral Surface & Typography
$color-bg-canvas:          #F8FAFC; // Slate 50 (App background)
$color-bg-surface:         #FFFFFF; // Pure White (Cards, modals, data tables)
$color-bg-subtle:          #F1F5F9; // Slate 100 (Input fills, table headers, dividers)
$color-border-default:     #E2E8F0; // Slate 200
$color-border-focus:       #3B82F6; // Blue 500

// Text Hierarchy
$color-text-primary:       #0F172A; // Slate 900 (High contrast headlines, primary labels)
$color-text-secondary:     #475569; // Slate 600 (Body copy, subtitles, metadata)
$color-text-muted:         #94A3B8; // Slate 400 (Placeholders, inactive tabs, timestamps)
$color-text-inverted:      #FFFFFF;
```

### 1.2 Typography Hierarchy
- **Font Family:** Inter, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif
- **Monospace Family (for OTPs, Tracking IDs, Serial Numbers, Coordinates):** JetBrains Mono, SF Mono, Menlo, monospace

| Scale Token | Font Size | Line Height | Weight | Usage |
|---|---|---|---|---|
| `display-1` | 40px / 2.5rem | 48px | 800 (Extrabold) | Landing Hero Headline |
| `h1` | 32px / 2.0rem | 40px | 700 (Bold) | Dashboard & Core Page Titles |
| `h2` | 24px / 1.5rem | 32px | 700 (Bold) | Section Headers, Product Titles |
| `h3` | 20px / 1.25rem | 28px | 600 (Semibold) | Modal Titles, Card Headings |
| `body-lg` | 16px / 1.0rem | 24px | 500 (Medium) | Emphasized Body, Form Labels |
| `body-base` | 14px / 0.875rem | 20px | 400 / 500 | Standard Body, Table Cells, Form Inputs |
| `caption` | 12px / 0.75rem | 16px | 400 / 600 | Badges, Micro-copy, Timestamps, Disclaimers |
| `code-mono` | 14px / 0.875rem | 20px | 600 (Semibold) | OTPs, IDs, Serial Numbers, Geo-pins |

### 1.3 Spacing, Radius & Elevation
- **Spacing Grid:** 4px baseline (`$space-1`: 4px, `$space-2`: 8px, `$space-3`: 12px, `$space-4`: 16px, `$space-6`: 24px, `$space-8`: 32px, `$space-12`: 48px, `$space-16`: 64px)
- **Border Radius:**
  - `radius-sm`: 6px (Badges, inner inputs, tooltips)
  - `radius-md`: 10px (Buttons, textfields, dropdowns)
  - `radius-lg`: 16px (Cards, dialog modals, calendar modules)
  - `radius-full`: 9999px (Pills, avatar icons, round buttons)
- **Shadow Tokens:**
  - `shadow-subtle`: `0 1px 3px rgba(15, 23, 42, 0.05), 0 1px 2px rgba(15, 23, 42, 0.02)`
  - `shadow-card`: `0 4px 6px -1px rgba(15, 23, 42, 0.08), 0 2px 4px -2px rgba(15, 23, 42, 0.04)`
  - `shadow-elevated`: `0 12px 24px -4px rgba(15, 23, 42, 0.12), 0 4px 6px -2px rgba(15, 23, 42, 0.05)` (Sticky checkout summary, floating modals)

---

## 2. Core Reusable UI Component Specifications

### 2.1 Trust & Verification Badges
Used across cards, detail views, owner profiles, and admin moderation tables:
1. **Verified Product Badge (`<BadgeVerifiedProduct />`):**
   - Style: Green pill, checkmark shield icon, text: `"Product Verified"`
   - Hover Tooltip: `"Ownership, serial number, and physical condition verified by platform inspection on [Date]"`
2. **KYC Verified Badge (`<BadgeKYC />`):**
   - Style: Blue pill, verified user icon, text: `"ID Verified"`
3. **Trust Score Meter (`<TrustScoreGauge score={val} />`):**
   - Numerical score (0 to 100) with color tier (85-100: Platinum Green, 70-84: Gold Blue, 50-69: Neutral Amber, <50: Critical Gray/Red) based strictly on verified platform rental history and zero unresolved disputes.
4. **Deposit Escrow Shield (`<BadgeEscrow />`):**
   - Text: `"₹[Amount] Security Deposit Held in Neutral Escrow"`

### 2.2 Dual-Step Condition Photo Inspector (`<ConditionEvidenceViewer />`)
Crucial differentiator for eliminating handover & return disputes:
- Side-by-side split screen / comparative slider:
  - **Left / Tab 1:** `Handover Evidence (Before)` – Time-stamped, GPS tagged, 6 angles + serial number photo.
  - **Right / Tab 2:** `Return Evidence (After)` – Uploaded during return handover.
- Discrepancy flagging pins: Enables clicking on an area to highlight scratches/dents with zoom loupe (2x magnifying glass).

### 2.3 Transparent Rental Price & Escrow Breakdown Card (`<PriceDepositBreakdown />`)
- **Hourly/Daily/Weekly/Monthly switcher toggle**
- Line Items:
  1. Base Rental Fee: `₹[Rate] × [Duration]`
  2. Platform Service Fee: `₹[PlatformFee]`
  3. Refundable Security Deposit: `₹[DepositAmount]` (Clearly flagged with `[Refundable]` label)
  4. Delivery / Pickup Logistics: `₹[Fee]`
  5. **Total Payable Now:** `₹[Total]`
  6. Callout note: *"Deposit of ₹[DepositAmount] is released immediately upon owner return confirmation & condition sign-off."*

---

## 3. Global Information Architecture & Navigation Systems

### 3.1 Header Navigation Layouts
- **Customer Navigation:**
  - `[Logo]` | `[Location Picker Dropdown (City/Pincode)]` | `[Search Bar with Category Filter & Date Picker Pill]` | `[Become an Owner / List Item]` | `[Wishlist Heart (Badge count)]` | `[My Bookings]` | `[Notifications Bell]` | `[User Avatar Dropdown]`
- **Owner Dashboard Navigation:**
  - `[Logo + Owner Portal Tag]` | `[Quick Switch to Customer Mode]` | `[+ Add Product Button]` | `[Earnings Snapshot Widget: ₹Current]` | `[Alerts/Booking Requests (Pulsing badge)]` | `[Owner Profile]`
- **Admin Navigation:**
  - `[Logo + Admin Control Panel]` | `[Global Search: User, Order, Listing, Serial #]` | `[Risk Alert Monitor (Red pill if pending fraud flag)]` | `[Admin Profile / Logout]`

### 3.2 Responsive Bottom Nav Bar (Mobile Viewports < 768px)
- **Customer Mode:** `[Explore (Home)]` | `[Categories]` | `[Search/Nearby]` | `[My Bookings]` | `[Account]`
- **Owner Mode:** `[Dashboard]` | `[My Listings]` | `[Requests (Counter)]` | `[Payouts]` | `[Profile]`

---

## 4. Detailed Screen-by-Screen UI/UX Design

---

### Module 1: Common Pages (Pages 1 to 7)

#### Page 1: Landing Page (`/`)
- **Goal:** Immediately establish trust, clarify how peer-to-peer / B2C rentals work, show supported categories, and drive discovery or listing creation.
- **Hero Section:**
  - Headline: *"Rent Anything, Anywhere. Safe, Verified, Insured."*
  - Floating Universal Rental Bar: `[Search items: e.g. Sony A7 IV, Bosch Drill...]` | `[Category Dropdown]` | `[Select Dates (Pickup - Return)]` | `[City/Pincode]` | `[Search CTA Button]`.
  - Trust Ticker Bar: *"100% Escrow Protected Deposits" • "KYC & Product Verified Owners" • "Zero-Dispute Photographic Handover"*.
- **Category Grid (8 core categories with custom iconography & photography):**
  - Electronics & Cameras, Power Tools & Machinery, Events & Audio-Visual, Camping & Outdoor, Furniture & Home, Vehicles & Mobility, Medical & Health, Education & Hobbies.
- **How It Works (Interactive 3-Step Slider):**
  1. *Book & Pay Securely* (Rental fee + escrow deposit)
  2. *Photo-Verified Handover* (Both parties sign off on product condition in app)
  3. *Easy Return & Instant Deposit Refund*.
- **Owner Conversion Banner:** *"Turn idle gear into monthly cash flow. Up to ₹50,000/month with full damage protection."* `[List Your Item Now]`.
- **Verified Reviews & Trust Testimonials Carousel.**
- **Footer:** Full category index, trust & safety charter, dispute policy, legal, KYC policy, mobile app download links.

#### Page 2: Register Page (`/register`)
- **Layout:** Two-column split layout. Left side: Highlighting safety guarantees ("You're protected by our ₹10,000 damage coverage guarantee"). Right side: Form container.
- **Form Controls:**
  - Full Name, Mobile Number (with `+91` selector), Email Address, Password (with interactive strength validator meter).
  - Intent Selector Radio Cards: `[I want to Rent Items]` / `[I want to List & Rent Items]` (Sets initial onboarding pipeline).
  - Terms & Consent Checkbox (explicit consent for identity verification).
  - `[Create Account & Send OTP]` CTA button.
  - Social OAuth alternatives: Google, Apple ID.

#### Page 3: Login Page (`/login`)
- **Layout:** Centered card with clean slate backdrop.
- **Authentication Toggle:** Tab 1: `Mobile Number (Fast OTP Login)` | Tab 2: `Email & Password`.
- **Form Controls:** Input with inline country code, `Remember this device` checkbox, `Forgot Password?` link, and reCAPTCHA v3 invisible trigger.
- **State Feedback:** Inline error messaging for rate limits, incorrect credentials, or suspended accounts.

#### Page 4: OTP Verification Page (`/auth/verify-otp`)
- **Layout:** 6-box individual digit input with auto-focus advance, paste listener, and backspace retreat.
- **Visuals:** Timer countdown (`00:45 seconds remaining`), `Resend OTP via SMS` / `Resend OTP via WhatsApp` action buttons (disabled until countdown expires).
- **Security Indicator:** *"OTP sent to +91 98765-XXXXX for session verification."*

#### Page 5: Forgot Password (`/auth/forgot-password`)
- **Form Controls:** Email / Mobile input.
- **Step Progression:**
  1. Request reset link / OTP
  2. Verify OTP / Auth token
  3. Enter New Password & Confirm Password (with live requirement checks: 8+ chars, 1 uppercase, 1 special char).
- **Success State:** Instant redirect with toast confirmation to `/login`.

#### Page 6: User Profile & KYC Center (`/account/profile`)
- **Profile Summary Header:** Avatar with upload modal, User Trust Score indicator, member since date, badges earned (`ID Verified`, `Phone Verified`, `Top Renter`).
- **Tabbed Sub-Sections:**
  - **Tab 1: Personal Details:** Name, email, mobile, alternate emergency contact, default delivery addresses (with Google Maps autocomplete pin-drop).
  - **Tab 2: KYC & Verification Center:**
    - Document Selector: Aadhaar (via Digilocker / masked e-KYC), Driving License, or Passport.
    - Live Camera Selfie Capture component with face-liveness detection ring.
    - Status Pill: `[Verified ✅]` / `[In Review ⏳]` / `[Action Required ⚠️]`.
  - **Tab 3: Bank Account / Payout Methods:** Required for owners to receive settlements (Account Holder, IFSC, Account Number, instant penny-drop validation badge).
  - **Tab 4: Security:** Change password, 2FA toggle, active sessions list with `Log out other devices` CTA.

#### Page 7: Notifications Center (`/account/notifications`)
- **Filter Tabs:** `All`, `Bookings & Orders`, `Deposit Refunds`, `Security & System`.
- **Item Row Components:**
  - Icon denoting event (Handover scheduled, Booking approved, Deposit released, Damage claim raised).
  - Unread indicator dot, relative timestamp, primary actionable CTA button (e.g. `[Inspect Return]`, `[View Invoice]`, `[Pay Deposit]`).
  - Batch action: `[Mark all as read]`.

---

### Module 2: Customer Module (Pages 8 to 22)

#### Page 8: Customer Home (`/home`)
- **Personalized Header:** *"Welcome back, Alex! Nearby gear available for rent today."*
- **Quick-Category Horizontal Slider:** 8 visual pills with category icons and active listing counts.
- **"Rent Again" Section:** Horizontal carousel of previously rented items with quick `[Book Again]` trigger.
- **Featured & Verified Gear Section:** Grid of top-rated items with Verified Product badges.
- **Nearby Map Toggle (`[Show Map View]`):** Renders interactive map pins with price bubbles.

#### Page 9: Category Listing (`/category/[slug]`)
- **Breadcrumb Navigation:** `Home > Electronics > Cameras & Lenses`.
- **Dynamic Header:** Category title, description, and subcategory pill carousel (e.g., DSLRs, Mirrorless, Cinema, Prime Lenses).
- **Responsive Layout:**
  - **Left Sidebar Filter Panel (Desktop) / Slide-over Drawer (Mobile):**
    - Subcategory checkboxes.
    - Price Range Slider (Hourly / Daily / Monthly limits).
    - Security Deposit limit filter.
    - Availability Date Picker Range (`From Date` - `To Date`).
    - Distance Radius Slider (`Within 5 km`, `10 km`, `25 km`, `City-wide`).
    - Badges toggle (`Only Verified Products ✅`, `Instant Booking ⚡`).
  - **Main Listing Grid:** Sort dropdown (`Popularity`, `Price: Low to High`, `Trust Score`, `Nearest`).
  - **Product Card (`<RentalCard />`):** Image carousel, Verified badge, Product title, Rating (`★ 4.9 (24)`), Distance (`2.4 km away`), Daily Rate, Deposit tag, and Wishlist heart.

#### Page 10: Search Results Page (`/search?q=...`)
- **Search Header:** Shows matching count: *"Showing 42 rental results for 'Sony FX3' in Mumbai"*.
- **Faceted Filters & Location Radius selector.**
- **Empty State Fallback:** "No products found matching your exact dates" with alternative suggestions, nearby categories, or an option to *"Notify me when an owner lists this item"*.

#### Page 11: Product Details Page (`/product/[id]`)
- **Layout:** Two-column desktop layout (Left: Media gallery & rich specs; Right: Sticky Booking Widget).
- **Left Column:**
  - **Media Gallery:** High-res image carousel, owner verification video/live photo snippet, and watermark indicating ownership verification.
  - **Product Verification Box:** Prominent green card with verified badge: *"Verified by Platform on Nov 15: Serial # confirmed (SN: 8493***), physical working test passed, zero sensor dust detected."*
  - **Product Specifications:** Structured key-value table (Brand, Model, Condition grade: Mint/Good/Fair, Included accessories list).
  - **Rental Rules & Policies:** Cancellation policy, late return penalty rules (e.g. 1.5x hourly fee), prohibited use notices.
  - **Owner Profile Snippet:** Owner Avatar, name, Trust Score (`96/100`), Identity Verified badge, Average response time (`< 15 mins`), total completed rentals (`142`).
  - **Verified Reviews List:** Only reviews from completed rentals, showing user verification status, rental duration, and date.
- **Right Column (Sticky Booking Widget):**
  - Base price display (`₹1,200 / day`).
  - Duration selector tabs: `Daily` / `Weekly (15% off)` / `Monthly (30% off)`.
  - Date & Time Picker: Pickup datetime and Return datetime.
  - Real-time Availability Indicator: Live check against owner's calendar.
  - Logistics toggle: `Self Pickup at Owner Location` or `Doorstep Delivery (+₹250)`.
  - Price & Escrow Breakdown component:
    - Rental: ₹2,400
    - Security Deposit: ₹5,000 (Refundable)
    - Platform Insurance & Fee: ₹180
    - **Total Initial Payment:** ₹7,580
  - Primary CTA: `[Proceed to Rent / Request Booking]` (or `[Instant Book ⚡]`).
  - Micro-copy: *"Your deposit remains safe in neutral escrow until you inspect and approve the product at handover."*

#### Page 12: Availability Calendar Component / Modal (`/product/[id]/availability`)
- Interactive dual-month calendar view.
- Color codes:
  - Green: Available for instant booking.
  - Red / Strikethrough: Booked by other users.
  - Amber: Blocked by owner for maintenance.
  - Highlighted Blue: User's selected rental range.
- Minimum and maximum duration limits dynamically displayed.

#### Page 13: Rental Duration & Time Selector Component
- Granular hourly and multi-day scheduler.
- Time slot dropdowns (e.g., 09:00 AM pickup, 08:00 PM return).
- Overtime warning calculator showing extra hourly rate calculations if returned late.

#### Page 14: Booking Checkout Page (`/checkout/[bookingId]`)
- **Step Indicator:** `1. Review & Dates > 2. Identity Verification > 3. Delivery/Pickup > 4. Payment`.
- **Rental Agreement Acknowledgment:** Embeds the digital rental terms contract with user initials or digital consent checkbox.
- **Delivery Address Confirmation / Pickup Point Map with owner privacy preservation** (exact address revealed upon payment completion).
- **Identification Confirmation:** Confirms active KYC document status. If not verified, shows inline prompt to complete KYC before payment.
- **Deposit Policy Confirmation:** Explicit acknowledgment: *"I understand ₹5,000 will be held as security deposit and refunded within 24 hours of successful product return inspection."*
- **Final Cost Summary Card.**
- `[Confirm and Pay ₹7,580]` CTA.

#### Page 15: Payment Page (`/checkout/payment`)
- **Direct integration with Payment Gateway (Razorpay/Cashfree/PayU):**
- **Payment Method Accordions:**
  - UPI (Google Pay, PhonePe, Paytm, QR scan)
  - Credit / Debit Cards (with auto OTP prompt)
  - Net Banking
  - Pre-authorized Escrow Hold support (where deposit is blocked on card rather than debited, if supported).
- **Security & SSL seals**, 256-bit encryption indicators, payment timer (15 minutes before slot hold expires).

#### Page 16: Booking Confirmation Page (`/booking/confirmed/[id]`)
- **Visuals:** Animated green success checkmark with confetti.
- **Order Details Card:** Booking Reference Number (`#RNT-94821`), Rental Period, Owner Contact Info & Pickup Coordinates.
- **Next Steps Checklist (Interactive):**
  1. `[Done]` Payment Received & Escrow Held.
  2. `[Pending]` Handover Scheduled for Tomorrow at 10:00 AM.
  3. `[Read Guidance]` How to inspect and photograph the product at handover.
- Action Buttons: `[Add to Google Calendar]`, `[Chat with Owner]`, `[View Booking Details]`.

#### Page 17: My Bookings Dashboard (`/customer/bookings`)
- **Status Filter Tabs:** `All`, `Requested / Awaiting Approval`, `Confirmed / Upcoming`, `Active Rentals (In Hand)`, `Completed`, `Cancelled / Disputed`.
- **Rental Booking Card:** Product thumbnail, Title, Booking ID, Dates, Status badge (`Active`, `Return Due Today`, `Deposit Refunded`), Current actionable button:
  - If Upcoming: `[View Pickup Instructions]`
  - If Active: `[Initiate Return]` / `[Request Extension]`
  - If Completed: `[View Return Receipt & Deposit Settlement]` / `[Leave Review]`.

#### Page 18: Booking Details Page (`/customer/bookings/[id]`)
- Comprehensive overview: Complete transaction timeline, payment invoices (downloadable PDF), owner details, chat history link, handover condition photographs, and dispute resolution trigger button (`[Report an Issue / Emergency]`).

#### Page 19: Return Request Page (`/customer/bookings/[id]/return`)
- Initiates the return sequence.
- **Select Return Method:** Self-drop at original location or courier/valet pickup.
- **Schedule Return Slot:** Date and hour selection.
- **Pre-Return Checklist for Renter:** "Cleaned and packed in original case?", "All accessories included?", "Batteries charged?".
- **Return Photograph Uploader (Optional pre-check):** Allows renter to upload photos before departure to establish baseline return condition.

#### Page 20: Rental & Handover Tracking Page (`/customer/bookings/[id]/track`)
- **Live Status Stepper:**
  `Booking Placed > Owner Accepted > Payment Confirmed > Handover In Progress > Active Rental > Return Scheduled > Owner Inspection > Deposit Released`.
- **Handover Verification Screen:**
  - Renter enters/shows 6-digit Secure Handover OTP to owner.
  - Review 6 condition photos uploaded by owner; renter clicks `[Approve Condition & Receive Item]`.

#### Page 21: Reviews & Ratings Page (`/customer/bookings/[id]/review`)
- Multi-dimensional rating criteria (1 to 5 stars):
  - Product Condition & Accuracy
  - Owner Communication & Punctuality
  - Value for Money
- Written Review box with guidelines discouraging personal insults or unverified claims.
- Photo attachment: Upload photos of the product during use.
- Verified Rental Badge indicator auto-tagged to the submitted review.

#### Page 22: Wishlist (`/customer/wishlist`)
- Grid of saved rental products with live price change indicators and date availability alerts.
- Quick action: `[Check Dates & Rent]`, `[Remove]`.

---

### Module 3: Owner Module (Pages 23 to 32)

#### Page 23: Owner Dashboard (`/owner/dashboard`)
- **Metrics Bar (KPI Cards):**
  - Total Monthly Earnings (`₹38,400`)
  - Active Rentals (`4 items out`)
  - Pending Booking Requests (`2 requiring action`)
  - Overall Owner Trust Score (`98% - Top Rated`)
- **Action Required Alert Box:** Highlighted notifications (e.g., *"Return inspection pending for Sony A7 IV returned 2 hours ago. Settle deposit within 22 hours."*).
- **Quick Actions:** `[+ Add New Product]`, `[Manage Availability Calendar]`, `[Withdraw Payout]`.
- **Live Mini-Schedule:** Today's handovers and pickups with one-click calling/messaging.

#### Page 24: Add Product (Multi-Step Creation Flow) (`/owner/products/new`)
A 5-step wizard designed to maximize listing quality and eliminate fraud:
- **Step 1: Category & Basic Info:** Title, Category, Subcategory, Brand, Model, Condition classification (Like New, Good, Fair), Description, Included accessories.
- **Step 2: Pricing & Deposit:**
  - Rental rate inputs (Hourly, Daily, Weekly discount %, Monthly discount %).
  - Security Deposit amount (Platform provides dynamic recommended deposit range based on item replacement value).
  - Minimum and Maximum rental days allowed.
- **Step 3: High-Res Photos & Media:**
  - Multi-image dropzone (Minimum 4 photos required: Front, Back, Serial Number plate, Accessories).
- **Step 4: Product Ownership Proof (For "Product Verified" Badge):**
  - Input: Serial Number / IMEI.
  - Upload: Purchase invoice / warranty card (optional but rewarded with Verified badge).
  - Live Verification Selfie: Owner holds product with a temporary on-screen verification code written on paper.
- **Step 5: Handover Location & Logistics:**
  - Exact pickup address, landmark, delivery availability toggle and per-km pricing.
- `[Submit for Admin Approval & Verification]` CTA.

#### Page 25: Manage Products (`/owner/products`)
- Table/Grid listing all owner inventory:
  - Product thumbnail, Title, Category, Daily Price, Current Status (`Active / Live`, `Rented Out`, `Pending Verification`, `Paused / Draft`).
  - Toggle switch: `[Active / Snooze Listing]`.
  - Action dropdown: `Edit Details`, `Manage Blocked Dates`, `View Analytics`, `Delete Listing`.

#### Page 26: Product Availability Calendar (`/owner/products/[id]/calendar`)
- Interactive full-screen master calendar for the specific product:
  - Block personal dates (e.g., owner using camera for a family event next weekend).
  - Bulk price modifiers (e.g. increase price by 20% on holidays or festival weekends).
  - Color-coded overlay of all existing customer bookings.

#### Page 27: Booking Requests Page (`/owner/requests`)
- Card-based request queue with countdown timer (Owner has 12 hours to respond before auto-cancellation):
  - Renter Card: Renter Name, Trust Score (`★ 4.8 / 12 completed rentals`), KYC status (`ID Verified ✅`).
  - Rental Request Details: Requested dates, Total rental earnings for owner (net of commission), Self-pickup vs. Delivery.
  - Action Buttons: `[Accept Request]` (prompts customer to pay) or `[Decline Request]` (prompts reason: unavailable, maintenance, etc.).

#### Page 28: Booking Management (`/owner/bookings`)
- Comprehensive table and kanban view of all bookings:
  - Filter by `Awaiting Handover`, `Currently With Renter`, `Return Due`, `Completed`.
  - Detailed modal with direct phone contact, handover OTP, and emergency platform support link.

#### Page 29: Handover & Return Management (`/owner/bookings/[id]/handover`)
The core operational trust interface:
- **Phase A: Handover Execution:**
  - Camera capture modal: Owner takes 6 mandatory real-time condition photos (all sides, screen/lenses, power-on state).
  - Enter Customer Handover OTP to verify physical presence.
  - Click `[Confirm Handover Complete - Start Rental]`.
- **Phase B: Return & Inspection Execution:**
  - Customer arrives with product.
  - Owner takes 6 return condition photos.
  - Side-by-side comparison interface displays original handover photos next to fresh return photos.
  - Inspection Decision Form:
    - Option 1: `[Product in Perfect Condition - Release 100% Deposit]` (Initiates instant deposit refund).
    - Option 2: `[Discrepancy / Damage Detected - Report Claim]` (Pauses deposit refund, prompts damage photos, repair estimate, and moves booking to Admin Dispute Queue).

#### Page 30: Earnings Dashboard (`/owner/earnings`)
- **Financial Cards:** Total Lifetime Earned, Pending Escrow Settlements, Available for Immediate Withdrawal, Platform Commission Paid.
- **Interactive Revenue Graph:** Monthly/Weekly revenue trends across products.
- **Withdrawal Action Widget:** One-click transfer to verified bank account via IMPS/NEFT.

#### Page 31: Payment History & Payout Records (`/owner/payouts`)
- Itemized financial ledger:
  - Columns: Transaction ID, Booking ID, Product Name, Gross Rental, Platform Fee (e.g., -10%), Net Payout, Payout Status (`Processed`, `In Escrow`, `Processing`), Downloadable GST Tax Invoice.

#### Page 32: Owner Profile & Verification Management (`/owner/profile`)
- Public Owner Profile editor: Bio, business name, operating hours, response time stats, badges portfolio.
- Bank Account verification settings, GSTIN details (for business owners), and pickup instructions.

---

### Module 4: Admin Module (Pages 33 to 44)

#### Page 33: Admin Login (`/admin/login`)
- Separate, hardened administrator login URL with Mandatory Multi-Factor Authentication (TOTP / Hardware Key), IP whitelist checks, and session auto-logout after 15 minutes of inactivity.

#### Page 34: Admin Dashboard (`/admin/dashboard`)
- **Platform Health KPI Bar:** Total Active Rentals, Platform GMV (Gross Merchandise Value), Active Disputes, Pending Listing Approvals, Flagged Risk Score Alerts.
- **Real-Time Operational Queues:**
  - Pending Product Ownership Verifications (Count: 14)
  - KYC Approvals Pending (Count: 28)
  - Damage/Deposit Disputes Requiring Mediation (Count: 3)
- **Geographic & Category Performance Visualizers:** Heatmaps of rental activity across cities and category distribution.

#### Page 35: User Management (`/admin/users`)
- Master searchable table of all Customers and Owners:
  - Columns: User ID, Name, Role, Trust Score, KYC Status, Active Rentals, Risk Rating (`Low`, `Medium`, `High`), Account Status (`Active`, `Suspended`, `Banned`).
  - User Inspection Drawer: View full KYC documents, booking history, fraud signal log, device fingerprints, and admin action buttons (`[Impersonate/Inspect]`, `[Suspend Account]`, `[Override KYC]`).

#### Page 36: Owner & KYC Verification Portal (`/admin/verifications/owners`)
- Dedicated split-screen review tool for identity audits:
  - Left: User-submitted Government ID & Selfie face-match score (e.g. 98.4% match).
  - Right: Digilocker / OCR extracted data vs. user entered form fields.
  - Actions: `[Approve KYC]`, `[Reject with Reason: Blurry Photo]`, `[Request Additional Document]`.

#### Page 37: Product Approval & Verification Queue (`/admin/verifications/products`)
- High-throughput review interface for new listings:
  - Review submitted serial number, invoice proof, live owner selfie holding item.
  - Tools: Check serial number against stolen goods / national registry blacklist if available.
  - Actions: `[Approve & Award 'Product Verified' Badge]`, `[Approve Standard Listing (Unverified)]`, `[Reject / Request Clearer Serial Photo]`.

#### Page 38: Category Management (`/admin/categories`)
- Category & Subcategory builder:
  - Add/Edit Categories, icons, SEO metadata, required specifications templates (e.g. cameras require `megapixels`, `mount_type`; cars require `transmission`, `fuel_type`).
  - Dynamic Security Deposit Guidelines: Set recommended deposit percentage range per category (e.g. 30% of MSRP for electronics, 10% for furniture).

#### Page 39: Booking Management & Monitoring (`/admin/bookings`)
- Live feed of all ongoing platform bookings:
  - Filter by high-risk bookings (e.g., first-time user renting high-value camera equipment).
  - Status overrides and intervention triggers (e.g., mark handover manually if emergency arises).

#### Page 40: Payment & Escrow Management (`/admin/payments`)
- Escrow ledger monitor:
  - Total deposits held in escrow accounts.
  - Pending refund queues.
  - Commission payouts and reconciliation reports.
  - Manual deposit release or forfeiture controls.

#### Page 41: Return, Damage & Dispute Management (`/admin/disputes`)
- **Tri-Party Dispute Resolution Workspace:**
  - Customer claim vs. Owner claim timeline.
  - Side-by-side photographic condition viewer: Compares Handover baseline photos with Return damage photos.
  - Independent repair quote uploader.
  - Deposit Allocation Slider: Admin decides deposit split (e.g., ₹3,500 awarded to owner for repair, ₹1,500 refunded to customer).
  - Binding resolution notes & audit trail logging.

#### Page 42: Review & Content Moderation (`/admin/reviews`)
- Moderation queue for flagged reviews and automated fake-review detection (detects reciprocal review rings, extreme sentiment anomalies, or offensive language).
- Actions: `[Approve Review]`, `[Mask / Remove Review with Notice]`.

#### Page 43: Reports & Analytics (`/admin/analytics`)
- Exportable CSV/PDF reports:
  - Platform Rental Volume & Seasonal Velocity
  - Loss Ratio / Damage Claim Frequency per Category
  - Category Growth Trends & Geographic Supply/Demand Gaps
  - KYC and Verification Conversion Funnels.

#### Page 44: Platform Settings & Risk Engine Configuration (`/admin/settings`)
- Global Fee Structure: Platform commission rate (e.g. 10% - 15%), customer convenience fee, insurance premium fee.
- Fraud & Risk Engine Thresholds:
  - Trigger manual review if item replacement value > ₹50,000 for a new renter.
  - Flag if multiple accounts use same payment card or device hardware fingerprint.
  - Set default deposit holding period and late return penalty multipliers.

---

## 5. End-to-End User Journeys & Critical Interaction Flows

### 5.1 The Trust-Centric Booking-to-Settlement Sequence
```
[Customer Searches & Finds Verified Product]
                 │
                 ▼
[Customer Selects Dates & Reviews Transparent Escrow Breakdown]
                 │
                 ▼
[KYC Status Check: Auto-verified or Fast-track KYC prompt]
                 │
                 ▼
[Owner Receives Notification & Accepts Request (12h SLA)]
                 │
                 ▼
[Customer Pays Rental Fee + Refundable Escrow Deposit]
                 │
                 ▼
[Handover Meeting: Owner Uploads 6 Photos + Customer Shares OTP]
                 │
                 ▼
   =============================
   RENTAL ACTIVE IN CUSTOMER HANDS
   =============================
                 │
                 ▼
[Return Meeting: Owner Takes 6 Return Inspection Photos]
                 │
       ┌─────────┴─────────┐
       ▼                   ▼
 [No Damage Found]   [Damage Reported]
       │                   │
       │                   ▼
       │         [Admin Tri-Party Dispute Queue]
       │         [Side-by-Side Photo Comparison]
       │         [Admin Allocates Repair & Refund]
       ▼                   │
 [Deposit Released To Customer (Instant)]
 [Owner Receives Rental Fee Minus Commission]
                 │
                 ▼
 [Reciprocal Verified-Only Reviews & Trust Scores Updated]
```

---

## 6. Responsive Breakpoint & Mobile UI Adaptations

| Breakpoint | Target Screen | UI Adaptations |
|---|---|---|
| `< 640px` (Mobile) | iPhone, Android | Bottom fixed booking bar on Product Details; slide-up bottom sheets for filters; full-screen photo comparison with pinch-to-zoom; camera native integration for handover photo capture. |
| `640px - 1024px` (Tablet) | iPad, Foldables | 2-column card grid; collapsible filter drawer; side-by-side modal for handover inspection. |
| `> 1024px` (Desktop) | Laptops, Monitors | Sticky booking widget; persistent sidebar filters; multi-column admin tables with inline actions and split-view verification workspace. |

---

## 7. Accessibility, Micro-interactions & Error Handling

1. **Accessibility (WCAG 2.1 AA Standard):**
   - High contrast ratios (minimum 4.5:1 for body copy against white/slate background).
   - Full keyboard navigability on date range pickers and image carousels (`Tab`, `Arrow keys`, `Escape` to close modals).
   - Screen-reader tags (`aria-label`) on all badges (`"Status: Product Verified"`).

2. **Micro-interactions & State Transitions:**
   - Skeleton shimmer loaders during search and image fetch.
   - Real-time price calculation debouncing (instant visual update without layout shifts).
   - Haptic vibration feedback on mobile when scanning OTP or capturing handover photo evidence.

3. **Defensive Error UX:**
   - Network drop during photo upload: Offline local caching via IndexedDB with automatic background resume.
   - Payment timeout: Clear timer state with one-click retry keeping booking slot reserved for 15 minutes.
   - Dispute protection banners: Reassuring explanatory copy at every sensitive step regarding neutral deposit holding.
