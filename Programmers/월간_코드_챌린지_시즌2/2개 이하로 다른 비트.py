def solution(numbers):
    answer = []

    for num in numbers:
        if num %2 ==0: # 짝수일 경우
            answer.append(num+1)
        else: # 홀수일 경우
            last_zero = (num+1) & (-num) # 최하위 비트 0
            zero_2_one = num | last_zero  # 최하위 비트를 0을 1로
            temp = (zero_2_one & (~(last_zero)>> 1)) # 최하위 비트 0 다음 비트 1을 0으로
            answer.append(temp)

    return answer