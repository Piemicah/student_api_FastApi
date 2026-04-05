from fastapi import Depends, HTTPException, Request, status
from jose import jwt, JWTError
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from data.database import get_session
from models.models import User
from util.config import ALGORITHM, SECRET_KEY



def get_current_user(
    request: Request,
    db: Session = Depends(get_session),
):
    token = request.cookies.get("access_token")

    if not token:
        raise HTTPException(status_code=401, detail="Not authenticated")

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])

        if payload.get("type") != "access":
            raise HTTPException(status_code=401)

        username = payload.get("sub")

    except JWTError:
        raise HTTPException(status_code=401)

    user = db.query(User).filter(User.username == username).first()

    if not user:
        raise HTTPException(status_code=401)

    return user

def require_roles(*roles: list[str]):
    def role_checker(user=Depends(get_current_user)):
        if user.role.name not in roles:
            raise HTTPException(
                status_code=403,
                detail="Forbiden",
            )
        return user

    return role_checker