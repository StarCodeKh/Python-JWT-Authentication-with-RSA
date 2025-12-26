from fastapi import APIRouter, HTTPException, Depends, Request
from app.middleware.auth import admin_required
from app.db.mysql import db

router = APIRouter()

@router.get("/users")
def list_users(user=Depends(admin_required)):
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT id, name, email, role, created_at FROM users")
    users = cursor.fetchall()
    return {"users": users}

@router.get("/users/{user_id}")
def get_user(user_id: int, user=Depends(admin_required)):
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT id, name, email, role, created_at FROM users WHERE id=%s", (user_id,))
    user_data = cursor.fetchone()
    if not user_data:
        raise HTTPException(status_code=404, detail="User not found")
    return user_data

@router.put("/users/{user_id}")
async def update_user(user_id: int, request: Request, user=Depends(admin_required)):
    data = await request.json()
    name = data.get("name")
    email = data.get("email")
    role = data.get("role")

    if not name or not email or not role:
        raise HTTPException(status_code=400, detail="Name, Email, and Role are required")

    cursor = db.cursor()
    cursor.execute("UPDATE users SET name=%s, email=%s, role=%s WHERE id=%s", (name, email, role, user_id))
    db.commit()

    return {"message": "User updated successfully"}

@router.delete("/users/{user_id}")
def delete_user(user_id: int, user=Depends(admin_required)):
    cursor = db.cursor()
    cursor.execute("DELETE FROM users WHERE id=%s", (user_id,))
    db.commit()
    return {"message": "User deleted successfully"}