from fastapi import HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import select, update, delete
from src.models.token import Token
from src.domain.entities.token_entity import TokenInput, TokenEntity, TokenCreate
from typing import List, Optional, Type


class TokenRepository:
    def __init__(self, session: Session):
        self.session = session

    def create(self, db_token: TokenCreate) -> TokenEntity:
        self.session.add(db_token)
        self.session.commit()
        self.session.refresh(db_token)
        return TokenEntity(**db_token.__dict__)

    def findByToken(self, db_token: TokenInput) -> TokenEntity:
        return self.session.query(Token).filter(Token.access_token == db_token.access_token, Token.refresh_token == db_token.refresh_token).first()
