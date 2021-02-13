import sys

n = int(input())

lines = [
    list(map(int,input().split()))
    for _ in range(n)
]
lines.sort()
idx = []

# 겹치지 않는 선분들인지 확인
def is_not_overlapped():

    base = 0 # 비교대상

    for i in idx:
        x1,x2 = lines[i][0], lines[i][1] # 선분 하나

        if base >= x1:
            return False

        base = x2

    return True

# 선분 고르기 ( n개중 m개 뽑기 )
def choice_the_line(curr_num,cnt):

    if curr_num == n:
        if cnt == m:
            if is_not_overlapped():
                print(len(idx))
                sys.exit()

        return

    idx.append(curr_num)
    choice_the_line(curr_num+1,cnt+1)
    idx.pop()

    choice_the_line(curr_num+1,cnt)


m = n
while m >= 1 : # n 개중 m개 뽑기 개수 줄여나가기
    choice_the_line(0,0)
    m -= 1
