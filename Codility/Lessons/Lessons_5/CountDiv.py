# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, B, K):
    # write your code in Python 3.6
    return (B//K) - (A//K) + 1 if A%K == 0 else (B//K) - (A//K)
