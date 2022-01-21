'''
An alphanumeric string consists of alphabets and digits. 
You are given an alphanumeric string and a number M. 
Form numbers having M digits by picking digits from this string from left to right.
Find the largest of these numbers and rotate the remaining string (the original string with digits stripped off)  towards right by as many times. 
It is guaranteed that the number of digits in the given alphanumeric string will be multiples of M.

Input format:
Each input consists of an alphanumeric string and the value of M separated by space.

Output format:
String in a single line.

Sample Input:
abc23gh12trpo2912rtq 2

Sample Output:
portqabcghtr

'''
def rotation(rotnum,alphastr):
    return alphastr[len(alphastr)-rotnum:] + alphastr[:len(alphastr)-rotnum]



mystr , num = map(str,input().split())
num = int(num)
inilist = list()

for i in mystr:
    if i.isdigit():
        inilist.append(i)

numlist = []

j=0

stor = ''
while len(inilist) != 0:
    cont = ""
    while j < num:
        j = j+1
        if len(inilist) == 0:
            continue
        stor = inilist.pop(0)
        cont = cont + stor
        
    j = 0
    numlist.append(cont)

numlist = [int(x) for x in numlist]
maximum = max(numlist)
alphastr = ''
for i in mystr:
    if i.isalpha():
        alphastr = alphastr + i
rotnum = maximum % len(alphastr)
print(rotation(rotnum,alphastr))
