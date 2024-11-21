from repository.AbstractRepository import AbstractRepository
from models.user import Users

class UserRepository(AbstractRepository):
    def __init__(self):
        self.entity = Users