class Solution(object):
    def transpose(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        newmatrix =[]
        for i in range(len(matrix[0])):
            submat = []
            for j in range(len(matrix)):
                submat.append(matrix[j][i])
            newmatrix.append(submat)
        return newmatrix