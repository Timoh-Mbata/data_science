'''
the square brackets [] is used to define a set of characters
the ? question_mark is used to define a zero or 1 occurence
the cali brackets {} is used to define the specific occurence
the	| Either or is used to define either or situation 
the () is used for capturing and grouping  
'''
import re
# quiz1 Find all vowels in the text.
practise_text1 = '''
My favorite color is blue.
Some prefer colour for spelling.
Colors or colours, both are correct.
'''
# quiz2 Match "color" and "colour".
practise_text2 = '''
My favorite color is blue.
Some prefer colour for spelling.
Colors or colours, both are correct.
'''
# quiz3 Extract exactly 3-digit numbers.
practise_text3 = '''
The area code is 123.
His phone number is 456-789-1234.
ID numbers: 456, 12, and 78910.
'''

# quiz4 Extract "blue car" and "red car" only.
practise_text4 = '''
He drives a blue car.
She owns a red car.
They are looking for a green car or yellow car.
'''

# quiz5 Find occurrences of either "cat" or "dog".
practise_text5 = '''
I own a cat.
My friend has a dog.
Some people prefer cats, others love dogs.
'''
fomular1 = r"[a,e,i,o,u]"
# print(re.findall(fomular1,practise_text1.lower()))

# formular2 = r"colou?r"
# print(re.findall(formular2,practise_text2.lower(),re.MULTILINE))

# formular3 = r"\d{3}"
# print(re.findall(formular3,practise_text3.lower(),re.MULTILINE))

formular4 = r"(blue|red) car"
print(re.findall(formular4,practise_text4.lower(),re.MULTILINE))


