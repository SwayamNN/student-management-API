
from sqlalchemy.orm import Session
from env.models import Student , Enrollment
from schemas import StudentCreate


# CREATE
def create_student(db: Session, student: StudentCreate):
    try:
        new_student = Student(**student.model_dump())
        db.add(new_student)
        db.commit()
        db.refresh(new_student)
        return new_student

    except Exception:
        db.rollback()
        raise


# READ ALL
def get_students(db: Session, skip: int = 0, limit: int = 10):
    return (
        db.query(Student)
        .offset(skip)
        .limit(limit)
        .all()
    )


# READ BY ID
def get_student(db: Session, student_id: int):
    return db.query(Student).filter(
        Student.student_id == student_id
    ).first()


# UPDATE
def update_student(db: Session, student_id: int, student_data: StudentCreate):
    try:
        student = get_student(db, student_id)

        if student is None:
            return None

        for key, value in student_data.model_dump().items():
            setattr(student, key, value)

        db.commit()
        db.refresh(student)
        return student

    except Exception:
        db.rollback()
        raise

# DELETE
def delete_student(db: Session, student_id: int):
    try:
        student = get_student(db, student_id)

        if student is None:
            return None

        db.delete(student)
        db.commit()
        return student

    except Exception:
        db.rollback()
        raise


# SEARCH STUDENTS BY NAME
def search_students(db: Session, name: str):
    return db.query(Student).filter(
        Student.name.ilike(f"%{name}%")
    ).all()


# FILTER STUDENTS BY MINIMUM MARKS
def filter_students_by_marks(db: Session, min_marks: int):
    return db.query(Student).filter(
        Student.marks >= min_marks
    ).all()

# FILTER STUDENTS BY MARKS AND AGE
def filter_students(db: Session, min_marks: int, min_age: int):
    return db.query(Student).filter(
        Student.marks >= min_marks,
        Student.age >= min_age
    ).all()

def get_student_enrollments(db: Session, student_id: int):
    return db.query(Enrollment).filter(
        Enrollment.student_id == student_id
    ).all()


def filter_students_by_age(db: Session, min_age: int, max_age: int):
    return db.query(Student).filter(
        Student.age >= min_age,
        Student.age <= max_age
    ).all()

def sort_students_by_marks(db: Session, order: str = "desc"):
    query = db.query(Student)

    if order == "asc":
        return query.order_by(Student.marks.asc()).all()

    return query.order_by(Student.marks.desc()).all()

def count_students(db: Session):
    return db.query(Student).count()