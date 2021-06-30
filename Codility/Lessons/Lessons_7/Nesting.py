# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S):
    # write your code in Python 3.6
    if len(S) % 2 == 1:
        return 0

    stack = []
    for b in S:  # bracket
        if b == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(b)
        else:
            stack.append(b)

    return 1 if not stack else 0
