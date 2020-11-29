'''
목표 : 네트워크의 개수 찾기
방법 : answer의 값을 0으로 초기화.
DFS를 활용하여 노드에 대한 모든곳을 방문하고 answer의 값을 1추가
# DFS를 활용하기 위해 computers의 정보를 활용하여 사전형으로 만들어준다.
# 예시1의 경우 사전형 => [1]:2, [2]:1, [3]:None
'''

def solution(n, computers):
    answer = 0
    computer_dict = dict()

    # DFS에 필요한 정보를 사전형으로 처리
    for idx,info in enumerate(computers):
        computer_dict.setdefault(idx+1)
        temp = []

        for order,node in enumerate(info):
            if order != idx and node != 0:
                temp.append(order+1)

        if temp:
            computer_dict[idx+1] = set(temp)

    # 모든 노드를 탐색하기 위해 리스트 생성
    num_list = [i for i in range(1,n+1)]

    # 모든 노드를 탐색할때까지 반복
    while num_list:

        visited = []
        stack = [num_list.pop()]

        while stack:
            n = stack.pop()
            if computer_dict.get(n) == None:
                break

            if n not in visited:
                visited.append(n)
                stack += computer_dict[n] - set(visited)

        num_list = list(set(num_list) - set(visited))
        answer += 1

    return answer

n = 3
#computers = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]
computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
print(solution(n,computers))