#156 
# 1 + 5 + 6 = 12 .. We know 156/12 = 13

inp = int(input("Enter the number"))

num = inp
summation = 0 
while num != 0:
    rem = num % 10
    num = num // 10
    summation += rem

if inp % summation == 0:
    print('Harshad Number')
else:
    print('NULL')
