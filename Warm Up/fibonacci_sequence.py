n = int(input("Enter a number"))
a,b = 0,1
temp = 0
print(a,b,sep=" ",end=" ")
while n > 2:
    temp = b
    b = a + b
    a = temp
    print(b,end=" ")
    n -= 1