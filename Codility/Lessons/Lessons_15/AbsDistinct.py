# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    distinct_num = set()
    for num in A:
        distinct_num.add(abs(num))

    return len(distinct_num)