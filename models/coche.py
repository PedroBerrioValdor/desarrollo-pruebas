from sqlalchemy import Column, ForeignKey, Integer, String, Boolean, Identity, DateTime, func
from config.db import Base

class Coche(Base):
    __tablename__ = "coche"
    matricula= Column(String, primary_key=True)
    marca= Column(String)
    tipoAveria= Column(String)
    idCliente=Column(Integer,ForeignKey("cliente.id"),nullable=False)
    updated_at= Column(DateTime(timezone=True), onupdate=func.now())
    created_at= Column(DateTime(timezone=True), server_default=func.now())
    active= Column(Boolean,default=True)