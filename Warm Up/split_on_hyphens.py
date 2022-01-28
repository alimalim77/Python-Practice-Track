'''
Exercise 13: Split a string on hyphens
Write a program to split a given string on hyphens and display each substring.
Given:
str1 = Emma-is-a-data-scientist
Expected Output:
Displaying each substring
 
Emma
is
a
data
scientist

'''
mystr = "Emma-is-a-data-scientist"

i = 0
substr = ""
li = list()
while i < len(mystr):
    if mystr[i] != '-':
        substr += mystr[i]
    else:
        li.append(substr)
        substr = ""
    i = i + 1
for i in li:
     print(i)

'''
Alternate/ Easier Method
li = list(map(str,mystr.split('-')))
for i in li:
    print(i)
'''