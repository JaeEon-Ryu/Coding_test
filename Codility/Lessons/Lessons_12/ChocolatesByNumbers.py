# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N, M):
    # write your code in Python 3.6
    def gcd(a, b):
        if b == 0:
            return a
        else:
            return gcd(b, a % b)

    num = gcd(N, M)

    return N // num