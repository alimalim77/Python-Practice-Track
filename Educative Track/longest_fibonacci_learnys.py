'''
Given space separated numbers as input. 
Print the longest fibonacci sequence that is present in the input. If no such sequence is present print -1.
 A fibonacci sequence is defined as numbers which follow the property given below:

fib[i] = fib[i - 1] + fib[i - 2], for all i > 1
fib[0] = 0 and fib[1] = 1, for 0 <= i <= 1

The fibonacci numbers may not be a contiguous subset of the given sequence.

Input format:
Space separated numbers.

Output format:
Space separated numbers.

Sample input:
0 1 2 2 1 2 3 8 5 4 5 6 7 8 9 8

Sample output:
0 1 1 2 3 5 8
'''

inp = list(map(int,input().split()))
thresold = max(inp)

fib1 = 0
fib2 = 1
li = [fib1,fib2]
while fib2 < thresold:
    fib1 = fib2
    li.append(fib1)
    fib2 = fib1 + fib2

if not li:
    print(-1)
for i in li:
    print(i,end = " ")
