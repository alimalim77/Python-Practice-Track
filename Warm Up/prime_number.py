#prime number
inp = int(input("Enter a number"))
flag=1
for i in range(2,inp):
    if inp%i == 0:
        print("Not a prime")
        flag=0
        break
    
if flag == 1:
    print("Number is prime")