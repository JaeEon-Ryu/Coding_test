
# [2,4,5,3,2,1,4,2,5,1]
# [1,3,4,2,1,0,3,1,4,0]
# [0,2,3,1,0,-1,2,0,3,-1]
# [-1,1,2,0,-1,-2,1,-1,2,-2]
# 리스트 내 숫자들 1 보다 작은 것 연속 -> k개 된다면 못지나감

def can_crossing(stones, k, mid):
    accumulation = 0

    for stone in stones:
        if stone-mid < 1:
            accumulation += 1
            if accumulation == k:
                return False
        else:
            accumulation = 0

    return True


def solution(stones, k):
    answer = 0

    L = 0
    R = 200000000

    while L <= R:
        mid = (L + R) // 2

        if can_crossing(stones, k, mid):
            L = mid + 1
        else:
            R = mid - 1

    return L



# # 시간초과가 났음
# # 코드 리팩도링 필요
#
# def solution(stones, k):
#     answer = 0
#     crossingable = True
#     stones.insert(0,'start')
#     stones.append('end')
#
#     while crossingable: # 몇바퀴째 돌고 있는지
#         position = 0
#         crossing = True
#
#         while crossing: # 건너는 중
#             position += 1
#
#             if stones[position] == 'end': # 끝까지 도착
#                 answer += 1
#                 break
#             elif stones[position] < 1: # 1칸 넘게 건너야 할 때
#
#                 release = 0
#                 for bonus in range(1,k):
#                     position += 1
#                     crossingable = False
#
#                     if stones[position] == 'end':
#                         crossingable = True
#                         crossing = False
#                         answer += 1
#                         break
#
#                     if stones[position] > 0:
#                         stones[position] -= 1
#                         crossingable = True
#                         break
#                     else :
#                         release += 1
#
#                 if release+1 == k :
#                     break
#
#
#             else: # 1칸만 건널 때
#                 stones[position] -= 1
#
#     return answer

stones = [2, 4, 5, 3, 2, 1, 4, 2, 5, 1]
k = 3
print(solution(stones,k))
