def solution(dirs):
    answer = 0
    x,y = 0,0
    visited = []

    for dir in dirs:
        # transfer_info에 기존xy,에서 바뀐xy로
        tranfer_info = ''

        if dir == "U":
            if y+1 > 5:
                continue
            y += 1
            tranfer_info = str(x) + str(y-1) + str(x) + str(y)

        elif dir == "D":
            if y-1 < -5:
                continue
            y -= 1
            tranfer_info = str(x) + str(y) + str(x) + str(y+1)

        elif dir == "L":
            if x-1 < -5:
                continue
            x -= 1
            tranfer_info = str(x) + str(y) + str(x+1) + str(y)

        else:
            if x+1 > 5:
                continue
            x += 1
            tranfer_info = str(x-1) + str(y) + str(x) + str(y)

        if tranfer_info not in visited:
            visited.append(tranfer_info)
            answer += 1

    return answer

dirs = 'ULURRDLLU'
print(solution(dirs))