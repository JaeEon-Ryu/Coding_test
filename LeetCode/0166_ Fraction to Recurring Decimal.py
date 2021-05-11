'''
Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.

If the fractional part is repeating, enclose the repeating part in parentheses.

If multiple answers are possible, return any of them.

It is guaranteed that the length of the answer string is less than 104 for all the given inputs.
'''


class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        # reference : tusizi
        n, remainder = divmod(abs(numerator), abs(denominator))  # 몫, 나머지
        sign = '-' if numerator * denominator < 0 else ''  # 음수 판별
        result = [sign + str(n), '.']
        stack = []

        while remainder not in stack:
            stack.append(remainder)
            n, remainder = divmod(remainder * 10, abs(denominator))
            result.append(str(n))

        idx = stack.index(remainder)
        result.insert(idx + 2, '(')
        result.append(')')

        return ''.join(result).replace('(0)', '').rstrip('.')