'''
Given two strings s and t, return the number of distinct subsequences of s which equals t.

A string's subsequence is a new string formed from the original string by deleting some (can be none) of the characters without disturbing the remaining characters' relative positions. (i.e., "ACE" is a subsequence of "ABCDE" while "AEC" is not).

It is guaranteed the answer fits on a 32-bit signed integer.
'''
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = [0] * len(t) + [1]

        for i in range(len(s) - 1, -1, -1):
            for j in range(len(t)):
                if s[i] == t[j]:
                    dp[j] += dp[j + 1]

        return dp[0]