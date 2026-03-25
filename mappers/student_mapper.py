from dtos.student_dto import StudentResponse
from models.models import Programme, Student
from data.database import get_sessionLocal


def student_to_model(dto: StudentResponse) -> Student:
    return Student(
        id=dto.id,
        name=dto.name,
        reg_no=dto.reg_no,
        phone=dto.phone,
        dob=dto.dob,
        state=dto.state,
        lga=dto.lga,
    )


def student_to_dto(model: Student) -> StudentResponse:
    student= StudentResponse(
        id=model.id,
        reg_no=model.reg_no,
        name=model.name,
        phone=model.phone,
        dob=model.dob,
        state=model.state,
        lga=model.lga,
        enrollments=model.enrollments
    )

    session = get_sessionLocal()
    student_dict = student.model_dump()
    enrollments = student_dict["enrollments"]
    if len(enrollments)>0:
        for enroll in enrollments:
            programme_name = session.query(Programme).filter(Programme.id==enroll["programme_id"]).first().programme_name
            enroll.pop("programme_id")
            enroll["Programme"]=programme_name

    student_dict["enrollments"]=enrollments
    session.close()
    return student_dict


