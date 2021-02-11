def solution(m, n, puddles):

    # DP로 구하기 위해서는 특정 셀 기준 왼쪽 셀과 위쪽 셀을 참고해야 하기 때문에
    # 원래 크기보다 1 더크게 만든다.
    path = [[0]*(m+1) for i in range(n+1)]
    path[1][1] = 1 # 출발지 설정

    for i in range(1,n+1):
        for j in range(1,m+1):
            if i==j==1: # 시작점 제외하고 DP 구하기
                continue
            elif [j,i] in puddles:
                path[i][j] = 0
            else:
                path[i][j] = path[i-1][j] + path[i][j-1]

    for i in path:
        print(i)

    return path[n][m]%1000000007

m = 4
n = 3
puddles = [[2,2]]
print(solution(m,n,puddles))