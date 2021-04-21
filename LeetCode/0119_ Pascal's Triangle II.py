'''
Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:
'''

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        triangle = [[1]]
        next_row = []

        if rowIndex == 0:
            return [1]

        for num_of_inner in range(rowIndex):
            next_row = [1]  # 왼쪽 1

            for n in range(num_of_inner):  # 1 과 1 사이에 존재하는 숫자들만큼 반복
                next_row.append(triangle[-1][n] + triangle[-1][n + 1])

            next_row.append(1)  # 오른쪽 1
            triangle.append(next_row)  # 삼각형 리스트에 만들어둔 행 추가

        return next_row