'''
Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.
'''

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        self.wordDict = wordDict
        self.is_solved = False
        self.visited = set()
        self.dfs(s)

        return self.is_solved

    def dfs(self, s: str): # Depth first search
        if self.is_solved:
            return

        if not s:
            self.is_solved = True

        for word in self.wordDict:
            if s.startswith(word):
                erased_s = s[len(word):] # 단어 하나 지우기

                if erased_s not in self.visited: # 이미 했던 계산이 아닌지 검사
                    self.visited.add(erased_s)
                    self.dfs(erased_s)


