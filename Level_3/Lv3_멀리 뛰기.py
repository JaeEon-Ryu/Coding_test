'''
동적 계획법
r1 = 1
r2 = 2
r3 = 3
r4 = 5
r5 = 8
'''


def solution(n):

    r1,r2 = 1,2
    for _ in range(n-1):
        r1,r2 = r2,r1+r2

    return r1%1234567

print(solution(4))