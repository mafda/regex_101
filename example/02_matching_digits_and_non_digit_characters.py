"""
  Task
  You have a test string S. Your task is to match the pattern xxXxxXxxxx
  Here x denotes a digit character, and X denotes a non-digit character.
"""

import re

Regex_Pattern = r"\d\d\D\d\d\D\d\d\d\d"

print(str(bool(re.search(Regex_Pattern, input()))).lower())
