def solution(n):
    answer = ''
    list = []

    for i in str(n):
        list.append(int(i))

    list.sort(reverse=True)

    for i in list:
        answer += str(i)

    return int(answer)

n = 118372
print(solution(n))
