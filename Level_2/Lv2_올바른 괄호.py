def solution(s):
    left = 0

    for _ in s:
        if _ == "(":
            left += 1
        else:
            left -= 1

        if left < 0 :
            return False

    return left == 0

s = "()()"
print(solution(s))