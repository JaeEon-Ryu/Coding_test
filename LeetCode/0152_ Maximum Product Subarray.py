'''
Given an integer array nums, find a contiguous non-empty subarray within the array that has the largest product, and return the product.

It is guaranteed that the answer will fit in a 32-bit integer.

A subarray is a contiguous subsequence of the array.
'''
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        '''
        reference : bindloss
        '''
        prev_min = prev_max = global_max = nums[0]
        for num in nums[1:]:
            current_min = min(num, prev_max * num, prev_min * num)
            current_max = max(num, prev_max * num, prev_min * num)

            prev_min, prev_max = current_min, current_max
            global_max = max(global_max, current_max)
        return global_max