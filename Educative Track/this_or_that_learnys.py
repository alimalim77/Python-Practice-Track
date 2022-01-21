'''
Given an alphanumeric string having alphabets, digits and some special characters.
 Extract the special characters from the string and print them if the sum of the digits is less than a number
  M otherwise print the alphabets in uppercase.

Input format:
First line will have a string and the second line will have the value of M.

Output format:
String in a single line.

Sample input:
n3*o3(bo7%g6h)a*1 
52

Sample output
*(%)*

'''
def checksum(numlist,m):
    sum = 0
    for i in numlist:
        sum = sum + int(i)
    if sum < m:
        return True
    else:
        return False


inp = input()
m = int(input())

lisp = list()
linum = list()
lialpha = list()

for i in inp:
    if not i.isalnum():
        lisp.append(i)
    if i.isdigit():
        linum.append(i)
    if i.isalpha():
        lialpha.append(i)
        
if checksum(linum,m):
    for i in lisp:
        print(i, end="")
else:
    for i in lialpha:
        
        print(i.capitalize(), end= "")
