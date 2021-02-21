class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        max_len = 0
        if len(s) == 1:
            return 1

        for i in range(len(s)):
            temp = [s[i]]

            for j in range(i + 1, len(s)):

                if s[j] in temp:
                    max_len = max(max_len, len(temp))
                    break
                else:
                    temp.append(s[j])

            max_len = max(max_len, len(temp))

        return max_len