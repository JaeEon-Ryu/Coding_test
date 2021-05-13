'''
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.
'''

'''
딕셔너리 자료형 사용 - 해쉬 매핑
key값에 nums에 해당하는 num 을 담고, value에는 그에대한 count값을 담는다
'''

class Solution:
    from collections import defaultdict
    def majorityElement(self, nums: List[int]) -> int:
        nums_dict = defaultdict(int)
        for num in nums:
            nums_dict[num] += 1

        return sorted(nums_dict.items(), key=lambda x: x[1])[-1][0] # value값 (즉, count)으로 정렬 후 제일 많이 나온 key값 반환