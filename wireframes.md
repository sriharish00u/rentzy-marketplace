# Low-to-Mid Fidelity Wireframe Architecture Specification (`wireframes.md`)
**Project:** All-in-One Multi-Category Rental Marketplace  
**Scope:** 14 Essential Working Prototype Screens (Customer, Owner, Admin, Common)  
**Layout Grid:** 12-Column Responsive Desktop Grid (1200px max container) / 4-Column Mobile Grid (390px viewport)  
**Document Purpose:** Structural wireframes defining layout zones, container hierarchies, UI components, interaction targets, and data bindings.

---

## Screen Flow Index

```
[Flow 1: Auth & Onboarding]
   ├── WF-01: User Registration & Intent Onboarding
   ├── WF-02: Secure Login & OTP Authentication
   └── WF-03: User Profile & KYC Verification Center

[Flow 2: Customer Discovery & Booking]
   ├── WF-04: Marketplace Landing Page
   ├── WF-05: Category Listing & Search Discovery
   ├── WF-06: Booking Checkout & Escrow Agreement
   ├── WF-07: Payment Gateway & Escrow Pre-Authorization
   └── WF-08: Customer Bookings & Live Tracking

[Flow 3: Owner Listing & Operations]
   ├── WF-09: Owner Operations & Fleet Dashboard
   ├── WF-10: Owner Equipment Listing & Verification Wizard
   ├── WF-11: Owner Booking Requests & Approval Queue
   └── WF-12: Dual-Step Condition Inspection & Handover (Core Trust USP)

[Flow 4: Platform Admin & Mediation]
   ├── WF-13: Admin Master Health Dashboard
   └── WF-14: Admin Tri-Party Dispute Resolution Workspace
```

---

## Module 1: Auth & Onboarding Wireframes

### WF-01: User Registration & Intent Onboarding
**File Target:** `user_registration__intent_onboarding.html`  
**Layout:** 50/50 Split View (Desktop) / Single Column Stack (Mobile)

```
+-------------------------------------------------------------------------------+
| [Logo] RENTHUB                                         Already registered? [Log In] |
+---------------------------------------+---------------------------------------+
|                                       | CREATE YOUR ACCOUNT                   |
|  [Illustration: Trust & Protection]   | Join thousands renting & monetizing.  |
|                                       |                                       |
|  "Rent High-Value Gear With           | 1. SELECT ACCOUNT TYPE:               |
|   100% Escrow Protection"             | +-----------------+ +---------------+ |
|                                       | | (*) Renter      | | ( ) Owner     | |
|  * Verified Item Ownership            | | Rent gear with  | | List items &  | |
|  * Photographic Handover Evidence     | | zero liability  | | earn payout   | |
|  * Instant Deposit Refunds            | +-----------------+ +---------------+ |
|                                       |                                       |
|  [Security Badge: 256-Bit Encrypted]  | Full Name                             |
|                                       | [ John Doe                          ] |
|                                       | Mobile Number                         |
|                                       | [+91 | 98765 43210                  ] |
|                                       | Email Address                         |
|                                       | [ john.doe@example.com              ] |
|                                       | Password                              |
|                                       | [ **********                      [o]] |
|                                       | [==== Strength: Strong ========]       |
|                                       |                                       |
|                                       | [x] I agree to KYC checks & Terms.    |
|                                       |                                       |
|                                       | [==== CONTINUE & SEND OTP (CTA) ====] |
|                                       |                                       |
|                                       | -------- Or continue with ----------- |
|                                       | [ G  Google ]     [ Apple ID ]        |
+---------------------------------------+---------------------------------------+
```

---

### WF-02: Secure Login & OTP Authentication
**File Target:** `secure_login__session_authentication.html`  
**Layout:** Centered Floating Card (Width: 440px)

