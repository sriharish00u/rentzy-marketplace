from fastapi import APIRouter, Depends, HTTPException
from bson import ObjectId
from app.db.mongo import get_db
from app.core.deps import require_roles
from app.core.roles import ADMIN
from app.models.common import serialize_doc

router = APIRouter(prefix="/api/categories", tags=["categories"])


@router.get("")
async def list_categories():
    db = get_db()
    items = []
    async for c in db.categories.find({"active": {"$ne": False}}).sort("name", 1):
        items.append(serialize_doc(c))
    return items


@router.post("")
async def create_category(payload: dict, admin=Depends(require_roles(ADMIN))):
    db = get_db()
    doc = {"name": payload.get("name","").strip(), "slug": payload.get("slug") or payload.get("name","").lower().replace(" ","-"), "icon": payload.get("icon",""), "active": True}
    if not doc["name"]:
        raise HTTPException(status_code=400, detail="Name required")
    res = await db.categories.insert_one(doc)
    doc["_id"] = res.inserted_id
    return serialize_doc(doc)
