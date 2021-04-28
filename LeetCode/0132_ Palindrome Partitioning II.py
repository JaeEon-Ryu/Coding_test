'''
Given a string s, partition s such that every substring of the partition is a palindrome.

Return the minimum cuts needed for a palindrome partitioning of s.
'''

'''
DP solution
'''
class Solution:
    def minCut(self, s: str) -> int:
        dp = [_ for _ in range(-1, len(s))]

        for i in range(len(s)):
            for j in range(i, len(s)):
                if s[i:j] == s[i:j][::-1]:
                    dp[j + 1] = min(dp[j + 1], dp[i] + 1)

        return dp[-1]
