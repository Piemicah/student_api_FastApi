from abc import ABC, abstractmethod

from dtos.student_dto import StudentCreate, StudentDto
from models.models import Student


class IStudentRepository(ABC):
    @abstractmethod
    def get_all_students(self) -> list[StudentDto]:
        pass

    @abstractmethod
    def get_student(self, reg_no: str) -> StudentDto:
        pass

    @abstractmethod
    def create_student(self, student: Student):
        pass
