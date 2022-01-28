#check armstrong number
def armstrongfunction(inp):
    first = inp
    sum=0
    rem=0

    while inp!= 0:
        rem = inp % 10
        inp = inp//10
        sum = sum + rem**3

    if sum == first:
        result = str(sum) + "is Armstrong Number"
        return result
    else:
        return None


start, end = map(int,input("Enter the values").split())
for i in range(start,end+1):
    res = armstrongfunction(i)
    if res != None:
        print(res, ' is Armstrong Number', end ="\n")
