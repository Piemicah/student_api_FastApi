from abc import abstractmethod, ABC

from dtos.enrollment_dto import EnrollmentCreate, EnrollmentResponse
from models.models import Enrollment


class IEnrollmentRepository(ABC):

    @abstractmethod
    def get_all_enrollments(self) -> list[EnrollmentResponse]:
        """Fetches all enrollments

        Returns:
            list[EnrollmentDto]: list of all enrollments
        """
        pass

    @abstractmethod
    def create_enrollment(self, data: EnrollmentCreate) -> dict:
        pass
