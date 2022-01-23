'''
A string is made-up of many smaller substrings, where each substring has one continuous span of alphabets
followed by one continuous span of digits. The span of digits should be considered as one single number.
This number denotes the importance of the span of alphabets which preceded the number. 

You are given such a string. 
Form another string consisting of only the alphabet spans of the given string but rearranged in the
increasing order of their importance. 

Sample Input:
abc23gh12trpo29rtq2

Sample Output:
rtqghabctrpo

Explanation. The importance of rtq is 2, which is lowest and hence rtq should come first.
 The importance of gh is 12, which is second lowest and hence gh should come second. And so on.

'''
mystr = input()
listr = []
lidigit = []

i=0
while i < len(mystr):
    tempdigit = ""
    tempstr = ""
    while i < len(mystr) and mystr[i].isdigit():
        tempdigit  = tempdigit + str(mystr[i])
        i = i + 1
    while i < len(mystr) and mystr[i].isalpha():
        tempstr  = tempstr + mystr[i]
        i = i + 1
    if tempstr != "":
        listr.append(tempstr)
    if tempdigit != "":
        lidigit.append(tempdigit)

dicstore = dict()
for i in range(len(lidigit)):
    dicstore[listr[i]] = lidigit[i]
dic2 = {k: v for k, v in sorted(dicstore.items(), key=lambda item: int(item[1]))}
finstr  = ""
for i in dic2.keys():
    finstr = finstr + i
print(finstr)

    

