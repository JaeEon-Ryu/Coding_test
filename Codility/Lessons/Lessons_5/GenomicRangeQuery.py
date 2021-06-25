# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S, P, Q):
    # write your code in Python 3.6
    result = []
    for i in range(len(P)):
        l, r = P[i], Q[i] + 1
        reduced = S[l:r]
        minimun = 5

        if 'A' in reduced:
            current = 1
        elif 'C' in reduced:
            current = 2
        elif 'G' in reduced:
            current = 3
        else:
            current = 4

        if minimun > current:
            minimun = current

        result.append(minimun)

    return result

    # mapper = {
    #     'A': 1,
    #     'C': 2,
    #     'G': 3,
    #     'T': 4
    # }
    #
    # converted_list = []
    # for s in S:
    #     converted_list.append(mapper[s])
    #
    # result = []
    # for p, q in zip(P, Q):
    #     result.append(min(converted_list[p:q + 1]))
    #
    # return result

