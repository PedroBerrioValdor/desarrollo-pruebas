from repository.ClienteRepository import ClienteRepository
from sqlalchemy.orm import Session
from fastapi.encoders import jsonable_encoder
from models.cliente import Cliente
from sqlalchemy import  func, DateTime
from datetime import datetime

class ClienteService():
    def __init__(self):
        self.repository = ClienteRepository()

    def getAllClientes(self,db:Session):
        return self.repository.get_all_active(db)
    
    def getCliente(self,id, db:Session):
        return self.repository.get_by_id(id, db)
    
    def createCliente(self, clienteNew, db:Session):
        obj_in_data = jsonable_encoder(clienteNew)
        db_obj = Cliente(**obj_in_data)
        print(obj_in_data)
        self.repository.add(db_obj, db)
        return db_obj
    
    def updateCliente(self, clienteUpdated, id, db:Session):
        obj_in_data = jsonable_encoder(clienteUpdated)
        self.repository.update(id, obj_in_data, db)
        return self.getCliente(id, db) 
    
    def deleteCliente(self, id,cliente, db:Session):
        obj_in_data = jsonable_encoder(cliente)
        self.repository.delete(id, obj_in_data, db)
        return self.getCliente(id, db)