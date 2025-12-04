import pyotp

SECRET_KEY = "JBSWY3DPEHPK3PXP"   # FIXED SECRET (can be any valid base32)

totp = pyotp.TOTP(SECRET_KEY)

def generate_totp():
    return totp.now()

def verify_totp(code: str):
    return totp.verify(code)
