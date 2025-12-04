from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from app.crypto_utils import encrypt_message, decrypt_message
from app.totp_utils import generate_totp, verify_totp

app = FastAPI()

# ---- Models ----
class LoginRequest(BaseModel):
    username: str
    password: str
    totp_code: str = None  # Optional TOTP code

# ---- Dummy user data ----
USER_DB = {
    "akhila": {
        "password": "mypassword",
        "totp_enabled": True  # Require TOTP
    }
}

@app.get("/")
def home():
    return {"message": "PKI + 2FA System Running"}

@app.post("/encrypt")
def encrypt(data: dict):
    try:
        message = data["message"]
        encrypted = encrypt_message(message)
        return {"encrypted_message": encrypted}
    except Exception:
        raise HTTPException(status_code=400, detail="Encryption failed")

@app.post("/decrypt")
def decrypt(data: dict):
    try:
        encrypted_message = data["encrypted_message"]
        decrypted = decrypt_message(encrypted_message)
        return {"decrypted_message": decrypted}
    except Exception:
        raise HTTPException(status_code=400, detail="Decryption failed")

@app.get("/generate-totp")
def generate():
    return {"totp_code": generate_totp()}

@app.post("/verify-totp")
def verify(data: dict):
    code = data["code"]
    is_valid = verify_totp(code)
    return {"valid": is_valid}

@app.post("/login")
def login(data: LoginRequest):
    user = USER_DB.get(data.username)
    if not user:
        raise HTTPException(status_code=401, detail="User not found")
    
    if data.password != user["password"]:
        raise HTTPException(status_code=401, detail="Incorrect password")
    
    if user.get("totp_enabled"):
        if not data.totp_code:
            raise HTTPException(status_code=401, detail="TOTP code required")
        if not verify_totp(data.totp_code):
            raise HTTPException(status_code=401, detail="Invalid TOTP code")
    
    return {"message": f"Login successful for {data.username}"}
