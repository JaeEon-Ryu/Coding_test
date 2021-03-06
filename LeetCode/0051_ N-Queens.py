'''
The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle.

Each solution contains a distinct board configuration of the n-queens' placement,
where 'Q' and '.' both indicate a queen and an empty space, respectively.
'''


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        import copy

        # 해당 위치 기준 8방향을 검사하며 배치될 수 있는지 검사
        def can_arrange(p, x, y):
            dx, dy = [-1, -1, -1, 0, 0, 1, 1, 1], [-1, 0, 1, -1, 1, -1, 0, 1]
            for i in range(8):
                new_x, new_y = x + dx[i], y + dy[i]

                while 0 <= new_x < len(p) and 0 <= new_y < len(p):
                    if p[new_x][new_y] == 'Q':
                        return False
                    new_x, new_y = new_x + dx[i], new_y + dy[i]

            return True

        def insert_Q(p, i, j):
            helper = list(p[i])  # making starting point
            helper[j] = 'Q'
            p[i] = ''.join(helper)

        def arrange_Q(p, i):  # p = puzzle
            for j in range(len(p)):
                if can_arrange(p, i, j):  # 해당 위치에 배치될 수 있음
                    p_copy = copy.deepcopy(p)  # 다음 column도 참조해야 하므로 copy 사용
                    insert_Q(p_copy, i, j)

                    if i + 1 < len(p):  # 다음 행으로 분기
                        arrange_Q(p_copy, i + 1)
                    else:  # 다음 행이 없으면 result에 추가
                        result.append(p_copy)

        result = []
        puzzle = ['.' * n] * n
        # 리스트, 행 인덱스 대한 정보를 인자로 넘겨주며 recursive하게 함수 실행
        arrange_Q(puzzle, 0)

        return result