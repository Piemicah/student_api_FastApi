from fastapi import APIRouter, Depends

from dtos.student_dto import StudentCreate, StudentResponse, StudentUpdate
from sqlalchemy.orm import Session
from data.database import get_session
from repositories.studentRepository.student_repository import StudentRepository
from services.student_service import StudentService
from auth.dependencies import require_roles


def get_student_service(db: Session = Depends(get_session)):
    repo = StudentRepository(db)
    return StudentService(repo)


router = APIRouter(prefix="/students", tags=["Students"])


@router.get("/", response_model=list[StudentResponse])
def get_all_students(
    service: StudentService = Depends(get_student_service),
    user=Depends(require_roles("admin","staff"))
    ):
    return service.get_all_students()


@router.get("/{reg_no}", response_model=dict)
def get_student(
    reg_no: str, 
    service: StudentService = Depends(get_student_service)
):
    return service.get_student(reg_no)


@router.post("/", response_model=StudentResponse)
def create_student(
    data: StudentCreate, 
    service: StudentService = Depends(get_student_service)
):
    return service.create_student(data)


@router.put("/{reg_no}", response_model=StudentResponse | dict)
def update_student(
    reg_no: str,
    data: StudentUpdate,
    service: StudentService = Depends(get_student_service),
    user=Depends(require_roles("admin"))
):
    return service.update_student(reg_no, data)


@router.delete("/{reg_no}", response_model=dict)
def delete_student(
    reg_no: str, 
    service: StudentService = Depends(get_student_service),
    user = Depends(require_roles("admin"))
    ):
    return service.delete_student(reg_no)
