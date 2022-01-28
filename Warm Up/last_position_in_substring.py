'''
Exercise 12: Find the last position of a given substring
Write a program to find the last position of a substring “Emma” in a given string.
Given:
str1 = "Emma is a data scientist who knows Python. Emma works at google."
Expected Output:
Last occurrence of Emma starts at index 43
'''

mystr = 'Emma is a data scientist who knows Python. Emma works at google.'
for i in mystr:
    if 'Emma' in mystr:
        print(mystr.rindex('Emma'))
        break





'''
Alternative Approach to print without restiction of upper or lowercase using basic logic
li = []
for i in range(len(mystr)):
    if (mystr[i] == 'E' or mystr[i] ==  'e') and (mystr[i+1] == 'm' or mystr[i+1] ==  'M') /and (mystr[i+2] == 'm' or mystr[i+2] ==  'M') and (mystr[i+3] == 'a' or mystr[i+3] ==  'A'):
        li.append(i)
print(li)
'''