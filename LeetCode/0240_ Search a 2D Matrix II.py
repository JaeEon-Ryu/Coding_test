'''
Write an efficient algorithm that searches for a target value in an m x n integer matrix. The matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.
'''

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        i, j = len(matrix) - 1, 0
        while (i >= 0 and i < len(matrix) and j >= 0 and j < len(matrix[0])):
            if (matrix[i][j] == target):
                return True

            if (matrix[i][j] > target):
                i -= 1
            if (matrix[i][j] < target):
                j += 1

        return False

        ''' 이 솔루션 속도가 더 빠름
        for row in matrix:
            if target in row:
                return True
        return False
        '''