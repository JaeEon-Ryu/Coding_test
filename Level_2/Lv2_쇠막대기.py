def solution(arr):
    answer = 0
    line = 0
    for i in range(len(arr)):
        if arr[i] == '(':
            line += 1
        else : # ')' 일 경우
            if arr[i] == ')' and arr[i-1] == '(': # 레이저 켜짐:
                line -= 1
                answer += line
            else: # 그냥 닫힐 경우
                answer += 1
                line -= 1

    return answer