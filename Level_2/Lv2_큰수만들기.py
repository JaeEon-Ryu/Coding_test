def solution(number, k):
    answer = ''
    answer_list = []
    answer_list.append(number[0])
    for num in number[1:]:
        while  len(answer_list) > 0 and answer_list[-1] < num and k > 0 :
            k -= 1
            answer_list.pop()
        answer_list.append(num)

    if k != 0:
        answer_list = answer_list[:-k]

    answer = ''.join(answer_list)
    return answer