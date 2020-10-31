def solution(s):
    number_dict = dict()

    num = ''
    for char in s:
        if ord(char)>47 and ord(char)<58:
            num += char
        else:
            if num:
                if num in number_dict:
                    number_dict[num] += 1
                else:
                    number_dict[num] = 1
                num = ''

    answer = [int(i) for i in sorted(number_dict,key = lambda x:number_dict[x],reverse=True)]

    return answer

s = "{{1,2,3},{2,1},{1,2,4,3},{2}}"
print(solution(s))