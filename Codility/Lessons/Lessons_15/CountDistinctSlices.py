# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(M, A):
    # write your code in Python 3.6
    result,pre_idx = 0,-1
    idx_mapper = [-1 for _ in range(M+1)]

    for i,num in enumerate(A):
        if idx_mapper[num] > pre_idx:
            pre_idx = idx_mapper[num]
        result += i - pre_idx
        idx_mapper[num] = i

        if result >= 1000000000 :
            return 1000000000

    return result

# # you can write to stdout for debugging purposes, e.g.
# # print("this is a debug message")
#
# def solution(M, A):
#     # write your code in Python 3.6
#     idx_mapper = dict()
#     A.append(A[-1])
#     result, curr, curr_sum = 0, 0, 0
#
#     for i, num in enumerate(A):
#         if idx_mapper.get(num) != None:
#             result += curr_sum
#             curr = i - idx_mapper[num]
#             curr_sum = curr
#         else:
#             curr += 1
#             curr_sum += curr
#         idx_mapper[num] = i
#
#         if result >= 1000000000:
#             return 1000000000
#
#     return result
