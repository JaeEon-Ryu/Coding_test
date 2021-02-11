'''
ex) 23시 8분일 경우, 문제에서는 23:08이 아닌 23:8
따라서 콜론 (' : ')을 기준으로 시간을 재정의함
'''


result = input()

for idx,t in enumerate(result):
    if t == ':':
        result = str(int(result[:idx]) + 1) + result[idx:]
        break

print(result)