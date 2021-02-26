class Solution:
    def longestValidParentheses(self, s: str) -> int:

        # reference solution
        stack = [0]
        longest = 0

        for p in s:  # parenthese in parentheses
            if p == "(":
                stack.append(0)
            else:
                if len(stack) > 1:
                    val = stack.pop()
                    stack[-1] += val + 2
                    longest = max(longest, stack[-1])
                else:
                    stack = [0]

        return longest


        ''' # Solution_  Brute-force _ Time Limit Exceeded
        if len(s) < 2:
            return 0
    
        def is_valid(parentheses):
            stack = []
    
            for p in parentheses:
                stack.append(p)
    
                if len(stack) > 1:
                    if stack[-2] == '(' and stack[-1] == ')':
                        del stack[-2],stack[-1]
    
            return True if len(stack) == 0 else False
    
        longest = 0
        for i in range(len(s)-1):
            for j in range(i+2,len(s)+1,2):
    
                if is_valid(s[i:j]):
                    longest = max(longest,j-i)
    
        return longest
        '''
