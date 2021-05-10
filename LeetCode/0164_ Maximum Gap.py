'''
Given an integer array nums, return the maximum difference between two successive elements in its sorted form. If the array contains less than two elements, return 0.
'''


class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0

        nums = sorted(list(set(nums)))
        max_value = 0
        for i in range(len(nums) - 1):
            max_value = max(max_value, nums[i + 1] - nums[i])

        return max_value
