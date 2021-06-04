'''
Given a string s which represents an expression, evaluate this expression and return its value.

The integer division should truncate toward zero.

Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().
'''

class Solution:
    def calculate(self, s: str) -> int:
        op = 0
        sign = '+'
        stack = []

        for char in s + '+':
            if char.isdigit():
                op = op * 10 + int(char)
            elif char in '+-*/':
                if sign == '+':
                    stack.append(op)
                elif sign == '-':
                    stack.append(-op)
                elif sign == '*':
                    stack.append(stack.pop() * op)
                elif sign == '/':
                    temp = stack.pop()
                    stack.append(math.trunc(temp / op))
                sign = char
                op = 0

        return sum(stack)