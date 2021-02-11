# 동적 계획법 사용

def solution(board):
    answer = board[0][0] # 0이나 1로 초기화시 테스트케이스 틀림
    board_dp = board[:]

    for r in range(1,len(board_dp)): # row
        for c in range(1,len(board_dp[0])): #column

            if board_dp[r][c] != 0:
                board_dp[r][c] = min(board_dp[r-1][c],board_dp[r][c-1],board_dp[r-1][c-1]) + 1

                if answer < board_dp[r][c]: #최대값을 뽑기 위함
                    answer = board_dp[r][c]

    return answer**2


board = [[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]]
print(solution(board))