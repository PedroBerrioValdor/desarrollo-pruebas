from fastapi import FastAPI
from models import *
from config.db import engine, Base
#from routers import auth, todos, admin, users
from routers.v1.controllers import clienteController


app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(clienteController.router)