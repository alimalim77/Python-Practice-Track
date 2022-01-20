'''
Given two strings containing digits, alphabets and special characters.
Generate a digit code by extracting the digits from the strings such that the digit code has a digit from the 
first string followed by the digit from the second string.

Input format:
Two lines having one string each.

Output format:
Integer in a single line.

Sample input:
a0b1$c3d4x8
b2c9*t7

Sample output:
2193748
'''
mystr1 = input()
mystr2 = input()


lione = list()
litwo = list()

for i in range(len(mystr1)):
    if mystr1[i].isdigit() and mystr1[i] != 0:
        lione.append(int(mystr1[i]))

for i in range(len(mystr2)):
    if mystr2[i].isdigit() and mystr2[i] != 0:
        litwo.append(int(mystr2[i]))

lithree = list()
ctr = 0
for i in range(len(lione)+len(litwo)):
    
    if not lione:
        while litwo:
            lithree.append(litwo.pop(0))
        break

    if not litwo:
        while lione:
            lithree.append(lione.pop(0))
        break
    
    if ctr%2 == 0 and lione:
        lithree.append(lione.pop(0))
    
    if ctr%2 != 0 and litwo:
        lithree.append(litwo.pop(0))
    ctr += 1


retstr = ""
for i in lithree:
    retstr = retstr + str(i)
print(int(retstr)

