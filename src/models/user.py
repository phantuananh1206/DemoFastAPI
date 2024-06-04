from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, MetaData
from sqlalchemy.orm import relationship
from sqlalchemy.orm import declarative_base
from . import Base
from src.constants import DB_NAMING_CONVENTION
metadata = MetaData(naming_convention=DB_NAMING_CONVENTION)

class User(Base):
    __tablename__ = "users"
    
    metadata
    id = Column(Integer, primary_key = True, index = True)
    name = Column(String(255), index = True)
    email = Column(String(255), unique = True, index = True)
    status = Column(Integer, default = 0)
    role = Column(Integer, default = 0)