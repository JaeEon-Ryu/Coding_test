'''
Given an array nums of distinct integers, return all the possible permutations.
You can return the answer in any order.
'''

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        result_nums = []
        idx_list = []

        def shuffle():
            if len(nums) == len(idx_list):
                if len(nums) == len(set(idx_list)): # 중복 제거
                    result_nums.append([nums[idx] for idx in idx_list])
                return

            for idx in range(len(nums)):
                idx_list.append(idx)
                shuffle()
                idx_list.pop()

        shuffle()

        return result_nums