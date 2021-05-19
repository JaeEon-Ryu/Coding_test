'''
Reverse bits of a given 32 bits unsigned integer.

Note:

Note that in some languages such as Java, there is no unsigned integer type. In this case, both input and output will be given as a signed integer type.
They should not affect your implementation, as the integer's internal binary representation is the same, whether it is signed or unsigned.
In Java, the compiler represents the signed integers using 2's complement notation.
Therefore, in Example 2 above, the input represents the signed integer -3 and the output represents the signed integer -1073741825.
Follow up:

If this function is called many times, how would you optimize it?
'''

class Solution:
    def reverseBits(self, n: int) -> int:
        n = str(bin(n))[2:]  # 10진수에서 정수로 바꾼 후 앞의 0b 부분 지우기
        n = '0' * (32 - len(n)) + n  # 32bit이므로 남은 부분을 0으로 메꾸기
        n = n[::-1]  # 뒤집기

        return (int(n, 2))  # 다시 정수형으로 반환
