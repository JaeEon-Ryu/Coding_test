def solution(s):
    p_cnt = s.count('p') + s.count('P')
    y_cnt = s.count('y') + s.count('Y')

    if p_cnt != y_cnt:
        return False
    else:
        return True

'''다른 사람 풀이
def numPY(s):
    return s.lower().count('p') == s.lower().count('y')
'''