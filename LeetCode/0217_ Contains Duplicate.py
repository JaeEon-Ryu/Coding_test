'''
Given an integer array nums,
return true if any value appears at least twice in the array, and return false if every element is distinct.
'''

'''
dict 자료형을 사용함으로써 중복을 발견 가능
'''
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        num_dict = dict()

        for num in nums:
            if num_dict.get(num) is not None:
                return True
            else:
                num_dict[num] = True

        return False