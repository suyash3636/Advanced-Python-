from fastapi import FastAPI , Query
import asyncio

app = FastAPI()

@app.get("/")
async def home():
    return {"message": "Hello from FastAPI with async!"}

@app.get("/wait")
async def wait_route():
    await asyncio.sleep(8)
    return {"message": "Thanks for waiting!"}

@app.get("/greet")
async def greet_user(name: str = "Guest", age: int = Query(...,ge=18)):
    return {
        "message": f"Hello {name}!",
        "note": f"You are {age} years old."
    }