```
+-------------------------------------------------------------------------------+
|                                [Logo] RENTHUB                                 |
|                                                                               |
|                     +-----------------------------------+                     |
|                     |             WELCOME BACK          |                     |
|                     | Enter credentials to access your  |                     |
|                     | rentals or owner dashboard.       |                     |
|                     |                                   |                     |
|                     | [ Tab 1: Mobile OTP ] [ Tab 2: PW ] |                     |
|                     | -------------------               |                     |
|                     |                                   |                     |
|                     | Mobile Number:                    |                     |
|                     | [+91 | 98765 43210              ] |                     |
|                     |                                   |                     |
|                     | Enter 6-digit Verification Code:  |                     |
|                     | [ 4 ] [ 8 ] [ 1 ] [ 9 ] [ 0 ] [ ] |                     |
|                     |                                   |                     |
|                     | Resend code in 00:38s             |                     |
|                     |                                   |                     |
|                     | [x] Keep me signed in on device   |                     |
|                     |                                   |                     |
|                     | [==== VERIFY & LOG IN (CTA) ====] |                     |
|                     |                                   |                     |
|                     | [?] Trouble logging in? [Help]    |                     |
|                     +-----------------------------------+                     |
|                                                                               |
|              Protected by Antigravity Trust & Safety Engine                   |
+-------------------------------------------------------------------------------+
```

---

### WF-03: User Profile & KYC Verification Center
**File Target:** `user_profile__kyc_verification_center.html`  
**Layout:** 3-Column Profile Dashboard (Left: User Card & Trust Score; Center: Document Verification; Right: Activity Summary)

```
+-------------------------------------------------------------------------------+
| [Logo] RENTHUB    [Explore] [Categories] [List Gear]     [Wishlist(3)] [User v] |
+-------------------------------------------------------------------------------+
| HOME > ACCOUNT > PROFILE & VERIFICATION                                       |
+-------------------+---------------------------------------+-------------------+
| [USER AVATAR]     | IDENTITY VERIFICATION (KYC)           | TRUST PROFILE     |
| Rahul Sharma      | Required before booking or listing.   |                   |
| Member since 2025 |                                       | TRUST SCORE: 94   |
| [✓ ID VERIFIED]   | 1. GOVERNMENT ID SELECTION:           | [====== 94/100 =] |
|                   | (*) Aadhaar / DigiLocker              | Tier: Platinum    |
| Badges:           | ( ) Driving License                   |                   |
| [Top Renter]      | ( ) Passport                          | Signals:          |
| [Punctual Return] |                                       | + 12 Rentals Done |
|                   | [==== CONNECT WITH DIGILOCKER ====]   | + 0 Late Returns  |
| Quick Nav:        | - Status: [Verified on 12 Nov 2026]   | + 0 Damage Claims |
| > KYC Center      |                                       |                   |
| > Bank Details    | 2. LIVE SELFIE BIOMETRIC MATCH:       | REVIEWS SUMMARY   |
| > Addresses       | +-----------------------------------+ | ★★★★★ 4.98 (12)  |
| > Security        | | [Preview: Face Centered in Oval]  | | "Great condition, |
|                   | | Liveness Test: [PASSED 99.2%]     | |  very polite!"   |
|                   | +-----------------------------------+ |                   |
|                   |                                       | BANK ACCOUNT      |
|                   | 3. REGISTERED RESIDENTIAL ADDRESS:    | HDFC Bank ****4892|
|                   | [ 402, Sunset Heights, Bandra West, ] | [✓ Penny Drop OK] |
|                   | [ Mumbai - 400050                   ] |                   |
|                   |                                       | [Withdraw Funds]  |
|                   | [==== UPDATE & SAVE PROFILE ====]     |                   |
+-------------------+---------------------------------------+-------------------+
```

---

## Module 2: Customer Discovery & Booking Wireframes

### WF-04: Marketplace Landing Page
**File Target:** `marketplace_landing_page.html`  
**Layout:** 12-Column Hero & Faceted Rental Hub

