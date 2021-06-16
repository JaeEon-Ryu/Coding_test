'''
Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.
'''


class Solution:
    def addDigits(self, num: int) -> int:
        num = str(num)

        while len(num) > 1:
            num = str(sum(list(map(int, list(num)))))

        return int(num)