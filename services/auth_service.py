from sqlalchemy.orm import Session
from dtos.auth_dto import UserLogin
from models.models import User
from auth.security import create_refresh_token, verify_password, create_access_token


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

        payload = {
                "sub": user.username,
                "role": user.role.name
                }

        access_token = create_access_token(payload)
        refresh_token = create_refresh_token(payload)

        return access_token, refresh_token