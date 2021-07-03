# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N):
    # write your code in Python 3.6
    result = 0
    for n in range(1, int(N ** 0.5) + 1):
        quotient, remainder = divmod(N, n)
        if remainder == 0:
            if n != quotient:
                result += 2
            else:
                result += 1

    return result

