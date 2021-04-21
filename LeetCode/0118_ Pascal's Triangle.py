'''
Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:
'''

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = [[1]]

        if numRows == 1:
            return triangle

        for num_of_inner in range(numRows - 1): # 맨 처음에 triangle 요소를 미리 만들었으므로 numRows-1
            next_row = [1] # 왼쪽 1

            for n in range(num_of_inner): # 1 과 1 사이에 존재하는 숫자들만큼 반복
                next_row.append(triangle[-1][n] + triangle[-1][n + 1])

            next_row.append(1) # 오른쪽 1
            triangle.append(next_row) # 삼각형 리스트에 만들어둔 행 추가

        return triangle
