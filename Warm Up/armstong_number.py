#check armstrong number
inp = int(input("Enter a number"))
first = inp
sum=0
rem=0

while inp!= 0:
    rem = inp % 10
    inp = inp//10
    sum = sum + rem**3

if sum == first:
    print("Armstrong Number")