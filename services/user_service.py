

from dtos.user_dto import UserCreate
from repositories.userRepository.user_repository import UserRepository


class UserService:
    def __init__(self,repository:UserRepository):
        self.repository=repository
    def get_all_users(self):
        return self.repository.get_all_users()
    
    def create_user(self,data:UserCreate):
        return self.repository.create_user(data)