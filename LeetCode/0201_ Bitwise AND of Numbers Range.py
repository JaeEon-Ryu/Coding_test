'''
Given two integers left and right that represent the range [left, right], return the bitwise AND of all numbers in this range, inclusive.
'''
class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        # reference : dietpepsi
        i = 0
        while left != right:
            left >>= 1 # 시프트 후 결과 할당
            right >>= 1 # 시프트 후 결과 할당
            i += 1
        return right << i