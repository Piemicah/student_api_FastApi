from typing import override
from sqlalchemy.orm import Session

from dtos.student_dto import StudentCreate, StudentResponse, StudentUpdate
from mappers.student_mapper import student_to_dto
from models.models import Enrollment, Programme, Student
from repositories.studentRepository.istudent_repository import IStudentRepository


class StudentRepository(IStudentRepository):
    def __init__(self, session: Session):
        self.session = session

    @override
    def get_all_students(self) -> list[dict]:

        result = self.session.query(Student).all()
        return [student_to_dto(model) for model in result]

    @override
    def get_student(self, reg_no: str) -> dict:
        student = self.session.query(Student).filter(Student.reg_no == reg_no).first()
        return student_to_dto(student)

    def get_student_detail(self, reg_no):
        student = self.get_student(reg_no)

        result = (
            self.session.query(Programme.programme_name)
            .join(Enrollment, Enrollment.programme_id == Programme.id)
            .join(Student, Student.id == Enrollment.student_id)
            .all()
        )

        return {
            "bio": student.model_dump(),
            "programmes": [row.programme_name for row in result],
        }

    @override
    def create_student(self, data: StudentCreate) -> StudentResponse:
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

    @override
    def update_student(self, reg_no: str, data: StudentUpdate) -> StudentResponse | dict:
        student = self.get_student(reg_no)

        if not student:
            return {
                "message": f"Student with registration number {reg_no} does not exist"
            }
        # convert data to dictionary and set student attributes
        for field, value in data.model_dump(exclude_unset=True).items():
            setattr(student, field, value)
            self.session.commit()
        return student

    def delete_student(self, reg_no: str) -> dict:
        student = self.get_student(reg_no)

        if not student:
            return {
                "message": f"Student with registration number {reg_no} does not exist"
            }

        self.session.delete(student)
        self.session.commit()
        return {"message": f"Student {reg_no} successfully deleted!"}
