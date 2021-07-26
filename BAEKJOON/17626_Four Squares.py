import math

n = int(input())
dp = [0 for i in range(50001)]

dp[0] = 0
dp[1] = 1

for i in range(2, n+1):
    min_num = float('inf')
    for j in range(1,int(math.sqrt(i))+1):
        # n개일 때 i보다 작은 제곱수로 빼보고 그 때 남은 수의 최적 경우
        min_num = min(min_num,dp[i - j*j])
    dp[i] = min_num + 1

print(dp[n])