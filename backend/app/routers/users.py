from datetime import datetime, timezone
from fastapi import APIRouter, Depends, HTTPException
from bson import ObjectId
from app.db.mongo import get_db
from app.core.deps import get_current_user, require_roles
from app.core.roles import ADMIN
from app.models.common import serialize_doc

router = APIRouter(prefix="/api/users", tags=["users"])


@router.get("/me")
async def get_me(user=Depends(get_current_user)):
    u = serialize_doc(user)
    u.pop("password_hash", None)
    return u


@router.put("/me")
async def update_me(payload: dict, user=Depends(get_current_user)):
    db = get_db()
    allowed = {"name", "phone", "profile", "address", "bank_details", "kyc_status"}
    update = {k: v for k, v in payload.items() if k in allowed}
    update["updated_at"] = datetime.now(timezone.utc)
    await db.users.update_one({"_id": user["_id"]}, {"$set": update})
    fresh = await db.users.find_one({"_id": user["_id"]})
    fresh = serialize_doc(fresh)
    fresh.pop("password_hash", None)
    return fresh


@router.get("")
async def list_users(user=Depends(require_roles(ADMIN))):
    db = get_db()
    users = []
    async for u in db.users.find().sort("created_at", -1):
        uid = str(u["_id"])
        prod_count = await db.products.count_documents({"owner_id": uid})
        booking_count = await db.bookings.count_documents({"$or": [{"customer_id": uid}, {"owner_id": uid}]})
        u = serialize_doc(u)
        u.pop("password_hash", None)
        u["products_count"] = prod_count
        u["bookings_count"] = booking_count
        users.append(u)
    return users


@router.get("/{user_id}")
async def get_user_detail(user_id: str, admin=Depends(require_roles(ADMIN))):
    if not ObjectId.is_valid(user_id):
        raise HTTPException(status_code=400, detail="Invalid user id")
    db = get_db()
    u = await db.users.find_one({"_id": ObjectId(user_id)})
    if not u:
        raise HTTPException(status_code=404, detail="User not found")
    uid = str(u["_id"])
    u = serialize_doc(u)
    u.pop("password_hash", None)
    
    # Enrich with all available data of this user/role
    products = [serialize_doc(p) async for p in db.products.find({"owner_id": uid}).sort("created_at", -1)]
    as_customer_bookings = [serialize_doc(b) async for b in db.bookings.find({"customer_id": uid}).sort("created_at", -1)]
    as_owner_bookings = [serialize_doc(b) async for b in db.bookings.find({"owner_id": uid}).sort("created_at", -1)]
    payments = [serialize_doc(p) async for p in db.payments.find({"$or": [{"customer_id": uid}, {"owner_id": uid}]}).sort("created_at", -1)]
    
    u["products"] = products
    u["as_customer_bookings"] = as_customer_bookings
    u["as_owner_bookings"] = as_owner_bookings
    u["payments"] = payments
    return u


@router.patch("/{user_id}/block")
async def block_user(user_id: str, payload: dict, admin=Depends(require_roles(ADMIN))):
    if not ObjectId.is_valid(user_id):
        raise HTTPException(status_code=400, detail="Invalid user id")
    db = get_db()
    blocked = bool(payload.get("blocked", True))
    await db.users.update_one({"_id": ObjectId(user_id)}, {"$set": {"blocked": blocked, "updated_at": datetime.now(timezone.utc)}})
    return {"ok": True, "blocked": blocked}


@router.patch("/{user_id}/verify")
async def verify_user(user_id: str, payload: dict, admin=Depends(require_roles(ADMIN))):
    if not ObjectId.is_valid(user_id):
        raise HTTPException(status_code=400, detail="Invalid user id")
    db = get_db()
    status_val = payload.get("kyc_status", "verified")
    await db.users.update_one({"_id": ObjectId(user_id)}, {"$set": {"kyc_status": status_val, "trust_score": 95 if status_val=="verified" else 50, "updated_at": datetime.now(timezone.utc)}})
    return {"ok": True, "kyc_status": status_val}


@router.delete("/{user_id}")
async def delete_user(user_id: str, admin=Depends(require_roles(ADMIN))):
    if not ObjectId.is_valid(user_id):
        raise HTTPException(status_code=400, detail="Invalid user id")
    db = get_db()
    res = await db.users.delete_one({"_id": ObjectId(user_id)})
    if res.deleted_count == 0:
        raise HTTPException(status_code=404, detail="User not found")
    return {"ok": True, "deleted_id": user_id}
