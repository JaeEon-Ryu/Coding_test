# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    A.append(0)
    idx_of_0 = []
    num_of_1 = 0
    result = 0

    # 전처리 : 첫 시작이 0이 되게끔
    for i in range(len(A)):
        if A[i] == 0:
            A = A[i:]
            break

    # 0이 있는 위치 얻기, 1의 개수 count
    for i in range(len(A)):
        if A[i] == 0:
            idx_of_0.append(i)
        else:
            num_of_1 += 1

    # 현재 0의 위치에서 다음 0의 위치로 넘어갈 때, 1의 개수 더하기 그리고 넘어간 인덱스만큼 1의 개수 빼기
    for i in range(len(idx_of_0) - 1):
        result += num_of_1
        if result > 1000000000:
            return -1
        num_of_1 -= (idx_of_0[i + 1] - idx_of_0[i] - 1)

    return result
