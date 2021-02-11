def solution(heights):
    answer = []
    flag = False

    for i in range(len(heights) - 1):
        checkNum = heights.pop()
        flag = False
        for i in range(len(heights), 0, -1):
            if checkNum < heights[i - 1]:
                answer.insert(0, i)
                flag = True
                break
        if flag == False:
            answer.insert(0, 0)
    answer.insert(0, 0)
    return answer