from typing import List, Optional
from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from src.models.token import Token
from src.domain.repositories.token_repository import TokenRepository
from src.domain.entities.token_entity import TokenEntity, TokenInput, TokenCreate


class TokenService:
    def __init__(self, session: Session):
        self.repository = TokenRepository(session)

    def create(self, data: TokenCreate) -> TokenEntity:
        db_token = Token(**data.model_dump())
        token = self.repository.create(db_token)
        return token

    def getAcessToken(self, data: TokenInput) -> bool:
        token = self.repository.findByToken(data)
        if token is not None:
            return True

        return False
