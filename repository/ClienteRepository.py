from repository.AbstractRepository import AbstractRepository
from models.cliente import Cliente

class ClienteRepository(AbstractRepository):
    def __init__(self):
        self.entity = Cliente