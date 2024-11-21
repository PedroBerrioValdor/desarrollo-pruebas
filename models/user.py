from sqlalchemy import Column, ForeignKey, Integer, String, Boolean, Identity, DateTime, func
from config.db import Base

class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True )
    email = Column(String, unique=True)
    username = Column(String, unique=True)
    first_name = Column(String)
    last_name = Column(String)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
    role = Column(String)
