from service.clienteService import ClienteService
from config.db_depend import get_db
from fastapi import HTTPException, APIRouter, Depends
from starlette import status
from sqlalchemy.orm import Session
from schemas.cliente import ClienteSchema, ClienteSchemaGet
from fastapi_utils.cbv import cbv
from typing import List

router = APIRouter()

@cbv(router)
class ClienteController:
    def __init__(self):
        self.service = ClienteService()

    @router.get("/", response_model=List[ClienteSchemaGet], status_code=200)
    def getClientes(self, db:Session = Depends(get_db)):
        clientes = self.service.getAllClientes(db)
        return clientes
    
    @router.get("/{id}", response_model=ClienteSchema, status_code=200)
    def getClienteById(self,id, db:Session = Depends(get_db)):
        cliente = self.service.getCliente(id, db)
        if cliente is None:
            raise HTTPException(status_code=404, detail="Not Found")
        return cliente
    
    @router.post("/createCliente", response_model=ClienteSchema, status_code=200)
    def addCliente(self, cliente: ClienteSchema ,db:Session = Depends(get_db)):
        return self.service.createCliente(cliente, db)
    
    @router.put("/{id}", response_model=ClienteSchema, status_code=200)
    def modificaCliente(self, cliente: ClienteSchema, id:int, db:Session = Depends(get_db)):
        return self.service.updateCliente(cliente, id, db)
    
    @router.delete("/deleteCliente/{id}", response_model=ClienteSchema, status_code=200)
    def borraCliente(self, id:int, db:Session = Depends(get_db)):
        cliente = self.service.getCliente(id, db)
        if cliente is None:
            raise HTTPException(status_code=404, detail="Not Found")
        return self.service.deleteCliente(id,cliente, db)

    


    