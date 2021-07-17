# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, B):
    # write your code in Python 3.6
    N = len(A)

    if N < 2:
        return N

    result = 1
    end,idx = B[0],1

    while idx < N :

        # end 보다 작은 것 모두 pass
        while idx < N and A[idx] <= end:
            idx += 1

        if idx == N:
            break

        # 갱신
        result += 1
        end = B[idx]

    return result