from sqlalchemy import Column, ForeignKey, Integer, String, Boolean, Identity, DateTime, func
from config.db import Base

class Cliente(Base):
    __tablename__ = "cliente"
    id= Column(Integer,Identity(start=1,cycle=True), primary_key=True)
    nombre= Column(String)
    apellido= Column(String)
    updated_at= Column(DateTime(timezone=True), onupdate=func.now())
    created_at= Column(DateTime(timezone=True), server_default=func.now())
    active= Column(Boolean,default=True)
    rol= Column(String,default="Cliente")