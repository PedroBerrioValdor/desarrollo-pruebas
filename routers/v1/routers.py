from fastapi import APIRouter
from routers.v1.controllers import clienteController, cocheController

api_router = APIRouter()

api_router.include_router(clienteController.router)
api_router.include_router(cocheController.router)
