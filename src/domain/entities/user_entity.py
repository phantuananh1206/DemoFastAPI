from pydantic import BaseModel, Field, EmailStr
from typing import Optional, Annotated

class UserEntity(BaseModel):
    id: int
    name: str
    email: EmailStr
    status: int
    role: int
    
class UserInput(BaseModel):
    name: str
    email: EmailStr
    hashed_password: str = Field(min_length = 6)
    status: int
    role: int
    
class UserLogin(BaseModel):
    email: str
    password: str
    
class UserAuthenticated(UserEntity):
    access_token: str
    refresh_token: str