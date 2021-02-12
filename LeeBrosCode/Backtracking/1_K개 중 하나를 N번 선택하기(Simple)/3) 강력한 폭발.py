n = int(input())
grid = [
    list(map(int,input().split()))
    for _ in range(n)
]

# 폭탄 종류에 따른 위치 변경 값
mapper = {1: [[0,-2, -1, 1, 2], [0,0, 0, 0, 0]],
          2: [[0,-1,0,1,0],[0,0,1,0,-1]],
          3: [[0,-1,-1,1,1],[0,-1,1,-1,1]]}

def in_range(x,y):
    return 0 <= x < n and 0 <= y < n

# 격자 안에 있는 1의 개수 세기
def count_1(grid):
    cnt = 0

    for row in grid:
        cnt += row.count(1)

    return cnt

# 순열 생성
def determine_the_type(cnt):

    if cnt == N:
        explode()
        return

    for i in range(1,4):
        type_of_bomb.append(i)
        determine_the_type(cnt+1)
        type_of_bomb.pop()

# 폭파시키기
def explode():

    global max_val
    idx = 0 # 폭탄 종류를 바꿔주기 위한 인덱스

    temp = [
        [0 for _ in range(n)]
        for _ in range(n)
    ]

    for i in range(n):
        for j in range(n):
            if grid[i][j] == 1:

                # 순열 값에 따라 폭탄 종류 정하기
                bombs_dir = mapper[type_of_bomb[idx]]
                dx,dy = bombs_dir[0], bombs_dir[1]

                # 위치 값 갱신
                for _ in range(5):
                    new_x,new_y = i + dx[_], j + dy[_]

                    if in_range(new_x,new_y):
                        temp[new_x][new_y] = 1

                # 폭탄 종류 바꾸기
                idx += 1

                # 폭발이 끝난 후 값 비교
                areas_affected = count_1(temp)
                max_val = max(max_val,areas_affected)


global max_val
max_val = 0
N = count_1(grid)
type_of_bomb = []

determine_the_type(0)

print(max_val)
