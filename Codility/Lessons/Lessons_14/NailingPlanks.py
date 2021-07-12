# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, B, C):
    # write your code in Python 3.6
    min_idx = 1
    max_idx = len(C)

    # 유효성 검사
    def is_valid(m):
        largest = max(A + B + C) + 1
        nail = [0 for _ in range(largest)]
        for i in range(m):
            nail[C[i]] = 1
        for i in range(1, largest):
            nail[i] += nail[i - 1]
        for a, b in zip(A, B):
            if nail[b] - nail[a - 1] == 0:
                return False
        return True

    # 이진탐색
    result = -1
    while min_idx <= max_idx:
        mid = (min_idx + max_idx) // 2
        if is_valid(mid):
            max_idx = mid - 1
            result = mid
        else:
            min_idx = mid + 1

    return result
