# 정해진 총액 이하에서 가능한 한 최대의 총 예산
# 1. 모든 요청 배정가능 -> 요청 금액 그대로
# 2. 모든 요청 배정불가 -> 특정한 정수 상한액 계산,
# 	그 이상인 예산요청 -> 상한액으로 배정
# 	그 이하의 예산요청 -> 요청 금액 그대로
#
#
# 120, 110, 140, 150
# 485
#
# 120, 110, 127, 127
# -> 484
#
# 합의점을 찾을 때 까지 무한반복
#
#
# 1 1 8 8
# 12
# -> 5
#
# 어떠한 알고리즘을 쓸 것인가?
# 이분탐색.
#
# budgets 원소들의 합이 M이하이면서 제일 가까워야 함
#
# 다시 돌아가서
# 120, 110, 140, 150
# 485
# 의 경우에서
# 485를 원소 개수인 4로 나눔 -> 121.xxxx
# 여기서. 121이하는 그대로 씀.
# 121이상 넘어가는 숫자들을 수정하는데 모두 같은 숫자로
# M에 도달하도록 바꿈
#
#
# def solution(budgets, M):
#     if sum(budgets) <= M: return budgets[len(budgets) - 1]
#     answer = 0
#     avg_M = int(M / len(budgets))
#     below_avg = 0
#     cnt = 0
#     for i in budgets:
#         if i <= avg_M:
#             cnt += 1
#             below_avg += i
#     M -= below_avg
#     answer = int(M / (len(budgets) - cnt))
#
#     return answer
#
# -> 당연히 틀림
# (막무가내로 쓴 끼워맞추기 알고리즘 )
#
#
# [1, 1, 1, 50], 20, 17
# [5, 2, 5, 2], 10, 3
#
# ------------------------------------
#
# M = 485
# 무엇을 이분탐색으로 찾을 것인가?
# budgets -> 정렬 후 탐색
# 110 120 140 150
# 중간값 -> 130
# 여기서 130 아래의 값들, 즉 110 120은 그냥
# 두고 나머지 윗값들은 130으로 변경
# 계산을 했을 경우 110 120 130 130 이므로
# 합은 490임. 따라서 총 예산인 M보다 5가 더 큼
# 총 예산을 초과하므로
# 중간 값은 더 내려가야 함.
# 다시. r = mid -1로 설정
# mid = (l+r)/2 으로 할 것


def solution(budgets, M):
    answer = 0
    budgets.sort()
    L, R = 0, budgets[-1]

    while L <= R:
        mid = (L + R) // 2
        sum_budgets = 0

        for value in budgets:
            if value > mid:
                sum_budgets += mid
            else:
                sum_budgets += value

        if sum_budgets <= M:
            L = mid + 1
            answer = mid
        else:
            R = mid - 1

    return answer