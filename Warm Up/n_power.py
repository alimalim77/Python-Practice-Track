# number to the power n
base = int(input("Enter the number"))
expo = int(input("Enter the exponential value"))

result=1
for i in range(expo,0,-1):
    result = result * base
print(result)



