'''
연속된 몇 개의 수를 선택해서 구할 수 있는 합 중 가장 큰 합

중간에 음수가 끼어있어도 가장 큰 합이 될 수 있음 ( ex: 1000,-1,1000,-1000,10,10,10,10 )
'''

n = int(input())
nums = list(map(int,input().split()))
dp = [-1001]
max_sum = -1001

for n in nums:
    val = max(n,n+dp[-1]) # 누적값과 현재값중 최대값
    dp.append(val)
    max_sum = max(max_sum,val)

print(max_sum)


