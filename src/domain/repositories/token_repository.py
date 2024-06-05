from fastapi import HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import select, update, delete
from src.models.token import Token
from src.domain.entities.token_entity import TokenInput, TokenEntity
from typing import List, Optional, Type

class TokenRepository:
    def __init__(self, session: Session):
        self.session = session

    def create(self, db_token: TokenInput) -> TokenEntity:
        self.session.add(db_token)
        self.session.commit()
        self.session.refresh(db_token)
        return TokenEntity(**db_token.__dict__)
    