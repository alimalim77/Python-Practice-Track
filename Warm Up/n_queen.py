# def check(n,li):
#     for i in range(n-1,-1,-1):
#         if li[i][i] == '1':
#             return False


# class chessBoard:
#     def __init__(self,n) -> None:
#         self.li = [['.' for _ in range(n)] for _ in range(n)]
#         self.len = n
#     def printBoard(self):
#         return self.li

#     def trav(self):
#         for i in range(self.len):
#             if check(n-1,self.li):

        
# cb = chessBoard(4)
# print(cb.printBoard())
# cb.trav()

def chessBoard(n):
    col, pos, neg = set(), set(), set()
    mat = [['.']* n for _ in range(n)]
    res = []
    def backtrack(r):
        if r == n:
            a = ["".join(row) for row in mat]
            res.append(a)
            return

        for c in range(n):
            if c in col or (r-c) in neg or (r+c) in pos:
                continue
            col.add(c)
            pos.add(r+c)
            neg.add(r-c)
            mat[r][c] = "Q"

            backtrack(r+1)
            
            col.remove(c)
            pos.remove(r+c)
            neg.remove(r-c)
            mat[r][c] = "."
            # return res

    backtrack(0)
    return res


print(chessBoard(4))