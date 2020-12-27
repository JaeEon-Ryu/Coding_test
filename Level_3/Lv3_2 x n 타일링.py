def solution(n):
    n1,n2 = 1,1

    for i in range(n):
        n1,n2 = n2,n1+n2

    return n1%1000000007

n = 4
print(solution(n))