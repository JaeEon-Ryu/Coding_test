'''
Given a positive integer n,
generate an n x n matrix filled with elements from 1 to n2 in spiral order.
'''


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:

        matrix = [
            [0 for _ in range(n)]
            for _ in range(n)
        ]

        def can_go(x, y):
            return 0 <= x < n and 0 <= y < n and matrix[x][y] == 0

        dx, dy, dir = [0, 1, 0, -1], [1, 0, -1, 0], 0
        x, y = 0, -1

        for num in range(1, n ** 2 + 1):
            new_x, new_y = x + dx[dir], y + dy[dir]

            if can_go(new_x, new_y): # 원래 방향대로 직진
                matrix[new_x][new_y] = num
            else: # 방향 꺾기
                dir += 1
                dir %= 4
                new_x, new_y = x + dx[dir], y + dy[dir]
                matrix[new_x][new_y] = num

            x, y = new_x, new_y

        return matrix