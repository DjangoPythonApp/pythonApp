# 1. Use re.search()

# When:
# You want to find something anywhere
#     Example:
#     Check if string contains a number
#     Check if email contains @

# ✔ Real use case:
# re.search(r"\d", "abc123")  # find any digit
# re.search(r"\d+", "abc123")  # find one or more digits

# re.search(r"\w", "abc123")  # find any word character
# re.search(r"\w+", "abc123")  # find one or more word characters

# import re

# if re.search("abc", "xabcx"):
#     print("Search: Match found")

# output:
# Search: Match found
# Because "abc" exists somewhere inside in "xabcx"

# -----------------------------------
# 2. Use re.match()

# When:
# You want to check only the beginning (only at position 0) and not bothering about the rest

# ✔ Real use case:
# Validate prefixes
# Check if string starts with "http"
# re.match(r"http", "http://example.com")

# import re

# if re.match("abc", "xabcx"):
#     print("Match: Match found")
# else:
#     print("Match: No match")

# Output:
# Match: No match
# Because string does not start with "abc"
# -----------------------------------

# 3. Use re.fullmatch() 
# When:

# You want strict validation
# Entire string must follow rules

# ✔ Real use case:

# Password validation
# Phone number
# Name validation
# re.fullmatch(r"[0-9]{10}", "9876543210")

# re.fullmatch()
# if re.fullmatch("abc", "xabcx"):
#     print("Fullmatch: Match found")
# else:
#     print("Fullmatch: No match")

# output:
# Fullmatch: No match
# Because entire string is not exactly "abc"

# -----------------------------------
# Anchors → ^ and $

# What they do
#     Anchors don’t match characters. They match positions:

# ^ → start of the string
# $ → end of the string

import re

pattern = r"^abc$"

user_input = input("Enter text: ")

if re.match(pattern, user_input):
    print("Match found!")
else:
    print("No match!")
# Note: using ^ and $ is behaving like fullmatch

# -----------------------------------