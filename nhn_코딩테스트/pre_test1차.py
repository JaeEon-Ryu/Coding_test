matrix_len = int(input())
matrix = []

# 입력
for i in range(matrix_len):
    matrix.append(list(map(int,input().split())))

is_explored = []
size_of_area = []
global size

def find_in_four_direction(li,r,c): # 4가지방향 인접한 원소 찾기
    global size
    try :
        if li[r+1][c] == 1 :
            if str(r+1)+str(c) not in is_explored:
                is_explored.append(str(r+1)+str(c))
                size += 1
                find_in_four_direction(li, r+1, c)
    except:
        pass

    try :
        if r-1 > 0 :
            if li[r-1][c] == 1 :
                if str(r-1)+str(c) not in is_explored:
                    is_explored.append(str(r-1)+str(c))
                    size += 1
                    find_in_four_direction(li, r-1, c)
    except:
        pass

    try :
        if li[r][c+1] == 1 :
            if str(r)+str(c+1) not in is_explored:
                is_explored.append(str(r)+str(c+1))
                size += 1
                find_in_four_direction(li, r, c+1)
    except:
        pass

    try :
        if c-1 > 0 :
            if li[r][c-1] == 1 :
                if str(r)+str(c-1) not in is_explored:
                    is_explored.append(str(r)+str(c-1))
                    size += 1
                    find_in_four_direction(li, r, c-1)
    except:
        pass


for i,row in enumerate(matrix):
    for j,element in enumerate(row):

        if element == 1:
            if str(i)+str(j) not in is_explored: # 탐색이 되지 않았을 경우

                size = 1
                is_explored.append(str(i)+str(j))
                find_in_four_direction(matrix, i, j)
                size_of_area.append(size)

# 출력

if size_of_area:
    size_of_area.sort()
    print(len(size_of_area))

    area_str = ''
    for idx,s in enumerate(size_of_area):
        if idx == len(size_of_area) - 1 : area_str += str(s)
        else :  area_str += str(s) + ' '
    print(area_str)
else:
    print(0)
