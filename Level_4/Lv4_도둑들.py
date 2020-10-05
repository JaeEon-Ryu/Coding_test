money = [1,2,3,1]

def solution(money):

    case1 = find_max(money[:-1])
    case2 = find_max(money[1:])
    return max(case1,case2)

def find_max(money):
    can_get = False
    value1,value2,current_max = 0,0,0

    for start_point in money:
        if can_get:
            if start_point + value1 > value2:
                current_max = start_point + value1
            else :
                current_max = value2
                can_get = False
        else:
            current_max = start_point + value2
            can_get = True
        value1 = value2
        value2 = current_max
    return current_max


print(solution(money))

# money = [1,1,1,1,1,1]
#
# def getMax(money):
#     print('**********')
#     print('money = ',money)
#     isget = False
#     first = 0
#     second = 0
#     cur_num = 0
#
#     for m in money:
#         print('-----------------------')
#         print('isget = ',isget)
#         print('m = ',m)
#         if isget:
#             if m + first > second:
#                 cur_num = m + first
#             else:
#                 cur_num = second
#                 isget = False
#         else:
#             cur_num = m + second
#             isget = True
#
#         first = second
#         second = cur_num
#         print('first = ', first)
#         print('second = ', second)
#         print('cur_num = ', cur_num)
#
#     return second
#
#
# def solution(money):
#     withFirst = getMax(money[:-1]) # 마지막x
#     withoutFirst = getMax(money[1:]) # 마지막까지
#     return max(withFirst, withoutFirst)
#
# print(solution(money))
#
#
# # a = 1
# #
# # def aa(a):
# #     a+=5
# #     return a
# # print(aa(a))
#
# # def calNums(base, *nums):
# #     total = 1
# #     for i in nums:
# #         for j in range(i):
# #             total *= base
# #         print(f'{base}의 {i} 제곱 값은 {total}이다.')
# #
# # calNums(5, 1, 2, 3)
# # calNums(2, 2, 4, 6, 8, 10)