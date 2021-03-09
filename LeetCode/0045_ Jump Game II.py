'''
Given an array of non-negative integers nums, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

You can assume that you can always reach the last index.

그리디로 푸는 방법
이분 탐색으로 푸는 방법
dp로 푸는 방법

'''

'''
# 시간제한 초과가 걸린 코드 ( 재귀 )

class Solution:
    def jump(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return 0

        global min_count, is_crossed
        min_count = len(nums)
        is_crossed = False

        def cross(idx, cnt):
            global min_count, is_crossed

            for i in range(idx + 1, idx + nums[idx] + 1):

                if i >= len(nums) - 1:
                    min_count = min(min_count, cnt)
                    is_crossed = True
                    break
                else:
                    cross(i, cnt + 1)

        cross(0, 1)
        return min_count if is_crossed else 0

'''