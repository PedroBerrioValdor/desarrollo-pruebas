from datetime import datetime, timedelta, timezone
from fastapi import FastAPI, APIRouter, Depends, HTTPException
from pydantic import BaseModel
from models.user import Users
from passlib.context import CryptContext
from typing import Annotated
from starlette import status
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from sqlalchemy.orm import Session
from jose import JWTError, jwt
from dotenv import load_dotenv
import os


load_dotenv(verbose=True)

bcrypt_context = CryptContext(schemes=['bcrypt'], deprecated= 'auto')
oauth2_bearer = OAuth2PasswordBearer(tokenUrl='auth/token')

async def get_current_user(token: Annotated[str, Depends(oauth2_bearer)]):
    try:
        payload = jwt.decode(token, os.environ['SECRET_KEY'], algorithms=[os.environ['ALGORITHM']]) #Coge el payload del token (username, id) -> Si falla al Except
        username: str = payload.get('sub')
        user_id: int = payload.get('id')
        user_role: str = payload.get('role')
        if username is None or user_id is None: #Verifica campos
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Could not validate user')
        return {'username':username, 'id':user_id, 'user_role': user_role}
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Could not validate user')
    
#Verificacion de que el usuario esta en el sistema y que la contraseña es correcta 
def authenticate_user(username:str, password:str, db):
    user = db.query(Users).filter(Users.username == username).first()
    if not user: #Si no existe el usuario
        return False
    if not bcrypt_context.verify(password, user.hashed_password): #Verifica relacion entre password y hash
        return False
    return user

#Creacion de token 
def create_access_token(username: str, user_id:int, role: str, expires_delta: timedelta):
    encode = {'sub': username, 'id': user_id, 'role': role}
    expire = datetime.now(timezone.utc) + expires_delta
    encode.update({'exp':expire}) #Añade tiempo de expiración
    return jwt.encode(encode,os.environ['SECRET_KEY'],algorithm=os.environ['ALGORITHM']) #JWT encode
    

