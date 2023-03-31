# def fun(arr,query):
#     for a,b in query:
#         temp = True
#         for i in range(a-1,b):
#             if temp:
#                 arr[i] += 1 
#             else:
#                 arr[i] -= 1 
#             temp = not temp
#             ans = arr[i]
#     return sum(arr)
        






# mod = 10000000007
# n = int(input())
# for i in range(n):
#     # Declare n and q
#     #Take array of n elements
#     # Take n number of queries
#     n,q = map(int,input().split())
#     arr = list(map(int,input().split()))
#     query = []
#     for i in range(q):
#         first,second = map(int,input().split())
#         for i in range(first-1,second):
#             if temp:
#                 arr[i] += 1 
#             else:
#                 arr[i] -= 1 
#             temp = not temp
            
#     print(sum(arr)%mod)

def fun(a,b):
    if b < a:
        return "NO"
    for i in range(10):

        #print( (b+i)% (a+i))
        if (b+i) % (a+i) == 0:
            return "YES"
    return "NO"



#for i in range(n):
a,b  = map(int,input().split())
print(fun(a,b))