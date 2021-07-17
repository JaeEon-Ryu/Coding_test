# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    A.sort()
    s, e = 0, len(A) - 1
    result = float('inf')

    while s <= e:
        curr = A[s] + A[e]
        result = min(result, abs(curr))

        if curr > 0:
            e -= 1
        else:
            s += 1

    return result