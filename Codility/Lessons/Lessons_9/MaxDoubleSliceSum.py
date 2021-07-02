# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    result,max_slice,max_current = 0,0,0
    min_element = A[1] if A[1] > 0 else 0

    for i in range(2,len(A) - 1):
        if A[i] <= min_element:
            max_slice = max_slice + min_element
            min_element = A[i]
        else:
            max_slice = max_slice + A[i]

        if max_slice <= max_current:
            max_slice = max_current
            min_element = A[i]

        max_current = max(0,max_current + A[i])
        result = max(result,max_slice)

    return result
