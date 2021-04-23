'''
You are given an array prices where prices[i] is the price of a given stock on the ith day.

Find the maximum profit you can achieve. You may complete at most two transactions.

Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).
'''

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        import copy
        '''
        reference : DBabichev
        '''

        if len(prices) <= 1:
            return 0

        n = len(prices)
        profits = [
            prices[i + 1] - prices[i]
            for i in range(len(prices) - 1)
        ]
        if 4 > n:
            return sum(_ for _ in profits if _ > 0)

        dp = [
            [0, 0, 0]
            for _ in range(n - 1)
        ]
        mp = copy.deepcopy(dp)

        dp[0][1], mp[0][1] = profits[0], profits[0]

        for i in range(1, n - 1):
            for j in range(1, 3):
                dp[i][j] = max(mp[i - 1][j - 1], dp[i - 1][j]) + profits[i]
                mp[i][j] = max(dp[i][j], mp[i - 1][j])

        return max(mp[-1])