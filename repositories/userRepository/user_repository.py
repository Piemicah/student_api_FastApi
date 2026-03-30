
from sqlalchemy.orm import Session

from auth.security import hash_password
from dtos.user_dto import UserResponse
from models.models import User
from repositories.userRepository.iuser_repository import IUserRepository


class UserRepository(IUserRepository):
    def __init__(self,session:Session):
        self.session=session

    def get_all_users(self):
        users = self.session.query(User).all()
        return [{"name":user.username,"role":user.role.name} for user in users]
    
    def create_user(self,data):
        hash_psw = hash_password(data.password)
        user = User(username = data.username,password=hash_psw,role_id=data.role_id)
        self.session.add(user)
        self.session.commit()
        return UserResponse.model_validate(user)
        