'''
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
'''

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return 1

        nums.sort()
        max_length, length = 1, 1

        for i in range(len(nums) - 1):
            if nums[i + 1] - nums[i] > 1: # 숫자가 이어지지 않을 때마다
                max_length = max(max_length, length) # 이어졌던 길이 값 비교
                length = 1
            elif nums[i + 1] == nums[i]:
                continue
            else: # 숫자가 이어진다면
                length += 1
        max_length = max(max_length, length) # 남아 있는 값 처리

        return max_length