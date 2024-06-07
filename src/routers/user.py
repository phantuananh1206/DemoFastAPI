from typing import List
from fastapi import APIRouter, Depends, status, Header
from sqlalchemy.orm import Session
from src.database import get_db
from src.domain.entities.user_entity import UserEntity, UserInput, UserLogin, UserAuthenticated
from src.domain.services.user_service import UserService
from src.domain.entities.token_entity import TokenInput, TokenEntity
from src.utils.auth import get_current_user, get_current_user_authorization


router = APIRouter(
    prefix="/user",
    tags=["user"]
)


@router.get("", status_code=status.HTTP_200_OK, response_model=List[UserEntity])
def get_regions(session: Session = Depends(get_db)) -> List[UserEntity]:
    _service = UserService(session)
    return _service.get_all()


@router.post("/register", status_code=status.HTTP_201_CREATED, response_model=UserEntity)
def register(data: UserInput, session: Session = Depends(get_db)):
    _service = UserService(session)
    return _service.register(data)


@router.get("/{user_id}", status_code=status.HTTP_200_OK, response_model=UserEntity)
def get_profile(user_id: int, session: Session = Depends(get_db), Authorization: str = Header(None), current_user: str = Depends(get_current_user_authorization)):
    # def get_profile(user_id: int, session: Session = Depends(get_db), Authorization: str = Header(None), current_user: str = Depends(get_current_user)):
    _service = UserService(session)
    return _service.get_profile(user_id)


@router.put("/{user_id}", status_code=status.HTTP_200_OK, response_model=UserEntity)
def update(user_id: int, data: UserInput, session: Session = Depends(get_db)):
    _service = UserService(session)
    return _service.update(user_id, data)


@router.delete("/{user_id}", status_code=status.HTTP_202_ACCEPTED, response_model={})
def delete(user_id: int, session: Session = Depends(get_db)):
    _service = UserService(session)
    return _service.delete(user_id)


@router.post("/login", status_code=status.HTTP_200_OK, response_model=UserAuthenticated)
def login(data: UserLogin, session: Session = Depends(get_db)):
    _service = UserService(session)
    return _service.login(data)


@router.post("/{user_id}", status_code=status.HTTP_201_CREATED, response_model=TokenEntity)
def get_access_token(user_id: int, data: TokenInput, session: Session = Depends(get_db)):
    _service = UserService(session)
    return _service.getAccessToken(user_id, data)
