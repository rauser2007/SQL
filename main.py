from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr
from typing import List

app = FastAPI()

# Модель користувача
class User(BaseModel):
    id: int
    username: str
    email: EmailStr

# Список користувачів
users = [
    User(id=1, username="user1", email="user1@example.com"),
    User(id=2, username="user2", email="user2@example.com"),
    User(id=3, username="user3", email="user3@example.com")
]

# Ендпоінт для отримання інформації про користувача за його id
@app.get("/users/{user_id}", response_model=User)
def get_user(user_id: int):
    for user in users:
        if user.id == user_id:
            return user
    raise HTTPException(status_code=404, detail="User not found")

# Ендпоінт для отримання списку всіх користувачів
@app.get("/users", response_model=List[User])
def get_all_users():
    return users

# Ендпоінт для створення нового користувача
@app.post("/create_user", response_model=User)
def create_user(user: User):
    users.append(user)
    return user
