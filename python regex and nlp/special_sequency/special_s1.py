'''
A special sequence is a \ followed by one of the characters in the list below, and has a special meaning:
    \A - Returns a match if the specified characters are at the beginning of the string
    \b - Returns a match where the specified characters are at the beginning or at the end of a word
       (the "r" in the beginning is making sure that the string is being treated as a "raw string")
    \B - Returns a match where the specified characters are present, but NOT at the beginning (or at the end) of a word
       (the "r" in the beginning is making sure that the string is being treated as a "raw string")
Exercises:
1. Match the specified characters at the beginning of the string (\A):
Write a regex pattern to find sentences that start with a name beginning with the letter 'A'.

Hint: Use the \A metacharacter.

2. Match specified characters at the beginning or end of a word (\b):
Write a regex pattern to find words that start or end with the letter 'b'.

Hint: Use \b to identify word boundaries.

3. Match specified characters NOT at the beginning or end of a word (\B):
Write a regex pattern to find words containing the letter 'b' but not at the beginning or end.

Hint: Use \B to exclude word boundaries.
'''
import re

practise_text = '''
Alice bought apples, bananas, and apricots. Bob baked blueberry muffins.  
Carla carefully counted candies in the basket. David dropped a book by the door.  
Emily enjoys exploring caves and climbing rocks.  
'''
# Regex to match sentences starting with 'A'
formular1 = r"(?:^|(?<=\.\s))(A\w.*?)(?=(\.|$))"
matches = re.findall(formular1, practise_text,re.MULTILINE)
print(matches)


# quiz2 : Write a regex pattern to find words that start or end with the letter 'b'.
formular2 = r"(\bb.|b\b)"
print(re.findall(formular2,practise_text,re.MULTILINE))