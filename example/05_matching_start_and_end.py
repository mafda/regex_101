```
  task
  You have a test string S. Your task is to match the pattern Xxxxx.
  Here, x denotes a word character, and X denotes a digit.
  S must start with a digit X and end with . symbol.
  S should be 6 characters long only.
```

import re

Regex_Pattern = r"^[\d][\w]{4}\.$"

print(str(bool(re.search(Regex_Pattern, input()))).lower())
