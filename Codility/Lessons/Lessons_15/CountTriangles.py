# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    N = len(A)
    A.sort()
    result = 0

    for i in range(N - 2): # 첫번째 수
        k = i + 2

        for j in range(i + 1, N): # 두번째 수
            while k < N and A[i] + A[j] > A[k]: # 세번째 수 및 조건 걸기
                k += 1
            if k > j:
                result += k - j - 1

    return result