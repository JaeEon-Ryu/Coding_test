'''
Given a string s representing a valid expression, implement a basic calculator to evaluate it, and return the result of the evaluation.

Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().
'''


class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        op = 0
        result = 0
        sign = 1

        for char in s:
            if char.isdigit():
                op = (op * 10) + int(char)
            elif char == '+':
                result += sign * op
                sign = 1
                op = 0
            elif char == '-':
                result += sign * op
                sign = -1
                op = 0
            elif char == '(':
                stack.append(result)
                stack.append(sign)
                sign = 1
                result = 0
            elif char == ')':
                result += sign * op
                result *= stack.pop()
                result += stack.pop()
                op = 0

        return result + sign * op