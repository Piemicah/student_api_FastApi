from abc import ABC, abstractmethod

from dtos.user_dto import UserCreate, UserResponse

class IUserRepository(ABC):
    
    @abstractmethod
    def create_user(self,data:UserCreate)->UserResponse:
        pass

    @abstractmethod
    def get_all_users(self)->list[dict[str,str]]:
        pass