def solution(arr, divisor):
    arr.sort()
    answer = [num for num in arr if num%divisor==0]
    if not answer : answer.append(-1)
    return answer