from fastapi import APIRouter, Depends, HTTPException, Request, Response
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm

from auth.security import create_access_token
from data.database import get_session
from dtos.auth_dto import UserLogin
from services.auth_service import AuthService
from jose import jwt

from util.config import ALGORITHM, SECRET_KEY

router = APIRouter(prefix="/auth", tags=["Auth"])



@router.post("/login")
def login_json(data: UserLogin, db: Session = Depends(get_session)):
    service = AuthService(db)
    result = service.login(data)

    if not result:
        return {"error": "Invalid credentials"}

    access_token, refresh_token = result

    response = Response(content="Login successful")

    response.set_cookie(
        key="access_token",
        value=access_token,
        httponly=True,
        secure=False,  # True in production (HTTPS)
        samesite="lax",
    )

    response.set_cookie(
        key="refresh_token",
        value=refresh_token,
        httponly=True,
        secure=False,
        samesite="lax",
    )

    return response

@router.post("/login-oauth2")
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

    access_token, refresh_token = result

    response = Response(content="Login successful")

    response.set_cookie(
        key="access_token",
        value=access_token,
        httponly=True,
        secure=False,  # True in production (HTTPS)
        samesite="lax",
    )

    response.set_cookie(
        key="refresh_token",
        value=refresh_token,
        httponly=True,
        secure=False,
        samesite="lax",
    )

    return response


@router.post("/refresh")
def refresh_token(request: Request):
    token = request.cookies.get("refresh_token")

    if not token:
        raise HTTPException(status_code=401, detail="No refresh token")

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])

        if payload.get("type") != "refresh":
            raise HTTPException(status_code=401, detail="Invalid token")

        new_access_token = create_access_token({
            "sub": payload["sub"],
            "role": payload["role"]
        })

        response = Response(content="Token refreshed")

        response.set_cookie(
            key="access_token",
            value=new_access_token,
            httponly=True,
            secure=False,
            samesite="lax",
        )

        return response

    except Exception:
        raise HTTPException(status_code=401, detail="Invalid refresh token")
    

@router.post("/logout")
def logout():
    response = Response(content="Logged out")

    response.delete_cookie("access_token")
    response.delete_cookie("refresh_token")

    return response