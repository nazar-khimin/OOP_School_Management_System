from typing import TYPE_CHECKING
from src.Person import Person
from src.utils.Validations import validate_grade_value

if TYPE_CHECKING:
    from src.Course import Course


class Student(Person):
    def __init__(self, name):
        super().__init__(name)
        self.courses: list["Course"] = []
        self.grades: list[int] = []
        self.grade_level: list[int] = []

    def enroll_course(self, course: "Course"):
        self.courses.append(course)

    def add_grade(self, grade):
        validate_grade_value(grade)
        pass

    def calculate_gpa(self):
        """
        Note: GPA (Grade Point Average) is calculated as the sum of (grade * credits) / total credits for all courses.
        """
        pass

    def __repr__(self):
        courses_names = [course.name for course in self.courses]
        return (f'Student('
                f'{super().__repr__()!r}, '
                f'courses = {courses_names!r}, '
                f'grades = {self.grades!r}, '
                f'grade_level = {self.grade_level!r}'
                f')')
