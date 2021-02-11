# 7
# 3  8
# 8  1  0
# 2  7  4  4
# 4  5  2  6  5
#
# 2행 1열 -> 1행1열 참조
# 2행 2열 -> 1행1열 참조
#
# 3행 1열 -> 2행1열 참조
# 3행 2열 -> 2행1열&2행2열 중 최대값 참조
# 3행 3열 -> 2행2열 참조
#
# 4행 1열 -> 3행1열 참조
# 4행 2열 -> 3행1열&3행2열 중 최대값 참조
# 4행 3열 -> 3행2열&3행3열 중 최대값 참조
# 4행 4열 -> 3행3열 참조
#
# 5행 1열 -> 4행1열 참조
# 5행 2열 -> 4행1열&4행2열 중 최대값 참조
# 5행 3열 -> 4행2열&4행3열 중 최대값 참조
# 5행 4열 -> 4행3열&4행4열 중 최대값 참조
# 5행 5열 -> 4행4열 참조
#
# case1 : 첫번째 값
# case2 : 끝 값
# case3 : 중간 값

def solution(triangle):
    for row in range(1,len(triangle)):
        for column in range(row+1):
            if column == 0:
                triangle[row][column] += triangle[row-1][column]
            elif column == row:
                triangle[row][column] += triangle[row-1][column-1]
            else:
                triangle[row][column] += max(triangle[row-1][column-1],triangle[row-1][column])
    return max(triangle[-1])