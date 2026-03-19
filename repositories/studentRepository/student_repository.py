from typing import override
from sqlalchemy.orm import Session

from dtos.student_dto import StudentCreate, StudentDto
from models.models import Student
from repositories.studentRepository.istudent_repository import IStudentRepository


class StudentRepository(IStudentRepository):
    def __init__(self, session: Session):
        self.session = session

    @override
    def get_all_students(self) -> list[StudentDto]:
        result = self.session.query(Student).all()
        return result

    @override
    def get_student(self, reg_no: str) -> StudentDto:
        student = self.session.query(Student).filter(Student.reg_no == reg_no).first()
        return student

    @override
    def create_student(self, data: StudentCreate) -> StudentDto:
        student = Student(
            reg_no=data.reg_no,
            name=data.name,
            phone=data.phone,
            dob=data.dob,
            state=data.state,
            lga=data.lga,
        )
        self.session.add(student)
        self.session.commit()
        return student
