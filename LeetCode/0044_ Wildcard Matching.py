def isMatch(s = 'acdcb',p='a*c?b'):

    # reference : StefanPochmann

    def find(s, p):
        for i in range(len(s) - len(p) + 1):
            if all(p[j] in (s[i + j], '?') for j in range(len(p))):
                return i
        return -1

    parts = p.split('*')

    # '*' 가 하나도 없을 때
    if len(parts) == 1:
        return len(s) == len(p) and find(s, p) >= 0

    print(find(s,parts[0]))
    if find(s, parts[0]) != 0:
        return False

    s = s[len(parts.pop(0)):]
    n = len(s) - len(parts[-1])
    if find(s[n:], parts.pop()) != 0:
        return False

    s = s[:n]
    for part in parts:
        index = find(s, part)
        if index < 0:
            return False
        s = s[index + len(part):]


    return True

    '''
    if len(s) - p.count('*') < len(p) - p.count('*'):
        return False

    possible_match = False
    q_mark = 0
    # 'abcd' , '???d' , '?d?'
    for m in p:  # match_char
        if m == '*':
            possible_match = True
            continue
        elif m == '?':
            q_mark += 1
            if s:
                if possible_match:
                    possible_match = False
            else:
                return False
        else:
            if s:
                if possible_match:
                    if m in s:
                        s = s[s.index(m)+1:]
                        possible_match = False
                    else:
                        return False
                else:
                    if s[0] == m:
                        s = s[1:]
                    else:
                        return False
            else:
                return False

    print(s)
    return True if not s or possible_match else 
    '''

print(isMatch())