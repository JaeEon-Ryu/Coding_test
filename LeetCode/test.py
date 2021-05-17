# class Solution:
#
#     # reference : user4507
#
#     def solveSudoku(self, board: 'List[List[str]]') -> 'None':
#         self.board = board
#         self.solve()
#
#     def findUnassigned(self):
#         for row in range(9):
#             for col in range(9):
#                 if self.board[row][col] == '.':
#                     return row, col
#         return -1, -1
#
#     def solve(self):
#         row, col = self.findUnassigned()
#         if (row, col) == (-1, -1):
#             return True
#
#         for num in map(str, range(1, 10)):
#             if self.isSafe(row, col, num):
#                 self.board[row][col] = num
#                 if self.solve(): # 다음 숫자 참조
#                     return True
#                 self.board[row][col] = '.'
#
#     # 가로, 세로, 사각형에 있는 중복된 숫자를 판별하는 기능
#     # 이 기능을 50~70 줄에 걸쳐 썼는데 이렇게 쓸 수 있음에 배우고 간다
#     def isSafe(self, row, col, ch):
#         rowSafe = all(self.board[row][_] != ch for _ in range(9))
#         colSafe = all(self.board[_][col] != ch for _ in range(9))
#         squareSafe = all(self.board[r][c] != ch for r in self.getRange(row) for c in self.getRange(col))
#         return rowSafe and colSafe and squareSafe
#
#     def getRange(self, x):
#         x -= x % 3
#         return range(x, x + 3)

'''
import copy

def solveSudoku(board) -> None:
    """
    Do not return anything, modify board in-place instead.
    """

    # 1 스도쿠 모든 배열을 순회한다
    #  1-1 순회할때마다 어느 숫자가 맞는지 확인하기 위해 1 ~ 9 의 반복문을 만든다
    #  1-2 리스트의 숫자가 해당 스도쿠 배열에 적용될 수 있다면 nums에 추가한다.
    #   1-2-1 만약 최종적으로 nums에 숫자가 한 개 남았다면 그 숫자로 할당한다
    # 모든 숫자가 할당될 때까지 1을 반복한다.

    def is_empty():
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    return True
        return False

    def is_valid(x, y, n):

        # is valid from horizontal
        for j in range(9):
            #print(board[x][j],n)
            if board[x][j] == n:
                # if x == 6 and y == 0:
                #     print('ho')
                return False


        # is valid from vertical
        for i in range(9):
            if board[i][y] == n:
                # if x == 6 and y == 0:
                #     print('v')
                return False

        # is valid from square
        while x % 3 != 0:
            x -= 1
        while y % 3 != 0:
            y -= 1
        for i in range(x, x + 3):
            for j in range(y, y + 3):
                if board[i][j] == n:
                    # if x == 6 and y == 0:
                    #     print('sq')
                    return False

        return True

    def insert_if_can(x,y):

        for i in range(x-2,x+1):
            for j in range(y-2,y+1):

                for num in possible_nums_in_board[i][j]:
                    flag = True
                    for new_i in range(x-2,x+1):
                        for new_j in range(y-2,y+1):
                            if i == new_i and j == new_j:
                                continue
                            else:
                                if num in possible_nums_in_board[new_i][new_j]:
                                    flag = False
                                    break
                    if flag:
                        board[i][j] = num
                        possible_nums_in_board[i][j] = [num]
                        break

    possible_nums_in_board = copy.deepcopy(board)

    while is_empty():
        for i in range(9):
            for j in range(9):

                if board[i][j] == '.':
                    nums = []
                    for num in range(1, 10):
                        if is_valid(i, j, str(num)):
                            nums.append(str(num))
                            # if i == 6 and j == 0:
                            #     print(nums)

                    possible_nums_in_board[i][j] = nums
                    if len(nums) == 1:
                        board[i][j] = nums[0]

        for i in range(9):
            for j in range(9):
                # 3x3 사각형을 탐색할 수 있는 위치
                if (i + 1) % 3 == 0 and (j + 1) % 3 == 0:
                    #print(i,j)
                    insert_if_can(i, j)
                    #print()

        # for i in range(9):
        #     for j in range(9):
        #         print(board[i][j],end=' ')
        #     print()
        # print()
        #
        # for i in range(9):
        #     for j in range(9):
        #         print(possible_nums_in_board[i][j],end=' ')
        #     print()
        # print()
'''

# board = [[".",".","9","7","4","8",".",".","."],
#      ["7",".",".",".",".",".",".",".","."],
#      [".","2",".","1",".","9",".",".","."],
#      [".",".","7",".",".",".","2","4","."],
#      [".","6","4",".","1",".","5","9","."],
#      [".","9","8",".",".",".","3",".","."],
#      [".",".",".","8",".","3",".","2","."],
#      [".",".",".",".",".",".",".",".","6"],
#      [".",".",".","2","7","5","9",".","."]]
#
# sol = Solution()
# sol.solveSudoku(board)
#
# for i in range(9):
#     for j in range(9):
#         print(board[i][j], end=' ')
#     print()
# print()

test = dict()
test[0] = 5
test[1] = 3

print(test)
for _ in test:
    print(_)