```
+-------------------------------------------------------------------------------+
| [Logo] RENTHUB  [City: Mumbai v]  [Categories v]   [List an Item]  [Sign In]  |
+-------------------------------------------------------------------------------+
| HERO SECTION                                                                  |
|                                                                               |
|     Rent Anything, Anywhere. Safe, Verified, Insured.                         |
|     Access cameras, tools, furniture & drones with escrow protection.         |
|                                                                               |
| +---------------------------------------------------------------------------+ |
| | [Search gear: Sony A7...] | [Category v] | [Pickup - Return Dates] | [GO] | |
| +---------------------------------------------------------------------------+ |
|                                                                               |
|   [✓ Escrow Deposit Shield]   [✓ Serial-Verified Items]   [✓ Photo Handover]  |
+-------------------------------------------------------------------------------+
| POPULAR RENTAL CATEGORIES                                                     |
| +------------+ +------------+ +------------+ +------------+ +------------+    |
| | [Cameras]  | | [Power]    | | [Camp &]   | | [AV &]     | | [Mobility] |    |
| | 420 Items  | | 185 Tools  | | 94 Outdoor | | 210 Events | | 64 Vehicles|    |
| +------------+ +------------+ +------------+ +------------+ +------------+    |
+-------------------------------------------------------------------------------+
| FEATURED VERIFIED GEAR NEAR YOU                                               |
| +-------------------+ +-------------------+ +-------------------+             |
| | [Img: Sony A7 IV] | | [Img: DJI Drone]  | | [Img: Bosch Hammer] |           |
| | [✓ Verified Gear] | | [✓ Verified Gear] | | [✓ Verified Gear] |             |
| | Sony Alpha A7 IV  | | DJI Mini 4 Pro 4K | | Rotary Hammer Drill |           |
| | ★ 4.9 (38) 1.8km  | | ★ 4.8 (19) 3.2km  | | ★ 5.0 (14) 0.9km  |             |
| | ₹1,200/day        | | ₹1,800/day        | | ₹450/day          |             |
| | Deposit: ₹5,000   | | Deposit: ₹8,000   | | Deposit: ₹1,500   |             |
| | [ Rent Now ]      | | [ Rent Now ]      | | [ Rent Now ]      |             |
| +-------------------+ +-------------------+ +-------------------+             |
+-------------------------------------------------------------------------------+
| FOOTER: Safety Charter | Escrow Guarantee | Categories | FAQ | Contact Us    |
+-------------------------------------------------------------------------------+
```

---

### WF-05: Category Listing & Search Discovery
**File Target:** `category_listing__search_discovery.html`  
**Layout:** 3-Column Left Sidebar Filters (25%) + 9-Column Product Grid (75%)

```
+-------------------------------------------------------------------------------+
| [Logo] RENTHUB  [Search: Sony           ] [Mumbai v]   [Wishlist] [Bookings]  |
+-------------------------------------------------------------------------------+
| Home > Electronics > Cameras & Lenses                                         |
+-----------------------+-------------------------------------------------------+
| FILTERS (Clear All)   | CAMERAS & LENSES (128 Items in Mumbai)                |
|                       | Sort by: [Distance: Nearest first v] [View: Grid / Map]|
| Subcategories:        +-------------------------------------------------------+
| [x] Mirrorless (84)   | +---------------------------------------------------+ |
| [ ] Cinema (16)       | | [Img] Sony A7 IV Mirrorless Camera Body           | |
| [ ] Prime Lenses (32) | | [✓ PRODUCT VERIFIED] [★ 4.9 (42) | Bandra - 1.2km]| |
|                       | | SN: 3849**** | Mint Condition | Dual SD Included  | |
| Price / Day:          | |                                                   | |
| [ ₹500 ====== ₹3500 ] | | Owner: Rajesh K. [✓ ID] [Trust: 98%]              | |
|                       | | Rate: ₹1,200/day | Security Deposit: ₹5,000       | |
| Security Deposit:     | |                                                   | |
| [ Up to ₹10,000     ] | | [ Instant Book ⚡ ]   [ View Full Details ]        | |
|                       | +---------------------------------------------------+ |
| Distance Radius:      | +---------------------------------------------------+ |
| [ (< 5km)  10km 25km] | | [Img] Canon EOS R5 C 8K Cinema Camera             | |
|                       | | [✓ PRODUCT VERIFIED] [★ 5.0 (18) | Andheri - 4.5km]| |
| Availability:         | | SN: 9102**** | 45MP / 8K RAW | 2x CFExpress Cards | |
| [From: 28 Nov 2026]   | |                                                   | |
| [To  : 30 Nov 2026]   | | Owner: Studio Hive [✓ Business] [Trust: 99%]      | |
|                       | | Rate: ₹3,200/day | Security Deposit: ₹15,000      | |
| Safety Options:       | |                                                   | |
| [x] Verified Gear Only| | [ Request Booking ]   [ View Full Details ]        | |
| [ ] Instant Book Only | +---------------------------------------------------+ |
+-----------------------+-------------------------------------------------------+
```

