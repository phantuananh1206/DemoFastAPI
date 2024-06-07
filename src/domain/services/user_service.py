from typing import List, Optional
from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from src.models.user import User
from src.domain.repositories.user_repository import UserRepository
from src.domain.entities.user_entity import UserEntity, UserInput, UserLogin, UserAuthenticated
from src.domain.entities.token_entity import TokenInput, TokenCreate, TokenEntity
from src.utils.auth import get_hashed_password, verify_password, create_access_token, create_refresh_token
from .token_service import TokenService
from src.utils.email import send_email_register


class UserService:
    def __init__(self, session: Session):
        self.repository = UserRepository(session)
        self.tokenService = TokenService(session)

    def get_all(self) -> List[Optional[UserEntity]]:
        return self.repository.get_all()

    def register(self, data: UserInput) -> UserEntity:
        data.hashed_password = get_hashed_password(data.hashed_password)
        db_user = User(**data.model_dump())
        user = self.repository.create(db_user)
        send_email_register(user)
        return user

    def get_profile(self, user_id: int) -> UserEntity:
        db_user = self.repository.find_user_by_id(user_id)
        if not db_user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

        return db_user

    def update(self, user_id: int, data: UserInput) -> UserEntity:
        db_user = self.repository.find_user_by_id(user_id)
        if not db_user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

        user = self.repository.update(db_user, data)
        return user

    def delete(self, user_id: int):
        db_user = self.repository.find_user_by_id(user_id)
        if not db_user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

        self.repository.delete(db_user)
        return {"detail": "User deleted"}

    def login(self, data: UserLogin) -> UserAuthenticated:
        user = self.repository.find_user_by_email(data.email)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail="Incorrect email")
        if not verify_password(data.password, user.hashed_password):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail="Incorrect password")

        user.access_token = create_access_token(
            {'user_id': user.id, 'name': user.name, 'role': user.role})
        user.refresh_token = create_refresh_token(user.id)
        token_input = TokenCreate(
            access_token=user.access_token, refresh_token=user.refresh_token, status=True, user_id=user.id)
        self.tokenService.create(token_input)
        return user

    def get_access_token(self, user_id: int, data: TokenInput) -> TokenEntity:
        user = self.repository.find_user_by_id(user_id)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
        db_token = self.tokenService.getAcessToken(data)
        if not db_token:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Invalid token")

        user.access_token = create_access_token(
            {'user_id': user.id, 'name': user.name, 'role': user.role})
        user.refresh_token = create_refresh_token(user.id)
        token_input = TokenCreate(
            access_token=user.access_token, refresh_token=user.refresh_token, status=True, user_id=user.id)
        return self.tokenService.create(token_input)
