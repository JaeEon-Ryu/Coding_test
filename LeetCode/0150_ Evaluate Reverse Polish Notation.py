'''
Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, and /. Each operand may be an integer or another expression.

Note that division between two integers should truncate toward zero.

It is guaranteed that the given RPN expression is always valid. That means the expression would always evaluate to a result, and there will not be any division by zero operation.
'''

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t in ['+', '-', '*', '/']:
                stack.append(self.calculator(int(stack.pop()), int(stack.pop()), t))
            else:
                stack.append(t)

        return stack[-1]

    def calculator(self, b: int, a: int, operator: str):
        if operator == '+':
            return a + b
        if operator == '-':
            return a - b
        if operator == '*':
            return a * b
        if operator == '/':
            return int(a / b)