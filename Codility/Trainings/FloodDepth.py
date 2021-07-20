# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6

    l, r = 0, len(A) - 1
    l_max, r_max = A[l], A[r]
    max_depth = 0

    while l < r:
        l_max, r_max = max(l_max, A[l]), max(r_max, A[r])
        if l_max <= r_max:
            depth = l_max - A[l]
            l += 1
        else:
            depth = r_max - A[r]
            r -= 1

        max_depth = max(max_depth, depth)

    return max_depth