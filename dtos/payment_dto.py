from typing import Optional

from pydantic import BaseModel


class PaymentDto(BaseModel):
    id1: int
    student_id: int
    programme_id: int
    pay1: float
    pay2: float
    pay3: float
    balance: float
    model_config = {"from_attributes": True}


class PaymentCreate(BaseModel):
    student_id: int
    programme_id: int
    pay1: float
    pay2: Optional[float] = 0.0
    pay3: Optional[float] = 0.0
    model_config = {"from_attributes": True}


class PaymentUpdate(BaseModel):
    student_id: int
    programme_id: int
    pay1: Optional[float] = None
    pay2: Optional[float] = None
    pay3: Optional[float] = None
    model_config = {"from_attributes": True}
