# 입력
n,m,k = map(int,input().split())
dists = list(map(int,input().split())) # 턴마다 나아갈 수 있는 거리
dist_index = []

def get_result():
    plate = [1 for _ in range(k)] # 윷놀이 판

    # record score
    for idx,dist in zip(dist_index,dists):
        plate[idx] += dist

    # count score
    cnt = 0
    for p in plate:
        if p >= m :
            cnt += 1

    return cnt

# 인덱스 탐색 순서
def find_order(cnt):
    global max_val

    if cnt == n:
        max_val = max(max_val,get_result())
        return

    for i in range(0,k):
        dist_index.append(i)
        find_order(cnt+1)
        dist_index.pop()

global max_val
max_val = 0
find_order(0)

print(max_val)
