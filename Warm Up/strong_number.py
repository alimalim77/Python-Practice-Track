#145
#1! + 4! + 5!
# 1 + 24 + 120 = 145

def factorial(inp):
    mynum = 1
    for i in range(1,inp+1):
        mynum = mynum * i
    return mynum

myinp = int(input("Enter a number"))
start = myinp
li = []
rem = 0
while myinp !=0:
    rem = myinp % 10
    myinp //= 10
    li.append(rem)
summation = 0
for i in li:
    summation += factorial(i)

if summation == start:
    print(True)
else:
    print(False)



