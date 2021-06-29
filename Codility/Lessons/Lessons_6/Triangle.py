# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    len_A = len(A)
    if len_A < 3:
        return 0

    A.sort()
    for i in range(len_A - 2):
        if A[i] + A[i + 1] > A[i + 2]:
            return 1

    return 0
