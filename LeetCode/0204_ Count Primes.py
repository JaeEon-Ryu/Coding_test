'''
Count the number of prime numbers less than a non-negative number, n.
'''

class Solution:
    def countPrimes(self, n: int) -> int:
        # reference : OldCoadingFarmer
        if n < 3:
            return 0

        dp = [True] * n
        dp[0] = dp[1] = False
        for i in range(2, n):
            if dp[i]:
                # print(i,'일때')
                for j in range(i * i, n, i):  # 서로소가 아닌 숫자들
                    dp[j] = False
                    # print(j,'는 false로',end=' ')
                # print()
        return sum(dp)

    '''시간초과
    def countPrimes(self, n: int) -> int:
        if n < 3:
            return 0

        cnt = 1
        for i in range(3,n,2):
            for j in range(3,((i+1)//2)+1,2):
                if i%j == 0:
                    break
            else:
                cnt += 1
        return cnt
    '''
