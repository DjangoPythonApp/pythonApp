# 1. Normal Way
numbers = [1, 2, 3, 4, 5]

square = []

for n in numbers:
    square.append(n * n)

print(square)

# List Comprehension
numbers = [1, 2, 3, 4, 5]
square = [n * n for n in numbers]               # [new_value for item in iterable]
print(square)

# -----------------------
# 2. List Comprehension with Condition

numbers = [1, 2, 3, 4, 5]
square = [n * n for n in numbers if n % 2 == 0]  # [new_value for item in iterable if condition]
print(square)

# -----------------------
# 3. List Comprehension with if-else
numbers = [10, -5, 7, -2, 0]
result = ["Positive" if n > 0 else "Negative or Zero" for n in numbers]
print(result)

# -----------------------
# 4. List Comprehension with Nested Condition

numbers = [1, 2, 3, 4, 5]
square = [n * n for n in numbers if n % 2 == 0 and n > 2]  # [new_value for item in iterable if condition]
print(square)

# -----------------------
# 5. List Comprehension with Multiple Iterables

numbers = [1, 2, 3, 4, 5]
square = [n * n for n in numbers for m in range(2)]  # [new_value for item in iterable for item in iterable]
print(square)

# -----------------------
# 6. List Comprehension with Multiple Iterables and Condition

numbers = [1, 2, 3, 4, 5]
square = [n * n for n in numbers for m in range(2) if m % 2 == 0]  # [new_value for item in iterable for item in iterable if condition]
print(square)

# -----------------------
# 7. Nested List Comprehension

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
flat = [item for row in matrix for item in row]
print(flat)

# ---------------------------
# 8. Dictionary Comprehension

numbers = [1, 2, 3, 4, 5]
square_dict = {n: n*n for n in numbers}
print(square_dict)

# ---------------------------
# 9. Set Comprehension

numbers = [1, 2, 3, 4, 5]
square_set = {n * n for n in numbers}
print(square_set)

# ---------------------------
# 10. Tuple Comprehension

numbers = [1, 2, 3, 4, 5]
square_tuple = tuple(n * n for n in numbers)
print(square_tuple)

# ---------------------------
# 11. Dictionary Comprehension with Condition

students = {
    "Amit": 78,
    "Rahul": 45,
    "Priya": 90,
    "Sneha": 30
}
passed = {name: marks for name, marks in students.items() if marks >= 50}
print(passed)

# ---------------------------
# 12. Extract Usernames

users = [
    {"username": "amit", "active": True},
    {"username": "rahul", "active": False},
    {"username": "priya", "active": True}
]

active_users = [user["username"] for user in users if user["active"]]
print(active_users)

# ---------------------
# 13. Transpose Matrix

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

transposed = [[row[i] for row in matrix] for i in range(3)]
print(transposed)