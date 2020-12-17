def solution(n, results):
    answer = 0
    winner = dict()
    loser = dict()

    for i in range(1,n+1):
        winner[i] = []
        loser[i] = []

    for A,B in results:
        winner[A].append(B)
        loser[B].append(A)


    for i in range(1, n+1):
    # i에게 승리한 사람은 i가 이긴 사람에게도 승리

        for win in loser[i]:
            if winner[i]:
                for w in winner[i]:
                    if w not in winner[win]:
                        winner[win].append(w)

        for lose in winner[i]:
            if loser[i]:
                for l in loser[i]:
                    if l not in loser[lose]:
                        loser[lose].append(l)

    for i in range(1, n+1):
        if len(winner[i]) + len(loser[i]) == n - 1:
            answer += 1

    return answer

n = 5
results = [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]
print(solution(n,results))

'''
다른 사람의 코드 
배울점 
-> defaultdict(set)
-> set을 이용한 중복처리 -> update()로 한꺼번에 추가
-> 리스트에도 extend가 있지만 중복제거를 할 수 있는 set()자료형을 이용했다는 점

from collections import defaultdict
def solution(n, results):
    answer = 0
    win, lose = defaultdict(set), defaultdict(set)
    for result in results:
            lose[result[1]].add(result[0])
            win[result[0]].add(result[1])

    for i in range(1, n + 1):
        for winner in lose[i]: win[winner].update(win[i])
        for loser in win[i]: lose[loser].update(lose[i])

    for i in range(1, n+1):
        if len(win[i]) + len(lose[i]) == n - 1: answer += 1
    return answer

'''