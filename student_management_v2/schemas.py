
from pydantic import BaseModel, EmailStr, Field, ConfigDict
from datetime import datetime


class StudentCreate(BaseModel):
    name: str = Field(min_length=2, max_length=100)
    email: EmailStr
    age: int = Field(ge=5)
    marks: int = Field(ge=0, le=100)


class StudentResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    student_id: int
    name: str
    email: EmailStr
    age: int
    marks: int
    created_at: datetime

class EnrollmentResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    enrollment_id: int
    student_id: int
    course: str