# lost 혹은 reserve의 크기가 0이 된다면 루프 해제

# 1 3 5 -> 0 2 2 4 4 6
# 1 3 5

# lost에서
# 2, 4일 때 -> 1, 2, 3 , 3,4, 5 로 변경
# ( 숫자는 여섯개지만 실질적 2개 )
# reserve 에서 1, 3, 5 일 때
# lost의 temp list에서 3개를 없애주어 1개가 남음

def solution(n, lost, reserve):
    answer = n - len(lost)
    for R in reserve:
        for L in lost:
            if L == R :
                reserve.remove(R)
                lost.remove(L)
                answer += 1

    for R in reserve:
        for L in lost:
            if L >= R - 1 and L <= R + 1 :
                lost.pop(lost.index(L))
                answer += 1
                break

    return answer


# 정답이긴 한데 시간복잡도가 너무 높다