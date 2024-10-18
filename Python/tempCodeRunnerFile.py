#Calculate student grades
def calculate_grade(marks):
    if not isinstance(marks, int) or marks < 0 or marks > 100:
        return "Invalid marks"
    elif marks >= 95:
        return "A+"
    elif marks >= 90:
        return "A"
    elif marks >= 80:
        return "B"
    elif marks >= 70:
        return "C"
    elif marks >= 60:
        return "D"
    elif marks < 60:
        return "F"

#Example usage
marks = int(input("Enter marks: "))
grade = calculate_grade(marks)
print(f"Grade: {grade}")