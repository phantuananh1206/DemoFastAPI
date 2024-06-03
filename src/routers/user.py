from typing import List

from fastapi import APIRouter, Depends, status
from pydantic import UUID4
from sqlalchemy.orm import Session
from src.database import get_db
from src.domain.entities.user_entity import UserEntity, UserInput
from src.domain.services.user_service import UserService


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
    return _service.create(data)

@router.put("/{user_id}", status_code=status.HTTP_200_OK, response_model=UserEntity)
def update(user_id: int, data: UserInput, session: Session = Depends(get_db)):
    _service = UserService(session)
    return _service.update(user_id, data)

@router.delete("/{user_id}", status_code=status.HTTP_202_ACCEPTED, response_model={})
def delete(user_id: int, session: Session = Depends(get_db)):
    _service = UserService(session)
    return _service.delete(user_id)