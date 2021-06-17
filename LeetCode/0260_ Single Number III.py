'''
Given an integer array nums, in which exactly two elements appear only once and all the other elements appear exactly twice.
Find the two elements that appear only once. You can return the answer in any order.

You must write an algorithm that runs in linear runtime complexity and uses only constant extra space.
'''


class Solution:
    from collections import defaultdict
    def singleNumber(self, nums: List[int]) -> List[int]:
        num_dict = defaultdict(int)
        result = []

        for num in nums: # 숫자가 나타나는 빈도 세기
            num_dict[num] += 1

        for num in num_dict: # unique한 숫자만 뽑기
            if num_dict[num] == 1:
                result.append(num)

        return result
