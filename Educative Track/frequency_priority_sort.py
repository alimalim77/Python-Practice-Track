'''
There are 5 types of tasks (represented by the alphabets, A, B, C, D and E). You are given a string representing a job consisting of some combination of these tasks. You are also given priorities of these tasks (represented by integers). Rearrange the given string according to the priority of the task (highest should come first), followed by frequency of the task (lowest should come first), followed by the dictionary order. 

Input format:
Two lines of input. The first line will have a string consisting of some combination of A, B, C, 
D and E. The second line will have 5 space separated integers. Note: Smaller the number, higher is its priority.

Output format:
Single line of output consisting of some combination of A, B, C, D and E.

Sample input:
ABCDBCDE
1 1 2 2 3

Sample output :
ABBCCDDE

'''


strinput = input()
numinput = input().split()
priority = ['A','B','C','D','E']
dicstore = dict()
for i in range(len(priority)):
    dicstore[priority[i]] = numinput[i]

freqdict = dict()
for i in strinput:
    if i not in freqdict:
        freqdict[i] = 1
    else:
        freqdict[i] += 1
freqdict = dict(sorted(freqdict.items(), key = lambda x: (x[1], x[0])))

finalstr = ""
for i in dicstore.keys():
    if i in freqdict.keys():
        finalstr += i * freqdict.get(i)
print(finalstr)