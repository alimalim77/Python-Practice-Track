inp1 = int(input("Enter the first number"))
inp2 = int(input("Enter the second number"))

li1 = list()
li2 = list()
for i in range(1,inp1):
    if inp1 % i == 0:
        li1.append(i)
for i in range(1,inp2):
    if inp2 % i == 0:
        li2.append(i)
out1 = sum(li1)/inp1
out2 = sum(li2)/inp2

if out1 == out2:
    print('Friendly Pair')
else:
    print("Undesired result")