from typing import List


class Course:
    def __init__(self, course_id: str, name: str, credits: int) -> None:
        self.course_id: str = course_id
        self.name: str = name
        self.credits: int = credits

    def __str__(self) -> str:
        return f"{self.name} ({self.course_id}), {self.credits} ECTS"


class Student:
    def __init__(self, name: str, student_id: int, tuition_balance: float) -> None:
        self.name: str = name
        self.student_id: int = student_id
        self.tuition_balance: float = tuition_balance
        self.enrolled_courses: dict[str, Course] = {}

    def enroll(self, course: Course) -> None:
        """Zapisuje studenta na kurs."""
        self.enrolled_courses[course.course_id] = course

    def get_course(self, course_id: str) -> Course:
        """Zwraca obiekt kursu na podstawie jego ID."""
        return self.enrolled_courses.get(course_id, None)


# Przykładowe użycie
student_1: Student = Student("Jan Nowak", 3125, 2000.0)

data_science: Course = Course("TDM-2000", "Data Science", 6)

print(type(student_1))
print(type(data_science))

# Zapisujemy studenta na kurs
student_1.enroll(data_science)

# Pobieramy kurs
retrieved_course = student_1.get_course("TDM-2000")

if retrieved_course:
    print(f"Znaleziony kurs: {retrieved_course}")
else:
    print("Kurs nie znaleziony.")


