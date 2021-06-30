# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(H):
    # write your code in Python 3.6
    # 현재 높이가 기존 높이보다 높다면 스택 남기기 + 추가
    # 현재 높이가 기존 높이보다 낮다면 스택 없애기 + 추가
    stack, result = [], 0

    for b in H:  # block

        while stack:
            if stack[-1] > b:
                stack.pop()
            else:
                break

        if not stack or stack[-1] < b:
            result += 1
            stack.append(b)

    return result
