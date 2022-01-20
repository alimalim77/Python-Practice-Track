
mycode = input("Enter the string value")
num = int(input("Enter the number of digits"))

oddlist = []
evenlist = []

actuallist = list(map(int,mycode))

for i in range(len(actuallist)):
    if i%2 ==0 :
        evenlist.append(actuallist[i]**2)
    else:
        oddlist.append(actuallist[i])


sumodd,sumeven = 0,0
for i in oddlist:
    sumodd = sumodd + i
for i in evenlist:
    sumeven = sumeven + i
newstr =str(sumeven)+ str(sumodd)

if len(newstr) < num:
    print(-1)
else:
    a = newstr[-num:-1:1] + newstr[-1]
    print(a)