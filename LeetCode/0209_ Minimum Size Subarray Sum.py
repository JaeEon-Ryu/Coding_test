'''
Given an array of positive integers nums and a positive integer target,
return the minimal length of a contiguous subarray [numsl, numsl+1, ..., numsr-1, numsr] of which the sum is greater than or equal to target.

If there is no such subarray, return 0 instead.
'''

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        # reference : OldCoadingFarmer
        # O(n)
        left = sum = 0
        result = len(nums) + 1

        for i in range(len(nums)):
            sum += nums[i]
            while sum >= target:
                result = min(result, i - left + 1)
                sum -= nums[left]
                left += 1

        return result if result <= len(nums) else 0

        ''' 시간초과 (O(n*n))
        import sys
        min_value = sys.maxsize

        for i in range(len(nums)):
            for j in range(1,len(nums)+1):
                if j-i < min_value and target <= sum(nums[i:j]):
                    min_value = j-i

        return min_value if min_value != sys.maxsize else 0
        '''
