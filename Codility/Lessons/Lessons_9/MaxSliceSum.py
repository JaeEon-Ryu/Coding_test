# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6

    max_slice, current_sum = float('-inf'),0
    for n in A:
        max_slice = max(max_slice,current_sum+n)
        current_sum = max(0,current_sum+n)

    return max_slice
