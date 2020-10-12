def solution(s):
    num_list = [int(x) for x in s.split()]
    return str(min(num_list)) + ' ' + str(max(num_list))

print(solution("-1 -2 -3 -4"))