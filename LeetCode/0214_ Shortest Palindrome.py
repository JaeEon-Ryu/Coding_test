class Solution:
    def shortestPalindrome(self, s: str) -> str:
        '''
        reference : StefanPochmann
        '''
        reversed_s = s[::-1]

        for i in range(len(s) + 1):
            if s.startswith(reversed_s[i:]):
                return reversed_s[:i] + s


