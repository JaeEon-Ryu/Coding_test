# # 각 stage에 대한 실패율을 구함
# # 모든 실패율을 구했으면 정렬함.
#
# def solution(N, stages):
#     count_stage = dict()
#     stages.sort(reverse=True)
#     people = 0
#
#     for stage in stages:
#         if stage > N : # N보다 클 경우에는 딕셔너리에 추가하지 않는다
#             people += 1
#         else:
#             if stage in count_stage:
#                 count_stage[stage] += 1
#             else:
#                 count_stage[stage] = 1
#
#     for stage in range(N,0,-1):
#         if stage in count_stage:
#             people += count_stage[stage]
#             count_stage[stage] = count_stage[stage] / people
#         else:
#             count_stage[stage] = 0
#
#
#     return count_stage
#
# N = 5
# stages = [2,1,2,6,2,4,3,3]
# print(solution(N,stages))

# '''
# runtime error와 testcase 2개가 틀린 코드
# testcase의 경우 while문을 돌고 맨 마지막 숫자를 추가하는 과정에서
# 생긴 문제 같음 -> 수정 가능
# runtrim error의 경우는 조금 더 찾아봐야할듯, 일단 리스트 인덱스부터
# 조사하여 할당되지 않은 값까지 조사할 예정
# '''
#
# import bisect # 정해진 구간의 인덱스를 얻고 싶을 때 사용한다
#
# def solution(N, stages):
#     answer = []
#     stages.sort()
#     find_N_position = bisect.bisect(stages, N) # N이 들어갈 인덱스 위치
#
#     # N보다 높은 stage가 있는 경우 amount에 미리 저장함
#     amount = len(stages) - find_N_position
#     stages = stages[:find_N_position]
#
#     is_not_cleared = 0
#     #print(stages)
#     while stages:
#         stage = stages.pop()
#         if N != stage:
#             if N-stage != 1:
#                 for _ in range(N-stage-1):
#                     answer.append(0)
#                     N -= 1
#
#             answer.append(is_not_cleared/amount)
#             is_not_cleared = 1
#             N -= 1
#
#         else:
#             is_not_cleared += 1
#
#         amount += 1
#     answer.append(is_not_cleared / amount)
#
#     if N>1:
#         for _ in range(N-1):
#             answer.append(0)
#
#     answer = answer[::-1]
#     answer = sorted(range(len(answer)),key=answer.__getitem__,reverse=True)
#     for _ in range(len(answer)):
#         answer[_] += 1
#
#     return answer
#
# N = 5
# stages = [2,1,2,6,2,4,3,3]
#
# #N = 4
# #stages = [4,4,4,4,4]
# print(solution(N,stages))