numbers = [2,1,3,4,1]

def solution(numbers):
    answer = []

    for i in range(len(numbers)):
        num1 = numbers.pop()

        if numbers:
            for num2 in numbers:
                sum = num1 + num2

                if sum not in answer:
                    answer.append(sum)

    answer.sort()
    return answer

print(solution(numbers))