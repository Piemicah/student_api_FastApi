from fastapi import APIRouter, Depends

from dtos.student_dto import StudentCreate, StudentDto
from sqlalchemy.orm import Session
from data.database import get_session
from repositories.studentRepository.student_repository import StudentRepository
from services.student_service import StudentService


def get_student_service(db: Session = Depends(get_session)):
    repo = StudentRepository(db)
    return StudentService(repo)


router = APIRouter(prefix="/students", tags=["Students"])


@router.get("/", response_model=list[StudentDto])
def get_all_students(service: StudentService = Depends(get_student_service)):
    return service.get_all_students()


@router.get("/{reg_no}", response_model=StudentDto)
def get_students(reg_no: str, service: StudentService = Depends(get_student_service)):
    return service.get_student(reg_no)


@router.post("", response_model=StudentDto)
def create_student(
    data: StudentCreate, service: StudentService = Depends(get_student_service)
):
    return service.create_student(data)
