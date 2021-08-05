N = int(input())
board = [
    list(map(int,input().split()))
    for _ in range(N)
]

dp = [
    [0 for _ in range(N)]
    for _ in range(N)
]

dp[0][0] = 1
for i in range(N):
    for j in range(N):
        num = board[i][j]

        if num != 0 and dp[i][j] != 0:
            if i + num < N: # 아래 방향
                dp[i+num][j] += dp[i][j]
            if j + num < N: # 오른쪽 방향
                dp[i][j+num] += dp[i][j]

print(dp[-1][-1])