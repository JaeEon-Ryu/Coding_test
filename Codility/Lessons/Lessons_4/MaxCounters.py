# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N, A):
    # write your code in Python 3.6
    # result = [0 for i in range(N)]
    # max_val = 0
    # for num in A:
    #     if num > N:
    #         result = [max_val for i in range(N)]
    #     else:
    #         result[num-1] += 1
    #         max_val = max(max_val,result[num-1])
    #
    # return result

    result = [0 for i in range(N)]
    prev_max,next_max = 0,0
    for num in A:
        if num > N:
            prev_max = next_max
        else:
            result[num - 1] = max(result[num - 1] + 1, prev_max + 1)
            next_max = max(result[num - 1], next_max)

    return [prev_max if n < prev_max else n for n in result]