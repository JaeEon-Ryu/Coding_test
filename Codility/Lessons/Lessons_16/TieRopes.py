# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(K, A):
    # write your code in Python 3.6
    curr_sum = 0
    result = 0

    for num in A:
        curr_sum += num
        if curr_sum >= K:
            result += 1
            curr_sum = 0

    return result