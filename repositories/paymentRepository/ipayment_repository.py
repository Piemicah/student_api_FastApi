from abc import abstractmethod, ABC

from dtos.payment_dto import PaymentCreate, PaymentDto
from models.models import Payment


class IPaymentRepository(ABC):

    @abstractmethod
    def create_payment(self, data: PaymentCreate) -> Payment:
        pass
