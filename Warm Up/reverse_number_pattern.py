# 1
# 21
# 321
# 4321
#1 -> 1-0
#2 -> 2-0 = 2, 2-1 = 1

inp = int(input())
for i in range(1,inp+1):
    for j in range(0,i):
        print(i-j,end="")
    print("")


