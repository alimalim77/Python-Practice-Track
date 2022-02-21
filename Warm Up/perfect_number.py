# 8 - Divisors of 8 are 1,2,4
# 1+2+4 = 7  o. 8 != 7
# 6 - Divisors of 6 are 1,2,3
#1+2+3 = 6 . Yes, it is a perfect number


inp = int(input("Enter a number"))
initial = inp
summation = 0
for i in range(1,inp-1):
    if inp % i == 0:
        summation += i
if summation == initial:
    print("Number is perfect")
else:
    print("Number is not perfect")
