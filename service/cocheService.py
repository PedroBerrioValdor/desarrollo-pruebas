from repository.CocheRepository import CocheRepository
from sqlalchemy.orm import Session
from fastapi.encoders import jsonable_encoder
from models.coche import Coche
from sqlalchemy import  func, DateTime
from datetime import datetime

class CocheService():
    def __init__(self):
        self.repository = CocheRepository()

    def getAllCoches(self,db:Session):
        return self.repository.get_all(db)
    
    def getCocheByMatricula(self,matricula, db:Session):
        return self.repository.get_by_matricula(matricula, db)
    
    def createCoche(self,db:Session, coche):
        obj_in_data = jsonable_encoder(coche)
        db_obj = Coche(**obj_in_data)
        self.repository.add(db_obj, db)
        return db_obj