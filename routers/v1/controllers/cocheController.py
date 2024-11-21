from service.cocheService import CocheService
from config.db_depend import get_db
from fastapi import HTTPException, APIRouter, Depends
from starlette import status
from sqlalchemy.orm import Session
from schemas.coche import CocheSchema
from fastapi_utils.cbv import cbv
from typing import List

router = APIRouter(
    tags=['coche'],
    prefix="/coche"
)

@cbv(router)
class CocheController:
    def __init__(self):
        self.service = CocheService()

    @router.get("/", response_model=List[CocheSchema], status_code=200)
    def getCoches(self, db:Session = Depends(get_db)):
        clientes = self.service.getAllCoches(db)
        return clientes
    
    @router.get("/{matricula}", response_model=CocheSchema, status_code=200)
    def getCoche(self,matricula:str, db:Session = Depends(get_db)):
        return self.service.getCocheByMatricula(matricula, db)
    
    @router.post("/createCoche", response_model=CocheSchema, status_code=200)
    def createCoche(self, coche:CocheSchema, db:Session = Depends(get_db)):
        return self.service.createCoche(coche, db)

    
    