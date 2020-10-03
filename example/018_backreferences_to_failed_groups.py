"""
Task

You have a test string S.
Your task is to write a regex which will match S, with following condition(s):

S consists of 8 digits.
S may have "-" separator such that string S gets divided in 4 parts, with each part having exactly two digits. (Eg. 12-34-56-78)
 """
 
import re

Regex_Pattern = r"^(\d){8}$|^(\d\d\-){3}(\d\d)$"

print(str(bool(re.search(Regex_Pattern, input()))).lower())
