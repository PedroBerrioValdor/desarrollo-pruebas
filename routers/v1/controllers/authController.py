from datetime import datetime, timedelta, timezone
from fastapi import FastAPI, APIRouter, Depends, HTTPException
from pydantic import BaseModel
from models.user import Users
from passlib.context import CryptContext
from typing import Annotated, Dict
from starlette import status
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from sqlalchemy.orm import Session
from jose import JWTError, jwt
from config.db_depend import get_db
from config.user_depend import get_current_user, authenticate_user, create_access_token
from schemas.user import User
from config.user_depend import bcrypt_context
from schemas.token import Token
from passlib.context import CryptContext
from schemas.user import User
from fastapi_utils.cbv import cbv
from service.userService import UserService

router = APIRouter(
    prefix='/auth',
    tags=['auth']
)


@cbv(router)
class AuthController:
    def __init__(self):
        self.service = UserService()


    #Metodo para crear un nuevo usuario
    @router.post("/", status_code=status.HTTP_201_CREATED)
    async def create_user(self,create_user_request: User,db:Session = Depends(get_db)):
        create_user_model = Users(
            email=create_user_request.email,
            username=create_user_request.username,
            first_name=create_user_request.first_name,
            last_name=create_user_request.last_name,
            role=create_user_request.role,
            hashed_password=bcrypt_context.hash(create_user_request.password),
            is_active=True
        )

        self.service.createUser(create_user_model, db)

    #Metodo que devuelve el token siempre que el usuario este autenticado
    @router.post("/token", response_model=Token)
    async def login_for_acces_token(self,form_data: Annotated[OAuth2PasswordRequestForm, Depends()], db:Session = Depends(get_db)):
        user = authenticate_user(form_data.username, form_data.password, db)
        if not user:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Could not validate user')
        
        token = create_access_token(user.username, user.id, user.role, timedelta(minutes=20))
        return {'access_token': token, 'token_type':'bearer' }