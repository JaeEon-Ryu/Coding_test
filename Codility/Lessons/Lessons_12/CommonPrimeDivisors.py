# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

import math

def solution(A, B):
    # write your code in Python 3.6
    def is_same_prime(num1, num2):
        gcd = math.gcd(num1, num2)
        num1_gcd, num2_gcd = 0, 0

        while num1_gcd != 1:
            num1_gcd = math.gcd(num1, gcd)
            num1 //= num1_gcd
        while num2_gcd != 1:
            num2_gcd = math.gcd(num2, gcd)
            num2 //= num2_gcd

        return True if num1 == 1 and num2 == 1 else False

    result = 0
    for a, b in zip(A, B):
        if is_same_prime(a, b):
            result += 1

    return result

