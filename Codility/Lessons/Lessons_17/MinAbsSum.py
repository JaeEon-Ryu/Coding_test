'''
주어진 수들의 합이나 차의 절대값이 가장 작은 수 찾기
'''


# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    # ref : https://myeasyprogramming.com/lesson-17-dynamic-programming/

    if not A:
        return 0

    A = [abs(n) for n in A]  # A의 모든 값을 절대값으로
    max_val, sum_A = max(A), sum(A)

    cnt = [0 for _ in range(max_val + 1)]
    for n in A:
        cnt[n] += 1

    dp = [-1 for _ in range(sum_A + 1)]
    dp[0] = 0

    for j in range(1, max_val + 1):
        if cnt[j] > 0:
            for i in range(sum_A + 1):
                if dp[i] >= 0: # visited
                    dp[i] = cnt[j]
                elif i >= j and dp[i - j] >= 0:
                    dp[i] = dp[i - j] - 1

    # 가장 작은 수 찾기
    result = float('inf')
    for i in range(sum_A // 2 + 1):
        if dp[i] >= 0:
            result = min(result, sum_A - 2 * i)

    return result