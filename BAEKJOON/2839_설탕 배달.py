n = int(input())

dp = [float('inf') for _ in range(n+1)]
dp[3] = 1

for i in range(5,n+1):
    dp[i] = min(dp[i], dp[i-3]+1, dp[i-5]+1)

if dp[i]!=float('inf'):
    print(dp[i])
else:
    print(-1)
