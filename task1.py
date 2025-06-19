students = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78,
    "Diana": 90
}

name = input("Enter student name: ")

if name in students:
    print("Marks of", name, "are", students[name])
else:
    print("Student not found.")
