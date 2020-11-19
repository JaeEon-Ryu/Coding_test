from math import gcd

def solution(arr):
    answer = arr.pop()
    while arr:
        num_compare = arr.pop()
        answer = answer * num_compare // gcd(answer,num_compare)

    return answer

print(solution([2,6,8,14]))