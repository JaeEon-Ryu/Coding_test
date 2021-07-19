# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

'''
지나간 요소의 합을 최대값으로
'''

def solution(A):
    # write your code in Python 3.6
    result = [A[0] for i in range(len(A) + 6)] # 주사위 범위

    for i in range(1, len(A)):
        result[i + 6] = max(result[i:i + 6]) + A[i] # 최대값만을 취하여 이동

    return result[-1]