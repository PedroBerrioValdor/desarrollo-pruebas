from abc import ABC, abstractmethod
from sqlalchemy.orm import Session
from sqlalchemy import  func, DateTime
from datetime import datetime



class AbstractRepository(ABC):
    entity:object = NotImplementedError

    @abstractmethod
    def __init__(self, entity:object):
        self.entity=entity

    def get_all(self, db:Session):
        return db.query(self.entity).all()
    
    def get_all_active(self, db:Session):
        return db.query(self.entity).filter(self.entity.active == True).all()
    
    def get_by_id(self, id:int, db:Session):
        return db.query(self.entity).filter(self.entity.id==id).one()
    
    def get_by_matricula(self, matricula:str, db:Session):
        return db.query(self.entity).filter(self.entity.matricula==matricula).one()
    
    def add(self, entity, db:Session):
        db.add(entity)
        db.commit()
        return entity
    
    def update(self, id:int, entity, db:Session):
        db.query(self.entity).filter(self.entity.id == id).update(entity)
        db.commit()
        return entity
    
    def delete(self, id:int, entity, db:Session):
        entity_to_update =  {"active": False}
        print(entity)
        db.query(self.entity).filter(self.entity.id == id).update(entity_to_update)
        db.commit()
        return entity
    
    
