'''
Implement pow(x, n), which calculates x raised to the power n (i.e. xn).
'''


class Solution:
    def myPow(self, x: float, n: int) -> float:

        N = abs(n)
        result = 1

        while N:
            if N % 2 == 1:
                result *= x
            x *= x
            N //= 2

        return result if n > 0 else 1 / result


        '''
        # 시간초과가 났던 코드
        # ( 지수적 증가의 속도로 문제를 풀어야 시간초과가 나지 않음 )

        result = 1
        for _ in range(abs(n)):
            result *= x

        return result if n > 0 else 1/result
        '''