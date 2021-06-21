# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6

    element = 1
    for num in sorted(A):
        if element != num:
            return element
        element += 1

    return element
