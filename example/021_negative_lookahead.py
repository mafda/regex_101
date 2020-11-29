"""
Task
You have a test String S.
Write a regex which can match all characters which are not immediately followed by that same character.
"""

import re

Test_String = input()

match = re.findall(Regex_Pattern, Test_String)

Regex_Pattern = '(.)(?!\1)'

print("Number of matches :", len(match))
