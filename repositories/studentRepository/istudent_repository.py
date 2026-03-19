from abc import ABC, abstractmethod

from dtos.student_dto import StudentCreate, StudentDto, StudentUpdate
from models.models import Student


class IStudentRepository(ABC):
    @abstractmethod
    def get_all_students(self) -> list[StudentDto]:
        pass

    @abstractmethod
    def get_student(self, reg_no: str) -> StudentDto | dict:
        pass

    @abstractmethod
    def create_student(self, data: Student):
        pass

    @abstractmethod
    def update_student(self, reg_no: str, data: StudentUpdate) -> StudentDto:
        pass

    @abstractmethod
    def delete_student(self, reg_no: str) -> dict:
        pass
