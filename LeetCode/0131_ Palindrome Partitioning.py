'''
Given a string s, partition s such that every substring of the partition is a palindrome.
Return all possible palindrome partitioning of s.

A palindrome string is a string that reads the same backward as forward.
'''

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        self.output = []
        self.dfs(s, [])

        return self.output

    def dfs(self, s, path):
        if not s:
            self.output.append(path)
            return
        for i in range(1, len(s) + 1):
            if s[:i] == s[:i][::-1]:
                self.dfs(s[i:], path + [s[:i]])
