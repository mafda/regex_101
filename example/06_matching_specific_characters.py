"""
    Task

    You have a test string S.
    Your task is to write a regex that will match S with following conditions:

    S must be of length: 6
    First character: 1, 2 or 3
    Second character: 1, 2 or 0
    Third character: x, s or 0
    Fourth character: 3, 0 , A or a
    Fifth character: x, s or u
    Sixth character: . or ,

"""

import re

Regex_Pattern = r'^[1-3][0-2][xs0][03aA][sux][\.\,]$'

print(str(bool(re.search(Regex_Pattern, input()))).lower())
