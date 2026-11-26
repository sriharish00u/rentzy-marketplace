from datetime import datetime, timezone
from fastapi import APIRouter, Depends, HTTPException
from bson import ObjectId
from app.db.mongo import get_db
from app.core.deps import get_current_user, require_roles
from app.core.roles import ADMIN, OWNER, CUSTOMER
from app.models.common import serialize_doc
from app.services.booking_service import dates_overlap, ACTIVE_STATUSES, compute_total

router = APIRouter(prefix="/api/bookings", tags=["bookings"])


async def check_availability(db, product_id: str, start: str, end: str, exclude_booking_id: str | None = None):
    async for b in db.bookings.find({"product_id": product_id, "status": {"$in": list(ACTIVE_STATUSES)}}):
        if exclude_booking_id and str(b["_id"]) == exclude_booking_id:
            continue
        if dates_overlap(start, end, b["start_date"], b["end_date"]):
            return False
    return True


@router.get("")
async def list_bookings(user=Depends(get_current_user)):
    db = get_db()
    role = user["role"]
    uid = str(user["_id"])
    filt = {}
    if role == CUSTOMER:
        filt["customer_id"] = uid
    elif role == OWNER:
        filt["owner_id"] = uid
    # admin sees all
    items = []
    async for b in db.bookings.find(filt).sort("created_at", -1):
        items.append(serialize_doc(b))
    return items


@router.get("/{booking_id}")
async def get_booking(booking_id: str, user=Depends(get_current_user)):
    if not ObjectId.is_valid(booking_id):
        raise HTTPException(status_code=400, detail="Invalid id")
    db = get_db()
    b = await db.bookings.find_one({"_id": ObjectId(booking_id)})
    if not b:
        raise HTTPException(status_code=404, detail="Not found")
    uid = str(user["_id"])
    if user["role"] != ADMIN and uid not in {b.get("customer_id"), b.get("owner_id")}:
        raise HTTPException(status_code=403, detail="Forbidden")
    return serialize_doc(b)


@router.post("/check-availability")
async def availability(payload: dict):
    db = get_db()
    product_id = payload.get("product_id")
    start = payload.get("start_date")
    end = payload.get("end_date")
    if not product_id or not start or not end:
        raise HTTPException(status_code=400, detail="product_id, start_date, end_date required")
    ok = await check_availability(db, product_id, start, end)
    return {"available": ok}


@router.post("")
async def create_booking(payload: dict, user=Depends(require_roles(CUSTOMER, OWNER, ADMIN))):
    db = get_db()
    product_id = payload.get("product_id")
    if not product_id or not ObjectId.is_valid(product_id):
        raise HTTPException(status_code=400, detail="Valid product_id required")
    product = await db.products.find_one({"_id": ObjectId(product_id), "status": "approved"})
    if not product:
        raise HTTPException(status_code=404, detail="Product not available")
    start = payload.get("start_date")
    end = payload.get("end_date")
    if not start or not end or start > end:
        raise HTTPException(status_code=400, detail="Invalid dates")
    ok = await check_availability(db, product_id, start, end)
    if not ok:
        raise HTTPException(status_code=409, detail="Product not available for selected dates")
    duration_unit = payload.get("duration_unit", "day")
    duration = int(payload.get("duration", 1))
    totals = compute_total(product.get("pricing", {}), duration_unit, duration, float(product.get("deposit", 0)))
    doc = {
        "product_id": product_id,
        "product_title": product.get("title"),
        "product_image": (product.get("images") or [None])[0],
        "owner_id": str(product.get("owner_id")),
        "customer_id": str(user["_id"]),
        "customer_name": user.get("name"),
        "start_date": start,
        "end_date": end,
        "duration_unit": duration_unit,
        "duration": duration,
        "pricing_breakdown": totals,
        "status": "pending",
        "payment_status": "unpaid",
        "notes": payload.get("notes", ""),
        "created_at": datetime.now(timezone.utc),
        "updated_at": datetime.now(timezone.utc),
    }
    res = await db.bookings.insert_one(doc)
    doc["_id"] = res.inserted_id
    return serialize_doc(doc)


@router.patch("/{booking_id}/status")
async def update_booking_status(booking_id: str, payload: dict, user=Depends(get_current_user)):
    if not ObjectId.is_valid(booking_id):
        raise HTTPException(status_code=400, detail="Invalid id")
    db = get_db()
    b = await db.bookings.find_one({"_id": ObjectId(booking_id)})
    if not b:
        raise HTTPException(status_code=404, detail="Not found")
    uid = str(user["_id"])
    role = user["role"]
    new_status = payload.get("status")
    allowed = {"pending","approved","rejected","payment_pending","confirmed","ready_for_pickup","active","return_requested","returned","inspection_pending","completed","dispute","cancelled","refund_processing"}
    if new_status not in allowed:
        raise HTTPException(status_code=400, detail="Invalid status")
    # simple role rules
    owner_only = {"approved","rejected","ready_for_pickup","returned","inspection_pending","completed"}
    customer_only = {"return_requested","cancelled"}
    if new_status in owner_only and role != ADMIN and uid != b.get("owner_id"):
        raise HTTPException(status_code=403, detail="Only owner/admin can set this status")
    if new_status in customer_only and role != ADMIN and uid != b.get("customer_id"):
        raise HTTPException(status_code=403, detail="Only customer/admin can set this status")
    await db.bookings.update_one({"_id": ObjectId(booking_id)}, {"$set": {"status": new_status, "updated_at": datetime.now(timezone.utc)}})
    return {"ok": True, "status": new_status}
