import re

def check_input(pattern, user_input):
    if re.fullmatch(pattern, user_input):
        print("Match found!")
    else:
        print("No match!")

pattern: str = r"[0-9]{3}"   # Exactly 3 digits
# pattern: str = r"[0-9]{2,5}"   # Between 2 and 5 digits

user_input: str = input("Enter a string to check: ")
check_input(pattern, user_input)