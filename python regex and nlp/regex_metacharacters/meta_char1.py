import re
txt = "The rain in Spain"
pattern = "^The.*Spain$"
# print(re.search(pattern,txt))
'''
the ^ implies - Start with 
the dot (.) - any character within exept the newline 
the asteric( * ) - zero or more occurances
the Dollar($) - ends with this 

Practice Text for Regex Metacharacters

^ (Start With):

Examples:
Regex: ^Apple — Matches lines that start with "Apple".
Practice Text:
Apple pie is delicious.
Pineapple is sweet.
Apples grow on trees.
. (Dot - Any Character Except Newline):

Examples:
Regex: c.t — Matches any three-letter word where the first and last letters are 'c' and 't', respectively.
Practice Text:
The cat is on the mat.
Cut the paper carefully.
Coat the surface with paint.
* (Asterisk - Zero or More Occurrences):

Examples:
Regex: go*d — Matches "gd", "god", "good", "goood", etc.
Practice Text:
He is a good boy.
They have gone to the market.
Go directly to the station.
$ (Ends With):

Examples:
Regex: end$ — Matches lines that end with "end".
Practice Text:
This is the end.
Let's pretend it never happened.
The weekend is near the end.
'''
practise_text1 = '''
Practice Text:
Apple pie is delicious.
Pineapple is sweet.
Apples grow on trees.
'''
practise_text2 = '''
Practice Text:
The cat is on the mat.
Cut the paper carefully.
Coat the surface with paint.
'''
# Quiz generate a regex formular to capture words that start with Apple
formular1 = r"^Apple."
print(re.findall(formular1,practise_text1,re.MULTILINE)) 

# Quiz generate a regex formular to capture words that start with c and ends with t a three letter word 
formular2 = r"c.t" 
print(re.findall(formular2,practise_text2.lower(),re.MULTILINE))

# Quiz generate a regex formular to capture words that start with Apple
practise_text3 = '''
Practice Text:
He is a good boy.
They have gone to the market.
Go directly to the station.
'''
formular3 = r"go*.."
print(re.findall(formular3,practise_text3.lower(),re.MULTILINE))

practise_text4 = '''
Practice Text:
He is a good boy.
They have gone to the market.
Go directly to the station.
$ (Ends With):
'''
formular4 = r"boy.$"
print(re.findall(formular4,practise_text4.lower(),re.MULTILINE))