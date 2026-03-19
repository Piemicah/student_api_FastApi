from dtos.student_dto import StudentDto
from models.models import Student


def student_to_model(dto: StudentDto) -> Student:
    return Student(
        id=dto.id,
        name=dto.name,
        reg_no=dto.reg_no,
        phone=dto.phone,
        dob=dto.dob,
        state=dto.state,
        lga=dto.lga,
    )


def student_to_dto(model: Student) -> StudentDto:
    return StudentDto(
        id=model.id,
        reg_no=model.reg_no,
        name=model.name,
        phone=model.phone,
        dob=model.dob,
        state=model.state,
        lga=model.lga,
    )
