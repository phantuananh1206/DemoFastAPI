from pydantic import BaseModel, Field
from typing import Optional, Annotated

class UserEntity(BaseModel):
    id: int
    name: str
    email: str
    status: int
    role: int
    
class UserInput(BaseModel):
    name: str
    email: str
    status: int
    role: int