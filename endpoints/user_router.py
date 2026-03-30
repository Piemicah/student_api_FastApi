from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from data.database import get_session
from dtos.user_dto import UserCreate, UserResponse
from repositories.userRepository.user_repository import UserRepository
from services.user_service import UserService


router = APIRouter(prefix="/users",tags=["User"])

def get_user_service(session:Session=Depends(get_session)):
    user_repo = UserRepository(session)
    return UserService(user_repo)

@router.get("",response_model=list[dict[str,str]])
@router.get("/",response_model=list[dict[str,str]])
def get_all_users(service:UserService=Depends(get_user_service)):
    return service.get_all_users()

@router.post("",response_model=UserResponse)
@router.post("/",response_model=UserResponse)
def create_user(data:UserCreate,service:UserService=Depends(get_user_service)):
    return service.create_user(data)