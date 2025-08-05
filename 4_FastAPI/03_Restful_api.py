from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr, Field
from typing import Dict

app = FastAPI()

# In-memory storage
fake_db: Dict[int, dict] = {}
current_id = 0

# Pydantic Model
class User(BaseModel):
    name: str = Field(..., min_length=3, max_length=50)
    age: int = Field(..., ge=18, le=100)
    email: EmailStr

# Create user
@app.post("/users")
async def create_user(user: User):
    global current_id
    current_id += 1
    fake_db[current_id] = user.dict()
    return {"id": current_id, "user": user}

# Get user by ID
@app.get("/users/{user_id}")
async def get_user(user_id: int):
    user = fake_db.get(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return {"id": user_id, "user": user}

# Get all users
@app.get("/users")
async def get_all_users():
    return fake_db

# Update user
@app.put("/users/{user_id}")
async def update_user(user_id: int, updated_user: User):
    if user_id not in fake_db:
        raise HTTPException(status_code=404, detail="User not found")
    fake_db[user_id] = updated_user.dict()
    return {"id": user_id, "user": updated_user}

# Delete user
@app.delete("/users/{user_id}")
async def delete_user(user_id: int):
    if user_id not in fake_db:
        raise HTTPException(status_code=404, detail="User not found")
    del fake_db[user_id]
    return {"message": f"User {user_id} deleted successfully"}
