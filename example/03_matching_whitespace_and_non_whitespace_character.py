import re

Regex_Pattern = r"\S\S\s\S\S\s\S\S"

print(str(bool(re.search(Regex_Pattern, input()))).lower())
