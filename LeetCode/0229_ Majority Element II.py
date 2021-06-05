'''
Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

Follow-up: Could you solve the problem in linear time and in O(1) space?
'''

class Solution:
    import collections
    def majorityElement(self, nums: List[int]) -> List[int]:
        n_counter = Counter()
        result = []

        for n in nums:
            n_counter[n] += 1
            if len(n_counter) == 3:
                n_counter -= Counter(set(n_counter))

        for n in n_counter:
            if nums.count(n) > len(nums) / 3:
                result.append(n)

        return result