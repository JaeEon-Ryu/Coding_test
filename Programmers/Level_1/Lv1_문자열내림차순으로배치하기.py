def solution(s):
    answer = list(s)
    answer.sort(reverse=True)
    answer = "".join(answer)
    return answer

s = "Zbcdefg"
print(solution(s))
