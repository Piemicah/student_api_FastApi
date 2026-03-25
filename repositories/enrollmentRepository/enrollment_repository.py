from sqlalchemy.orm import Session

from dtos.enrollment_dto import EnrollmentCreate, EnrollmentResponse
from models.models import Enrollment, Student

from .ienrollment_repository import IEnrollmentRepository


class EnrollmentRepository(IEnrollmentRepository):
    def __init__(self, session: Session):
        self.session = session

    def get_all_enrollments(self):
        return self.session.query(Enrollment).all()

    def create_enrollment(self, data: EnrollmentCreate):
        student = self.session.query(Student).filter(Student.id == data.student_id).first()
        if not student:
            raise Exception("student not found")
        
        # Enforce number of programmes
        if len(student.enrollments) >=3:
            raise Exception("Student cannot register more than 3 programmes")
        enroll = Enrollment(
            student_id=data.student_id,
            programme_id=data.programme_id,
            subject1=data.subject1,
            subject2=data.subject2,
            subject3=data.subject3,
        )

        self.session.add(enroll)
        self.session.commit()
        return EnrollmentResponse.model_validate(enroll)
