from collections import Counter
def solution(a):

    answer = 0
    # 리스트에 있는 숫자들의 빈도 세기
    num_counted = Counter(a)

    for key in num_counted.keys():

        idx = 0
        # 숫자 빈도에 대한 키값과 그에 상응하는 수열을 찾기 위해
        # 그리고 이 두개의 값이 만족되어야만 스타수열이 1증가되므로
        # selected 변수 두개 각각 None으로 선언하고
        # 이 두개가 None이 아닐 경우에만 count를 하도록 한다.
        key_value_selected = None
        value_selected = None
        cnt = 0

        if num_counted[key] <= answer: # 이 부분을 쓰지 않으면 시간 초과
            continue

        while idx < len(a):
            if a[idx] == key :
                key_value_selected = key
            else:
                value_selected = a[idx]

            if key_value_selected != None and value_selected != None:
                key_value_selected = None
                value_selected = None
                cnt += 1

            idx += 1

        if answer < cnt :
            answer = cnt

    return answer*2 # 스타수열 1개 -> 길이 2

a = [0,3,3,0,7,2,0,2,2,0]
print(solution(a))