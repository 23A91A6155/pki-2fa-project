import pyotp

# Static seed for demo
SECRET_KEY = "JBSWY3DPEHPK3PXP"

def generate_totp():
    totp = pyotp.TOTP(SECRET_KEY)
    return totp.now()

def verify_totp(code):
    totp = pyotp.TOTP(SECRET_KEY)
    return totp.verify(code)
