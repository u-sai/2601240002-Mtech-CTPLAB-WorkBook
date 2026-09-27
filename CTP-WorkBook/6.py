from dataclasses import dataclass


class StudentTraditional:

    def __init__(self, name: str, roll_no: int, marks: float) -> None:
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

    def display(self) -> None:
        print(self.name, self.roll_no, self.marks)


@dataclass
class Student:

    name: str
    roll_no: int
    marks: float

    def display(self) -> None:
        print(self.name, self.roll_no, self.marks)


traditional_student = StudentTraditional(
    "Surya",
    101,
    85.5
)

dataclass_student = Student(
    "Ramya",
    102,
    91.5
)


print("Traditional Class:")
traditional_student.display()

print("\nDataclass:")
dataclass_student.display()

print("\nDataclass Object:")
print(dataclass_student)