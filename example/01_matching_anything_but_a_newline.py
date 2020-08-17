import re
import sys

test_string = input()

match = re.match(regex_pattern, test_string) is not None

regex_pattern = r"^(.{3}\.){3}.{3}$"

print(str(match).lower())
