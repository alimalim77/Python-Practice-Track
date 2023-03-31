# def fun():
#     n = 6
#     for i in range(n):
#         for j in range(n):
#             #or ((i==6//2) and ((1)<j<3))
#             if (((0<i<n-1)  and (j==0))) or (((i==0 or i ==n-1) and (0<j<(n-1)))) or ((j==n-1) and (((n//2)<=i<n-1)) or (i==(n//2)) and ((n//2)<=j<n-1)):
#                 print("*",end="")
#             else:
#                 print(" ",end="")
#         print()
            

# fun()

# #Not Considering stars
from collections import defaultdict
def fun():
    g = defaultdict(list)
    g[1].append(3)
    print(g)
    n = 6
    for i in range(n):
        for j in range(n):
            #or ((i==6//2) and ((1)<j<3))
            if ( (0<i<n-1)  and (j==0) ) or ((i==0 or i ==n-1) and (0<j<=n//2)) or ( (j==n//2+1) and  (n//2<=i<n-1) )  or(i==n//2) and (n//2<=j<=n-1) :
                print("*",end="")
            else:
                print(" ",end="")
        print()
            

fun()

