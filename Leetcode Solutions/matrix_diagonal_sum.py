class Solution(object):
    def diagonalSum(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        mid = len(mat)//2
        sum = 0
        
        
        for i in range(len(mat)):
            sum = sum + mat[i][i]
            sum = sum + mat[len(mat)-1-i][i]
            
        if len(mat) % 2 == 1:
            sum = sum - mat[mid][mid]
        return sum