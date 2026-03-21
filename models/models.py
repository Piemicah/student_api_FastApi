from sqlalchemy import (
    Column,
    Computed,
    DateTime,
    Integer,
    Numeric,
    String,
    ForeignKey,
)
from sqlalchemy.orm import relationship

from data.base import Base


class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, autoincrement=True)
    reg_no = Column(String, unique=True)
    name = Column(String)
    phone = Column(String)
    dob = Column(DateTime, nullable=True)
    state = Column(String, nullable=True)
    lga = Column(String, nullable=True)
    enrollments = relationship("Enrollment")
    payments = relationship("Payment")


class Programme(Base):
    __tablename__ = "programmes"

    id = Column(Integer, primary_key=True, autoincrement=False)
    programme_name = Column(String)
    enrollments = relationship("Enrollment")
    payments = relationship("Payment")


class Enrollment(Base):
    __tablename__ = "enrollments"

    id = Column(Integer, primary_key=True, autoincrement=True)
    student_id = Column(ForeignKey("students.id"))
    programme_id = Column(ForeignKey("programmes.id"))
    subject1 = Column(String)
    subject2 = Column(String)
    subject3 = Column(String)


class Payment(Base):

    __tablename__ = "payments"
    id = Column(Integer, primary_key=True, autoincrement=True)
    student_id = Column(ForeignKey("students.id"))
    programme_id = Column(ForeignKey("programmes.id"))
    pay1 = Column(Numeric(8, 2), default=0.0)
    pay2 = Column(Numeric(8, 2), default=0.0)
    pay3 = Column(Numeric(8, 2), default=0.0)
    balance = Column(Numeric(8, 2), Computed("300000-(pay1+pay2+pay3)"))
