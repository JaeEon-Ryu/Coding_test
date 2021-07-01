# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

from collections import defaultdict

def solution(A):
    # write your code in Python 3.6

    left, right = defaultdict(int), defaultdict(int)
    for n in A:
        right[n] += 1
    l_size, r_size = 0, len(A)
    leader,leader_cnt,result = 0, 0, 0

    for idx, n in enumerate(A):
        left[n] += 1
        right[n] -= 1
        l_size += 1
        r_size -= 1

        if left[n] > leader_cnt:
            leader = n
            leader_cnt = left[n]

        if leader_cnt > l_size//2 and right[leader] > r_size//2:
            result += 1

    return result