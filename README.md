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
| -   | A hyphen (-) inside a character class specifies a range of characters where the left and right operands are the respective lower and upper bounds of the range. | [08_matching_character_ranges.py](https://github.com/mafda/regex_101/blob/master/example/08_matching_character_ranges.py) |

## Repetitions

| Regex | Description | Example |
| :---: | :---------- | :------ |
| {x} | The tool {x} will match exactly  repetitions of character/character class/groups. | [09_matching_x_repetitions.py](https://github.com/mafda/regex_101/blob/master/example/09_matching_x_repetitions.py) |
| {x,y} | The {x,y} tool will match between x and y (both inclusive) repetitions of character/character class/group. | [010_matching_xy_repetitions.py](https://github.com/mafda/regex_101/blob/master/example/010_matching_xy_repetitions.py) |
| * | The * tool will match zero or more repetitions of character/character class/group. | [011_matching_zero_or_more_repetitions.py](https://github.com/mafda/regex_101/blob/master/example/011_matching_zero_or_more_repetitions.py) |
| + | The + tool will match one or more repetitions of character/character class/group. | [012_matching_one_or_more_repetitions.py](https://github.com/mafda/regex_101/blob/master/example/012_matching_one_or_more_repetitions.py) |
| $ | The $ boundary matcher matches an occurrence of a character/character class/group at the end of a line. | [013_matching_ending_items.py](https://github.com/mafda/regex_101/blob/master/example/013_matching_ending_items.py) |

## Grouping and Capturing

| Regex | Description | Example |
| :---: | :---------- | :------ |
|   \b  | \b assert position at a word boundary. Three different positions qualify for word boundaries : Before the first character in the string, if the first character is a word character. Between two characters in the string, where one is a word character and the other is not a word character. After the last character in the string, if the last character is a word character. | [014_matching_word_boundaries.py](https://github.com/mafda/regex_101/blob/master/example/014_matching_word_boundaries.py) |
|   ()  | Parenthesis ( ) around a regular expression can group that part of regex together. This allows us to apply different quantifiers to that group. These parenthesis also create a numbered capturing. It stores the part of string matched by the part of regex inside parentheses. These numbered capturing can be used for backreferences. ( We shall learn about it later ) | [015_capturing_and_noncapturing_groups.py](https://github.com/mafda/regex_101/blob/master/example/015_capturing_and_noncapturing_groups.py) |

## Backreferences

## Assertions

## Applications

---

made with 💙 by [mafda](https://mafda.github.io/)
