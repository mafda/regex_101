"""
We define a word character to be any of the following:

An English alphabetic letter (i.e., a-z and A-Z).
A decimal digit (i.e., 0-9).
An underscore (i.e., _, which corresponds to ASCII value 95).

Given n sentences consisting of one or more words separated by non-word characters, process q queries where each query consists of a single string, s. 
To process each query, count the number of occurrences of s as a sub-word in all n sentences, then print the number of occurrences on a new line.
"""

import re 

n = int(input())
text = "\n".join(input() for _ in range(n))

t = int(input())

for _ in range(t):
    print(len(re.findall(r'\w%s\w' % input().strip(), text)))
