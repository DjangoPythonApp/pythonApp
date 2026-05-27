# Exception Handling with List
students = ["Rahul", "Ankit", "Priya"]

try:
    index = int(input("Enter index number: "))
    print("Student Name:", students[index])

except IndexError:
    print("Index out of range.")

except ValueError:
    print("Please enter integer value only.")