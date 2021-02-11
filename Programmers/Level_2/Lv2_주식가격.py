def solution(prices):
    answer = []
    print(len(prices))
    for i in range(len(prices) - 1):
        count = 0
        for j in range(i + 1, len(prices)):
            if prices[i] <= prices[j]:
                count += 1
            else:
                count += 1
                break
        answer.append(count)

    return answer