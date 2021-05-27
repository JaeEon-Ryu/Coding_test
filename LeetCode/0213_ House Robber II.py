'''
You are a professional robber planning to rob houses along a street.
Each house has a certain amount of money stashed. All houses at this place are arranged in a circle.
That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.
'''

class Solution:
    def rob_max(self, nums: List[int]) -> int:
        l = r = 0
        for num in nums:
            l, r = r, max(num + l, r)
        return r

    def rob(self, nums: List[int]) -> int:
        if nums:
            return max(self.rob_max(nums[:-1]), self.rob_max(nums[1:]), nums[0])
        else:
            return 0