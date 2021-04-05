'''
Given an integer n, return the number of structurally unique BST's (binary search trees)
which has exactly n nodes of unique values from 1 to n.
'''

'''
n==1 : 1 // 1 1
n==2 : 2 // 1 1 , 1 1
n==3 : 5 // 1 2 , 1 1, 2 1
n==4 : 14 // 1 5 , 1 2, 2 1, 5 1
'''

class Solution:
    def numTrees(self, n: int) -> int:

        dp = [0] * (n+1)
        dp[0] = 1

        for i in range(1, n+1):
            for j in range(i):
                dp[i] += dp[j] * dp[i- 1 - j]

        return dp[n]

sol = Solution().numTrees(5)
print(sol)
