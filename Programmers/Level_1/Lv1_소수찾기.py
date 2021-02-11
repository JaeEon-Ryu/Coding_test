import math
def solution(n):
    answer = 0
    for number in range(2,n+1):
        is_prime = True

        for i in range(2, int(math.sqrt(number))+1):
            if number % i == 0:
                is_prime = False
                break

        if is_prime:
            print(number)
            answer += 1

    return answer

print(solution(10))