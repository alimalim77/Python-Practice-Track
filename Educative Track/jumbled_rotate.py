
'''
You are given a set of strings consisting of digits, alphabets and special characters. 
From each string extract the digits, find their sum and square it. 
If the resultant number is odd, perform as many left rotations else perform as many right rotations.

Input format:
Multiple strings in a single line separated by space.

Output format:
For each string there should be one output string. All the strings should be in a single line separated by space.

Sample input:
Lo3us02 flo2at1er

Sample output:
ousL oaterfl

'''
def check(mystr):
    restr = 0
    rotstr = ""
    for i in mystr:
        if i.isdigit():
            restr = restr + int(i)
        else:
            rotstr = rotstr + i
    restr = restr**2
    rot = restr % len(rotstr) 
    return rotstr[rot:] + rotstr[:rot] 
final = []
inp = list(map(str,input().split()))
for i in inp:
    final.append(check(str(i)))
for i in final:
    print(i, end=" ")