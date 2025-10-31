from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr, Field, SecretStr
from passlib.context import CryptContext

app = FastAPI()

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

users_db = {}

class Users(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr

class UserCreate(Users):
    password: str

class UserOut(Users):
    pass


#Create Hash password helper functions

def hash_password(plain_password: str) -> str:
    return pwd_context.hash(plain_password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


@app.get("/")
def server_check():
    return "Server is running"

@app.post("/signup", response_model=UserOut)
async def create_acc(user: UserCreate):
    if user.email in users_db:
        raise HTTPException(status_code=400, detail="User already exist")
    
    hashed = hash_password(user.password)

    users_db[user.email] = {
        "first_name": user.first_name,
        "last_name": user.last_name,
        "hashed_password": hashed
    }

    return UserOut(first_name=user.first_name, last_name=user.last_name, email=user.email)




@app.get("/users_db/email/{email}", response_model=UserOut)
async def get_user(email: str):
    #for u in users_db:
       # if u.email == email:
         #   return u

    #ChatGPT fix

    if email not in users_db:
        raise HTTPException(status_code=404, detail="User not found")
    
    user=users_db[email]
    return UserOut(
        first_name=user["first_name"],
        last_name=user["last_name"],
        email=email
        
    )


