# Regex 101

A regular expression is a sequence of characters that define a search pattern.

## Introduction

| Regex | Description | Example |
| :---: | :---------- | :------ |
| dot   | The dot (.) matches anything (except for a newline). | [01_matching_anything_but_a_newline.py](https://github.com/mafda/regex_101/blob/master/example/01_matching_anything_but_a_newline.py) |
| \d    | The expression \d matches any digit [0-9]. |  |
| \D    | The expression \D matches any character that is not a digit. | [02_matching_digits_and_non_digit_characters.py](https://github.com/mafda/regex_101/blob/master/example/02_matching_digits_and_non_digit_characters.py) |
| \s    | The expression \s matches any whitespace character [ \r\n\t\f ]. |  |
| \S    | The expression \S matches any non-white space character | [03_matching_whitespace_and_non_whitespace_character.py](https://github.com/mafda/regex_101/blob/master/example/03_matching_whitespace_and_non_whitespace_character.py) |
| \w    | The expression \w will match any word character. Word characters include alphanumeric characters (a-z, A-Z and 0-9) and underscores (_). |  |
| \W    | The expression \W matches any non-word character. Non-word characters include alphanumeric characters (a-z, A-Z and 0-9) and underscores (_).| [04_matching_world_and_non_world_character.py](https://github.com/mafda/regex_101/blob/master/example/04_matching_world_and_non_world_character.py) |
| ^    | The ^ symbol matches the position at the start of a string. |  |
| $    | The $ symbol matches the position at the end of a string. | [05_matching_start_and_end.py](https://github.com/mafda/regex_101/blob/master/example/05_matching_start_and_end.py) |

## Character Class

| Regex | Description | Example |
| :---: | :---------- | :------ |
| [ ]   | The character class [ ] matches only one out of several characters placed inside the square brackets. | [06_matching_specific_characters.py](https://github.com/mafda/regex_101/blob/master/example/06_matching_specific_characters.py) |
| [^]   | The negated character class [^] matches any character that is not in the square brackets. | [07_excluding_specific_characters.py](https://github.com/mafda/regex_101/blob/master/example/07_excluding_specific_characters.py) |

## Repetitions

## Grouping and Capturing

## Backreferences

## Assertions

## Applications

---

made with 💙 by [mafda](https://mafda.github.io/)
