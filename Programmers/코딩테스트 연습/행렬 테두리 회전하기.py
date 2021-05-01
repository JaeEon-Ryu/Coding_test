def solution(rows, columns, queries):
    answer = []
    grid = [
        [j+(columns*i) for j in range(1,columns+1)]
        for i in range(rows)
    ]

    def rotate(sx,sy,ex,ey): # start_x, start_y, end_x, end_y
        dx,dy = [0,1,0,-1],[1,0,-1,0]
        x,y = sx,sy
        dir = 0

        def in_range(x, y):
            return sx<=x<=ex and sy<=y<=ey

        min_value = temp = grid[x][y]
        while True:
            new_x, new_y = x+dx[dir],y+dy[dir]

            if not in_range(new_x,new_y):
                dir += 1
                new_x,new_y = x+dx[dir],y+dy[dir]

            # 최소값 찾기
            min_value = min(min_value, grid[new_x][new_y])

            # 값 교체
            temp2 = grid[new_x][new_y]
            grid[new_x][new_y] = temp
            temp = temp2

            # 좌표값 수정
            x,y = new_x,new_y

            # 한바퀴 다 돌았다면 정지
            if new_x == sx and new_y == sy:
                break

        answer.append(min_value)
        return

    for start_x,start_y,end_x,end_y in queries:
        rotate(start_x-1,start_y-1,end_x-1,end_y-1)

    return answer

print(solution(6,6,[[2,2,5,4],[3,3,6,6],[5,1,6,3]]))