#to print the greatest of three numbers
a,b,c = map(int, input().split()) 
result = max(a,max(b,c))
print(result, " is greatest")



'''if a > b:
    if a > c:
        print(a," is greatest")
    else:
        print(c," is greatest")
else:
    if b > c:
        print(b," is greatest")
    else:
        print(c," is greatest")
'''



