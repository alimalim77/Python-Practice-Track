#n!/(n-r)!
#n is students
#r is seats
def fact(n):
    total = 1
    for i in range(1,n+1):
        total *= i
    return total 



n = int(input("Enter the student number"))
r = int(input("Enter the seats"))
perm = fact(n)/fact(n-r)
print(perm)

