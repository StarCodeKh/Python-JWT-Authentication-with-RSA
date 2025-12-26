from fastapi import APIRouter, HTTPException
import bcrypt
from app.utils.rsa import decrypt_password
from app.utils.jwt import sign_token
from app.db.mysql import db

router = APIRouter()

@router.post("/login")
def login(data: dict):
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users WHERE email=%s", (data["email"],))
    user = cursor.fetchone()
    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    decrypted = decrypt_password(data["password"])
    if not bcrypt.checkpw(decrypted.encode(), user["password"].encode()):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    return {
        "user": {
            "id": user["id"],
            "email": user["email"],
            "role": user["role"]
        },
        "access_token": sign_token(user),
        "token_type": "Bearer"
    }