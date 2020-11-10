# 이중 for문으로는 풀 수 없는 문제
# 복잡도를 O(n)으로 줄여서 풀어야 한다.
# 접근 방법을 다시 생각하도록 해야 함

def solution(gems):
    answer = []
    return answer

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

gems = ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]
print(solution(gems))