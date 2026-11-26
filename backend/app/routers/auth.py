from datetime import datetime, timezone
from fastapi import APIRouter, HTTPException, Depends
from bson import ObjectId
from app.db.mongo import get_db
from app.models.auth import RegisterRequest, LoginRequest, OTPRequest, OTPVerifyRequest, ForgotPasswordRequest, ResetPasswordRequest
from app.core.security import hash_password, verify_password, create_access_token
from app.core.deps import get_current_user
from app.services.otp_mock import create_otp, verify_otp
from app.models.common import serialize_doc

router = APIRouter(prefix="/api/auth", tags=["auth"])


def public_user(u: dict) -> dict:
    u = serialize_doc(u)
    u.pop("password_hash", None)
    return u


@router.post("/register")
async def register(payload: RegisterRequest):
    db = get_db()
    email = payload.email.lower()
    existing = await db.users.find_one({"email": email})
    if existing:
        raise HTTPException(status_code=400, detail="Email already registered")
    doc = {
        "name": payload.name.strip(),
        "email": email,
        "phone": payload.phone.strip(),
        "password_hash": hash_password(payload.password),
        "role": payload.role,
        "kyc_status": "pending",
        "trust_score": 50,
        "blocked": False,
        "email_verified": False,
        "created_at": datetime.now(timezone.utc),
        "updated_at": datetime.now(timezone.utc),
    }
    res = await db.users.insert_one(doc)
    doc["_id"] = res.inserted_id
    otp = await create_otp(email, "verify")
    token = create_access_token({"sub": str(res.inserted_id), "role": doc["role"]})
    return {"access_token": token, "token_type": "bearer", "user": public_user(doc), "mock_otp": otp}


@router.post("/login")
async def login(payload: LoginRequest):
    db = get_db()
    email = payload.email.lower()
    user = await db.users.find_one({"email": email})
    if not user or not verify_password(payload.password, user.get("password_hash", "")):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    if user.get("blocked"):
        raise HTTPException(status_code=403, detail="User blocked")
    token = create_access_token({"sub": str(user["_id"]), "role": user["role"]})
    return {"access_token": token, "token_type": "bearer", "user": public_user(user)}


@router.get("/me")
async def me(user=Depends(get_current_user)):
    return public_user(user)


@router.post("/otp/request")
async def otp_request(payload: OTPRequest):
    db = get_db()
    email = payload.email.lower()
    user = await db.users.find_one({"email": email})
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    code = await create_otp(email, payload.purpose)
    return {"ok": True, "message": "Mock OTP generated", "mock_otp": code}


@router.post("/otp/verify")
async def otp_verify(payload: OTPVerifyRequest):
    db = get_db()
    email = payload.email.lower()
    ok = await verify_otp(email, payload.purpose, payload.code)
    if not ok:
        raise HTTPException(status_code=400, detail="Invalid or expired OTP")
    if payload.purpose == "verify":
        await db.users.update_one({"email": email}, {"$set": {"email_verified": True, "updated_at": datetime.now(timezone.utc)}})
    return {"ok": True}


@router.post("/forgot-password")
async def forgot_password(payload: ForgotPasswordRequest):
    db = get_db()
    email = payload.email.lower()
    user = await db.users.find_one({"email": email})
    if not user:
        # avoid leaking existence; still return ok
        return {"ok": True, "message": "If account exists, mock OTP generated"}
    code = await create_otp(email, "reset")
    return {"ok": True, "message": "Mock OTP generated", "mock_otp": code}


@router.post("/reset-password")
async def reset_password(payload: ResetPasswordRequest):
    db = get_db()
    email = payload.email.lower()
    ok = await verify_otp(email, "reset", payload.code)
    if not ok:
        raise HTTPException(status_code=400, detail="Invalid or expired OTP")
    await db.users.update_one({"email": email}, {"$set": {"password_hash": hash_password(payload.new_password), "updated_at": datetime.now(timezone.utc)}})
    return {"ok": True}
