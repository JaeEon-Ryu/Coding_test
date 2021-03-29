'''
We can scramble a string s to get a string t using the following algorithm:

1. If the length of the string is 1, stop.
2. If the length of the string is > 1, do the following:

    Split the string into two non-empty substrings at a random index, i.e.,
    if the string is s, divide it to x and y where s = x + y.

    Randomly decide to swap the two substrings or to keep them in the same order.
    i.e., after this step, s may become s = x + y or s = y + x.

    Apply step 1 recursively on each of the two substrings x and y.

Given two strings s1 and s2 of the same length,
return true if s2 is a scrambled string of s1, otherwise, return false.
'''


class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        # reference : Jeffrey_2020

        memo = {} # 딕셔너리 형태로 저장
        def dfs(s1, s2):
            if (s1, s2) not in memo:
                if sorted(s1) != sorted(s2):
                    is_equal = False
                elif s1 == s2:
                    is_equal = True
                else: # 문자가 서로 다르지만 정렬하면 같은 경우
                    for i in range(1, len(s1)):
                        is_equal = (dfs(s1[:i], s2[:i]) and dfs(s1[i:], s2[i:])) \
                               or (dfs(s1[:i], s2[-i:]) and dfs(s1[i:], s2[:-i]))
                        if is_equal:
                            break
                memo[s1, s2] = is_equal # memoization
            return memo[s1, s2]

        return dfs(s1, s2)

