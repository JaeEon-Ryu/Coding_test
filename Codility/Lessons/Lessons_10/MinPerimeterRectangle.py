# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N):
    # write your code in Python 3.6
    for n in range(int(N ** 0.5) + 1, 0, -1):
        quotient, remainder = divmod(N, n)  # 몫, 나머지
        if remainder == 0:
            return (n + quotient) * 2

    return 4