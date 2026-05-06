# Escape	Meaning
# \d	digit (0–9)
# \w	word char (a-z, A-Z, 0-9, _)
# \s	whitespace (space, tab, newline)
# \D	not a digit (complement of \d)
# \W	not a word char (complement of \w)
# \S	not whitespace (complement of \s)


import re

pattern = r"\d"     # i.e. “Does the string contain at least one digit?”, 

user_input = input("Enter text: ")

if re.search(pattern, user_input):
    print("Match found!")
else:
    print("No match!")

# output:
# Enter text: 123
# Match found!

# output:
# Enter text: abc
# No match

# output:
# Enter text: 123abc
# Match found (re.search checks at least one digit in the entire string)