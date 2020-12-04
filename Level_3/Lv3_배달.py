# 1번 마을로부터 다른 마을까지 접근해야함. -> 탐색문제
# 경로가 여러개 있을 수도 있다

def solution(N, road, K):
    answer = 0
    road_dict = dict()

    # 그래프 생성
    for r in road:
        # r[2] = distance
        key = r[0] # from
        if road_dict.get(key) == None:
            road_dict[key] = [(r[1],r[2])]
        else:
            road_dict[key].append((r[1],r[2]))

        key = r[1] # to
        if road_dict.get(key) == None:
            road_dict[key] = [(r[0],r[2])]
        else:
            road_dict[key].append((r[0],r[2]))


    distance = dict()
    # distance 그래프 생성
    for n in range(1, N+1):
        if n == 1:
            distance[n] = 0
        else:
            distance[n] = 500001 # 이 부분 때문에 테스트케이스 30,31,32가 틀렸었다.
            # 도로를 지나는데 걸리는 최대 시간 10000을 보고 10001로 정의하였었는데
            # 다시 보니 아래에 추가적으로 K가 음식 배달이 가능한 시간을 나타내며 최대값은 500000이었다.

    stack = [1]
    while stack:
        n = stack.pop()
        for road in road_dict[n]:
            if distance[road[0]] > distance[n] + road[1]:
                distance[road[0]] = distance[n] + road[1]
                stack.append(road[0])

    for d in distance.values():
        if K >= d:
            answer += 1

    return answer


N = 5 # 마을의 개수
road = [[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]]
K = 3 # 음식 배달이 가능한 시간
print(solution(N,road,K))