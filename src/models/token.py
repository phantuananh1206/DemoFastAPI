from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, MetaData
from sqlalchemy.orm import relationship
from sqlalchemy.orm import declarative_base
from . import Base
from src.constants import DB_NAMING_CONVENTION
metadata = MetaData(naming_convention=DB_NAMING_CONVENTION)


class Token(Base):
    __tablename__ = "tokens"

    metadata
    id = Column(Integer, primary_key=True, index=True)
    access_token = Column(String(255))
    refresh_token = Column(String(255))
    status = Column(Boolean, default=True)
    user_id = Column(Integer, ForeignKey('users.id'))

    user = relationship('User', back_populates='token')
