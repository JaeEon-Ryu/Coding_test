# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

from collections import defaultdict

def solution(A):
    # write your code in Python 3.6
    N = len(A)
    element = defaultdict(int)

    for a in A:
        element[a] += 1

    mapper = defaultdict(int)
    for curr in set(A): # 중복을 피하기위해 set 사용
        cnt = 0
        for k in range(1, int(curr ** 0.5) + 1): # 에라토스네네스의 체
            if curr % k == 0:
                cnt += element[k]
                if k != curr // k:
                    cnt += element[curr // k]

        mapper[curr] = N - cnt

    result = []
    for a in A: # mapper를 사용하여 중복된 결과도 적용
        result.append(mapper[a])

    return result