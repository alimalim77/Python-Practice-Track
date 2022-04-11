"""
size is n units
"""
import math
n = int(input(""))
number = 0
for i in range(2,10):
    if n % i == 0:
        number = i
        break
ctr = 0
val =number
while number != n:
    number = number*val
    ctr += 1
print(math.ceil(ctr/2))


