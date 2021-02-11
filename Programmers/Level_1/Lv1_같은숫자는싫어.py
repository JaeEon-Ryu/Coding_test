def solution(arr):

    answer = []
    compare_num = 10

    for num in arr:
        if num != compare_num :
            answer.append(num)
            compare_num = num

    return answer

print(solution([1,1,3,3,0,1,1]))