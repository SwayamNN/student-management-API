from fastapi import FastAPI, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session

from env.database import SessionLocal
from schemas import StudentCreate, StudentResponse, EnrollmentResponse
import crud


app = FastAPI(
    title="Student Management API V2",
    description="Student API using FastAPI, SQLAlchemy and PostgreSQL",
    version="2.0.0"
)


# DATABASE SESSION DEPENDENCY
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# CREATE STUDENT
@app.post(
    "/students",
    response_model=StudentResponse,
    status_code=status.HTTP_201_CREATED
)
def create_student(
    student: StudentCreate,
    db: Session = Depends(get_db)
):
    try:
        return crud.create_student(db, student)
    except Exception:
        db.rollback()
        raise HTTPException(
            status_code=500,
            detail="Could not create student"
        )


# GET ALL STUDENTS
@app.get("/students", response_model=list[StudentResponse])
def read_students(
    skip: int = Query(default=0, ge=0),
    limit: int = Query(default=10, ge=1, le=100),
    db: Session = Depends(get_db)
):
    return crud.get_students(db, skip, limit)


# SEARCH STUDENTS BY NAME
@app.get("/students/search", response_model=list[StudentResponse])
def search_students(
    name: str,
    db: Session = Depends(get_db)
):
    return crud.search_students(db, name)


# FILTER STUDENTS BY MARKS
@app.get("/students/filter", response_model=list[StudentResponse])
def filter_students(
    min_marks: int,
    db: Session = Depends(get_db)
):
    if min_marks < 0 or min_marks > 100:
        raise HTTPException(
            status_code=400,
            detail="Marks must be between 0 and 100"
        )

    return crud.filter_students_by_marks(db, min_marks)

# FILTER STUDENTS BY MARKS AND AGE
@app.get("/students/filter/advanced", response_model=list[StudentResponse])
def advanced_filter(
    min_marks: int,
    min_age: int,
    db: Session = Depends(get_db)
):
    return crud.filter_students(db, min_marks, min_age)


@app.get(
    "/students/{student_id}/enrollments",
    response_model=list[EnrollmentResponse]
)
def read_student_enrollments(
    student_id: int,
    db: Session = Depends(get_db)
):
    student = crud.get_student(db, student_id)

    if student is None:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return crud.get_student_enrollments(db, student_id)



@app.get("/students/filter/age", response_model=list[StudentResponse])
def filter_by_age(
    min_age: int,
    max_age: int,
    db: Session = Depends(get_db)
):
    if min_age < 5 or max_age > 120 or min_age > max_age:
        raise HTTPException(
            status_code=400,
            detail="Invalid age range"
        )

    return crud.filter_students_by_age(db, min_age, max_age)

@app.get("/students/sort", response_model=list[StudentResponse])
def sort_students(
    order: str = "desc",
    db: Session = Depends(get_db)
):
    if order not in ["asc", "desc"]:
        raise HTTPException(
            status_code=400,
            detail="Order must be 'asc' or 'desc'"
        )

    return crud.sort_students_by_marks(db, order)

@app.get("/students/count")
def get_student_count(db: Session = Depends(get_db)):
    total = crud.count_students(db)

    return {
        "total_students": total
    }


# GET STUDENT BY ID
@app.get("/students/{student_id}", response_model=StudentResponse)
def read_student(
    student_id: int,
    db: Session = Depends(get_db)
):
    student = crud.get_student(db, student_id)

    if student is None:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return student


# UPDATE STUDENT
@app.put("/students/{student_id}", response_model=StudentResponse)
def update_student(
    student_id: int,
    student_data: StudentCreate,
    db: Session = Depends(get_db)
):
    try:
        student = crud.update_student(
            db, student_id, student_data
        )

        if student is None:
            raise HTTPException(
                status_code=404,
                detail="Student not found"
            )

        return student

    except HTTPException:
        raise

    except Exception:
        db.rollback()
        raise HTTPException(
            status_code=500,
            detail="Could not update student"
        )


# DELETE STUDENT
@app.delete("/students/{student_id}")
def remove_student(
    student_id: int,
    db: Session = Depends(get_db)
):
    try:
        student = crud.delete_student(db, student_id)

        if student is None:
            raise HTTPException(
                status_code=404,
                detail="Student not found"
            )

        return {
            "message": "Student deleted successfully"
        }

    except HTTPException:
        raise

    except Exception:
        db.rollback()
        raise HTTPException(
            status_code=500,
            detail="Could not delete student"
        )
