import base64
import binascii
import os
import casbin_sqlalchemy_adapter
import casbin
from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from . import models, database
from src.routers.api import router
from fastapi import FastAPI
from starlette.authentication import AuthenticationBackend, AuthenticationError, SimpleUser, AuthCredentials
from starlette.middleware.authentication import AuthenticationMiddleware
from fastapi_authz import CasbinMiddleware
from .utils.auth import decode_jwt
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import Response
from typing import Optional, Annotated


# models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

app.include_router(router)


# class BasicAuth(AuthenticationBackend):
#     async def authenticate(self, request):
#         if "Authorization" not in request.headers:
#             return None

#         token = request.headers["Authorization"].split(" ")[1]
#         try:
#             verified_token = decode_jwt(token)
#             user = eval(verified_token['payload'])
#             sub = user['role']
#             obj = request.url.path
#             act = request.scope['method']
#             if e.enforce(sub, obj, act):
#                 return AuthCredentials(["authenticated"]), SimpleUser(user['name'])
#             else:
#                 raise HTTPException(
#                     status_code=status.HTTP_403_FORBIDDEN, detail="No permission")
#         except (ValueError, UnicodeDecodeError, binascii.Error):
#             raise AuthenticationError("Invalid basic auth credentials")


# adapter = casbin_sqlalchemy_adapter.Adapter(os.getenv("DATABASE_URL"))
# e = casbin.Enforcer('./rbac_model.conf', adapter)

# app.add_middleware(CasbinMiddleware, enforcer=e)
# app.add_middleware(AuthenticationMiddleware, backend=BasicAuth())
