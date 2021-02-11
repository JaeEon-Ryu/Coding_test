def solution(d, budget):
    answer = 0
    d_sum = 0
    d.sort()

    for num in d:
        if d_sum + num > budget:
            break
        else:
            d_sum += num
            answer += 1

    return answer

d = [1,3,2,5,4]
budget = 9
print(solution(d,budget))