'''
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1.
You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.
'''


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visited = [0 for _ in range(numCourses)]
        graph = defaultdict(list)

        for a, b in prerequisites:
            graph[b].append(a)
            visited[a] += 1

        stack = []
        for i, node in enumerate(visited):
            if node == 0:
                stack.append(i)

        while stack:
            node = stack.pop()
            for vertex in graph[node]:
                visited[vertex] -= 1
                if visited[vertex] == 0:
                    stack.append(vertex)

        return True if sum(visited) == 0 else False