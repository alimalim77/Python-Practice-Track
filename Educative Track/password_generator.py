'''
Given a set of strings, where each string is in the following format. employee_name:employee_number. 
Each string is separated by a comma and a space. 

For each string, find the largest digit in the employee_number,
which is less than or equal to the length of the corresponding employee_name. 
If such a digit is present (M), concatenate the character present at the Mth  position in the employee_name 
to the output. If no such digit exists, concatenate the character X to the output.

It should be noted that position starts from 1. 

Input format: 
Single line of input consisting of one or more strings in the format specified as above.

Output format:
Single line consisting of a single string.

Sample input:
Robert:36787, Tina:68721, Jo:56389

Sample output:
tiX

Explanation: 
Length of Robert is 6 and 6 is present in the employee_number of Robert (36787). 
Alphabet at the 6th position (t) is appended. Length of Tina is 4 and 4 is not present in 68721.
4 is not present in the employee_code of Tina. But the largest digit which is less than or equal to 4 is 2. 
The 2nd character in Tina is i. Length of Jo is 2. 2 is not present in the employee_code of Jo, 
neither a digit which is less than or equal to 2 is present in the employee_code of 2. 
Hence X is appended to the output.

'''
def checklen(l, mystr,actstring):
    numlist = []
    for i in mystr:
        if int(i) <= len(actstring):
            numlist.append(int(i))
    if numlist:
        a = max(numlist)
        return actstring[a-1]
    else:
        return 'X'
    

contup = list(map(str,input().split()))
namelist = []
for i in contup:
    if i[-1] == ",":
        namelist.append(i[:len(i)-1])
    else:
        namelist.append(i)

newlist = []
for i in namelist:
    newlist.append(tuple(map(str,i.split(":"))))

result = ""

for i in newlist:
    l = len(i[0])
    ret = checklen(l,i[1],i[0])
    if ret == 'X':
        result += ret
    else:
        result += ret
print(result)