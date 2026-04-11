from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from data.database import get_session
from dtos.payment_dto import PaymentCreate, PaymentResponse
from repositories.paymentRepository.payment_repository import PaymentRepository
from services.payment_service import PaymentService

router = APIRouter(prefix="/payments", tags=["Payments"])


def get_payment_service(session: Session = Depends(get_session)):
    repo = PaymentRepository(session)
    return PaymentService(repository=repo)


@router.post("/", response_model=PaymentResponse)
def create_payment(
    data: PaymentCreate, service: PaymentService = Depends(get_payment_service)
):
    return service.create_payment(data)
