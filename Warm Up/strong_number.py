#145
#1! + 4! + 5!
# 1 + 24 + 120 = 145
def factorial(num):
    finnum = 1
    for i in range(num,1,-1):
        print("Fin num is", finnum,i)
        finnum = finnum * i
    return finnum

inp = int (input())
num = inp

rem = 0 
li = []
while num > 0:
    rem = num % 10
    li.append(rem)
    num = num // 10
flist = []
print(li)
for i in li:
    flist.append(factorial(i))
print(sum(flist))
    