---

### WF-06: Booking Checkout & Escrow Agreement
**File Target:** `booking_checkout__escrow_agreement.html`  
**Layout:** 8-Column Checkout Journey + 4-Column Sticky Cost & Escrow Summary

```
+-------------------------------------------------------------------------------+
| [Logo] RENTHUB                      Secure Checkout [🔒 256-Bit SSL]          |
+-------------------------------------------------------------------------------+
| STEP 1: RENTAL DURATION & LOGISTICS     | ORDER & ESCROW BREAKDOWN            |
|                                         |                                     |
| Product: Sony Alpha A7 IV               | [Item Thumb] Sony Alpha A7 IV       |
| Handover Date: 28 Nov 2026 @ 10:00 AM   | Duration: 2 Days                    |
| Return Date  : 30 Nov 2026 @ 10:00 AM   | ----------------------------------- |
|                                         | Base Rental Fee (₹1,200 x 2): ₹2,400|
| Handover Mode:                          | Platform Protection Fee     :   ₹180|
| (*) Self Pickup: Bandra West Hub        | Delivery / Valet            :     ₹0|
| ( ) Doorstep Courier Delivery (+₹250)   |                                     |
| --------------------------------------- | REFUNDABLE SECURITY DEPOSIT:        |
| STEP 2: VERIFICATION CHECK              | [ ₹5,000 - HELD IN ESCROW 🛡️ ]      |
|                                         | "Deposit is never paid to owner.    |
| Verified Renter: Rahul Sharma           |  Held in neutral escrow & returned  |
| [✓ Govt ID Verified] [✓ Selfie Matched] |  within 2 hours of sign-off."       |
| --------------------------------------- | ----------------------------------- |
| STEP 3: DIGITAL RENTAL CONTRACT         | TOTAL PAYABLE NOW:          ₹7,580  |
|                                         | (Includes ₹5,000 refundable)        |
| [x] I agree that condition photos will  |                                     |
|     be taken at pickup and return.      | [==== PROCEED TO PAYMENT (CTA) ====]|
| [x] I acknowledge that damages beyond   |                                     |
|     wear & tear will be deducted from   | [✓] Money Back Guarantee            |
|     escrow deposit under Admin review.  | [✓] Zero Deposit Risk Guarantee     |
+-----------------------------------------+-------------------------------------+
```

---

### WF-07: Payment Gateway & Escrow Pre-Authorization
**File Target:** `payment_gateway__escrow_pre-authorization_hold.html`  
**Layout:** Centered Gateway Frame (Width: 600px)

```
+-------------------------------------------------------------------------------+
|                                [Logo] RENTHUB                                 |
|                                                                               |
|                   +---------------------------------------+                   |
|                   | COMPLETE PAYMENT & ESCROW HOLD        |                   |
|                   | Total: ₹7,580 (Rent: ₹2,580 | Escrow: ₹5,000)             |
|                   | Session expires in: 14:22 mins        |                   |
|                   +---------------------------------------+                   |
|                   | SELECT PAYMENT METHOD:                |                   |
|                   |                                       |                   |
|                   | [v] UPI (Google Pay, PhonePe, Paytm)  |                   |
|                   |     Enter UPI VPA:                    |                   |
|                   |     [ rahul@okhdfcbank             ]  |                   |
|                   |     [ Pay & Authorize via App ]       |                   |
|                   |                                       |                   |
|                   | [>] Credit / Debit Cards (Pre-Auth)   |                   |
|                   |     * Supports card pre-authorization |                   |
|                   |       (deposit held, not debited)     |                   |
|                   |                                       |                   |
|                   | [>] Net Banking                       |                   |
|                   |                                       |                   |
|                   | ------------------------------------- |                   |
|                   | Escrow Trustee: Razorpay / Cashfree   |                   |
|                   | Funds protected in segregated account |                   |
|                   +---------------------------------------+                   |
+-------------------------------------------------------------------------------+
```

