def solution(n):
    answer = 0
    system = ''

    while n >= 1:
        system = str(int(n%3)) + system
        n /= 3

    multiple = 1
    for digit in system:
        answer += int(digit) * multiple
        multiple *= 3

    return answer

n = 45
print(solution(n))