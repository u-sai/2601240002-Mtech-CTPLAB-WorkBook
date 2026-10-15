def calculate_grade(marks: int) -> str:
    if marks < 0 or marks > 100:
        return "Invalid Marks"

    if marks >= 90:
        return "A"
    elif marks >= 80:
        return "B"
    elif marks >= 70:
        return "C"
    elif marks >= 60:
        return "D"
    else:
        return "F"


def main() -> None:
    marks = int(input("Enter marks: "))

    grade = calculate_grade(marks)

    print("Marks:", marks)
    print("Grade:", grade)


if __name__ == "__main__":
    main()