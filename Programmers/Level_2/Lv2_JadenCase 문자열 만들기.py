def solution(s):
    answer = ''
    upper_signal = True

    for str in s.lower():
        if str == ' ':
            answer += ' '
            upper_signal = True
        else:
            if upper_signal:
                answer += str.upper()
                upper_signal = False
            else:
                answer += str

    return answer

s = "3people unFollowed me for the last week"
print(solution(s))

'''
def solution(s):
    return ' '.join([word.replace(word[0],word[0].upper(),1) for word in s.lower().split()])
원래 코드는 이런식으로 짰었는데 계속 런타임 에러가 났다.
알아보니 공백이 여러개일수도 있다는 말에 그냥 문자 하나하나를 보는식으로 고쳤다.
'''