"""
Task

Given a test string, s, write a RegEx that matches s under the following conditions:

s must start with Mr., Mrs., Ms., Dr. or Er..
The rest of the string must contain only one or more English alphabetic letters (upper and lowercase).
"""

import re

Regex_Pattern = r'^(Mr\.|Mrs\.|Dr\.|Er\.)[a-zA-Z]+$'

print(str(bool(re.search(Regex_Pattern, input()))).lower())
