#name = "JAZ"
#name = "JEROEN"
#name = "JAN"
name = "ABABAAAAABA"

# A = 65
# Z = 90
# 65 ~ 90 ex) 68일때, 90-68과 68-65 중 차이 작은 것

# 숫자에서 문자로 -> chr()
# 문자에서 숫자로 -> ord()

def solution(name):
    answer = 0

    # 수직 이동 거리 계산
    vertical_distance = 0
    for alpha in name:
        chr_to_num = ord(alpha)
        less_move = min(91-chr_to_num,chr_to_num-65)
        vertical_distance += less_move # 위 혹은 아래로 이동

    # 수평 이동 거리 계산
    count_A = [0,0]
    for idx in range(1,len(name)): # 오른쪽으로
        if name[idx]=='A':
            count_A[0] +=1
        else:
            break

    for idx in range(len(name)-1,1,-1): # 왼쪽으로
        if name[idx]=='A':
            count_A[1] +=1
        else:
            break

    horizontal_distance = len(name)-1-max(count_A)

    answer = vertical_distance + horizontal_distance

    return answer

print(solution(name))