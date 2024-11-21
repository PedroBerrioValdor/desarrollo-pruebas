from pydantic import BaseModel
from typing import Optional

class ClienteSchema(BaseModel):
    nombre: str
    apellido: str
    rol: str

class ClienteSchemaGet(BaseModel):
    id: int
    nombre: str
    apellido: str
    active: bool


    