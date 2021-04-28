"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

'''
BFS Solution
'''


class Solution:
    import collections
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None

        cloned_graph = dict()  # 복제될 공간
        cloned_graph[node.val] = Node(node.val)
        queue = collections.deque()
        queue.append(node)

        while queue:
            current = queue.popleft()

            for neighbor in current.neighbors:
                if neighbor.val not in cloned_graph:
                    cloned_graph[neighbor.val] = Node(neighbor.val)  # key-value 값으로 저장
                    queue.append(neighbor)
                cloned_graph[current.val].neighbors.append(cloned_graph[neighbor.val])

        return cloned_graph[node.val]