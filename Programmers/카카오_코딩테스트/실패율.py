# # 각 stage에 대한 실패율을 구함
# # 모든 실패율을 구했으면 정렬함.

def solution(N, stages):
    count_stage = dict()
    stages.sort(reverse=True)
    people = 0

    # 각 스테이지의 개수를 저장하도록 한다.
    for stage in stages:
        if stage > N : # N보다 클 경우에는 딕셔너리에 추가하지 않는다
            people += 1
        else:
            if stage in count_stage:
                count_stage[stage] += 1
            else:
                count_stage[stage] = 1

    # 각 스테이지에 대한 실패율을 구하며 스테이지가 없을 경우 그곳에 0(실패율0%) 추가
    for stage in range(N,0,-1):
        if stage in count_stage:
            people += count_stage[stage]
            count_stage[stage] = count_stage[stage] / people
        else:
            count_stage[stage] = 0

    # 실패율 기반 답 정렬
    count_stage = sorted(count_stage.items(),key= lambda x:x[0])
    answer = sorted(count_stage,key = lambda x:x[1],reverse=True)

    return [i[0] for i in answer]

N = 5
stages = [2,1,2,6,2,4,3,3]
print(solution(N,stages))

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


'''
본 문제의 답 중 제일 인기있던 코드이다.
나의 경우 단순하게 제일 큰 수에서 작은수로, 
가면 갈수록 인원수를 늘림으로써 실패율을 계산했다.
하지만 아래 코드는 나와 정반대이다. 
확실히 아래 코드로 하면 내 코드보다 훨씬 깔끔하고 간결해보인다.
문제를 해결함에 있어 다양한 측면에서 코드를 보는것이 중요해보인다. 

def solution(N, stages):
    result = {}
    denominator = len(stages)
    for stage in range(1, N+1):
        if denominator != 0:
            count = stages.count(stage)
            result[stage] = count / denominator
            denominator -= count
        else:
            result[stage] = 0
    return sorted(result, key=lambda x : result[x], reverse=True)

'''