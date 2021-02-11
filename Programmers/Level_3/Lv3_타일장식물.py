# 타일의 개수 N이 주어질 때,
# N개의 타일로 구성된 직사각형의 둘레?
#
# N=5 -> 26
# N=6 -> 42
#
# N은 1이상 80이하인 자연수
#
# N = 1 -> 4
# N = 2 -> 6
# N = 3 -> 10
# N = 4 -> 16
# N = 5 -> 26
# N = 6 -> 42
# N = 7 -> 68
#
# 2 4 6 10 12 16
#
# N = 7 -> 56? -> x
#
# 26 42 -> 68
# ----------------------------------------------------
# solution
# 최초(N=1)에 둘레 4로 정의.
# 다음 단계로 넘어갈 때 마다 제일 긴 변
# (max함수 사용) *3을 한 변수를 더한다.
#
# solution 정정 -> 변의 정보를 갖고 있어야 함. (가로, 세로)
# rectangle(짧은변, 긴변)
# N = 1 -> rectangle(1,1)
# N = 2 -> rectangle(1,2)
# N = 3 -> rectangle(2,3)
# N = 4 -> rectangle(3,5)
# N = 5 -> rectangle(5,8)
#
# solution 정정 :
# recShort -> 짧은 변
# recLong -> 긴 변
#
# 루프가 돌 때마다 :
# 짧은변 = 긴변
# 긴변 = 긴변 + 짧은변
# (중간에 임시로 보관할 temp필요)
#

import math
def solution(N):
    shortSide = 1
    longSide = 1
    for i in range(N-1):
        tempShortSide = shortSide
        shortSide = longSide
        longSide += tempShortSide
    answer = (shortSide + longSide)*2
    return answer
