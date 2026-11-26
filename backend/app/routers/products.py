from datetime import datetime, timezone
from fastapi import APIRouter, Depends, HTTPException, Query
from bson import ObjectId
from app.db.mongo import get_db
from app.core.deps import get_current_user, require_roles
from app.core.roles import ADMIN, OWNER, CUSTOMER
from app.models.common import serialize_doc

router = APIRouter(prefix="/api/products", tags=["products"])


def product_doc(payload: dict, owner_id: str) -> dict:
    return {
        "owner_id": owner_id,
        "title": payload.get("title", "").strip(),
        "description": payload.get("description", "").strip(),
        "category_id": payload.get("category_id"),
        "category_name": payload.get("category_name", ""),
        "images": payload.get("images", []),
        "location": payload.get("location", ""),
        "pricing": {
            "hour": float(payload.get("price_hour") or payload.get("pricing", {}).get("hour") or 0),
            "day": float(payload.get("price_day") or payload.get("pricing", {}).get("day") or 0),
            "week": float(payload.get("price_week") or payload.get("pricing", {}).get("week") or 0),
            "month": float(payload.get("price_month") or payload.get("pricing", {}).get("month") or 0),
        },
        "deposit": float(payload.get("deposit", 0)),
        "availability": payload.get("availability", "available"),
        "status": "approved",  # Instant live publishing - no admin approval required
        "rules": payload.get("rules", ""),
        "created_at": datetime.now(timezone.utc),
        "updated_at": datetime.now(timezone.utc),
    }


@router.get("")
async def list_products(q: str | None = None, category_id: str | None = None, status: str | None = Query(default="approved"), owner_id: str | None = None):
    db = get_db()
    filt = {}
    if status:
        filt["status"] = status
    if owner_id:
        filt["owner_id"] = owner_id
    if category_id:
        filt["category_id"] = category_id
    if q:
        filt["$or"] = [{"title": {"$regex": q, "$options": "i"}}, {"description": {"$regex": q, "$options": "i"}}, {"location": {"$regex": q, "$options": "i"}}]
    items = []
    async for p in db.products.find(filt).sort("created_at", -1):
        items.append(serialize_doc(p))
    return items


@router.get("/mine")
async def my_products(user=Depends(require_roles(CUSTOMER, OWNER, ADMIN))):
    db = get_db()
    filt = {} if user["role"] == "admin" else {"owner_id": str(user["_id"])}
    items = []
    async for p in db.products.find(filt).sort("created_at", -1):
        items.append(serialize_doc(p))
    return items


@router.get("/{product_id}")
async def get_product(product_id: str):
    if not ObjectId.is_valid(product_id):
        raise HTTPException(status_code=400, detail="Invalid id")
    db = get_db()
    p = await db.products.find_one({"_id": ObjectId(product_id)})
    if not p:
        raise HTTPException(status_code=404, detail="Product not found")
    owner = await db.users.find_one({"_id": ObjectId(p["owner_id"])}) if ObjectId.is_valid(str(p.get("owner_id",""))) else None
    p = serialize_doc(p)
    p["owner"] = {"id": str(owner["_id"]), "name": owner.get("name"), "kyc_status": owner.get("kyc_status"), "trust_score": owner.get("trust_score", 50)} if owner else None
    return p


@router.post("")
async def create_product(payload: dict, user=Depends(require_roles(CUSTOMER, OWNER, ADMIN))):
    db = get_db()
    doc = product_doc(payload, str(user["_id"]))
    if not doc["title"]:
        raise HTTPException(status_code=400, detail="Title required")
    doc["status"] = "approved"  # Always active & approved instantly
    res = await db.products.insert_one(doc)
    doc["_id"] = res.inserted_id
    return serialize_doc(doc)


@router.put("/{product_id}")
async def update_product(product_id: str, payload: dict, user=Depends(require_roles(CUSTOMER, OWNER, ADMIN))):
    if not ObjectId.is_valid(product_id):
        raise HTTPException(status_code=400, detail="Invalid id")
    db = get_db()
    p = await db.products.find_one({"_id": ObjectId(product_id)})
    if not p:
        raise HTTPException(status_code=404, detail="Not found")
    if user["role"] != "admin" and str(p.get("owner_id")) != str(user["_id"]):
        raise HTTPException(status_code=403, detail="Not your product")
    allowed = {"title","description","category_id","category_name","images","location","pricing","deposit","availability","rules","price_hour","price_day","price_week","price_month"}
    update = {k:v for k,v in payload.items() if k in allowed}
    if any(k in update for k in ["price_hour","price_day","price_week","price_month"]):
        pricing = p.get("pricing",{})
        for k in ["hour","day","week","month"]:
            pk = f"price_{k}"
            if pk in update: pricing[k] = float(update.pop(pk) or 0)
        update["pricing"] = pricing
    update["updated_at"] = datetime.now(timezone.utc)
    await db.products.update_one({"_id": ObjectId(product_id)}, {"$set": update})
    return serialize_doc(await db.products.find_one({"_id": ObjectId(product_id)}))


@router.delete("/{product_id}")
async def delete_product(product_id: str, user=Depends(require_roles(CUSTOMER, OWNER, ADMIN))):
    if not ObjectId.is_valid(product_id):
        raise HTTPException(status_code=400, detail="Invalid id")
    db = get_db()
    p = await db.products.find_one({"_id": ObjectId(product_id)})
    if not p:
        raise HTTPException(status_code=404, detail="Not found")
    if user["role"] != "admin" and str(p.get("owner_id")) != str(user["_id"]):
        raise HTTPException(status_code=403, detail="Not your product")
    await db.products.delete_one({"_id": ObjectId(product_id)})
    return {"ok": True}


@router.patch("/{product_id}/status")
async def set_product_status(product_id: str, payload: dict, admin=Depends(require_roles(ADMIN))):
    if not ObjectId.is_valid(product_id):
        raise HTTPException(status_code=400, detail="Invalid id")
    status_val = payload.get("status")
    if status_val not in {"pending","approved","rejected","inactive"}:
        raise HTTPException(status_code=400, detail="Invalid status")
    db = get_db()
    await db.products.update_one({"_id": ObjectId(product_id)}, {"$set": {"status": status_val, "updated_at": datetime.now(timezone.utc)}})
    return {"ok": True, "status": status_val}
