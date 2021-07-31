'''
1 -> 1
2 -> 3
3 -> 5
4 -> 11
5 -> 21
'''

n = int(input())
dp = [0,1,3]

for i in range(3,n+1):
    val = (dp[i-2]*2 + dp[i-1]) % 10007
    dp.append(val)

print(dp[n])
