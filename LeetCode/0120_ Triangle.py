'''
Given a triangle array, return the minimum path sum from top to bottom.

For each step, you may move to an adjacent number of the row below. More formally,
if you are on index i on the current row, you may move to either index i or index i + 1 on the next row.
'''


class Solution:

    # bottom-up 풀이
    def minimumTotal(self, triangle: List[List[int]]) -> int:

        cumulative_list = triangle[-1]
        for i in range(len(triangle) - 2, -1, -1):
            for j in range(len(triangle[i])):
                cumulative_list[j] = min(cumulative_list[j], cumulative_list[j + 1]) + triangle[i][j]

        return cumulative_list[0]

    ''' greedy풀이 -> 시간초과
    import sys
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        self.min_total = sys.maxsize
        self.triangle = triangle
        self.finish_line = len(self.triangle)

        self.search_path(0,0,0)
        return self.min_total

    def search_path(self, total: int, row: int, col: int):
        total += self.triangle[row][col]

        if self.finish_line-1 == row: # 종료시점
            self.min_total = min(self.min_total,total)
            return

        # 분기
        self.search_path(total,row+1,col)
        self.search_path(total,row+1,col+1)
    '''

