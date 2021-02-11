# 123 일 때,  1 st, 1b ->
# answer_possible =
#
# 스트라이크 1이라고 가정
# 볼=3 : 134, 135, 136, 137, 138, 139
# 볼=2 : 142, 152, 162, 172, 182, 192
#
# 스트라이크 3이라고 가정
# 볼=2 : 243, 253, 263, 273, 283, 293
# 볼=1 : 413, 513, 613, 713, 813, 913
#
# 스트라이크 2라고 가정
# 볼=1 : 421, 521, 621, 721, 821, 921
# 볼=3 : 324, 325, 326, 327, 328, 329
#
# ------------------->   총 36가지


# 356 일 때, 1st, 0 b ->
# answer_possible =
#
# 스트라이크 3 이라고 가정
# 312, 314, 315, 316, 317, 318, 319
# 321, 324, ~
# 341, 34
# 스트라이트 5 라고 가정
#
# 스트라이크 6 이라고 가정
#
# 경우의 수 따져가기
# 무식하게 푼다(brute-force)'는
# 컴퓨터의 빠른 계산 능력을 이용해
# 가능한 경우의 수를 일일이 나열하면서
# 답을 찾는 방법을 의미.
# 이렇게 가능한 방법을 전부 만들어 보는
# 알고리즘을 뜻한다.
#
# 완전 탐색 방법 5가지.
# Brute Force : for, if 사용 - 처음부터 끝까지 탐색
# 비트마스크
# 순열 : 순열의 시간 복잡도는 O(N!)
# 백트래킹
# BFS
#
#
# st = 1, 2, 3


def solution(baseball):
    answer = 0

    # 모든 경우의 수 구하기
    for all_num in range(123, 988):
        check = str(all_num)
        if check[0] == check[1] or check[1] == check[2]: continue
        if check[0] == check[2] or '0' in check: continue

        # 야구 게임 횟수만큼 반복
        for i, (question, strike, ball) in enumerate(baseball):
            strike_cnt = 0
            ball_cnt = 0

            # 스트라이크 판별 ( 자리수 비교 )
            for digits in range(3):
                if check[digits] == str(question)[digits]:
                    strike_cnt += 1
            if strike_cnt != strike: break

            # 볼 판별 ( 자리수 비교 )
            for digits in range(3):
                if check[digits] == str(question)[digits - 1]:
                    ball_cnt += 1
                if check[digits] == str(question)[digits - 2]:
                    ball_cnt += 1
            if ball_cnt != ball: break

            # 게임 끝까지 보고 판별해야 하므로
            if i == len(baseball) - 1: answer += 1

    return answer