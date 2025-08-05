from fastapi import FastAPI, Query
from pydantic import BaseModel , Field,EmailStr

app = FastAPI() 
class User(BaseModel):
    name: str =Field(...,min_length=3, max_length=50, description="The name of the user")
    age: int = Field(..., ge=18, le=100, description="The age of the user, must be between 18 and 100")
    email: EmailStr = Field(..., description="The email address of the user")

@app.post("/user")
async def create_user(user: User):
    print(f"User {user.name} created successfully!" , f"age {user.age}")
    return {"message": f"User {user.name} created successfully!", "age": user.age}