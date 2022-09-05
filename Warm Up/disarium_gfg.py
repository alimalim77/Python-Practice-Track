#Positional Iterative
# inp = 145
# n = len(str(inp))

# ans = 0
# for i in range(n,-1,-1):
#     cur = inp%10
#     inp = inp//10

#     ans += (cur**i)
# print(ans)


#Recursive solution
# def fun(inp):
#     if inp == 0:
#         return 0
#     print((inp%10 ** len(str(inp))))
#     return ((inp%10) ** len(str(inp))) + fun(inp//10)



# inp = int(input())
# print(fun(inp))

#Map solution
inp = input()

li = list(map(int,inp))

new = 0
for j in range(1,len(inp)+1):
    new += li[j-1]**j
print(new)

