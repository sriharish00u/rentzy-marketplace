from datetime import datetime, timezone
from app.db.mongo import get_db
from app.core.security import hash_password

CATEGORIES = [
    {"name": "Electronics", "slug": "electronics", "icon": "devices", "active": True},
    {"name": "Vehicles", "slug": "vehicles", "icon": "directions_car", "active": True},
    {"name": "Tools", "slug": "tools", "icon": "construction", "active": True},
    {"name": "Furniture", "slug": "furniture", "icon": "chair", "active": True},
    {"name": "Event Equipment", "slug": "event-equipment", "icon": "celebration", "active": True},
]

async def seed():
    db = get_db()
    # categories
    for c in CATEGORIES:
        await db.categories.update_one({"slug": c["slug"]}, {"$setOnInsert": c}, upsert=True)
    # admin
    admin_email = "admin@rental.local"
    await db.users.update_one(
        {"email": admin_email},
        {"$setOnInsert": {
            "name": "Platform Admin",
            "email": admin_email,
            "phone": "9999999999",
            "password_hash": hash_password("admin123"),
            "role": "admin",
            "kyc_status": "verified",
            "trust_score": 100,
            "blocked": False,
            "email_verified": True,
            "created_at": datetime.now(timezone.utc),
            "updated_at": datetime.now(timezone.utc),
        }},
        upsert=True,
    )
    # demo owner
    owner_email = "owner@rental.local"
    owner = await db.users.find_one({"email": owner_email})
    if not owner:
        res = await db.users.insert_one({
            "name": "Demo Owner",
            "email": owner_email,
            "phone": "8888888888",
            "password_hash": hash_password("owner123"),
            "role": "owner",
            "kyc_status": "verified",
            "trust_score": 92,
            "blocked": False,
            "email_verified": True,
            "created_at": datetime.now(timezone.utc),
            "updated_at": datetime.now(timezone.utc),
        })
        owner_id = str(res.inserted_id)
    else:
        owner_id = str(owner["_id"])
    # demo customer
    await db.users.update_one(
        {"email": "customer@rental.local"},
        {"$setOnInsert": {
            "name": "Demo Customer",
            "email": "customer@rental.local",
            "phone": "7777777777",
            "password_hash": hash_password("customer123"),
            "role": "customer",
            "kyc_status": "verified",
            "trust_score": 85,
            "blocked": False,
            "email_verified": True,
            "created_at": datetime.now(timezone.utc),
            "updated_at": datetime.now(timezone.utc),
        }},
        upsert=True,
    )
    # demo products
    if await db.products.count_documents({}) == 0:
        cat = await db.categories.find_one({"slug": "electronics"})
        cat2 = await db.categories.find_one({"slug": "tools"})
        await db.products.insert_many([
            {
                "owner_id": owner_id, "title": "Sony Alpha Camera Kit", "description": "Professional mirrorless camera with 24-70mm lens. Ideal for events and shoots.",
                "category_id": str(cat["_id"]) if cat else None, "category_name": "Electronics",
                "images": ["https://images.unsplash.com/photo-1516035069371-29a1b244cc32?w=800&q=80"],
                "location": "Coimbatore", "pricing": {"hour": 200, "day": 1500, "week": 8000, "month": 25000},
                "deposit": 5000, "availability": "available", "status": "approved", "rules": "Handle with care. Return with all accessories.",
                "created_at": datetime.now(timezone.utc), "updated_at": datetime.now(timezone.utc),
            },
            {
                "owner_id": owner_id, "title": "Bosch Drill Machine Set", "description": "Heavy-duty drill with bit set and case. Perfect for home and site work.",
                "category_id": str(cat2["_id"]) if cat2 else None, "category_name": "Tools",
                "images": ["https://images.unsplash.com/photo-1504148455328-c376907d081c?w=800&q=80"],
                "location": "Coimbatore", "pricing": {"hour": 100, "day": 500, "week": 2500, "month": 8000},
                "deposit": 1500, "availability": "available", "status": "approved", "rules": "Return clean and in working condition.",
                "created_at": datetime.now(timezone.utc), "updated_at": datetime.now(timezone.utc),
            },
        ])
