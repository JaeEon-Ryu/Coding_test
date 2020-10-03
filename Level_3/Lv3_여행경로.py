#tickets = [['ICN', 'JFK'], ['HND', 'IAD'], ['JFK', 'HND']]
tickets = [['ICN', 'SFO'], ['ICN', 'ATL'], ['SFO', 'ATL'], ['ATL', 'ICN'], ['ATL','SFO']]
#tickets = [["ICN", "BOO"], ["ICN", "COO"], ["COO", "DOO"], ["DOO", "COO"], ["BOO", "DOO"], ["DOO", "BOO"], ["BOO", "ICN"], ["COO", "BOO"]]

def solution(tickets):
    answer = []
    graph = dict()
    tickets.sort(reverse=True)

    # 그래프로 관계도 작성
    for SP,EP in tickets: # StartingPoint, EndingPoint
        if SP in graph:
            graph[SP].append(EP)
        else:
            graph[SP] = [EP]

    stack = ['ICN']

    while stack: # 재귀표현이 아닌 스택으로 진행
        node = stack[-1]

        if node in graph and len(graph[node])!=0:
            stack.append(graph[node].pop()) # 스택에 경로 추가
        else:
            answer.append(stack.pop()) # 경로 확정

    return answer[::-1] # reverse

print(solution(tickets))


# def solution(tickets):
#     answer = ['ICN']
#
#     start = 'ICN'
#     end = 'ZZZ'
#
#     while len(tickets)!= 0:
#         extract_idx = 0
#         end = 'ZZZ'
#         for idx,path in enumerate(tickets):
#             if start == path[0] and end > path[1]:
#                 end = path[1]
#                 extract_idx = idx
#
#         start = tickets[extract_idx][1]
#         answer.append(start)
#         tickets.pop(extract_idx)
#
#     return answer
#rint(solution(tickets))