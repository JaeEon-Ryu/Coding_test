'''
You are given an n x n 2D matrix representing an image,
rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place,
which means you have to modify the input 2D matrix directly.
DO NOT allocate another 2D matrix and do the rotation.
'''

# 가로 한줄씩(len(matrix[i])) 떼서 세로줄에 각각 할당하는 방법으로 풀이함
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:

        n = len(matrix)
        for i in range(n-1,-1,-1):
            curr_mat = matrix[i][:n] # to distribute numbers
            matrix[i] = matrix[i][n:] # remove curr_mat partial

            for new_i,num in enumerate(curr_mat): # distribute sequentially from the curr_mat
                matrix[new_i].append(num)