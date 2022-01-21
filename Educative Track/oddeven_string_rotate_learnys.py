'''
There are a number of space separated strings. 
Each string is in the form of the alphabet:digits.
 From each string, find the sum of squares of the digits.
  If the sum is even then rotate the alphabets of that string one place to right and print those alphabets 
  after rotation. If the sum is odd then rotate the alphabets two places to the left and print the alphabets 
  after rotation. If there is a negative value after the colon print -1 instead. 

Input format:
Space separated strings in a single line.

Output format:
Multiple lines of output, each line having a single string.

Sample input: 
hello:11 card:23

Sample output: 
ohell
rdca
'''
def check(n,a):
  sumcheck = 0
  for i in n:
    if i == '-':
      sumcheck = -sumcheck
      continue
    sumcheck = sumcheck + int(i) 
    
  if sumcheck < 0:
    return -1
  elif sumcheck % 2 == 0:
    return a[len(a)-1:] + a[:len(a)-1]
  elif sumcheck % 2 != 0:
    return a[2:] + a[:2]


li = list(map(str,input().split()))

tu = list()
num = []
alpha = []

for i in li:
    tu.append(tuple(map(str,i.split(":"))))
    
for i in tu:
    num.append(i[1])
    alpha.append(i[0])

for i in range(len(num)):
    print(check(num[i] , alpha[i]))


    