'''
The gray code is a binary numeral system where two successive values differ in only one bit.

Given an integer n representing the total number of bits in the code, return any sequence of gray code.

A gray code sequence must begin with 0.
'''


class Solution:
    def grayCode(self, n: int) :
        res = [0]
        bit = 1

        for _ in range(n):
            layer = res[::-1]
            for i in layer:
                res.append(i + bit)

            bit *= 2

        return res
