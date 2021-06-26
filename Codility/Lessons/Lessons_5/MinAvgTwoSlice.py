# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    N = len(A)
    min = sum(A[0:2])/2
    result = 0

    if N == 2:
        return result

    for i in range(3,N+1):

        avg = sum(A[i-2:i])/2
        if avg < min:
            result = i-2
            min = avg

        avg = sum(A[i-3:i])/3
        if avg < min:
            result = i-3
            min = avg

    return result
