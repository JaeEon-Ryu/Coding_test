# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(K, M, A):
    # write your code in Python 3.6
    min_block = max(A) # minimal large sum
    sum_block = sum(A)

    if K == 1:
        return sum_block
    if K >= len(A):
        return min_block

    def is_valid(m): # 블록 유효성 검사
        b_sum, b_cnt = 0, 0

        for a in A:
            if b_sum + a > m: # 정해놓은 minimal large sum보다 커진다면 블록 초기화
                b_sum = a
                b_cnt += 1
            else:
                b_sum += a

            if b_cnt >= K:
                return False
        return True

    while (min_block <= sum_block):
        mid = (min_block + sum_block) // 2

        if is_valid(mid):
            sum_block = mid - 1
        else:
            min_block = mid + 1

    return min_block
