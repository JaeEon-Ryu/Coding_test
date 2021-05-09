'''
A peak element is an element that is strictly greater than its neighbors.

Given an integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.

You may imagine that nums[-1] = nums[n] = -∞.
'''

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        return nums.index(max(nums))

        # 혹은 이진탐색 활용  ( ref : OldCoadingFarmer)

    def findPeakElement(self, nums):
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if (mid - 1 < 0 or nums[mid] > nums[mid - 1]) and (mid + 1 >= len(nums) or nums[mid] > nums[mid + 1]):
                return mid
            elif mid - 1 >= 0 and nums[mid] < nums[mid - 1]:  # the opposite of the above "if" are these two "elif"
                r = mid - 1
            elif mid + 1 < len(nums) or nums[mid] < nums[mid + 1]:
                l = mid + 1
        return l