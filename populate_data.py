import uuid
from models.base import SessionLocal
from models.schools.school import School
from models.teachers.subject_specialities import SubjectSpecialty, SubjectSpecialties
from models.teachers.teacher import Teacher

# Sample data
schools_data = [
    {"name": "Springfield Elementary"},
    {"name": "Shelbyville High"},
]

subject_specialties_data = [
    {"name": SubjectSpecialties.MATH},
    {"name": SubjectSpecialties.SCIENCE},
    {"name": SubjectSpecialties.HISTORY},
    {"name": SubjectSpecialties.LITERATURE},
    {"name": SubjectSpecialties.ART},
    {"name": SubjectSpecialties.MUSIC},
    {"name": SubjectSpecialties.PHYSICAL_EDUCATION},
]

# Populate the database
def populate_data():
    # Create a new session
    session = SessionLocal()

    try:
        # Add schools
        for school_data in schools_data:
            school = School(name=school_data["name"])
            session.add(school)

        # Add subject specialties
        for specialty_data in subject_specialties_data:
            specialty = SubjectSpecialty(name=specialty_data["name"])
            session.add(specialty)

        # Commit the session to save the data
        session.commit()

        # Add teachers
        schools = session.query(School).all()
        specialties = session.query(SubjectSpecialty).all()

        teachers_data = [
            {"name": "John Doe", "subject_specialty_id": specialties[1].id, "grade_level": 5, "school_id": schools[0].id},
            {"name": "Jane Smith", "subject_specialty_id": specialties[0].id, "grade_level": 6, "school_id": schools[0].id},
            {"name": "Emily Johnson", "subject_specialty_id": specialties[3].id, "grade_level": 4, "school_id": schools[1].id},
        ]

        for teacher_data in teachers_data:
            teacher = Teacher(
                name=teacher_data["name"],
                subject_specialty_id=teacher_data["subject_specialty_id"],
                grade_level=teacher_data["grade_level"],
                school_id=teacher_data["school_id"]
            )
            session.add(teacher)

        # Commit the session to save data to the database
        session.commit()

        # Verify data
        print("Schools:")
        for school in session.query(School).all():
            print(f"ID: {school.id}, Name: {school.name}")

        print("\nSubject Specialties:")
        for specialty in session.query(SubjectSpecialty).all():
            print(f"ID: {specialty.id}, Name: {specialty.name.value}")

        print("\nTeachers:")
        for teacher in session.query(Teacher).all():
            print(f"ID: {teacher.id}, Name: {teacher.name}, Subject Specialty ID: {teacher.subject_specialty_id}, Grade Level: {teacher.grade_level}, School ID: {teacher.school_id}")

        print("Data added successfully!")

    except Exception as e:
        session.rollback()
        print(f"Error: {e}")

    finally:
        session.close()

if __name__ == "__main__":
    populate_data()