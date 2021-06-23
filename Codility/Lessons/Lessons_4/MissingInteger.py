# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    result = 1
    A = sorted(list(set(A)))
    for num in A:
        if num < 1:
            continue

        if result == num:
            result += 1
        else:
            return result

    return result



