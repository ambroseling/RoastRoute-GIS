from fastapi import FastAPI
from typing import List

app = FastAPI()
#client = MongoClient("mongo://localhost:27017/")
# Set up MongoDB connection
# client = MongoClient("mongodb://localhost:27017/")
# db = client["ECE297_DB"]
# collection = db["Users"]

users = []

@app.get("/")
def read_root():
    return {"Hello":"World"}
#run server with uvicorn main:app --reload

@app.get("/get_users")
async def get_users() -> List[dict]:
    """
    Returns a list of all users in the database
    """
    return users

@app.get("/create_users")
async def create_user(name: str, latitude: float, longitude: float, active: bool):
    """
    Creates a new user entry in the database
    """
    new_user = {
        "name": name,
        "latitude": latitude,
        "longitude": longitude,
        "active": active
    }
    users.append(new_user)
    return {"message": "User created successfully"}