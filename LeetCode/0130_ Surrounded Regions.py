'''
Given an m x n matrix board containing 'X' and 'O', capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.
'''

class Solution:
    '''
    reference : OldCoadingfarmer
    '''

    # BFS
    def solve(self, board):
        queue = collections.deque([])
        for r in range(len(board)):
            for c in range(len(board[0])):
                if (r in [0, len(board) - 1] or c in [0, len(board[0]) - 1]) and board[r][c] == "O":
                    queue.append((r, c))

        while queue:
            r, c = queue.popleft()
            if 0 <= r < len(board) and 0 <= c < len(board[0]) and board[r][c] == "O":
                board[r][c] = "."
                queue.extend([(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)])

        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == ".":
                    board[r][c] = "O"

    ''' 오답
    def solve(self, board):
        """
        Do not return anything, modify board in-place instead.
        """
        self.board = board
        self.visited = [
            [False for _ in range(len(board[0]))]
            for _ in range(len(board))
        ]
        self.blocked_area = []

        for i in range(len(board)):
            for j in range(len(board[0])):
                if not self.visited[i][j] and board[i][j] == 'O':
                    if self.is_blocked(i,j):
                        self.change_o_to_x()
                    else:
                        self.blocked_area = []

    def change_o_to_x(self):

        while self.blocked_area:
            x,y = self.blocked_area.pop()
            self.board[x][y] = 'X'

    def in_range(self,x,y):
        return 0<=x<len(self.board) and 0<=y<len(self.board[0])

    def is_blocked(self,x,y):
        self.flag = True

        def search(x, y):
            if self.visited[x][y]:
                return
            else:
                self.blocked_area.append([x, y])
                self.visited[x][y] = True

            dx, dy = [1, -1, 0, 0], [0, 0, -1, 1]
            for i in range(4):
                new_x, new_y = x+dx[i], y+dy[i]
                if self.in_range(new_x,new_y):
                    if self.board[new_x][new_y] == 'O':
                        search(new_x,new_y)
                else:
                    self.flag = False
                    return
        search(x,y)

        return self.flag
    '''


