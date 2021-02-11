
def solution(msg):
    answer = []
    str_dict = dict()

    # 사전 만들기
    i = 1
    while chr(ord('A') + i - 1) <= 'Z':
        str_dict[chr(ord('A') + i - 1)] = i
        i += 1

    # 새로운 색인번호 저장
    w,c = 0,2
    while c < len(msg)+1:
        if msg[w:c] not in str_dict:
            str_dict[msg[w:c]] = len(str_dict) + 1 # 사전 추가 (w + c)
            answer.append(str_dict[msg[w:c-1]]) # w 색인 저장
            w = c - 1

        c += 1

    answer.append(str_dict[msg[w:c]])
    return answer

print(solution('KAKAO'))