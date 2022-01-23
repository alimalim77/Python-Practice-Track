'''
Given a set of strings. Find the longest common prefix in all the strings.
 Assume that there is at least one string in the set. If no common prefix is found print -1.

Input format:
Multiple strings in a single line separated by space.

Output format:
Single line of string.

Sample input:
assistant assist assistance

Sample output:
assist

'''

def check(mystr,checkli):
    flag = 1
    for i in checkli:
        if mystr in i:
            flag = 0
        else:
            return -1
    if flag == 0:
        return mystr    
        
import string


initial = list(map(str,input().split()))
smstr = initial[0]
for i in initial:
    if len(i) < len(smstr):
        smstr = i

for i in range(len(smstr)):
    a = check(smstr[i:],initial)
    if a != -1:
        print(a)
        exit()
print(-1)