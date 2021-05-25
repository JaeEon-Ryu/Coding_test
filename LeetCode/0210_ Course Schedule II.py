'''
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.
'''

'''
207번 문제 활용
bfs형식으로 뻗어나가는 것을 생각하여 시작점을 순서대로 집어 넣으면 된다
'''

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        visited = [0 for _ in range(numCourses)]
        graph = defaultdict(list)
        result = []

        for a, b in prerequisites:
            graph[b].append(a)
            visited[a] += 1

        stack = []
        for i, node in enumerate(visited):
            if node == 0:
                stack.append(i)
                result.append(i)

        while stack:
            node = stack.pop()
            for vertex in graph[node]:
                visited[vertex] -= 1
                if visited[vertex] == 0:
                    stack.append(vertex)
                    result.append(vertex)

        return result if sum(visited) == 0 else []