# tusizi solution 참조

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:

        result = 0

        pos_dividend, pos_divisor = abs(dividend), abs(divisor)

        # 2의 지수승, 비트연산자를 이용
        while pos_dividend >= pos_divisor:
            temp, i = pos_divisor, 1
            while pos_dividend >= temp:
                pos_dividend -= temp
                result += i
                i <<= 1
                temp <<= 1

        if (dividend < 0 and divisor < 0) or (dividend > 0 and divisor > 0):
            return min(2147483647, result)
        else:
            return max(-2147483648, -result)


'''시간초과가 났던 코드
def divide(dividend = -2147483648, divisor = -1):
    result = 0
    multiple_divisor = 0

    pos_dividend, pos_divisor = abs(dividend), abs(divisor)

    while pos_dividend >= multiple_divisor + pos_divisor:
        result += 1
        multiple_divisor += pos_divisor
        print(multiple_divisor)

    if (dividend < 0 and divisor < 0) or (dividend > 0 and divisor > 0):
        return result
    else:
        return -result

print(divide())
'''
