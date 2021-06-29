# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, B):
    # write your code in Python 3.6
    stack, cnt = [], len(A)

    for size, direction in zip(A, B):
        if direction == 1:  # 내려갈 경우
            stack.append(size)
        else:
            while stack and stack[-1] < size:
                cnt -= 1
                stack.pop()
            if stack:
                cnt -= 1

    return cnt
