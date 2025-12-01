from fastapi import FastAPI, HTTPException
from app.crypto_utils import encrypt_message, decrypt_message
from app.totp_utils import generate_totp, verify_totp

app = FastAPI()

@app.get("/")
def home():
    return {"message": "PKI + 2FA System Running"}

# ----------- PKI ENCRYPTION -----------

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

# ----------- TOTP 2FA -----------

@app.get("/generate-totp")
def generate():
    return {"totp_code": generate_totp()}

@app.post("/verify-totp")
def verify(data: dict):
    code = data["code"]
    is_valid = verify_totp(code)
    return {"valid": is_valid}
