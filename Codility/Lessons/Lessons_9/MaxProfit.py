# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
# 제일 가격이 낮을 때 사서, 높을 때 파는 

def solution(A):
    # write your code in Python 3.6
    if not A:
        return 0

    min_val, result = A[0], 0
    for n in A[1:]:
        if min_val < n:
            result = max(result, n - min_val)
        else:
            min_val = n

    return result