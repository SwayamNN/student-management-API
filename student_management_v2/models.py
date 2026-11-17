
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

from env.database import Base







class Student(Base):
    __tablename__ = "students_v2"

    student_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    age = Column(Integer, nullable=False)
    marks = Column(Integer, default=0)

    created_at = Column(DateTime(timezone=True), server_default=func.now())
    enrollments = relationship(
    "Enrollment",
    back_populates="student",
    cascade="all, delete-orphan"
)

class Enrollment(Base):
    __tablename__ = "enrollments_v2"

    enrollment_id = Column(Integer, primary_key=True, index=True)
    student_id = Column(
        Integer,
        ForeignKey("students_v2.student_id"),
        nullable=False
    )
    course = Column(String(100), nullable=False)

    student = relationship("Student", back_populates="enrollments")