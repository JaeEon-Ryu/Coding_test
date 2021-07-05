# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    peaks = []
    len_A = len(A)

    # peak들 구하기
    for i in range(1, len_A - 1):
        if A[i - 1] < A[i] > A[i + 1]:
            peaks.append(i)

    # block 개수를 구하고 block 슬라이스
    for i in range(len(peaks), 0, -1):
        if len_A % i == 0:
            len_block = len_A // i
            block = [False for _ in range(i)]
            cnt = 0

            # peak가 어디에 포함되는지 계산
            for j in range(len(peaks)):
                idx = peaks[j] // len_block
                if block[idx] == False:
                    block[idx] = True
                    cnt += 1

            if cnt == i:
                return cnt

    return 0