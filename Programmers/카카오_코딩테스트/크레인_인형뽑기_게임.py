board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]

def solution(board, moves):
    answer = 0
    basket = []
    for column in moves: # moves만큼 반복
        for row in board: # board의 모든 행을 참조
            if row[column-1] != 0: # 꺼낼것이 있다면
                basket.append(row[column-1]) # 바구니에 추가
                row[column-1] = 0 # 꺼냈던 위치 0으로 할당

                while len(basket) > 1:
                    if basket[-1] == basket[-2]:
                        del basket[-2:]
                        answer += 2
                    else:
                        break

                break

    return answer

print(solution(board,moves))

