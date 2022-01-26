#prime number in range
first, second = map(int, input().split())

for i in range(first, second+1):
    flag = 0
    for j in range(2,i):
        if i % j == 0:
            flag = 1
            break
    if flag == 0:
        print(i,"is prime")

    
