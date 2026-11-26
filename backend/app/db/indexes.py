from app.db.mongo import get_db

async def ensure_indexes():
    db = get_db()
    await db.users.create_index("email", unique=True)
    await db.users.create_index("phone")
    await db.users.create_index("role")
    await db.products.create_index([("owner_id", 1), ("status", 1)])
    await db.products.create_index([("category_id", 1)])
    await db.products.create_index([("status", 1)])
    await db.bookings.create_index([("customer_id", 1), ("created_at", -1)])
    await db.bookings.create_index([("owner_id", 1), ("created_at", -1)])
    await db.bookings.create_index([("product_id", 1)])
    await db.payments.create_index([("booking_id", 1)])
    await db.otps.create_index("key", unique=True)
    await db.notifications.create_index([("user_id", 1), ("created_at", -1)])
