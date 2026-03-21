from typing import Optional

from pydantic import BaseModel


class EnrollmentDto(BaseModel):
    id: int
    student_id: int
    programme_id: int
    subject1: str
    subject2: str
    subject3: str
    model_config = {"from_attributes": True}


class EnrollmentCreate(BaseModel):
    student_id: int
    programme_id: int
    subject1: str
    subject2: str
    subject3: str
    model_config = {"from_attributes": True}


class EnrollmentUpdate(BaseModel):
    subject1: Optional[str] = None
    subject2: Optional[str] = None
    subject3: Optional[str] = None
    model_config = {"from_attributes": True}
