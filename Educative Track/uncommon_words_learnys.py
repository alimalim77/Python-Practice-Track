'''
Given three sentences as strings. The task is to print the count of all the words from the first sentence which do not appear in the other two sentences. 

Input Format:
Three sentences in three separate lines.

Output Format:
An integer in a single line.

Sample Input:
python for programming is best
learning from python for programming
python for programming

Sample Output: 
2
'''
onestr = input()
twostr = input()
threestr = input()

lione = list(map(str,onestr.split()))
litwo = list(map(str,twostr.split()))
lithree = list(map(str,threestr.split()))
ctr = 0

for i in lione:
    if i not in litwo:
        if i not in lithree:
            ctr += 1

print(ctr)