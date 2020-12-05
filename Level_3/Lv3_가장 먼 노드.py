from collections import deque
def solution(n, edge):

    # 그래프 생성
    graph = dict()
    for edge_from,edge_to in edge:
        if graph.get(edge_from) == None:
            graph[edge_from] = [edge_to]
        else:
            graph[edge_from].append(edge_to)

        if graph.get(edge_to) == None:
            graph[edge_to] = [edge_from]
        else:
            graph[edge_to].append(edge_from)

    # bfs 탐색
    answer = []
    visited = []
    queue = deque([1])
    dist = 0

    while queue:
        for i in range(len(queue)):
            n = queue.popleft()
            if n not in visited:
                visited.append(n)
                answer.append(dist)
                queue += set(graph[n]) - set(visited)
        dist += 1

    return answer.count(max(answer))

n = 6
edge = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
print(solution(n,edge))