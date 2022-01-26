#sum of digits
myinp = int(input("Enter a number"))
sum = 0

while myinp != 0:
    rem = myinp % 10
    sum = sum + rem
    myinp = myinp//10
print(sum)
