def solution(n):
    if int(n**0.5)**2 == n :
        return (int(n**0.5)+1)**2
    else:
        return -1

n = 121
print(solution(n))