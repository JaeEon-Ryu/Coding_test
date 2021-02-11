import math
def solution(n,a,b):
    answer = 1

    # a와b의 차이가 1이라면 만난 것임
    # 추가로 더 큰 수가 홀수라면 만난 상태가 아님
    while abs(a-b) != 1 or max(a,b)%2==1:
        a = math.ceil(a/2)
        b = math.ceil(b/2)
        answer += 1

    return answer

print(solution(8,4,5))


'''
다른 사람의 풀이
XOR의 개념을 이용하고 비트의 길이를 구함

def solution(n,a,b):
    return ((a-1)^(b-1)).bit_length()

'''