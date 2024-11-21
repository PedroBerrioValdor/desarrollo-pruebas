from repository.AbstractRepository import AbstractRepository
from models.coche import Coche

class CocheRepository(AbstractRepository):
    def __init__(self):
        self.entity = Coche