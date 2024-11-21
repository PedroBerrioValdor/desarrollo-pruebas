from fastapi import FastAPI, Depends, HTTPException, Path, APIRouter
from pydantic import BaseModel, Field
from models import *
#from database import  SessionLocal
from typing import Annotated, List
from sqlalchemy.orm import Session
from starlette import status
#from .auth import get_current_user
from passlib.context import CryptContext
from config.db_depend import get_db
from fastapi_utils.cbv import cbv
from service.userService import UserService
from schemas.user import UserGet
from schemas.user import User
from config.user_depend import bcrypt_context
from models.user import Users

router = APIRouter(
    tags=['user'],
    prefix="/users"
)

@cbv(router)
class UserController:
    def __init__(self):
        self.service = UserService()

    @router.get("/",response_model=List[UserGet], status_code=200)
    async def getUsers(self, db:Session = Depends(get_db)):
        users = self.service.getAllUsers(db)
        return users
    
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

