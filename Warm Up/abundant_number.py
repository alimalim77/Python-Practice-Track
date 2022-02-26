inp = int(input("Enter the number"))

factorlist = list()
for i in range(1,inp):
    if inp % i == 0:
        factorlist.append(i)
summation = sum(factorlist)

if summation > inp:
    print("abundant number")
else:
    print('not abundant')