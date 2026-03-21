from abc import ABC, abstractmethod

from dtos.student_dto import StudentCreate, StudentDto, StudentUpdate
from models.models import Student


class IStudentRepository(ABC):
    @abstractmethod
    def get_all_students(self) -> list[StudentDto]:
        """Fetches all students from the database

        Returns:
            list[StudentDto]: list of studentDto
        """
        pass

    @abstractmethod
    def get_student(self, reg_no: str) -> StudentDto | dict:
        """Fetch a single student record

        Args:
            reg_no (str): Student registration number

        Returns:
            StudentDto | dict: returns student record if exist or a dictionary of message
        """
        pass

    @abstractmethod
    def get_student_detail(self, reg_no: str) -> dict:
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
