'''
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time.
The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

Now consider if some obstacles are added to the grids.
How many unique paths would there be?

An obstacle and space is marked as 1 and 0 respectively in the grid.
'''


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:

        dp = [
            [0 for _ in range(len(obstacleGrid[0]) + 1)]
            for _ in range(len(obstacleGrid) + 1)
        ]
        dp[0][1] = 1
        m, n = len(dp), len(dp[0])

        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i - 1][j - 1] == 1: # 장애물이 있으면 갈 수 없는 곳
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[-1][-1]