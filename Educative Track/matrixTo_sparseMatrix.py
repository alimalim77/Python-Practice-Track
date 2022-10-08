
def fun(m,n):
    mat = [[0 for _ in range(m)] for _ in range(n)]
    mat[1][1] = 6
    mat[0][2] = 35
    mat[3][3] = 42
    mat[2][1] = 4 
    
    sparse = []
    for i in range(n):
        for j in range(m):
            if mat[i][j] != 0:
                sparse.append([i,j,mat[i][j]])
    return sparse








m,n = map(int,input().split())
print(fun(m,n))