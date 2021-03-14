'''
Given an array of non-negative integers nums,
you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.
'''


class Solution:
    def canJump(self, nums: List[int]) -> bool:

        arrival = len(nums) - 1

        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= arrival:
                arrival = i

        return arrival == 0

        '''
        시간초과가 났던 코드
            if len(nums) == 1:
                return True
        
            arrival = len(nums)-1
            global result
            result = False
        
            def jump(idx):
                global result
                if result: return
        
                for i in range(1,nums[idx]+1):
                    if idx + i >= arrival:
                        result = True
                        return
                    else:
                        jump(idx+i)
        
            jump(0)
        
            return result
        '''
 