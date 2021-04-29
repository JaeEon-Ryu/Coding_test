'''
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

Follow up: Could you implement a solution with a linear runtime complexity and without using extra memory?
'''


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        output = 0
        for num in nums:
            output ^= num  # xor 연산 ( 같은 비트가 있으면 빼고 없으면 더하는 것을 이용 )
            print(output)

        return output

