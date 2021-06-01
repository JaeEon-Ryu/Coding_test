'''
Given an m x n binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.
'''

'''
dp 사용
'''
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:

        largest_square = 0
        m, n = len(matrix), len(matrix[0])
        dp = [
            [0 for i in range(n + 1)]
            for j in range(m + 1)
        ]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if matrix[i - 1][j - 1] == "1":
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                    largest_square = max(largest_square, dp[i][j])

        return largest_square ** 2
