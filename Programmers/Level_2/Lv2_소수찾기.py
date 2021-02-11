import math
from itertools import permutations

def isPrime(num):
    if num < 2 :
        return False
    else:
        for i in range(2,int(math.sqrt(num))+1):
            if num % i == 0:
                return False

    return True

def solution(numbers):
    answer = []
    numbers_list = [i for i in numbers]

    for i in range(1, len(numbers) + 1):
        p_list = list(map(''.join, permutations(list(numbers), i)))

        for i in list(set(p_list)):
            if isPrime(int(i)):
                answer.append(int(i))

    return len(set(answer))

numbers = "123"

print(solution(numbers))