# ---------------- STUDENT DATABASE ---------------- #

students = {
    101: {"name": "Pooja", "marks": 89},
    102: {"name": "Rahul", "marks": 75}
}

# ---------------- CREATE STUDENT ---------------- #

def create_student():
    try:
        roll: int = int(input("Enter Roll Number: "))

        if roll in students:
            raise KeyError("Duplicate Roll Number")

        name: str = input("Enter Student Name: ")
        marks: int = int(input("Enter Student Marks: "))

        if marks < 0 or marks > 100:
            raise ValueError("Marks should be between 0 and 100")

        students[roll] = {
            "name": name,
            "marks": marks
        }

        print("Student Added Successfully")
        logging.info(f"Student Added -> Roll: {roll}")

    except ValueError as v:
        print(v)
        logging.error(v)

    except KeyError as k:
        print(k)
        logging.error(k)