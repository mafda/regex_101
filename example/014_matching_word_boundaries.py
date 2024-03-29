"""
Task

You have a test String S.
Your task is to write a regex which will match word starting with vowel (a,e,i,o, u, A, E, I , O or U).
The matched word can be of any length. The matched word should consist of letters (lowercase and uppercase both) only.
The matched word must start and end with a word boundary.
"""

import re

Regex_Pattern = r'\b[aeiouAEIOU][a-zA-Z]*\b'

print(str(bool(re.search(Regex_Pattern, input()))).lower())
