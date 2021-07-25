T = int(input())

dp = [
    [0 for _ in range(31)]
    for _ in range(31)
]
for i in range(31):
    dp[i][0] = 1

for i in range(1,31):
    for j in range(1,31):
        dp[i][j] = dp[i-1][j] + dp[i-1][j-1]

for _ in range(T):
    n,m = map(int,input().split())
    print(dp[m][n])

