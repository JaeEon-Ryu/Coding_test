'''
Given an integer n, return true if it is a power of two. Otherwise, return false.

An integer n is a power of two, if there exists an integer x such that n == 2x.
'''

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        power = 1

        if n > 0:
            while power < n:
                power *= 2
        else:
            return False

        return True if power == n else False
