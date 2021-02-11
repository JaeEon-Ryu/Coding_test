def solution(n, s):

    if n > s:
        return [-1]

    answer = [s//n for _ in range(n)]
    for idx in range(1,s-sum(answer)+1):
        answer[-idx] += 1

    return answer

print(solution(2,8))