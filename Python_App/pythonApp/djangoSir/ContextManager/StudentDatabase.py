# A Context Manager is a Python construct used to automatically manage resources such as files, database connections, 
# network connections, and locks. It ensures that resources are properly acquired before use and properly released after use, 
# even if an exception occurs. In Python, Context Managers are typically implemented using the
# __enter__() and __exit__() methods.

import json
import os

class StudentDatabase:
    def __init__(self, filename):
        self.filename = filename

    def __enter__(self):
        # Create file if not exists
        if not os.path.exists(self.filename):
            with open(self.filename, "w") as file:
                json.dump([], file)

        self.file = open(self.filename, "r+")
        try:
            self.students = json.load(self.file)
        except json.JSONDecodeError:
            self.students = []
        return self.students

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            print("Error Occurred:", exc_val)
            
        self.file.seek(0)
        json.dump(self.students, self.file, indent=4)
        self.file.truncate()
        self.file.close()
        print("\nContext Manager Cleanup Completed")


def create_student():
    roll: int = int(input("Enter Roll: "))
    name: str = input("Enter Name: ")
    course: str = input("Enter Course: ")

    with StudentDatabase("students.json") as students:
        for student in students:
            if student["roll"] == roll:
                print("Roll Number Already Exists")
                return

        students.append({
            "roll": roll,
            "name": name,
            "course": course
        })
        print("Student Added Successfully")


def view_students():
    with StudentDatabase("students.json") as students:
        if not students:
            print("No Students Found")
            return
        print("\nStudent Records")

        for student in students:
            print(
                f"Roll: {student['roll']} | "
                f"Name: {student['name']} | "
                f"Course: {student['course']}"
            )


def search_student():
    roll = int(input("Enter Roll To Search: "))

    with StudentDatabase("students.json") as students:
        for student in students:
            if student["roll"] == roll:
                print("\nStudent Found")
                print(f"Roll: {student['roll']}")
                print(f"Name: {student['name']}")
                print(f"Course: {student['course']}")
                return

        print("Student Not Found")


def menu():
    while True:
        print("\n====== STUDENT MANAGEMENT ======")
        print("1. Create Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Exit")
        choice = input("Enter Choice: ")

        if choice == "1":
            create_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            print("Thank You")
            break
        else:
            print("Invalid Choice")

if __name__ == "__main__":
    menu()