from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
import base64

with open("storage/rsa/private.pem", "rb") as f:
    private_key = serialization.load_pem_private_key(
        f.read(),
        password=None
    )

def decrypt_password(encrypted):
    decrypted = private_key.decrypt(
        base64.b64decode(encrypted),
        padding.PKCS1v15()
    )
    return decrypted.decode()