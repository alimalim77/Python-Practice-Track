class Solution(object):
    def construct2DArray(self, original, m, n):
        """
        :type original: List[int]
        :type m: int
        :type n: int
        :rtype: List[List[int]]
        """
        if len(original) != m*n:
            return []
        
        matrix  = []
        for i in range(m):
            submat = []
            for j in range(n):
                submat.append(original.pop(0))
            matrix.append(submat)
        return matrix