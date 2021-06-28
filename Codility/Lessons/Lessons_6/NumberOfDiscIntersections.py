# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    disc = []
    for i, d in enumerate(A):
        disc.append((i - d, -1))
        disc.append((i + d, 1))

    disc.sort()
    t,r = 0,0

    for d in disc:
        if d[1] == 1:
            t -= 1
        else:
            r += t
            t += 1

            if r > 10000000:
                return -1

    return r
