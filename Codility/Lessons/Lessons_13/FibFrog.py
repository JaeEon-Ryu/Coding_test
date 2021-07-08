# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    fibo = [0, 1]
    A.append(1) # 반복문 마지막이 실행되기 위함
    N = len(A)

    while fibo[-1] < N: #
        fibo.append(fibo[-1] + fibo[-2])

    len_f = len(fibo)
    memo = [N + 1 for _ in range(N + 1)]
    memo[0] = 0

    for i in range(N):
        if A[i] == 1: # on the leaf
            for j in range(len_f):
                if fibo[j] <= i + 1:
                    memo[i + 1] = min(memo[i + 1], 1 + memo[i + 1 - fibo[j]]) # dp

    return memo[N] if memo[N] != N + 1 else -1

