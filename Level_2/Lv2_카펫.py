# brown = 2(X+Y) + 4
# yellow = X * Y

def solution(brown, yellow):

    for X in range(1, int(yellow ** 0.5) + 1):
        if yellow % X == 0:
            Y = yellow // X

            if 2*X + 2*Y + 4 == brown: # 값 맞는지 확인
                return [Y + 2, X + 2]


b = 10
y = 2
print(solution(b,y))