'''
Given an integer n, return the number of trailing zeroes in n!.

Follow up: Could you write a solution that works in logarithmic time complexity?
'''

class Solution:
    def trailingZeroes(self, n: int) -> int:
        if n < 1:
            return 0

        n = self.factorial(n)
        cnt_trailing_zero = 0

        for num in str(n)[::-1]:
            if num == '0':
                cnt_trailing_zero += 1
            else:
                break

        return cnt_trailing_zero

    def factorial(self, num: int):
        if num < 1:
            return 0
        result = 1

        while num > 0:
            result *= num
            num -= 1

        return result
