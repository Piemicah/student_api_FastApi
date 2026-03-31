from datetime import datetime
from typing import Optional

from pydantic import BaseModel

from dtos.enrollment_dto import EnrollmentResponse


class StudentResponse(BaseModel):
    id: int
    reg_no: str
    name: str
    phone: str
    dob: Optional[datetime] = None
    state: Optional[str] = None
    lga: Optional[str] = None
    model_config = {"from_attributes": True}


class StudentCreate(BaseModel):
    reg_no: str
    name: str
    phone: str
    dob: Optional[datetime] = None
    state: Optional[str] = None
    lga: Optional[str] = None


class StudentUpdate(BaseModel):
    name: Optional[str] = None
    phone: Optional[str] = None
    dob: Optional[datetime] = None
    state: Optional[str] = None
    lga: Optional[str] = None
