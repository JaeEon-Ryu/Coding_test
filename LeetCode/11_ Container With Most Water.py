class Solution:
    def maxArea(self, height: List[int]) -> int:

        max_val = 0
        l, r = 0, len(height) - 1

        while l < r:
            max_val = max(max_val, min(height[l], height[r]) * (r - l))
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return max_val

        '''former solution
        max_val = 0

        for i in range(len(height)):
         for j in range(i+1,len(height)):
             max_val = max(max_val,min(height[i],height[j]) * (j-i))

        return max_val
        '''