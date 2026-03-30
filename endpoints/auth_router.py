from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm

from data.database import get_session
from dtos.auth_dto import UserLogin
from services.auth_service import AuthService

router = APIRouter(prefix="/auth", tags=["Auth"])



@router.post("/login-json")
def login_json(data: UserLogin, db: Session = Depends(get_session)):
    service = AuthService(db)
    result = service.login(data)

    if not result:
        return {"error": "Invalid credentials"}

    return result

@router.post("/login")
def login_oauth2(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_session),
):
    service = AuthService(db)
    result = service.login(
        UserLogin(username=form_data.username,
         password= form_data.password)
    )

    if not result:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    return result