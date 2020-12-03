# 1번 마을로부터 다른 마을까지 접근해야함. -> 탐색문제
# 경로가 여러개 있을 수도 있다

def solution(N, road, K):
    answer = 1 # 첫번째 지점은 무조건 가능하므로
    road_dict = dict()

    # 그래프 생성
    for r in road:
        key = r[0]
        if road_dict.get(key) == None:
            road_dict[key] = [(r[1],r[2])]
        else:
            road_dict[key].append((r[1],r[2]))

        key = r[1]
        if road_dict.get(key) == None:
            road_dict[key] = [(r[0],r[2])]
        else:
            road_dict[key].append((r[0],r[2]))

    print(road_dict)

    # 스택을 사용한 DFS
    visited = []
    stack = [1]

    while stack:
        n = stack.pop()
        if n not in visited:
            visited.append(n)
            for road in road_dict[n]:
                stack += set([road[0]]) - set(visited)

    print(visited)
    return answer


N = 5 # 마을의 개수
road = [[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]]
K = 3 # 음식 배달이 가능한 시간
print(solution(N,road,K))