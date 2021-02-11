'''
시간 복잡도를 줄였지만 정확성, 효율성 둘 다 전보다 떨어졌다,,
내일 또 다른방법으로 풀어보아야겠다,,,,,,,,,
'''
#
# def solution(gems):
#
#     start_index,end_index = 0,1
#     unique_gems = len(set(gems))
#
#     start_size_up_flag = False
#     while start_index <= len(gems) and end_index <= len(gems):
#
#         if start_size_up_flag:
#             start_index += 1
#             if len(set(gems[start_index:end_index])) != unique_gems:
#                 break
#         else:
#
#             if len(set(gems[start_index:end_index])) == unique_gems:
#                 start_size_up_flag = True
#             else:
#                 end_index += 1
#
#     return [start_index,end_index]

# 시간초과가 난 코드
# def solution(gems):
#
#     unique_gems = set(gems)
#     mininum = 100001
#     sp,ep = 0,0
#
#     for position in range(0,len(gems)-len(unique_gems)):
#         idx_plus = 0
#         unique_gems_copy = unique_gems.copy()
#         #print(unique_gems_copy)
#         while unique_gems_copy:
#             #print(unique_gems_copy)
#             if mininum < idx_plus : # 불필요한 계산을 줄이기 위함
#                 break
#             else:
#                 if position + idx_plus > len(gems) - 1:
#                     break
#                 else:
#                     gem = gems[position+idx_plus]
#                     if gem in unique_gems_copy:
#                         unique_gems_copy.remove(gem)
#                     idx_plus += 1
#
#         #print(mininum," ",idx)
#         if len(unique_gems_copy)==0 and mininum > idx_plus:
#             mininum = idx_plus
#             sp = position + 1
#             ep = position + idx_plus
#             #print(sp," ",ep)
#
#     return [sp,ep]
gems = ["ZZZ", "YYY", "NNNN", "YYY", "BBB"]
#gems = ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]
print(solution(gems))