from env.database import SessionLocal
from env.models import Student, Enrollment

db = SessionLocal()

try:
    # Find an existing student
    student = db.query(Student).first()

    if student is None:
        print("No students found. Create a student first.")
    else:
        # Create an enrollment for that student
        existing_enrollment = db.query(Enrollment).filter(
        Enrollment.student_id == student.student_id,
        Enrollment.course == "Machine Learning"
        ).first()

        if existing_enrollment is None:
            enrollment = Enrollment(course="Machine Learning")
            student.enrollments.append(enrollment)
            db.commit()
            print("Enrollment created successfully!")

        else:
            print("Student is already enrolled in this course.")
        db.commit()
        db.refresh(student)

        print("Student:", student.name)
        print("Courses:")

        for item in student.enrollments:
            print("-", item.course)

except Exception as e:
    db.rollback()
    print("Error:", e)

finally:
    db.close()