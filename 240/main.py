class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        N = len(matrix)
        if not N:
            return False
        M = len(matrix[0])
        i = N - 1
        j = 0
        while i >= 0:
            while j < M:
                if matrix[i][j] == target:
                    return True
                if matrix[i][j] < target:
                    j += 1
                elif matrix[i][j] > target:
                    i -= 1
        return False

Solution().searchMatrix([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]],20)