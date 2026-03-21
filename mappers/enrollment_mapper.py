from dtos.enrollment_dto import EnrollmentDto
from models.models import Enrollment


def enrollment_to_dto(model: Enrollment):
    return EnrollmentDto(
        id=model.id,
        student_id=model.student_id,
        programme_id=model.programme_id,
        subject1=model.subject1,
        subject2=model.subject2,
        subject3=model.subject3,
    )
