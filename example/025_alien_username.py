"""
In a galaxy far, far away, on a planet different from ours, each computer username uses the following format:

- It must begin with either an underscore, _ (ASCII value 95), or a period, . (ASCII value 46).
- The first character must be immediately followed by one or more digits in the range 0 through 9.
- After some number of digits, there must be 0 or more English letters (uppercase and/or lowercase).
- It may be terminated with an optional _ (ASCII value 95). Note that if it's not terminated with an underscore, 
then there should be no characters after the sequence of 0 or more English letters.
- Given n strings, determine which ones are valid alien usernames. If a string is a valid alien username, print VALID on a new line; otherwise, print INVALID.
"""

import re

n = int(input())

for _ in range(n):
    i = input()
    m = re.match(r'^[_\.]\d+[a-zA-Z]*_?$', i)
    if m:
        print('VALID')
    else:
        print('INVALID')
