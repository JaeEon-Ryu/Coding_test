'''
Given an integer array nums that may contain duplicates, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.
'''


class Solution:
    def subsetsWithDup(self, nums: [int]):
        result = [[]]
        subset = []
        nums.sort()

        def generator(start_num):
            if subset not in result:
                result.append(subset.copy())

            if len(subset) == len(nums): # 분기해제
                return

            for i in range(start_num,len(nums)):
                subset.append(nums[i])
                generator(i+1)
                subset.pop()

        generator(0)

        return result
