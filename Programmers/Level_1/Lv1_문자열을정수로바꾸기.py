def solution(s):
    if s[0] == '-' : return int(s[1:])*-1
    else : return int(s)

## 그냥 처음부터 int씌워도 된다