# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, K):
    # write your code in Python 3.6
    if not A:
        return A

    K %= len(A)
    idx = len(A) - 1

    A = A[idx - K + 1:] + A[:idx - K + 1]

    return A