---

### WF-08: Customer Bookings & Live Tracking
**File Target:** `customer_bookings__live_tracking.html`  
**Layout:** Top Lifecycle Stepper + 2-Column Handover Details & Actions

```
+-------------------------------------------------------------------------------+
| [Logo] RENTHUB    [Explore] [My Bookings (Active: 1)]     [Wishlist] [Profile]|
+-------------------------------------------------------------------------------+
| BOOKING #RNT-83921: SONY ALPHA A7 IV                                          |
|                                                                               |
|  [✓ Booked] -----> [✓ Paid & Escrow] -----> [⏳ HANDOVER] -----> [Active] -> [Return]
|  26 Nov 12:30      26 Nov 12:32             Today 10:00 AM                    |
+-------------------------------------------+-----------------------------------+
| HANDOVER DETAILS & LOCATION               | HANDOVER AUTHENTICATION           |
|                                           |                                   |
| Pickup Location:                          | SHOW THIS OTP TO OWNER AT PICKUP: |
| Bandra West, Near Starbucks, Mumbai       | +-------------------------------+ |
| Owner: Rajesh K. [📞 Call] [💬 Chat]      | |       * 8  4  9  2 *          | |
|                                           | +-------------------------------+ |
| Time: Today at 10:00 AM (In 45 mins)      | Do not share until you physically |
|                                           | inspect the camera and battery!   |
| Pre-Handover Checklist:                   |                                   |
| [ ] Inspect front & rear lens glass       | [==== VIEW HANDOVER PHOTOS ====]  |
| [ ] Turn on body & check sensor screen    | (Owner has uploaded 6 check photos|
| [ ] Verify serial number matches 3849**** |  awaiting your approval)          |
|                                           |                                   |
| Security Deposit:                         | Emergency Hotline:                |
| ₹5,000 [SAFE IN ESCROW 🛡️]               | [ Report No-Show / Fraud Item ]   |
+-------------------------------------------+-----------------------------------+
```

---

## Module 3: Owner Listing & Fleet Operations Wireframes

### WF-09: Owner Operations & Fleet Dashboard
**File Target:** `owner_operations__fleet_dashboard.html`  
**Layout:** 4-Card KPI Header + 2-Column Operational Queue & Quick Actions

```
+-------------------------------------------------------------------------------+
| [Logo] RENTHUB [OWNER PORTAL]   [+ Add Item] [Earnings: ₹38,400]    [Owner v] |
+-------------------------------------------------------------------------------+
| KPI METRICS OVERVIEW                                                          |
| +-----------------+ +-----------------+ +-----------------+ +---------------+ |
| | MONTHLY INCOME  | | ACTIVE RENTALS  | | PENDING REQUESTS| | TRUST SCORE   | |
| | ₹38,400         | | 4 Items Out     | | 2 Action Items  | | 98% (Top-Tier)| |
| | +18% vs last mo | | Total value: 1.2L| | SLA: < 2 hrs    | | 142 Rentals   | |
| +-----------------+ +-----------------+ +-----------------+ +---------------+ |
+---------------------------------------+---------------------------------------+
| ACTION REQUIRED QUEUE (2)             | ACTIVE RENTALS IN FIELD               |
|                                       |                                       |
| 1. RETURN INSPECTION PENDING:         | * Sony FX3 Cinema Rig                 |
|    Item: Sony A7 IV                   |   Renter: Vikram S. [✓ KYC]           |
|    Returned by: Rahul S. 20 mins ago  |   Due: Tomorrow, 6:00 PM              |
|    [=== START RETURN INSPECTION ===]  |   Status: [Active & On Schedule]      |
|                                       |                                       |
| 2. NEW BOOKING REQUEST:               | * DJI Ronin RS3 Gimbal                |
|    Item: DJI Mini 4 Pro Drone         |   Renter: Anita P. [✓ KYC]            |
|    Dates: 29 Nov - 02 Dec (3 Days)    |   Due: 30 Nov, 10:00 AM               |
|    Net Earnings: ₹4,860               |   Status: [Active & On Schedule]      |
|    [ Accept (10h left) ] [ Decline ]  |                                       |
| ------------------------------------- | ------------------------------------- |
| QUICK CONTROLS:                       | FLEET QUICK ACCESS:                   |
| [ Manage Calendar ] [ Payouts Center ]| [View All 12 Gear Items in Fleet >]   |
+---------------------------------------+---------------------------------------+
```

