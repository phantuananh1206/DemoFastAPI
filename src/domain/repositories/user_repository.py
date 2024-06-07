from fastapi import HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import select, update, delete
from src.models.user import User
from src.domain.entities.user_entity import UserEntity, UserInput
from typing import List, Optional, Type


class UserRepository:
    def __init__(self, session: Session):
        self.session = session

    def get_all(self) -> List[Optional[UserEntity]]:
        users = self.session.query(User).all()
        return [UserEntity(**user.__dict__) for user in users]

    def find_user_by_id(self, user_id: int):
        return self.session.query(User).filter(User.id == user_id).first()

    def find_user_by_email(self, email: str):
        return self.session.query(User).filter(User.email == email).first()

    def create(self, db_user: UserInput) -> UserEntity:
        self.session.add(db_user)
        self.session.commit()
        self.session.refresh(db_user)
        return UserEntity(**db_user.__dict__)

    def update(self, db_user: UserInput, data: UserInput) -> UserEntity:
        for key, value in data.__dict__.items():
            setattr(db_user, key, value)

        self.session.commit()
        self.session.refresh(db_user)
        return UserEntity(**db_user.__dict__)

    def delete(self, db_user) -> bool:
        self.session.delete(db_user)
        self.session.commit()
        return True
