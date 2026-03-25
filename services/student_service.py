from dtos.student_dto import StudentCreate, StudentResponse, StudentUpdate
from models.models import Student
from repositories.studentRepository.istudent_repository import IStudentRepository


class StudentService:
    def __init__(self, repository: IStudentRepository):
        self.repository = repository

    def get_all_students(self) -> list[dict]:
        return self.repository.get_all_students()

    def get_student(self, reg_no: str) -> dict:
        return self.repository.get_student(reg_no)

    def get_student_detail(self, reg_no: str) -> dict:
        return self.repository.get_student_detail(reg_no)

    def create_student(self, data: StudentCreate) -> StudentResponse:
        return self.repository.create_student(data)

    def update_student(self, reg_no: str, data: StudentUpdate) -> StudentResponse:
        return self.repository.update_student(reg_no, data)

    def delete_student(self, reg_no: str) -> dict:
        return self.repository.delete_student(reg_no)
