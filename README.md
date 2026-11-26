# Rental Marketplace MVP

Full-stack MVP for an all-in-one rental marketplace.

## Stack
- **Frontend**: HTML, CSS, vanilla JS (Stitch-inspired design system)
- **Backend**: Python FastAPI
- **Database**: MongoDB (`DATABASE_URL` and `DB_NAME` loaded directly from `../CollabHub/backend/.env`)

## Features (MVP)
- Auth: register/login, mock OTP verification, JWT, role-based access (customer/owner/admin)
- Products: browse/search/detail, owner add/manage, admin approve/reject
- Bookings: availability check, create booking, owner approve/reject/complete
- Payments: mock UPI intent generation + mock callback simulation
- Dashboards: owner and admin summaries

## Run backend

```bash
cd backend
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
```

Backend serves API at `http://localhost:8000/api` and frontend at `http://localhost:8000/`.

## Demo accounts (seeded on startup)
- Admin: `admin@rental.local` / `admin123`
- Owner: `owner@rental.local` / `owner123`
- Customer: `customer@rental.local` / `customer123`

## Notes
- MongoDB config is read directly from `../CollabHub/backend/.env` (`DATABASE_URL`, `DB_NAME`).
- OTP and UPI payment flows are mocked for MVP.
- Uploaded product images use image URLs in MVP.
