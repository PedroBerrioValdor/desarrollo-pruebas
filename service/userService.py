
from repository.UserRepository import UserRepository

from sqlalchemy.orm import Session
from fastapi.encoders import jsonable_encoder
from models.user import Users
from sqlalchemy import  func, DateTime
from datetime import datetime

class UserService():
    def __init__(self):
        self.repository = UserRepository()

    def getAllUsers(self,db:Session):
        return self.repository.get_all(db)

    def createUser(self, userNew, db:Session):
        obj_in_data = jsonable_encoder(userNew)
        db_obj = Users(**obj_in_data)
        print(obj_in_data)
        self.repository.add(db_obj, db)
        return db_obj