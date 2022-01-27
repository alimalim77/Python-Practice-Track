'''
Exercise 8: Find all occurrences of a substring in a given string by ignoring the case
Write a program to find all occurrences of “USA” in a given string ignoring the case.
Given:
str1 = "Welcome to USA. usa
awesome, isn't it?"
Expected Outcome:
The USA count is: 2

'''

mystr = input('Enter the string')
count = 0

for i in range(len(mystr)):
    if (mystr[i]=='U' or mystr[i]=='u') and (mystr[i+1]=='S' or mystr[i+1]=='s') and (mystr[i+2]=='A' or mystr[i+2]=='a'):
        count = count + 1

print(count)
