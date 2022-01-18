#implementation of 2D array
row = int(input("Enter the number of rows"))
col = int(input("Enter the number of columns"))
matrix = [] 

for i in range(0,row):
    li = []
    for j in range(0,col):
        get = int(input("Enter the value"))
        li.append(get)
    matrix.append(li)

print(matrix[1][2])

 