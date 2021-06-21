# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    sum_left, sum_right = 0, sum(A)
    min_num = float('inf')

    for i in range(len(A) - 1):
        sum_left += A[i]
        sum_right -= A[i]

        min_num = min(min_num, abs(sum_right - sum_left))

    return min_num
