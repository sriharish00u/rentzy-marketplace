from pydantic import BaseModel, EmailStr, Field

class RegisterRequest(BaseModel):
    name: str = Field(min_length=2, max_length=80)
    email: EmailStr
    phone: str = Field(min_length=8, max_length=20)
    password: str = Field(min_length=6, max_length=128)
    role: str = Field(pattern="^(customer|owner)$")

class LoginRequest(BaseModel):
    email: EmailStr
    password: str

class OTPRequest(BaseModel):
    email: EmailStr
    purpose: str = Field(default="verify", pattern="^(verify|reset)$")

class OTPVerifyRequest(BaseModel):
    email: EmailStr
    code: str = Field(min_length=4, max_length=8)
    purpose: str = Field(default="verify", pattern="^(verify|reset)$")

class ForgotPasswordRequest(BaseModel):
    email: EmailStr

class ResetPasswordRequest(BaseModel):
    email: EmailStr
    code: str
    new_password: str = Field(min_length=6, max_length=128)

class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
    user: dict
