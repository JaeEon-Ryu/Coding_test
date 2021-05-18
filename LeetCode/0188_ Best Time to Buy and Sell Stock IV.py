'''
You are given an integer array prices where prices[i] is the price of a given stock on the ith day, and an integer k.

Find the maximum profit you can achieve. You may complete at most k transactions.

Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).
'''

class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:

        # reference : 101leetcode
        n = len(prices)
        max_profit = 0
        if k >= n / 2:
            for i in range(1, n):
                max_profit += max(prices[i] - prices[i - 1], 0)
            return max_profit

        dp = [
            [0 for j in range(n)]
            for i in range(k + 1)
        ]

        for i in range(1, k + 1):
            maxpr = -prices[0]
            for j in range(1, n):
                dp[i][j] = max(dp[i][j - 1], maxpr + prices[j])
                maxpr = max(maxpr, -prices[j] + dp[i - 1][j])

        return dp[-1][-1]