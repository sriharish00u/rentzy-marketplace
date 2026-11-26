from datetime import datetime, timezone
from fastapi import APIRouter, Depends, HTTPException
from bson import ObjectId
from app.db.mongo import get_db
from app.core.deps import get_current_user, require_roles
from app.core.roles import CUSTOMER, OWNER, ADMIN
from app.models.common import serialize_doc
from app.services.upi_mock import build_upi_intent

router = APIRouter(prefix="/api/payments", tags=["payments"])


@router.post("/upi-intent")
async def create_upi_intent(payload: dict, user=Depends(require_roles(CUSTOMER, OWNER, ADMIN))):
    db = get_db()
    booking_id = payload.get("booking_id")
    if not booking_id or not ObjectId.is_valid(booking_id):
        raise HTTPException(status_code=400, detail="Valid booking_id required")
    booking = await db.bookings.find_one({"_id": ObjectId(booking_id)})
    if not booking:
        raise HTTPException(status_code=404, detail="Booking not found")
    if booking.get("customer_id") != str(user["_id"]):
        raise HTTPException(status_code=403, detail="Not your booking")
    amount = float(booking.get("pricing_breakdown", {}).get("total", 0))
    intent = build_upi_intent(amount, booking_id)
    doc = {
        "booking_id": booking_id,
        "customer_id": str(user["_id"]),
        "owner_id": booking.get("owner_id"),
        "amount": amount,
        "currency": "INR",
        "method": "upi_intent_mock",
        "status": "pending",
        "intent_url": intent["intent_url"],
        "txn_ref": intent["txn_ref"],
        "pa": intent["pa"],
        "created_at": datetime.now(timezone.utc),
        "updated_at": datetime.now(timezone.utc),
    }
    res = await db.payments.insert_one(doc)
    doc["_id"] = res.inserted_id
    await db.bookings.update_one({"_id": ObjectId(booking_id)}, {"$set": {"status": "payment_pending", "payment_id": str(res.inserted_id), "updated_at": datetime.now(timezone.utc)}})
    return serialize_doc(doc)


@router.get("/booking/{booking_id}")
async def payments_for_booking(booking_id: str, user=Depends(get_current_user)):
    db = get_db()
    items = []
    async for p in db.payments.find({"booking_id": booking_id}).sort("created_at", -1):
        items.append(serialize_doc(p))
    return items


@router.post("/mock-callback")
async def mock_callback(payload: dict, user=Depends(get_current_user)):
    # mock callback: in real UPI intent flow, app callback/deeplink status would be verified
    db = get_db()
    payment_id = payload.get("payment_id")
    status_val = payload.get("status", "success")
    if not payment_id or not ObjectId.is_valid(payment_id):
        raise HTTPException(status_code=400, detail="Valid payment_id required")
    payment = await db.payments.find_one({"_id": ObjectId(payment_id)})
    if not payment:
        raise HTTPException(status_code=404, detail="Payment not found")
    if user["role"] != ADMIN and payment.get("customer_id") != str(user["_id"]):
        raise HTTPException(status_code=403, detail="Forbidden")
    if status_val not in {"success", "failed"}:
        raise HTTPException(status_code=400, detail="Invalid status")
    pay_status = "paid" if status_val == "success" else "failed"
    await db.payments.update_one({"_id": ObjectId(payment_id)}, {"$set": {"status": pay_status, "updated_at": datetime.now(timezone.utc), "callback_payload": payload}})
    booking_update = {"payment_status": pay_status, "updated_at": datetime.now(timezone.utc)}
    if pay_status == "paid":
        booking_update["status"] = "confirmed"
    await db.bookings.update_one({"_id": ObjectId(payment.get("booking_id"))}, {"$set": booking_update})
    return {"ok": True, "payment_status": pay_status, "booking_status": "confirmed" if pay_status == "paid" else "payment_pending"}
