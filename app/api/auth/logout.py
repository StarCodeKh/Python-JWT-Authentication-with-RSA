from fastapi import APIRouter, Depends
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from app.db.mysql import db

router = APIRouter()
security = HTTPBearer()

@router.post("/logout")
def logout(credentials: HTTPAuthorizationCredentials = Depends(security)):
    token = credentials.credentials
    cursor = db.cursor()
    cursor.execute("INSERT INTO token_blacklist (token) VALUES (%s)", (token,))
    db.commit()
    return {"message": "Successfully logged out"}