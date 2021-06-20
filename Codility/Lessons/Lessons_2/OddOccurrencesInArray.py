# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

from collections import defaultdict


def solution(A):
    # write your code in Python 3.6
    num_cnt = defaultdict(int)
    for num in A:
        num_cnt[num] += 1 # 숫자 개수 세기

    for n in num_cnt:
        if num_cnt[n] % 2 == 1: # 개수가 홀수인 것 뽑기
            return n

    return A[-1]
