class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # 조건 - 가로 길이 9 탐색, 세로 길이 9 탐색, 길이3의 정사각형 내부 탐색

        # 가로 길이 9 탐색
        # 해당 열에 대한 루프 탐색 내장함수 in이나 count로 수행 가능

        # 세로 길이 9 탐색
        # 반복문을 통해 행을 일일히 탐색해야함

        # 길의 3의 정사각형 내부 탐색
        # 좌표 4,1 이라면 -> 3,0 3,1 ,3,2 4,0 4,1 4,2 5,0 5,1 5,2 탐색해야함
        # 행의 시작점 0,3,6
        # 열의 시작점 0,3,6
        # 좌표가 주어진다면 3으로 나눈 나머지가 0일때까지 계속하여 값을 빼서 기준점을 찾도록 한다

        def is_valid_horizontal(x, y):
            return True if board[x].count(board[x][y]) < 2 else False

        def is_valid_vertical(x, y):
            cnt = 0
            for i in range(9):
                if board[i][y] == board[x][y]:
                    cnt += 1

            return True if cnt < 2 else False

        def is_valid_square(x, y):
            val = board[x][y]
            while x % 3 != 0:
                x -= 1
            while y % 3 != 0:
                y -= 1

            cnt = 0
            for i in range(x, x + 3):
                for j in range(y, y + 3):
                    if board[i][j] == val:
                        cnt += 1

            return True if cnt < 2 else False

        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue
                if not (is_valid_horizontal(i, j) and is_valid_vertical(i, j) and is_valid_square(i, j)):
                    return False

        return True

