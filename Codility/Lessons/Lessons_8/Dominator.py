# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
from collections import defaultdict


def solution(A):
    # write your code in Python 3.6
    num_cnt = defaultdict(int)
    half_of_A = len(A) // 2

    for idx, n in enumerate(A):
        if num_cnt[n] == half_of_A:
            return idx
        num_cnt[n] += 1

    return -1
