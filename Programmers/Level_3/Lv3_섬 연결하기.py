def solution(n, costs):
    answer = 0

    costs.sort(key = lambda x:x[2]) # 거리순 정렬
    visited = [0 for i in range(n)]
    visited[0] = 1

    while sum(visited) != n:
        for cost in costs:
            if visited[cost[0]] + visited[cost[1]] == 1: # 둘 중 한곳만 방문 했을 경우
                visited[cost[0]],visited[cost[1]] = 1,1
                answer += cost[2]
                break

    return answer

n = 4
costs = [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]
print(solution(n,costs))