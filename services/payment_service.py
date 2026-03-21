from dtos.payment_dto import PaymentCreate
from repositories.paymentRepository.ipayment_repository import IPaymentRepository


class PaymentService:
    def __init__(self, repository: IPaymentRepository):
        self.repository = repository

    def create_payment(self, data: PaymentCreate):
        return self.repository.create_payment(data)
