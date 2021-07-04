# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    N = len(A)
    peaks = []
    for i in range(1, N - 1):
        if A[i - 1] < A[i] > A[i + 1]:
            peaks.append(i)

    if len(peaks) < 3:
        return len(peaks)

    max_flags_possible = len(peaks)
    while max_flags_possible * (max_flags_possible - 1) > (peaks[-1] - peaks[0]):
        max_flags_possible -= 1

    for k in range(max_flags_possible, 0, -1):
        flags_set = 1
        distance = 0

        for i in range(1, len(peaks)):
            distance += abs(peaks[i - 1] - peaks[i])
            if distance >= k:
                flags_set += 1
                distance = 0

        if flags_set >= k:
            return k

    return 0
