# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, B):
    # write your code in Python 3.6
    max_num = 2 ** 30
    fibo = [0, 1, 2]

    for i in range(3, max(A) + 1):
        fibo.append((fibo[i - 1] + fibo[i - 2]) % max_num) # big integer 제한

    result = []
    for a, b in zip(A, B):
        result.append(fibo[a] % (2 ** b))

    return result



