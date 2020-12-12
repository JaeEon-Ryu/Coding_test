'''
[1, 2, 3]
[1, 3, 2]
[2, 1, 3]
[2, 3, 1]
[3, 1, 2]
[3, 2, 1]


factorial -> math 함수 있음
'''

def factorial(n):
    result = 1

    for i in range(2,n+1):
        result *= i

    return result

def solution(n, k):
    answer = []
    items = [item for item in range(1, n + 1)]

    while n > 0: # n개의 정수를 구할때까지
        f = factorial(n - 1)
        answer.append(items.pop((k-1)// f))
        n -= 1
        k %= f

    return answer

'''
시간초과가 났던 코드
import itertools
def solution(n, k):

    items = [item for item in range(1,n+1)]
    answer = list(itertools.permutations(items, n))[k-1]

    return list(answer)
'''

n = 3
k = 5
print(solution(n,k))