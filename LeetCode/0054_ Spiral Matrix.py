'''
Given an m x n matrix, return all elements of the matrix in spiral order.
'''


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        len_x, len_y = len(matrix), len(matrix[0])
        size_of_matrix = len_x * len_y
        visited = [
            [False for _ in range(len_y)]
            for _ in range(len_x)
        ]

        def can_go(x, y):
            return 0 <= x < len_x and 0 <= y < len_y and visited[x][y] == False

        dx, dy, dir = [0, 1, 0, -1], [1, 0, -1, 0], 0
        x, y = 0, -1

        result = []
        cnt = 0

        while cnt != size_of_matrix:
            new_x, new_y = x + dx[dir], y + dy[dir]

            if can_go(new_x, new_y):
                result.append(matrix[new_x][new_y])
                visited[new_x][new_y] = True
                cnt += 1
                x, y = new_x, new_y
            else:  # 방향 전환
                dir += 1
                dir %= 4  # dir = 0,1,2,3 중 하나여야 하므로

        return result