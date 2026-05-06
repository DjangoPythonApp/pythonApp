# ---- Quantifiers or Counting ----
# ? means ZERO or EXACTLY one                       ex: ab?a         aba
# + means ATLEAST one or more                       ex: ab+a         aba, abba, abbba, abbbba
# * means ZERO or more                              ex: ab*a         aa, aba, abba, abbba, abbbba   

# . means EXACTLY one letter, number, symbol
# Regular Expression: A sequence of characters that forms a search pattern

import re

def check_input(pattern, user_input):
    if re.fullmatch(pattern, user_input):
        print("Match found!")
    else:
        print("No match!")

pattern: str = r"ab+a"        # Regular Exp String
user_input: str = input("Enter a string to check: ")
check_input(pattern, user_input)
    