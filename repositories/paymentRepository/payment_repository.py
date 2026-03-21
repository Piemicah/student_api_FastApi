from sqlalchemy.orm import Session

from dtos.payment_dto import PaymentCreate, PaymentDto
from models.models import Payment

from .ipayment_repository import IPaymentRepository


class PaymentRepository(IPaymentRepository):
    def __init__(self, session: Session):
        self.session = session

    def create_payment(self, data: PaymentCreate):
        payment = Payment(
            student_id=data.student_id,
            programme_id=data.programme_id,
            pay1=data.pay1,
            pay2=data.pay2,
            pay3=data.pay3,
        )

        self.session.add(payment)
        self.session.commit()
        return payment
