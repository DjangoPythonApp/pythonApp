# ---- Quantifiers or Counting ----
# ? means ZERO or EXACTLY one     
# + means ATLEAST one or more     
# * means ZERO or more            

import re


def check_input(pattern, user_input):
    if re.fullmatch(pattern, user_input):
        print("Match found!")
    else:
        print("No match!")

pattern: str = r"(ab)"       # Match the exact sequence "ab" as a unit
# pattern = r"abc(ab)?"       # Grouping
user_input: str = input("Enter a string to check: ")
check_input(pattern, user_input)

