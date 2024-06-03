from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import models, database
from src.routers.api import router

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

app.include_router(router)
