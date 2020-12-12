"""
Task
You have a test String S.
Write a regex which can match all the occurences of digit which are immediately preceded by odd digit.
"""

import re

Test_String = input()

match = re.findall(Regex_Pattern, Test_String)

Regex_Pattern = '(?<=[13579])[\d]'

print("Number of matches :", len(match))
