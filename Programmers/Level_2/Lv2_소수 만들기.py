from itertools import combinations

def is_prime(num):

    for i in range(2,int(num**0.5)+1):
        if num % i == 0:
            return False

    return True

def solution(nums):
    answer = 0
    combination = list(combinations(nums,3))

    for num_list in combination:
        if is_prime(sum(num_list)):
            answer += 1

    return answer

nums = [1,2,7,6,4]
print(solution(nums))