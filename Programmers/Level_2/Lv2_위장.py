# x1,y1,y2 의 경우
# 1. x,y1
# 2. x,y2
# 3. x
# 4. y1
# 5. y2
# 총 5개가 있음.
# => 리스트[1], 리스트[2]
# 1 + 2 + 1X2 => 5
#
# y1,y2,y3 의 경우
# 1. y1
# 2. y2
# 3. y3
# 총 3개가 있음
# => 리스트[3]
# 3 + 3X0 => 3
#
# 문제는, x와 y라는 것을 어떻게 구별하여서
# 그 개수만큼 더해서 저장할 것인가?
# -> 리스트를 두개생성? (딕셔너리 사용)
#
# --------------------------------------------------
#
# 옷 3가지의 경우
# x1 y1 z1
# 1. x1
# 2. y1
# 3. z1
# 4. x1,y1
# 5. x1,z1
# 6. x1,y1,z1
# 7. y1,z1
#
# 2 2 2
#
# -----------------------------------------------

def solution(clothes):
    dict_clothes = {}
    for i in clothes:
        if i[1] in dict_clothes :
            dict_clothes[i[1]] += 1
        else :
            dict_clothes[i[1]] = 1

    number_of_process = list(dict_clothes.values())
    if len(number_of_process) == 1 :
        return sum(number_of_process)
    else :
        answer = 1
        for i in number_of_process :
            answer *= i+1
        return answer -1

# 꽤 길게 풀었다,,
# 그렇게 길게 쓸 코드가 아니었던 것 같다.
# Counter라는 클래스를 몰랐기 때문에
# 그 함수를 일일히 손수 썼다.
# 다음부터는 Counter라는 함수를 이용하여
# 간단히 작성해야겠다.