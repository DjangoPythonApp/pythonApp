# ---- Quantifiers or Counting ----
# ? means ZERO or EXACTLY one                       ex: ab?a        aba
# + means ATLEAST one or more                       ex: ab+a         aba, abba, abbba, abbbba
# * means ZERO or more                              ex: ab*a         aa, aba, abba, abbba, abbbba   

import re


def check_input(pattern, user_input):
    if re.fullmatch(pattern, user_input):
        print("Match found!")
    else:
        print("No match!")

pattern: str = r"[0-9]+[a-zA-Z]*"       # Single character from a set
# pattern = r"[ab]"       # Single characters from a set, i.e. a or b only
user_input: str = input("Enter a string to check: ")
check_input(pattern, user_input)
