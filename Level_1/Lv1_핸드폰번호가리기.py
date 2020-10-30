def solution(phone_number):
    answer = ''
    for idx,i in enumerate(phone_number):
        if idx < 4:
            answer += '*'
        else:
            answer += i

    return answer

phone_number = "01033334444	"
print(solution(phone_number))