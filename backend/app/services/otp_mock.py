from datetime import datetime, timedelta, timezone
import random
from app.db.mongo import get_db

OTP_TTL_MINUTES = 10

async def create_otp(key: str, purpose: str) -> str:
    db = get_db()
    code = f"{random.randint(100000, 999999)}"
    doc = {
        "key": f"{purpose}:{key}",
        "code": code,
        "purpose": purpose,
        "target": key,
        "expires_at": datetime.now(timezone.utc) + timedelta(minutes=OTP_TTL_MINUTES),
        "verified": False,
    }
    await db.otps.update_one({"key": doc["key"]}, {"$set": doc}, upsert=True)
    return code


async def verify_otp(key: str, purpose: str, code: str) -> bool:
    db = get_db()
    k = f"{purpose}:{key}"
    doc = await db.otps.find_one({"key": k})
    if not doc:
        return False
    exp = doc.get("expires_at")
    if exp and exp.replace(tzinfo=timezone.utc) < datetime.now(timezone.utc):
        return False
    if doc.get("code") != code:
        return False
    await db.otps.update_one({"key": k}, {"$set": {"verified": True}})
    return True
