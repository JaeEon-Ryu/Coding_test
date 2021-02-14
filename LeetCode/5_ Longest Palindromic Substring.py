class Solution:
    def longestPalindrome(self, s: str) -> str:

        len_s = len(s)
        longest_p = ""

        def helper(i, j): # from inside to outside
            while i >= 0 and j < len_s and s[i] == s[j]:
                i, j = i - 1, j + 1
            return s[i + 1:j]

        for k in range(len_s):
            longest_p = max(helper(k, k), helper(k, k + 1), longest_p, key=len) # 홀수, 짝수 

        return longest_p

# DBabichev 참고