---

### WF-10: Owner Equipment Listing & Verification Wizard
**File Target:** `owner_equipment_listing__verification_wizard.html`  
**Layout:** 5-Step Horizontal Breadcrumb Wizard with Form Container

```
+-------------------------------------------------------------------------------+
| [Logo] RENTHUB [OWNER PORTAL]                      [Save Draft] [Exit Wizard] |
+-------------------------------------------------------------------------------+
| STEP 1: Specs  >  STEP 2: Pricing  > [STEP 3: OWNERSHIP PROOF] > Step 4 > Done|
+-------------------------------------------------------------------------------+
| VERIFY PRODUCT OWNERSHIP (Earn "Product Verified ✅" Badge)                   |
| Increase rental bookings by 3.5x with verified proof.                         |
|                                                                               |
| 1. PRODUCT SERIAL NUMBER / IMEI:                                              |
|    [ SN-9482019482                                                   ]        |
|                                                                               |
| 2. UPLOAD SERIAL NUMBER PLATE PHOTO:                                          |
|    +----------------------------------------------------------------+         |
|    | [Img: High-res photo showing crisp serial number plate]        |         |
|    | [✓ OCR Verified: Serial number matches entered text]           |         |
|    +----------------------------------------------------------------+         |
|                                                                               |
| 3. PROOF OF PURCHASE OR OWNERSHIP INVOICE (Optional but recommended):         |
|    [ Upload PDF / Invoice Image: invoice_sony_croma.pdf (1.2 MB)  ]           |
|                                                                               |
| 4. LIVE VERIFICATION PHOTO:                                                   |
|    Take a photo of yourself holding the gear with today's date code: "RNT-77" |
|    +----------------------------------------------------------------+         |
|    | [ WebCam / Mobile Capture Preview: Owner holding camera & code]|         |
|    +----------------------------------------------------------------+         |
|                                                                               |
| [ Back: Pricing ]                    [==== CONTINUE TO LOGISTICS (CTA) ====]  |
+-------------------------------------------------------------------------------+
```

---

### WF-11: Owner Booking Requests & Approval Queue
**File Target:** `owner_booking_requests__approval_queue.html`  
**Layout:** 2-Column Request Cards with Renter Trust Analysis

```
+-------------------------------------------------------------------------------+
| [Logo] RENTHUB [OWNER PORTAL]   [Dashboard] [Requests (2)]  [Fleet] [Payouts] |
+-------------------------------------------------------------------------------+
| PENDING BOOKING REQUESTS (2 Requiring Action)                                 |
+-------------------------------------------------------------------------------+
| REQUEST #REQ-921: SONY A7 IV BODY (2 Days)             [Timer: 08:42:15 Left] |
| Requested Dates: 29 Nov 2026, 10:00 AM - 01 Dec 2026, 10:00 AM                |
+---------------------------------------+---------------------------------------+
| RENTER TRUST DOSSIER                  | FINANCIAL & LOGISTICS SUMMARY         |
|                                       |                                       |
| [User Avatar] Rahul Sharma            | Gross Rental (2 Days)   : ₹2,400      |
| Member since: March 2025              | Platform Commission(10%):  -₹240      |
| TRUST SCORE: 96 / 100 [Platinum]      | ------------------------------------- |
|                                       | YOUR NET EARNINGS       : ₹2,160      |
| Verification Badges:                  |                                       |
| [✓ Govt ID Verified] [✓ Bank Verified]| Escrow Deposit Collected: ₹5,000      |
| [✓ Phone & Email]    [✓ Selfie Match] | (Held safely in platform escrow)      |
|                                       |                                       |
| Rental History:                       | Handover Mode: Self-Pickup at your hub|
| * 12 Completed Rentals                |                                       |
| * 0 Overdue Incidents                 | [==== ACCEPT BOOKING REQUEST ====]    |
| * 5.0 Star Average Reviews            | [ Decline Request / Suggest Other ]   |
+---------------------------------------+---------------------------------------+
```

