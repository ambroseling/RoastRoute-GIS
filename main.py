import json
from fastapi import FastAPI
from typing import List

app = FastAPI()
#client = MongoClient("mongo://localhost:27017/")
# Set up MongoDB connection
# client = MongoClient("mongodb://localhost:27017/")
# db = client["ECE297_DB"]
# collection = db["Users"]


USER_DATA_FILE = "users.json"

def load_user_data():
    try:
        with open(USER_DATA_FILE, "r") as f:
            data = json.load(f)
            print(data)
            return data
    except:
        return []

def save_user_data(data):
    with open(USER_DATA_FILE, "w") as f:
        json.dump(data, f)
        print(data)

users = load_user_data()



@app.get("/")
def read_root():
    return {"Hello":"World"}
#run server with uvicorn main:app --reload

@app.get("/get_users")
async def get_users():
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
    print(users)
    save_user_data(users)
    return {"message": "User created successfully","users":users}