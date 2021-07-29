n = int(input())

'''
n = 1 -> 1
n = 2 -> 2
n = 3 -> 3
n = 4 -> 5
n = 5 -> 8
'''

dp = [1,2]
for i in range(2,n):
    dp.append((dp[i-1] + dp[i-2])%10007)

print(dp[n-1])