---

### WF-12: Dual-Step Condition Inspection & Handover (Core Trust USP)
**File Target:** `dual-step_condition_inspection__handover.html`  
**Layout:** Split-Screen Comparative Photo Inspector with Loupe Zoom & Sign-Off

```
+-------------------------------------------------------------------------------+
| [Logo] RENTHUB TRUST ENGINE        Booking #RNT-83921: Condition Sign-Off     |
+-------------------------------------------------------------------------------+
| RETURN INSPECTION & CONDITION COMPARISON                                      |
| Compare Handover (Before) vs. Return (After) to confirm deposit release.     |
+---------------------------------------+---------------------------------------+
| STEP 1: HANDOVER EVIDENCE (BEFORE)    | STEP 2: RETURN EVIDENCE (AFTER)       |
| Captured: 26 Nov 2026, 10:02 AM       | Captured: 28 Nov 2026, 10:15 AM       |
| GPS: Bandra West (Verified)           | GPS: Bandra West (Verified)           |
|                                       |                                       |
| +-----------------------------------+ | +-----------------------------------+ |
| | [PHOTO: Front Lens Element]       | | | [PHOTO: Front Lens Element]       | |
| |                                   | | |                                   | |
| | Status: 100% Clean, No Scratches  | | | Inspection: [Pristine Condition]  | |
| +-----------------------------------+ | +-----------------------------------+ |
| Angles: [Front] [Rear] [Sensor] [SN]  | Angles: [Front] [Rear] [Sensor] [SN]  |
|                                       |                                       |
| [ Loupe Zoom 2.5x Inspection Mode ]   | [ Pin Discrepancy / Mark Scratch ]    |
+---------------------------------------+---------------------------------------+
| INSPECTION SIGN-OFF & DEPOSIT DECISION                                        |
|                                                                               |
| [x] All 6 angles inspected and verified identical to handover condition.      |
| [x] Battery, charger, lens cap, and strap returned.                           |
|                                                                               |
| [==== RELEASE FULL ESCROW DEPOSIT (₹5,000) ====]  [ Report Damage Dispute ]   |
| (Triggers instant refund to renter's original UPI/Card account)               |
+-------------------------------------------------------------------------------+
```

---

## Module 4: Platform Admin & Mediation Wireframes

### WF-13: Admin Master Health Dashboard
**File Target:** `admin_master_health_dashboard.html`  
**Layout:** 4-Stat Metrics Ribbon + 3 Operational Queues (Verifications, Disputes, Risk)

```
+-------------------------------------------------------------------------------+
| [Logo] RENTHUB ADMIN CONSOLE       [Search: User, Booking, Serial] [Admin v]  |
+-------------------------------------------------------------------------------+
| PLATFORM REAL-TIME HEALTH                                                     |
| +-----------------+ +-----------------+ +-----------------+ +---------------+ |
| | ACTIVE ESCROW   | | MONTHLY GMV     | | PENDING KYC     | | OPEN DISPUTES | |
| | ₹42,80,000      | | ₹1.82 Crore     | | 18 Verifications| | 3 Mediation   | |
| | Segregated Pool | | +24% MoM        | | SLA: 45 mins    | | Requiring Dec | |
| +-----------------+ +-----------------+ +-----------------+ +---------------+ |
+-------------------------------------------------------------------------------+
| OPERATIONAL WORKSPACES                                                        |
|                                                                               |
| [Tab 1: Damage & Disputes (3)] [Tab 2: KYC Queue (18)] [Tab 3: Flagged Fraud] |
| ------------------------------                                                |
| +---------------------------------------------------------------------------+ |
| | Booking ID | Product      | Renter       | Owner       | Deposit | Action | |
| | #RNT-7491  | Sony FX3     | Amit V.      | Rajesh K.   | ₹15,000 | [Review] |
| |            | Claim: Scratched rear LCD during return inspection.           | |
| | #RNT-6204  | DJI Inspire 3| Karan M.     | Apex Studios| ₹25,000 | [Review] |
| |            | Claim: Propeller motor error after return.                    | |
| +---------------------------------------------------------------------------+ |
|                                                                               |
| AUTOMATED RISK & FRAUD SIGNALS:                                               |
| * Flagged User #U-9402: 3 accounts detected on same IMEI hardware. [Inspect]  |
| * Low-Price Alert: Sony A7 IV listed at ₹200/day (MSRP anomaly). [Block]      |
+-------------------------------------------------------------------------------+
```

