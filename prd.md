**Product Requirements Document (PRD)**  
**All-in-One Rental Marketplace**

**Version:** 1.0  
**Date:** 26 November 2026  
**Status:** Draft for MVP and phased development

---

### 1. Overview

The All-in-One Rental Marketplace is a unified web platform that enables individuals and businesses to list physical products for short-term rental and allows customers to discover, book, pay for, receive, and return those products. The platform supports multiple categories (electronics, tools, furniture, vehicles, event equipment, outdoor gear, education items, and machinery) within a single experience.

The system serves three primary roles: Customer (renter), Owner (lister), and Admin (platform operator). It manages the complete rental lifecycle from registration and listing through booking, payment, handover, active rental, return, inspection, settlement, and review.

Trust and safety form a core product pillar. The platform must protect both owners and renters against common risks such as non-existent products, non-return of items, damage disputes, identity fraud, and payment issues.

---

### 2. Goals and Objectives

**Primary Goals**
- Provide a seamless end-to-end rental experience across categories.
- Enable owners to monetise idle assets with transparent earnings and minimal operational friction.
- Give customers a reliable way to rent items with clear pricing, availability, and condition evidence.
- Reduce fraud and disputes through identity verification, product verification, security deposits, handover evidence, and risk monitoring.

**Success Metrics (MVP)**
- Successful completion rate of bookings (Confirmed → Completed).
- Percentage of listings that receive Product Verified status.
- Average time from booking request to confirmation.
- Dispute rate and resolution time.
- Owner earnings settlement accuracy and timeline adherence.
- User retention measured by repeat rentals and repeat listings.

---

### 3. Target Users

| Role | Description | Key Needs |
|------|-------------|-----------|
| Customer | Individual or organisation seeking temporary use of products | Easy search and filtering, transparent pricing and deposits, reliable availability, clear handover and return process, secure payments, ability to rate and report |
| Owner | Individual or business listing products for rent | Simple listing flow, verification of ownership and identity, control over availability and requests, earnings visibility, protection via deposits and evidence |
| Admin | Platform operator | User and product approval, monitoring of risk signals, dispute handling, payment and commission oversight, reporting and configuration |

---

### 4. Functional Requirements

#### 4.1 Authentication and User Management
- Registration via mobile number or email with OTP verification.
- Login, forgot-password, and profile management.
- Role-based access (Customer, Owner, Admin). An account may hold both Customer and Owner capabilities.
- Identity verification (KYC): mobile OTP, email OTP, government ID, selfie matching, bank account verification for owners, and address verification where required.
- Only necessary personal data shall be collected; consent must be obtained; raw sensitive identity data (e.g., Aadhaar) shall not be stored unnecessarily. A legitimate KYC provider must be used.

#### 4.2 Product Management
- Owners create listings with name, category, description, images, rental price (hourly/daily/weekly/monthly), security deposit, location, and availability calendar.
- Optional supporting evidence: serial number, purchase invoice, live verification, and owner selfie with product.
- Admin reviews and approves or rejects listings.
- Product Verified badge displayed only after successful verification. Identity verification alone does not constitute product ownership proof.
- Owners manage existing products (edit, deactivate, block dates).

#### 4.3 Discovery and Booking
- Customer home with categories and featured products.
- Category listing, search by name/location, filters, and product detail pages showing images, price, deposit, owner information, ratings, and availability.
- Selection of rental duration and dates; calculation of rental cost + security deposit + platform fee.
- Booking request flow with optional notes and delivery/self-pickup preference.
- Owner acceptance or rejection of requests.
- Payment via integrated gateway; booking confirmation only after successful payment verification via server-side webhooks.

#### 4.4 Handover, Active Rental, and Return
- At handover: both parties confirm condition; photographs uploaded; digital acknowledgement or OTP.
- Status transitions to Active.
- Customer initiates return; owner inspects and uploads return photographs.
- System retains before-and-after condition records for comparison.
- Security deposit held and refunded (full or partial) according to agreed policy after inspection. Clear disclosure of terms and timelines is mandatory.
- Disagreements route to dispute resolution.

#### 4.5 Payments, Settlements, and Reviews
- Supported gateways: Razorpay, Cashfree, or PayU (or equivalent recognised provider).
- Recommended flow: Booking → Payment Gateway → Server-side verification → Confirmation → Handover → Active → Return → Inspection → Settlement → Review.
- Owner receives rental amount minus platform commission.
- Reviews permitted only for completed rentals; one review per booking; verified rental badge; reporting and moderation of reviews.
- Fake-review detection patterns and admin moderation.

#### 4.6 Trust, Safety, and Fraud Prevention
Multi-layered controls:
- Identity and product verification with visible badges (Identity Verified, Product Verified, Bank Verified, Trusted Owner).
- Security deposit system.
- Handover and return photographic evidence with discrepancy flagging.
- Automated fraud detection and risk scoring (illustrative factors only; scores are not definitive proof of fraud). Examples of signals: multiple accounts on same phone, repeated failed payments, unusual booking patterns, suspiciously low prices, repeated complaints.
- Risk levels used for review queues, not automatic permanent bans.
- Emergency reporting for non-delivery, non-return, damage, payment fraud, fake listings, and identity issues.
- Dedicated Trust & Safety / Fraud Monitoring Dashboard for Admin showing pending KYC, unverified products, flagged accounts, disputes, damage cases, return delays, reported listings, and blocked accounts.
- Rental Trust Score / Profile for owners and renters based on verified history (successful rentals, ratings, on-time returns, unresolved complaints). Scores derive from platform records only.

