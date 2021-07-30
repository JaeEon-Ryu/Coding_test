'''
1번계단 -> 계단1
2번계단 -> 계단1 + 계단2
3번계단 -> 계단1+계단3  or  계단2+계단3
4번계단 -> 계단2+계단3 or 계단1+계단3+계단4
'''

n = int(input())
stairs = [0]
dp = []

for _ in range(n):
    stair = int(input())
    stairs.append(stair)

if n == 1:
    print(stairs[-1])
else:
    dp = [0,stairs[1], stairs[1] + stairs[2]]

    for i in range(3, n + 1):
        val = max(dp[i - 3] + stairs[i - 1] + stairs[i], dp[i - 2] + stairs[i])
        dp.append(val)

    print(dp[n])

