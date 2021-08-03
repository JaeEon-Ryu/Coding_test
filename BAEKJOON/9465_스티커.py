'''
50 10 100 20 40
30 50 70  10 60

50 40  200 140 250
30 100 120 210 260
'''

T = int(input())

for _ in range(T):

    n = int(input())
    stickers = []
    stickers.append([0,0] + list(map(int,input().split())))
    stickers.append([0,0] + list(map(int, input().split())))

    for j in range(2,n+2):
        stickers[0][j] += max(stickers[1][j - 1], stickers[1][j - 2])
        stickers[1][j] += max(stickers[0][j - 1], stickers[0][j - 2])

    print(max(stickers[0][n+1],stickers[1][n+1]))