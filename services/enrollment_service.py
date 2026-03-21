from dtos.enrollment_dto import EnrollmentCreate
from repositories.enrollmentRepository.ienrollment_repository import (
    IEnrollmentRepository,
)


class EnrollmentService:

    def __init__(self, repository: IEnrollmentRepository):
        self.repository = repository

    def get_all_enrollments(self):
        return self.repository.get_all_enrollments()

    def create_enrollment(self, data: EnrollmentCreate):
        return self.repository.create_enrollment(data)
