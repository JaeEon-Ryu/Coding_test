'''
10	20	10	30	20	50
1	2	1	3	2	4
'''


N = int(input())

nums = list(map(int, input().split()))

dp = [1 for i in range(N)]

for i in range(N):
    for j in range(i):
        if nums[i] > nums[j]: # 현재 위치의 값보다 작은 값이라면
            dp[i] = max(dp[i], dp[j]+1) # 작은 값에 해당하는 dp에 1을 더해서 dp저장

print(max(dp))
