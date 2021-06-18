def solution(N):
    # write your code in Python 3.6

    if N < 3:
        return 0

    # 2진수 11111111111 등을 사전에 제거하기 위함
    Npow_of_2 = 2
    while Npow_of_2 < N:
        Npow_of_2 **= 2
    if Npow_of_2 - 1 == N:
        return 0


    # 맨 처음 나오는 1까지 접근하여 그 다음 인덱스부터 시작하도록 함
    str_N = str(bin(N))[2:]
    start_idx = 0
    for i in range(len(str_N)):
        if str_N == '1':
            start_idx = i
            break
    str_N = str_N[start_idx+1:]


    # 개수 세기, 최대값 찾기
    max_cnt, cnt = 0, 0
    for num in str_N:
        if num == '0':
            cnt += 1
        else:
            max_cnt = max(max_cnt,cnt)
            cnt = 0

    return max_cnt


print(solution(1162))



