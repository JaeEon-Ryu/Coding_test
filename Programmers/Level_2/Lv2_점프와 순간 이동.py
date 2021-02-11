def solution(n):
    ans = 0
    print(bin(n))
    while n > 0:
        if n % 2 == 1:
            ans += 1
        n //= 2

    return ans

'''
다른 사람의 풀이
def solution(n):
    return bin(n).count('1')

--> 2진수 활용 : 메커니즘은 내가 푼 방법과 같다
'''

print(solution(5000))