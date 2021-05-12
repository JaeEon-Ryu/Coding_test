'''
Given an integer columnNumber, return its corresponding column title as it appears in an Excel sheet.

For example:

A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28
AZ -> 52
..
BA -> 53
BZ -> 78
..

'''


class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = ''

        while columnNumber > 0:
            columnNumber -= 1
            result += chr(columnNumber % 26 + ord('A'))
            columnNumber //= 26

        return result[::-1]