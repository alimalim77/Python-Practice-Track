# Python Program to Print Negative Numbers in a Range:
# Loop + enumerate function
# 2.  lambda
# 3. list comprehension


#Part 1
# a,b = -3,5
# li = list(map(int,range(a,b)))

# for i,j in enumerate(li):
#     if j < 0:
#         print(j,end=" ")


#Part 2
# a,b = -3,5
# li = list(map(int,range(a,b)))
# ans = list(filter(lambda x: x<0,li))
# print(ans)

#Part 3
a,b  =-3,5
print([i for i in range(a,b+1) if i < 0])
