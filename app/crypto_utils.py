from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes

# ----------- Generate RSA Keys -----------
private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
public_key = private_key.public_key()

def encrypt_message(message: str) -> str:
    encrypted = public_key.encrypt(
        message.encode(),
        padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()),
                     algorithm=hashes.SHA256(),
                     label=None),
    )
    return encrypted.hex()

def decrypt_message(encrypted_hex: str) -> str:
    encrypted = bytes.fromhex(encrypted_hex)
    decrypted = private_key.decrypt(
        encrypted,
        padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()),
                     algorithm=hashes.SHA256(),
                     label=None),
    )
    return decrypted.decode()
