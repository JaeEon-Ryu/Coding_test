'''
Given a string s consists of some words separated by spaces,
return the length of the last word in the string. If the last word does not exist, return 0.

A word is a maximal substring consisting of non-space characters only.
'''


class Solution:
    def lengthOfLastWord(self, s: str) -> int:

        cnt = 0
        for sub_s in s[::-1]:
            if cnt == 0 and sub_s == " ":
                continue

            if sub_s == ' ':
                break
            else:
                cnt += 1

        return cnt