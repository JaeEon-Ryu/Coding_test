def solution(people, limit):
    answer = 0
    people.sort()
    L = 0
    R = len(people)-1

    while L<=R:
        if people[L] + people[R] <= limit:
            L += 1
            R -= 1
        else :
            R -= 1
        answer += 1
    return answer

