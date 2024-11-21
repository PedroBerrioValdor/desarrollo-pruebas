from fastapi import FastAPI
from models import *
from config.db import engine, Base
#from routers import auth, todos, admin, users
from routers.v1.controllers import clienteController
from routers.v1.routers import api_router


app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(api_router)