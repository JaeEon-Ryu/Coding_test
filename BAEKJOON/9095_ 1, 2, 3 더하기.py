'''
n > 3 일때, f(n) = f(n-3) + f(n-2) + f(n-1)
'''

T = int(input())

def get_cnt(n):
    dp = [1, 2, 4]
    for i in range(3,n):
        dp.append(dp[i-3] + dp[i-2] + dp[i-1])

    return dp[n-1]

for _ in range(T):

    N = int(input())
    print(get_cnt(N))


