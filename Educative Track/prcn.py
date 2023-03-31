n = 6
alpha = 65
for i in range(n):
    count = 1
    
    for j in range(n):
        if j >= (n-i):
            if i % 2 == 0:
                print(count,end="")
                count += 1
            else:
                print(chr(alpha),end="") 
                alpha += 1
            
        else:
            print(" ",end="")
    print()