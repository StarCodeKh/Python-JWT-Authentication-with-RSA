from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer
from app.utils.jwt import verify_token
from app.db.mysql import db

security = HTTPBearer()

def auth_required(credentials=Depends(security)):
    token = credentials.credentials
    cursor = db.cursor()
    cursor.execute("SELECT id FROM token_blacklist WHERE token=%s", (token,))
    if cursor.fetchone():
        raise HTTPException(status_code=401, detail="Token has been revoked")
    return verify_token(token)

def admin_required(credentials=Depends(security)):
    user = auth_required(credentials)
    if user.get("role") != "admin":
        raise HTTPException(status_code=403, detail="Admin access required")
    return user