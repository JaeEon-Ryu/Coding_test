n = int(input())

global result
result = 0
nums = []

# 아름다운 숫자인지 판별
def is_a_beatiful_number():

    idx = 0

    while idx < len(nums):
        # 현재 숫자 뽑기
        curr_num = nums[idx]

        # 뽑은 숫자의 크기만큼 동일한 숫자가 있는지 확인
        for i in range(curr_num):

            # 인덱스 에러 or 다른 숫자일 경우
            if idx+i >= len(nums) or curr_num != nums[idx+i]:
                return False

        idx += curr_num

    return True


def find_num(cnt):
    global result

    if cnt == n:
        if is_a_beatiful_number():
            result += 1
        return

    for i in range(1,5): # 1부터 4 사이의 숫자들
        nums.append(i)
        find_num(cnt+1)
        nums.pop()

find_num(0)
print(result)
