'''
Given a string s and a dictionary of strings wordDict, add spaces in s to construct a sentence where each word is a valid dictionary word.
Return all such possible sentences in any order.

Note that the same word in the dictionary may be reused multiple times in the segmentation.
'''

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        self.wordDict = wordDict
        self.output = []
        self.dfs(s, [])
        return self.output

    def dfs(self, s: str, sub_answer: List[str]):
        if not s: # 문장 s를 모두 읽었을 경우 -> 정답
            self.output.append(' '.join(sub_answer))

        for word in self.wordDict:
            if s.startswith(word):
                erased_s = s[len(word):]
                self.dfs(erased_s, sub_answer + [word])

