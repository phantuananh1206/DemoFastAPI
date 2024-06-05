from pydantic import BaseModel, Field
from typing import Optional, Annotated

class TokenEntity(BaseModel):
    id: int
    access_token: str
    refresh_token: str
    status: bool

class TokenInput(BaseModel):
    access_token: str
    refresh_token: str
    status: bool
