from fastapi import APIRouter, Depends
from app.db.mongo import get_db
from app.core.deps import require_roles
from app.core.roles import ADMIN, OWNER, CUSTOMER
from app.models.common import serialize_doc

router = APIRouter(prefix="/api/dashboard", tags=["dashboard"])


@router.get("/user")
@router.get("/owner")
async def user_dashboard(user=Depends(require_roles(CUSTOMER, OWNER, ADMIN))):
    db = get_db()
    uid = str(user["_id"])
    is_admin = user["role"] == ADMIN

    # Both listing & booking stats
    my_products_count = await db.products.count_documents({} if is_admin else {"owner_id": uid})
    
    # Bookings where user is renter (customer)
    as_renter_bookings = await db.bookings.count_documents({} if is_admin else {"customer_id": uid})
    
    # Bookings where user is item owner
    as_owner_bookings = await db.bookings.count_documents({} if is_admin else {"owner_id": uid})
    
    pending_incoming = await db.bookings.count_documents({**({} if is_admin else {"owner_id": uid}), "status": "pending"})
    active_incoming = await db.bookings.count_documents({**({} if is_admin else {"owner_id": uid}), "status": {"$in": ["confirmed", "ready_for_pickup", "active", "return_requested"]}})
    completed_incoming = await db.bookings.count_documents({**({} if is_admin else {"owner_id": uid}), "status": "completed"})
    
    # Earnings from owned items that received payment
    paid_query = {**({} if is_admin else {"owner_id": uid}), "status": "paid"}
    earnings = 0.0
    async for p in db.payments.find(paid_query):
        earnings += float(p.get("amount", 0))

    # Recent activity
    recent_bookings = []
    async for b in db.bookings.find({} if is_admin else {"$or": [{"customer_id": uid}, {"owner_id": uid}]}).sort("created_at", -1).limit(10):
        recent_bookings.append(serialize_doc(b))

    return {
        "total_products": my_products_count,
        "as_renter_bookings": as_renter_bookings,
        "as_owner_bookings": as_owner_bookings,
        "total_bookings": as_renter_bookings + as_owner_bookings if not is_admin else await db.bookings.count_documents({}),
        "pending_requests": pending_incoming,
        "active_rentals": active_incoming,
        "completed_rentals": completed_incoming,
        "earnings": round(earnings, 2),
        "recent_bookings": recent_bookings,
    }


@router.get("/admin")
async def admin_dashboard(user=Depends(require_roles(ADMIN))):
    db = get_db()
    users_count = await db.users.count_documents({"role": {"$ne": "admin"}})
    pending_kyc = await db.users.count_documents({"kyc_status": "pending"})
    verified_kyc = await db.users.count_documents({"kyc_status": "verified"})
    blocked_users = await db.users.count_documents({"blocked": True})

    total_products = await db.products.count_documents({})
    total_bookings = await db.bookings.count_documents({})
    active_rentals = await db.bookings.count_documents({"status": {"$in": ["confirmed","ready_for_pickup","active","return_requested"]}})
    completed_rentals = await db.bookings.count_documents({"status": "completed"})
    
    total_revenue = 0.0
    async for p in db.payments.find({"status": "paid"}):
        total_revenue += float(p.get("amount", 0))

    # Recent live registrations & transactions
    recent_users = []
    async for u in db.users.find().sort("created_at", -1).limit(5):
        recent_users.append({"id": str(u["_id"]), "name": u.get("name"), "email": u.get("email"), "role": u.get("role"), "kyc_status": u.get("kyc_status"), "blocked": u.get("blocked", False)})

    recent_bookings = []
    async for b in db.bookings.find().sort("created_at", -1).limit(6):
        recent_bookings.append(serialize_doc(b))

    return {
        "total_users": users_count,
        "pending_kyc": pending_kyc,
        "verified_kyc": verified_kyc,
        "blocked_users": blocked_users,
        "total_products": total_products,
        "total_bookings": total_bookings,
        "active_rentals": active_rentals,
        "completed_rentals": completed_rentals,
        "total_revenue": round(total_revenue, 2),
        "recent_users": recent_users,
        "recent_bookings": recent_bookings,
    }