#### 4.7 Admin Capabilities
- Dashboard with key platform metrics.
- User management, owner verification, product approval, category management.
- Booking, payment, return/damage, and review oversight.
- Commission, fee, and platform settings configuration.
- Reports and analytics.
- Dispute management and resolution recording.

#### 4.8 Notifications
- Booking requests, approvals/rejections, payment status, handover reminders, return due dates, deposit settlement, and dispute updates via in-app, SMS, and/or email channels.

---

### 5. Non-Functional Requirements

- Security: Authenticated server-side payment verification; no reliance on customer-uploaded payment screenshots; secure storage of identity and financial data; role-based access control.
- Reliability: Clear status machine for bookings (Pending, Approved, Rejected, Payment Pending, Confirmed, Ready for Pickup, Active, Return Requested, Returned, Inspection Pending, Completed, Dispute, Cancelled, Refund Processing).
- Usability: Role-based navigation and dashboards; mobile-responsive web application.
- Compliance: Consent for data collection; transparent deposit and refund policies; avoidance of indefinite holding of customer funds.
- Scalability considerations for later phases (delivery partners, advanced automation).

---

### 6. Key User Flows (Summary)

**Overall Lifecycle**  
REGISTER → (Customer: Search/Select or Owner: List/Verify) → BOOKING REQUEST → OWNER APPROVAL → PAYMENT & DEPOSIT → CONFIRMATION → HANDOVER (evidence) → ACTIVE RENTAL → RETURN → INSPECTION → DEPOSIT SETTLEMENT → REVIEW → COMPLETED

High-risk bookings may route through manual review before payment confirmation.

**Owner Earnings Example**  
Rental amount minus platform commission (illustrative 10 %) equals owner payout after successful completion and inspection.

---

### 7. Page / Screen Inventory

Approximately 30–44 screens are required when fully expanded; many can be shared across roles. Recommended prioritisation:

**Phase 1 – MVP (Essential)**  
Common: Landing, Register, Login.  
Customer: Home, Search, Product Details, Booking Checkout, Payment, My Bookings.  
Owner: Dashboard, Add Product, Manage Products, Booking Requests.  
Admin: Admin Dashboard, User Management, Product Approval, Booking Management.

**Phase 2**  
Availability calendar, rental tracking, return management, earnings dashboard, payment history, reviews & ratings, notifications, verification status pages, handover confirmation, security deposit details.

**Phase 3**  
Full dispute management, advanced fraud dashboard, Trust Score profiles, damage protection enhancements, delivery partner integration, advanced analytics, automated refunds, recommendation system.

Additional fraud-related pages: Identity Verification, Product Verification, Verification Status, Report a User, Dispute Management, Fraud Monitoring Dashboard, Trust & Safety Settings.

Navigation (illustrative):  
- Customer: Home | Categories | Search | My Bookings | Wishlist | Profile  
- Owner: Dashboard | My Products | Add Product | Bookings | Earnings | Profile  
- Admin: Dashboard | Users | Owners | Products | Categories | Bookings | Payments | Reports | Settings

---

### 8. Recommended Technology Stack

| Layer              | Technology                          |
|--------------------|-------------------------------------|
| Frontend           | React.js                            |
| Backend            | Node.js + Express.js                |
| Database           | PostgreSQL                          |
| Authentication     | JWT + OTP                           |
| Payment Gateway    | Razorpay (or Cashfree / PayU)       |
| Maps & Location    | Google Maps API                     |
| Image Storage      | Cloudinary                          |
| Notifications      | Firebase Cloud Messaging            |
| Hosting            | AWS / Render                        |

---

### 9. Phased Delivery Recommendation

For a college or initial project scope, target 20–25 functional screens covering the five core capabilities:
1. User registration and login (with OTP).
2. Product listing by owners (with basic verification).
3. Product search, details, and availability.
4. Rental booking and payment (including deposit).
5. Product return, inspection, and owner earnings settlement.

Subsequent phases add full KYC, advanced fraud detection, Trust Score, comprehensive dispute tooling, and ecosystem features.

---

### 10. Assumptions and Constraints

- The platform operates primarily in the Indian market (INR pricing, local KYC and payment expectations).
- Physical product handovers occur in person or via arranged delivery; full logistics integration is out of scope for MVP.
- Payment gateway and KYC providers are third-party services; integration must follow their official APIs and compliance requirements.
- Risk scores and badges are decision-support tools only; final enforcement actions remain under human admin review where appropriate.
- Deposit funds handling must comply with applicable payment regulations and provider capabilities regarding holds and refunds.

---

### 11. Out of Scope (Initial Versions)

- Real-time multi-party chat beyond notifications.
- Full logistics / delivery partner network.
- Insurance underwriting or third-party damage insurance products.
- Mobile native applications (web-first).
- Advanced AI-based pricing or recommendation engines (later phase).

---

**Document Owner Notes**  
Trust and safety must be treated as a product differentiator rather than solely an administrative afterthought. The combination of verified identity, verified products, security deposits, photographic handover evidence, risk monitoring, and transparent Trust Profiles is intended to give both owners and renters confidence when exchanging high-value physical items with strangers.

This PRD consolidates the requirements expressed across the provided workflow, page inventory, and fraud-prevention specifications. Further refinement of acceptance criteria, detailed API contracts, and UI wireframes should follow once the MVP scope is confirmed.
