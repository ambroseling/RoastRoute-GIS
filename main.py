import json
from fastapi import FastAPI
from typing import List
from fastapi.middleware.cors import CORSMiddleware
 
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://ece297mapper.herokuapp.com/"], # replace * with the domain(s) of your client
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
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
    users = load_user_data()
    """
    Returns a list of all users in the database
    """
    return users

@app.get("/get_user/{name}")
async def get_user(name: str):
    """
    Returns the user with the provided name
    """
    users = load_user_data()
    for user in users:
        if user["name"] == name:
            return {"user": user}
    return {"message": "User not found"}

@app.get("/create_users")
async def create_user(name: str, latitude: float, longitude: float, active: bool):
    """
    Creates a new user entry in the database
    """
    users = load_user_data()

    new_user = {
        "name": name,
        "latitude": latitude,
        "longitude": longitude,
        "active": active,
        "date_requests":[]
    }
    users.append(new_user)
    print(users)
    save_user_data(users)
    return {"message": "User created successfully","users":users}


@app.get("/delete_all_users")
async def delete_all_users():
    """
    Deletes all user entries from the database
    """
    users = []
    save_user_data(users)
    return {"message": "All users deleted successfully"}

@app.get("/delete_user/{name}")
async def delete_user(name: str):
    """
    Deletes a user entry with the provided name from the database
    """
    users = load_user_data()
    for user in users:
        if user["name"] == name:
            users.remove(user)
            save_user_data(users)
            return {"message": "User deleted successfully", "user": user}
    return {"message": "User not found"}


@app.get("/update_user_active")
async def update_user_active(name: str, active: bool):
    """
    Updates the active field of a user's entry in the database
    """
    users = load_user_data()
    for user in users:
        if user["name"] == name:
            user["active"] = active
            save_user_data(users)
            return {"message": "User updated successfully", "user": user}
    return {"message": "User not found"}

@app.get("/send_request")
async def send_request(sender: str, receiver: str):
    """
    Adds the sender to the receiver's date_requests list
    """
    users = load_user_data()
    # Find the receiver in the user list
    for user in users:
        if user["name"] == receiver:
            # Append an object with sender's name and status to the receiver's date_requests list
            user["date_requests"].append({"sender_name": sender, "status": 0})
            save_user_data(users)
            return {"message": f"{sender} has sent a date request to {receiver}"}
    return {"message": f"{receiver} not found"}


@app.get("/cancel_request")
async def cancel_request(sender: str, receiver: str):
    """
    Removes the sender's object from the receiver's date_requests list
    """
    users = load_user_data()

    # Find the receiver in the user list
    for user in users:
        if user["name"] == receiver:
            # Loop through the date_requests list to find the sender's object and remove it
            for request in user["date_requests"]:
                if request["sender_name"] == sender:
                    user["date_requests"].remove(request)
                    save_user_data(users)
                    return {"message": f"{sender}'s date request to {receiver} has been cancelled"}
            # If the sender's object is not found in the date_requests list, return a message
            return {"message": f"{sender}'s date request to {receiver} was not found"}
    # If the receiver is not found in the user list, return a message
    return {"message": f"{receiver} not found"}

@app.put("/update_request_status")
async def update_request_status(sender: str, receiver: str, status: int):
    """
    Updates the status field of a date_requests object in the database
    """
    users = load_user_data()

    # Find the receiver in the user list
    for user in users:
        if user["name"] == receiver:
            # Loop through the date_requests list to find the sender's object and update its status field
            for request in user["date_requests"]:
                if request["sender_name"] == sender:
                    request["status"] = status
                    save_user_data(users)
                    return {"message": f"Request status updated for {sender}'s request to {receiver}"}
            # If the sender's object is not found in the date_requests list, return a message
            return {"message": f"{sender}'s request to {receiver} was not found"}
    # If the receiver is not found in the user list, return a message
    return {"message": f"{receiver} not found"}
