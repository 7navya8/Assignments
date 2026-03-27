# Assignment (19/02/2026)

# Assignment Name : Student Data Manager
# Description : Store data for 5 students 
# using dictionaries, print topper, class average, and assign grades.

def assign_grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 75:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 40:
        return "D"
    else:
        return "F"

students = {
    "Alice": 95,
    "Bob": 82,
    "Charlie": 67,
    "David": 45,
    "Eva": 38
}

print("Student Results:")
for name, marks in students.items():
    grade = assign_grade(marks)
    print(f"{name}: {marks} marks, Grade {grade}")

topper = max(students, key=students.get)
print(f"\nTopper: {topper} with {students[topper]} marks")

average = sum(students.values()) / len(students)
print(f"Class Average: {average:.2f}")