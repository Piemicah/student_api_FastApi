from sqlalchemy.orm import Session
from dtos.auth_dto import UserLogin
from models.models import User
from auth.security import verify_password, create_access_token


class AuthService:
    def __init__(self, db: Session):
        self.db = db

    def authenticate_user(self, username: str, password: str):
        user = self.db.query(User).filter(User.username == username).first()

        if not user or not verify_password(password, user.password):
            return None

        return user

    def login(self,data:UserLogin):
        user = self.authenticate_user(data.username, data.password)

        if not user:
            return None

        token = create_access_token(
            {
                "sub": user.username,
                "role": user.role.name,
            }
        )

        return {"access_token": token, "role": user.role.name}