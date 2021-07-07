# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N, P, Q):
    # write your code in Python 3.6
    result = []
    semiprimes = [0 for _ in range(N + 1)]
    flags = [0 for _ in range(N + 1)]

    for i in range(2, N + 1):
        for j in range(i, int(N / i) + 1):
            num1 = semiprimes[i]
            num2 = semiprimes[j]

            if num1 == 0 and num2 == 0:
                semiprimes[i * j] += 1
            elif num1 == 0 or num2 == 0:
                semiprimes[i * j] += 2

    flags[0] = semiprimes[0]

    for idx, semi in enumerate(semiprimes[1:]):
        if semi == 1:
            flags[idx + 1] = flags[idx] + 1
        else:
            flags[idx + 1] = flags[idx]

    for p, q in zip(P, Q):
        result.append(flags[q] - flags[p - 1])

    return result