class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        # convert from idx to parentheses
        def idx_to_parentheses(idxs):
            p = []
            for idx in idxs:
                if idx == 0:
                    p.append('(')
                else:
                    p.append(')')

            return p

        # check that the well-formed parentheses
        def isValid(s):
            stack = []

            mapping = {")": "("}
            for char in s:
                if char in mapping:
                    top_element = stack.pop() if stack else '#'

                    if mapping[char] != top_element:
                        return False
                else:
                    stack.append(char)

            return not stack

        possible_idx = []
        result = []

        # make index order
        def make_idx(cnt):
            if cnt == n * 2:  # make index complete
                parentheses = idx_to_parentheses(possible_idx)  # index to parentheses

                if isValid(parentheses):
                    result.append(''.join(parentheses))
                return

            for i in range(0, 2):
                possible_idx.append(i)
                make_idx(cnt + 1)
                possible_idx.pop()

        make_idx(0)

        return result




'''
LeetCode's solution - brute force

class Solution(object):
    def generateParenthesis(self, n):
        def generate(A = []):
            if len(A) == 2*n:
                if valid(A):
                    ans.append("".join(A))
            else:
                A.append('(')
                generate(A)
                A.pop()
                A.append(')')
                generate(A)
                A.pop()

        def valid(A):
            bal = 0
            for c in A:
                if c == '(': bal += 1
                else: bal -= 1
                if bal < 0: return False
            return bal == 0

        ans = []
        generate()
        return ans

'''

'''
LeetCode's solution - backtracking

class Solution(object):
    def generateParenthesis(self, N):
        ans = []
        def backtrack(S = '', left = 0, right = 0):
            if len(S) == 2 * N:
                ans.append(S)
                return
            if left < N:
                backtrack(S+'(', left+1, right)
            if right < left:
                backtrack(S+')', left, right+1)

        backtrack()
        return ans

'''


'''
StefanPochmann's solution

def generateParenthesis(self, n):
    def generate(p, left, right, parens=[]):
        if left:         generate(p + '(', left-1, right)
        if right > left: generate(p + ')', left, right-1)
        if not right:    parens += p,
        return parens
    return generate('', n, n)

'''



