from fastapi import APIRouter
import bcrypt
from app.db.mysql import db

router = APIRouter()

@router.post("/register")
def register(data: dict):
    cursor = db.cursor()
    hashed = bcrypt.hashpw(data["password"].encode(), bcrypt.gensalt())
    cursor.execute(
        "INSERT INTO users (name, email, password, role) VALUES (%s, %s, %s, %s)",
        (data["name"], data["email"], hashed, data.get("role", "user"))
    )
    db.commit()
    return {"message": "User registered successfully"}