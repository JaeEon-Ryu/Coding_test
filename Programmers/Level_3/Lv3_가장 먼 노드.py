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
    visited = [-1 for i in range(n)]
    queue = deque([[1,0]]) # start node, count distance

    while queue:
        n = queue.popleft()
        node = n[0]
        dist = n[1]

        if visited[node-1] == -1:
            visited[node-1] = dist
            dist += 1
            for i in graph[node]:
                queue.append([i,dist])

    return visited.count(max(visited))

n = 6
edge = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
print(solution(n,edge))


'''
그래프를 생성할 떄 
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
        
if else문 쓰지 않고 그냥
graph =[  [] for _ in range(n + 1) ]
for (a, b) in edge:
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)
라는 방법으로 이중 리스트를 활용하여 사전형을 쓰지 않고도 풀 수 있다.
a-1, b-1은 각각 인덱스를 더 쉽게 활용하기 위해서 -1을 한 것 같다.    

'''