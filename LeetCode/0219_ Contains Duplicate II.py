'''
Given an integer array nums and an integer k,
return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.
'''


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if len(nums) == 1 or len(nums) == len(set(nums)):
            return False

        num_dict = dict()
        for i, num in enumerate(nums):
            if num in num_dict:
                if abs(i - num_dict[num]) <= k:
                    return True
                else:
                    num_dict[num] = i  # 최신 인덱스로 갱신
            else:
                num_dict[num] = i

        return False