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

def rotate(mystr1):
        return mystr1[len(mystr1)-1:] + mystr1[:len(mystr1)-1]

mystr1,mystr2 = map(str,input().split())

ctr=0
for i in range(len(mystr1)):
    mystr1 = rotate(mystr1)
    ctr += 1
    if mystr1 == mystr2:
        break

if mystr1==mystr2:
    print(ctr)
else:
    print(-1)


