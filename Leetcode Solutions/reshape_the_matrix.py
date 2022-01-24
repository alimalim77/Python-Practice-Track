class Solution(object):
    def matrixReshape(self, mat, r, c):
        """
        Problem No. 566
        :type mat: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        
        a = 0 
        for i in mat:
            a  = a + len(i)

        if a != r * c:
            return mat
            
        ans = [[]]
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                k = mat[i][j]
                if len(ans[-1]) < c:
                    ans[-1].append(k)
                else:
                    newm = []
                    newm.append(k)
                    ans.append(newm)
        return ans