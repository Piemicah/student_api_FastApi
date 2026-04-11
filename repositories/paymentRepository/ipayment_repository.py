from abc import abstractmethod, ABC

from dtos.payment_dto import PaymentCreate, PaymentResponse
from models.models import Payment


class IPaymentRepository(ABC):

    @abstractmethod
    def create_payment(self, data: PaymentCreate) -> PaymentResponse:
        pass
