from abc import ABC, abstractmethod

from dtos.student_dto import StudentCreate, StudentResponse, StudentUpdate
from models.models import Student


class IStudentRepository(ABC):
    @abstractmethod
    def get_all_students(self) -> list[dict]:
        """Fetches all students from the database

        Returns:
            list[StudentDto]: list of studentDto
        """
        pass

    @abstractmethod
    def get_student(self, reg_no: str) -> dict:
        """Fetch a single student record

        Args:
            reg_no (str): Student registration number

        Returns:
            dict: returns student record
        """
        pass

    
    @abstractmethod
    def create_student(self, data: Student):
        pass

    @abstractmethod
    def update_student(self, reg_no: str, data: StudentUpdate) -> StudentResponse:
        pass

    @abstractmethod
    def delete_student(self, reg_no: str) -> dict:
        pass
