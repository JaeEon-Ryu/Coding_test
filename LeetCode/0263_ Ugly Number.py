'''
An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.

Given an integer n, return true if n is an ugly number.
'''


class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False

        while n > 1:
            for num in (5, 3, 2):
                quotient, remainder = divmod(n, num)  # 몫, 나머지
                if remainder == 0:
                    n = quotient
                    break
            else: # for - else 구문 활용 ( break이 걸리지 않으면 False )
                return False

        return True