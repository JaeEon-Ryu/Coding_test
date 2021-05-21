'''
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
You may assume all four edges of the grid are all surrounded by water.
'''

'''
visited를 활용하여 방문하지 않은 곳이라면 방문하여 bfs 형식으로 인접한 모든 경로를 방문하게끔 함 
'''

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        self.visited = [
            [False for j in range(len(grid[i]))]
            for i in range(len(grid))
        ]
        result = 0

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1" and not self.visited[i][j]:
                    self.bfs(grid, i, j)
                    result += 1

        return result

    def bfs(self, grid, x, y):
        self.visited[x][y] = True

        dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
        for i in range(4):
            new_x, new_y = x + dx[i], y + dy[i]
            # 다음 위치가 틀을 벗어나지 않는지, 다음 위치가 "1" 을 만족하는지, 다음 위치가 방문 하지 않은 곳인지
            if 0 <= new_x < len(grid) and 0 <= new_y < len(grid[new_x]) and \
                    grid[new_x][new_y] == "1" and \
                    not self.visited[new_x][new_y]:
                self.bfs(grid, new_x, new_y)

'''
문제풀이를 완료한 후 돌아본 결과
-> 굳이 visited를 활용하지 않아도 된다
-> 방문했다면 "1"을 "0"으로 바꾸는 것만으로 해도 문제 해결 가능
-> 더 적은 메모리 사용, 더 빠른 실행 결과가 나올 것으로 예상
'''