def solution(A,B):
    answer = 0
    A.sort(reverse=True)
    B.sort()

    for i in range(len(A)):
        answer += A.pop() * B.pop()

    return answer

A = [1,2]
B = [3,4]
print(solution(A,B))
