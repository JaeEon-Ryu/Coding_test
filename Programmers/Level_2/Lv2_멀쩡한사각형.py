import math
def solution(w,h):
    answer = w * h - (w + h - math.gcd(w,h))
    return answer

w = 8
h = 12
print(solution(w,h))