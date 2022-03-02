#n!/(n-r)!
#n is students
#r is seats

def fact(n):
    val = 1
    for i in range(n,1,-1):
        val *=  i
    return val

ninput = int(input("enter the value of students"))
rinput = int(input("Enter the valuen of seats"))
ans = 0

ans = fact(ninput)//fact(ninput-rinput)
print(ans)



