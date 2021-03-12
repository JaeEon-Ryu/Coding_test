'''
The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle.

Each solution contains a distinct board configuration of the n-queens' placement,
where 'Q' and '.' both indicate a queen and an empty space, respectively.
'''

def solveNQueens(n=5):

    def can_arrange(p,x,y):
        dx,dy = [-1,-1,-1,0,0,1,1,1],[-1,0,1,-1,1,-1,0,1] # 8 directions
        for i in range(8):
            new_x,new_y = x+dx[i],y+dy[i]

            while 0 <= new_x < len(p) and 0 <= new_y < len(p):
                if p[new_x][new_y] == 'Q':
                    return False
                new_x,new_y = new_x + dx[i], new_y + dy[i]

        return True


    def insert_Q(p,i,j):
        helper = list(p[i])  # making starting point
        helper[j] = 'Q'
        p[i] = ''.join(helper)

    def arrange_Q(p): # p = puzzle
        for i in range(1,len(p)):
            for j in range(len(p)):
                if can_arrange(p,i,j):
                    insert_Q(p, i, j)

    def count_Q(p):
        cnt = 0
        for i in range(len(p)):
            cnt += p[i].count('Q')
        return cnt

    result = []
    for i in range(n+2):
        for j in range(i):
            puzzle = ['.' * i] * i
            insert_Q(puzzle,0,j)
            arrange_Q(puzzle)

            if count_Q(puzzle) == n:
                result.append(puzzle)

        if result:
            break

    for r in result:
        print(r)

    return result

solveNQueens()



'''
output
[["Q....","..Q..","....Q",".Q...","...Q."],
[".Q...","...Q.","Q....","..Q..","....Q"],
["..Q..","Q....","...Q.",".Q...","....Q"],
["...Q.","Q....","..Q..","....Q",".Q..."]]

expected
[["Q....","..Q..","....Q",".Q...","...Q."],
["Q....","...Q.",".Q...","....Q","..Q.."],
[".Q...","...Q.","Q....","..Q..","....Q"],
[".Q...","....Q","..Q..","Q....","...Q."],
["..Q..","Q....","...Q.",".Q...","....Q"],
["..Q..","....Q",".Q...","...Q.","Q...."],
["...Q.","Q....","..Q..","....Q",".Q..."],
["...Q.",".Q...","....Q","..Q..","Q...."],
["....Q",".Q...","...Q.","Q....","..Q.."],
["....Q","..Q..","Q....","...Q.",".Q..."]]

'''