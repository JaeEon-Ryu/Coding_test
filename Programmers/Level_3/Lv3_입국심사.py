
# 결과적으로 시간이 어떻게 찍히는지 다 찍어본다.
# 이분탐색 구조로 처음부터 L <= R 무한루프를 그림
# 기존에 주어진 times라는 리스트의 각 원소로 M을
# 나눈 몫을 case에 중첩하여 더함.
# 여기서 M은 시간이 제일 짧은 경우 + 시간이 제일 긴 경우
# 를 2로 나눈 몫. ( 이분탐색 )

def solution(n, times):
    answer = 0
    L, R = 0, max(times) * n

    while L <= R :
        M = (L + R) // 2
        case = 0
        for time in times:
            case += M // time
        if case >= n:
            answer = M
            R = M - 1
        else :
            L = M + 1
    return answer