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

for i in mystr1:
    if i.isdigit():
        lione.append(i)

for i in mystr2:
    if i.isdigit():
        litwo.append(i)

print(lione)
print(litwo)
newone = list(map(int,lione))
newtwo = list(map(int,litwo))

lithree = list()
ctr = 0
ct1= 0
ct2 = 0
for i in range(len(newone)+len(newtwo)):
    
    if not newone:
        while newtwo:
            lithree.append(newtwo.pop(0))
        break

    if not newtwo:
        while newone:
            lithree.append(newone.pop(0))
        break
    
    if ctr%2 == 0 and newone:
        lithree.append(newone.pop(0))
    
    if ctr%2 != 0 and newtwo:
        lithree.append(newtwo.pop(0))

    
    ctr += 1

for i in lithree:
    if i == 0:
        lithree.remove(i)
retstr = ""
for i in lithree:
    retstr = retstr + str(i)
print(int(retstr))