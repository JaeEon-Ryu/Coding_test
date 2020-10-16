def solution(s):

    if len(s) !=4 and len(s) !=6:
        return False

    for chr in s:
        if not(ord(chr) >= 47 and ord(chr) <= 57) :
            return False

    return True


'''눈여겨 볼 만한 다른 사람의 풀이
def alpha_string46(s):
    return s.isdigit() and len(s) in (4, 6)
'''