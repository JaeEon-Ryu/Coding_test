'''
솔루션
1. stations안에 값들을 기준으로 전파 시작점, 마침점을 찾는다.
2. 그 두개를 활용해 비어있는 전파거리를 계산한다.
3. 비어있는 전파거리는 w를 사용하여 몇개로 채워야 하는지 각각 계산한다.
모든 인덱스를 참조할 때까지 1,2,3 반복
'''

import math
def solution(n, stations, w):

    answer = 0
    end = 0

    for station in stations:
        start = station - w

        if start > 1:
            block = start - (end+1)
            answer += math.ceil(block / ((w * 2) + 1))

        end = station + w

    if end < n+1:
        block = (n+1) - (end + 1)
        answer += math.ceil(block / ((w * 2) + 1))

    return answer

'''
N개의 아파트만큼 리스트를 생성하여 
전파 연결이 된다면 그곳에 1 안된다면 0 을 넣는 방식을 사용
시간초과 + 코드에 오류도 있음

import math
def solution(n, stations, w):

    answer = 0
    installed = [0 for _ in range(n+1)]
    installed[0] = 1

    for station in stations:

        installed[station] = 1
        for cal in range(1,w+1):
            if station-cal > 0:
                installed[station-cal] = 1
            if station+cal < n:
                installed[station+cal] = 1


    installed.pop(0)
    current = 0

    for idx,install in enumerate(installed):

        if install == 0 :
            current += 1
            if idx == n-1:
                answer += math.ceil(current / ((w * 2) + 1))

        elif install == 1:
            if current != 0:
                answer += math.ceil(current/((w*2)+1))
            current = 0

    return answer
'''

#n = 11
#stations = [4,11]
#w = 1

n = 16
stations = [9]
w = 2


print(solution(n, stations, w))