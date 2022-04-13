def checker(mat,num):
    r = len(mat)
    c = len(mat[0])
    ctr = 0
    for i in [-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]:
        a =num[0] + i[0]
        b =num[1] + i[1]
        if (not 0<=a<r) or (not 0 <= b < c):
            continue
        if mat[a][b] == 1:
            ctr += 1
    return ctr


def gameOfLife(board):
        
    r = len(board)
    c = len(board[0])
    res = float("inf")
    newboard = [[board[row][col] for col in range(c)] for row in range(r)]
    for i in range(r):
        for j in range(c):
            res = checker(newboard,[i,j])
            if newboard[i][j] == 1 and res < 2:
                board[i][j]= 0
            elif newboard[i][j] == 1 and res > 3:
                board[i][j]=0
            elif newboard[i][j] == 0 and res == 3:
                board[i][j] = 1
    return board

print(gameOfLife([[0,1,0],[0,0,1],[1,1,1],[0,0,0]]))