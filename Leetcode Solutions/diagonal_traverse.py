from typing import final


def findDiagonalOrder(mat):
        a = 0
        b = len(mat)
        x = 0
        y = len(mat[0])
        
        i = 0
        j = 0
        
        def check(i,j):
            if a <= i < b and x <= j < y:
                return True
            else:
                return False
        uhf = list()
        lhf = list()
        final = []
        for k in range(0, len(mat)):
            j = 0
            submat = []
            for l in range(len(mat[0])):
                if check(i,j):
                    submat.append(mat[i][j])
                i -= 1
                j += 1
            if k % 2 != 0:
                submat = submat[::-1]
            final.extend(submat)
            i = k+1
        org, fin = k,l
        twofinal = []
        print('val of k and l is', k ,l)
        j = len(mat[0])-1
        for k in range(len(mat)-1,0,-1):
            i = len(mat) - 1
            submat = []
            for l in range(len(mat[0])-1,0,-1):
                if check(i,j):
                    submat.append(mat[i][j])
                i -= 1
                j += 1
            if k % 2 == 0:
                submat = submat[::-1]
            twofinal.extend(submat)
            j = k-1
        twofinal = twofinal[::-1]
        final.extend(twofinal)
        print(final)
        

findDiagonalOrder([[1,2,3],[4,5,6],[7,8,9]])
findDiagonalOrder([[1,2],[3,4]])