'''
Given an integer columnNumber, return its corresponding column title as it appears in an Excel sheet.

For example:

A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28 
...
 

Example 1:

Input: columnNumber = 1
Output: "A"
Example 2:

Input: columnNumber = 28
Output: "AB"
'''
def fun(num):
    newstr = ""
    while num <= 0:
        newstr = chr(ord('A') + (num-1)%26) + newstr
        print(newstr)
        num = num-1 // 26
    



fun(701))