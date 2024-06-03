from typing import List, Optional

from fastapi import HTTPException, status
from pydantic import UUID4
from sqlalchemy.orm import Session
from src.models.user import User
from src.domain.repositories.user_repository import UserRepository
from src.domain.entities.user_entity import UserEntity, UserInput


class UserService:
    def __init__(self, session: Session):
        self.repository = UserRepository(session)

    def get_all(self) -> List[Optional[UserEntity]]:
        return self.repository.get_all()

    def create(self, data: UserInput) -> UserEntity:
        db_user = User(**data.model_dump())
        user = self.repository.create(db_user)
        return user
    
    def update(self, user_id: int, data: UserInput) -> UserEntity:
        db_user = self.repository.findUserById(user_id)
        if not db_user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
        
        user = self.repository.update(db_user, data)
        return user
    
    def delete(self, user_id: int):
        db_user = self.repository.findUserById(user_id)
        if not db_user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
        
        self.repository.delete(db_user)
        return { "detail": "User deleted"}