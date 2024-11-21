from pydantic import BaseModel
from typing import Optional

class CocheSchema(BaseModel):
    matricula:str
    marca:str
    tipoAveria:str
    idCliente:int
