from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr, Field



app = FastAPI()



class UserCreate(BaseModel):   #<- This is the main parameters of data that the API expects
    username: str = Field(min_length=3, max_length=15)
    age: int = Field(ge=0, le=99)
    email: EmailStr


class UserPublic(UserCreate):       #< - this is the daughter of the UserCreate and once Usercreate is initated a id will generate
    id: int


users: list[UserPublic]=[]  #<- This creates a list of the users 

@app.get("/")
def serveron():
    return("Server is on")

@app.get("/users", response_model=list[UserPublic])  #<- first route is http get, and its getting users , which is a list,  response_model is used to ensure the output matches UserPublic.
async def list_user():   #<- funuction named list_users , returns the users list
    return users

@app.post("/users", response_model=UserPublic, status_code=201)  #<-- New route HTTP post <- allows users to create a user and recieved status code 201
async def create_user(user: UserCreate): #<- function that allows usrs to create users using the UserCreate Pydantic model <- those parameters have to be met
 
    if any(u.username == user.username for u in users): #<-- loops through u.usename < u is a variable like in a for loop, is it like the same as self in classes? It checks if the username is already there
        raise HTTPException(status_code=409, detail="username already exists") #<- uses built in HTTPexecption 409 sayisn username already exist
    new_user = UserPublic(id=len(users) + 1, **user.model_dump())  #< -- new user get an id and updated to the users? 
    users.append(new_user) #<- Oh wait this si where the users list is actually updated
    return new_user #<--- shows the new user created



@app.get("/users/id/{id}",response_model=UserPublic)
async def get_user(id: int):
    for u in users:                # loop through each saved user
        if u.id == id:             # if this user's id matches the path id
            return u               # return that user immediately
    # only runs if no match found
    raise HTTPException(status_code=404, detail="User not found")


@app.get("/users/username/{username}", response_model=UserPublic) #<-- umm i guess it looks in the users list, for usersname, and gives theoption to for input of the username. 
async def check_user(username: str): #<- checks username to ensure its a string
    for u in users: #<- u is a variable and its looping through users, 
        if u.username == username: # < if username == username typed then return u < - whcih is the username
            return u
    raise HTTPException(status_code=404, detail="User not found")