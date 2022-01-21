'''
Given two space separated strings S1 and S2. 
You need to find out the minimum number of string rotations for the given string S1 to obtain S2.
 If string S1 and S2 are not convertible, print -1. Ignore the case of the characters while comparing the strings.

Input Format:
Space separated strings s1 and s2.

Output Format:
An integer number.

Sample Input: programPython Pythonprogram
Sample Output: 6

'''

from turtle import right


def rightrotate(mystr1):
        return mystr1[len(mystr1)-1:] + mystr1[:len(mystr1)-1]

def leftrotate(mystr1):
        return mystr1[1:] + mystr1[:1]

mystr1,mystr2 = map(str,input().split())

rctr=0
rightstr = mystr1
leftstr = mystr1
for i in range(len(rightstr)):
    rightstr = rightrotate(rightstr)
    rctr += 1
    if rightstr == mystr2:
        break

lctr=0
for i in range(len(leftstr)):
    leftstr = rightrotate(leftstr)
    lctr += 1
    if leftstr == mystr2:
        break

if leftstr != mystr2 or rightstr != mystr2:
    print(-1)
else:
    print(max(lctr,rctr))


