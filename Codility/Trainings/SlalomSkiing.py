# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
from bisect import bisect_left


def solution(A):
    # write your code in Python 3.6
    max_A = max(A)
    case = []
    for n in A:
        case += [2 * max_A + n, 2 * max_A - n, n]

    dp = []
    for c in case:
        idx = bisect_left(dp, c)
        if idx == len(dp):
            dp.append(c)
        else:
            dp[idx] = c

    return len(dp)