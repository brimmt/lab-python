
# Aug 4 2025

from fastapi import FastAPI #for building routes
from pydantic import BaseModel # For classes, logic placeholder
from passlib.context import CryptContext #For passwords
from fastapi import HTTPException

app = FastAPI()

@app.get("/")
def root():
    return {"message": "BrimmAuth is Live"}



# Placeholder logic using pydantic and creating classes

class UserSignup(BaseModel):
    first_name: str
    last_name: str
    user_name: str
    email: str
    password: str

pwd_context = CryptContext(schemes=['bcrypt'], deprecated ='auto')

@app.post("/signup")
def signup(user: UserSignup):
    hashed_password = pwd_context.hash(user.password)
    return {
        "message": "User created successfully",
        "username": user.user_name,
        "email": user.email
    }

fake_users_db = {
    "testuser":{
        "username": "testuser",
        "hashed_password": '$2b$12$fry/4cGYwwvL3XijCEUcLuAVYHywOdOji8UHoToI3WNR2FZCgdSju'
    },
    "testuser2":{
        "username": "Tati",
        "hashed_password": "$2b$12$fry/4cGYwwvL3XijCEUcLuAVYHywOdOji8UHoToI3WNR2FZCgdSju"

    }  

    }



class UserLogin(BaseModel):
    user_name: str
    password: str

@app.post("/login")
def login(user: UserLogin):
   if user.user_name not in fake_users_db:
        raise HTTPException(status_code=404, detail="User not found")
   
   stored_user = fake_users_db[user.user_name]
   hashed_password = stored_user["hashed_password"]

   if not pwd_context.verify(user.password, hashed_password):
        raise HTTPException(status_code=401, detail="Incorrect password")

   return {"message": "Successfully logged in!"}

@app.get("/me")
def get_current_user(user_name: str):
    if user_name not in fake_users_db:
        raise HTTPException(status_code=404, detail="User not found")
    
    stored_user = fake_users_db[user_name]
    return {
        "username": stored_user["username"],
        "message" : f"Welcome back, {stored_user['username']}"
    }

@app.post("/logout")
def logout(user_name: str):
    if user_name not in fake_users_db:
        raise HTTPException(status_code=404, detail="User not found")

    return {"message": f"{user_name} logged out successfully"}