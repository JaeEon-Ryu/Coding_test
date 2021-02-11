# 이진 변화의 횟수
# 변환 과정에서 제거된 모든 0의 개수

def solution(s):
    answer = [0,0]

    while s != '1':
        answer[1] += s.count('0') # 변환 과정에서 제거된 모든 0 의 개수
        s = str(format(s.count('1'),'b'))
        answer[0] += 1 # 이진 변화의 횟수

    return answer

s = "110010101001"

print(solution(s))