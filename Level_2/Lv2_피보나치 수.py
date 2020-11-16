def solution(n):
    n1 = 0
    n2 = 1

    for _ in range(1,n):
        temp = n1
        n1 = n2
        n2 += temp

    return n2%1234567

print(solution(5))