N = int(input())
dp = [0,0,1,1] # 인덱스 조정을 위해 맨 처음 0 추가

'''
1을 뺐을 때, 3으로 나눴을 때, 2로 나눴을 때의 값을 각각 비교
이전에 구해놓았던 값을 활용 ( 메모이제이션 - 하향식 접근법 ), 최소값 대입
'''
for i in range(4,N+1):
    prev = dp[i-1] + 1

    if i%3==0:
        prev = min(prev,dp[i//3]+1)
    if i%2==0:
        prev = min(prev,dp[i//2]+1)

    dp.append(prev)

print(dp[N])