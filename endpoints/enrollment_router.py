from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from data.database import get_session
from dtos.enrollment_dto import EnrollmentCreate, EnrollmentResponse
from repositories.enrollmentRepository.enrollment_repository import EnrollmentRepository
from services.enrollment_service import EnrollmentService


def get_enrollment_service(session: Session = Depends(get_session)):
    repo = EnrollmentRepository(session)
    return EnrollmentService(repo)


router = APIRouter(prefix="/enrollments", tags=["Enrollments"])


@router.get("/", response_model=list[EnrollmentResponse])
def get_all_enrollments(service: EnrollmentService = Depends(get_enrollment_service)):
    return service.get_all_enrollments()


@router.post("/", response_model=EnrollmentResponse)
def create_enrollment(
    data: EnrollmentCreate, service: EnrollmentService = Depends(get_enrollment_service)
):
    return service.create_enrollment(data)
