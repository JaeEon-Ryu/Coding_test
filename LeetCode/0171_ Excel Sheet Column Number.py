'''
Given a string columnTitle that represents the column title as appear in an Excel sheet, return its corresponding column number.
'''

'''
A -> 1 ( 1 )
AA -> 27 ( 1 + 26 )
AAA -> 703 ( 1 + 26 + 676 )

자리가 늘어날 때마다 26의n승으로 늘어남을 알 수 있음
따라서 A~Z에 해당하는 숫자에 26의 n승을 곱해주면 된다
'''

class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        result = 0
        for idx, title in enumerate(columnTitle[::-1]):
            result += (ord(title) - 64) * (26 ** idx)

        return result