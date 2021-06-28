# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    A.sort()
    left_product = A[0]*A[1]*A[-1] # 음수쪽부터 봤을 때 최대값
    right_product = A[-1]*A[-2]*A[-3] # 양수쪽부터 봤을 때 최대값
    return left_product if left_product > right_product else right_product
