def solution(dartResult):
    answer = []
    bonus = ['S','D','T']
    flag = False

    for idx,chr in enumerate(dartResult):

        if ord(chr) >= 48 and ord(chr) <= 57: # 숫자 0~9
            if flag==True and int(chr) == 0:
                answer[-1] = 10
            else:
                answer.append(int(chr))
            flag = True

        else:
            flag = False
            
            if chr in bonus:
                answer[-1] **=  (bonus.index(chr)+1)
            else: # ( * or # )
                if chr == '*':
                    if len(answer) > 1:
                        answer[-1] *= 2
                        answer[-2] *= 2
                    else:
                        answer[-1] *= 2
                else: # ( # )
                    answer[-1] *= -1

    return sum(answer)



# 다른 사람의 풀이
# 정규표현식을 사용함으로써 더 이해하기 쉽게 표현
import re

def solution(dartResult):
    bonus = {'S' : 1, 'D' : 2, 'T' : 3}
    option = {'' : 1, '*' : 2, '#' : -1}
    p = re.compile('(\d+)([SDT])([*#]?)')
    dart = p.findall(dartResult)
    print(dart)
    for i in range(len(dart)):
        if dart[i][2] == '*' and i > 0:
            dart[i-1] *= 2
        dart[i] = int(dart[i][0]) ** bonus[dart[i][1]] * option[dart[i][2]]

    answer = sum(dart)
    return answer

dartResult = '1S2D*3T'
print(solution(dartResult))