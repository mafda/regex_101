"""
Task
You have a test string S.
Write a regex that can match all occurrences of o followed immediately by oo in S.
"""

import re

Test_String = input()

match = re.findall(Regex_Pattern, Test_String)

print("Number of matches :", len(match))

Regex_Pattern = 'o(?=oo)'
