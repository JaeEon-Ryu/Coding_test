'''
풀이방법
내림차순으로 정렬 후 그 리스트를 반복문으로 참조 ( 최댓값 << works[0] )
1. 거기서 최댓값 기준 같은 숫자들은 모두 -1 시키며 n 또한 -1 시킴
2. 해당 최댓값보다 숫자가 작다면 다시 맨처음 숫자로 돌아가서 최대값 갱신
마찬가지로 1의 과정을 반복 ( n이 0이 될때까 )

'''
def solution(n, works):
    answer = 0
    if sum(works) <= n:
        return 0

    works.sort(reverse=True)
    idx = 0
    current_max = works[0]

    while n > 0:
        if idx == len(works) or works[idx] < current_max:
            idx = 0  # 인덱스 최초 위치로
            current_max = works[idx] # 최댓값 갱신
        elif works[idx] == current_max:
            works[idx] -= 1
            n -= 1
            idx += 1

    for w in works:
        answer += w ** 2

    return answer

''' 시간초과
def solution(n, works):
    answer = 0
    if sum(works) <= n :
        return 0

    works.sort(reverse=True)
    for i in range(n):
        works[works.index(max(works))] -=1
    
    for i in works:
        answer += i**2
    
    return answer
'''

n = 4
works = [4,3,3]
print(solution(n,works))