---

### WF-14: Admin Tri-Party Dispute Resolution Workspace
**File Target:** `admin_tri-party_dispute_resolution_workspace.html`  
**Layout:** 3-Way Comparative Evidence Board (Owner Claim, Renter Defense, Admin Split Slider)

```
+-------------------------------------------------------------------------------+
| [Logo] RENTHUB MEDIATION               Dispute Case #DSP-1094 (Booking #7491) |
+-------------------------------------------------------------------------------+
| DISPUTE SUMMARY: Sony FX3 Rear LCD Scratch | Total Escrow: ₹15,000             |
+-----------------------------------+-------------------------------------------+
| OWNER CLAIM & EVIDENCE            | RENTER STATEMENT & EVIDENCE               |
| Owner: Rajesh K. [Trust: 98%]     | Renter: Amit V. [Trust: 94%]              |
|                                   |                                           |
| "Scratch on LCD not present at    | "Scratch was existing under protector;    |
|  handover. Authorized repair      |  photos from handover show hairline."     |
|  estimate: ₹4,200."               |                                           |
|                                   | +---------------------------------------+ |
| +-------------------------------+ | | [Photo: Return Handover Timestamped]  | |
| | [Photo: Marked scratch pin]   | | +---------------------------------------+ |
| +-------------------------------+ |                                           |
| Invoice Attached: sony_est.pdf    | Defense Dossier: 14 past clean rentals    |
+-----------------------------------+-------------------------------------------+
| ADMIN MEDIATION & ESCROW ALLOCATION                                           |
|                                                                               |
| Review Finding: Minor surface scratch verified on return LCD. Repair justified.|
|                                                                               |
| DEPOSIT SPLIT ALLOCATION SLIDER:                                              |
|                                                                               |
|   Award to Owner: ₹4,200 (Repair)          Refund to Renter: ₹10,800          |
|   [=========================O--------------------------------------]          |
|                                                                               |
| Binding Reason for Ruling:                                                    |
| [ Official Sony service quote validated. ₹4,200 awarded to owner, remainder ] |
| [ of ₹10,800 refunded instantly to renter.                                  ] |
|                                                                               |
| [==== EXECUTE BINDING RESOLUTION & RELEASE ESCROW FUNDS ====]                 |
+-------------------------------------------------------------------------------+
```

---

## Component Key & Interaction Specifications

| Wireframe Symbol | Meaning | User Interaction / Behavior |
|---|---|---|
| `[ Button ]` | Interactive CTA | Triggers screen transitions or submits asynchronous requests. |
| `[x] / ( )` | Checkbox / Radio | Configures rental options, consent terms, or filters. |
| `[ Text Input ]` | Form Field | Validates inline with regex (mobile, email, password strength). |
| `[v] / [>]` | Accordion / Dropdown | Expands to reveal additional configurations (e.g. payment methods). |
| `[====== O ==]` | Range Slider | Adjusts continuous variables (Price range, dispute settlement split). |
| `[✓ BADGE]` | Verified Pill | Hover/click opens modal revealing proof timestamps & inspection certificates. |
| `[PHOTO 2.5x]` | Visual Inspection | Clicks open split comparative loupe with coordinate pin-flagging. |
