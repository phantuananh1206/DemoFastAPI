from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import models, database
from src.routers.api import router

import base64
import binascii
import os

import casbin_sqlalchemy_adapter
import casbin

from fastapi import FastAPI
from starlette.authentication import AuthenticationBackend, AuthenticationError, SimpleUser, AuthCredentials
from starlette.middleware.authentication import AuthenticationMiddleware

from fastapi_authz import CasbinMiddleware

# models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

app.include_router(router)

class BasicAuth(AuthenticationBackend):
    async def authenticate(self, request):
        if "Authorization" not in request.headers:
            return None

        auth = request.headers["Authorization"]
        try:
            scheme, credentials = auth.split()
            decoded = base64.b64decode(credentials).decode("ascii")
        except (ValueError, UnicodeDecodeError, binascii.Error):
            raise AuthenticationError("Invalid basic auth credentials")

        username, _, password = decoded.partition(":")
        return AuthCredentials(["authenticated"]), SimpleUser(username)


adapter = casbin_sqlalchemy_adapter.Adapter(os.getenv("DATABASE_URL"))
e = casbin.Enforcer('./rbac_model.conf', adapter)

app.add_middleware(CasbinMiddleware, enforcer=e)
app.add_middleware(AuthenticationMiddleware, backend=BasicAuth())