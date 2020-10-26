def solution(num):
    answer = 0
    flag = False
    count = 0

    if num == 1:
        return 0

    while count != 500:

        if num%2 == 0:
            num /= 2
        else :
            num = (num*3) + 1

        answer += 1
        count += 1

        if num == 1:
            flag = True
            break

    if flag :
        return answer
    else:
        return -1

print(solution(626331))