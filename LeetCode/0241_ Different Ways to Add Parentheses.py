'''
Given a string expression of numbers and operators,
return all possible results from computing all the different possible ways to group numbers and operators.

You may return the answer in any order.
'''

class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        # reference : StarInTheNight, O_Leet_Code

        if expression.isdigit():
            return [int(expression)]

        result = []
        for idx, char in enumerate(expression):
            if char in "+-*":
                left = self.diffWaysToCompute(expression[:idx])
                right = self.diffWaysToCompute(expression[idx + 1:])

                for l in left:
                    for r in right:
                        result.append(self.compute(l, r, char))

        return result

    def compute(self, n1, n2, op):
        if op == '+':
            return n1 + n2
        elif op == '-':
            return n1 - n2
        else:
            return n1 * n2