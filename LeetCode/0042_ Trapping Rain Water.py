class Solution:
    def trap(self, height: List[int]) -> int:

        if not height or len(height) < 3:
            return 0

        result = 0
        l, r = 0, len(height) - 1
        l_max, r_max = height[l], height[r]

        while l < r:
            l_max, r_max = max(height[l], l_max), max(height[r], r_max)
            if l_max <= r_max:
                result += l_max - height[l]
                l += 1
            else:
                result += r_max - height[r]
                r -= 1

        return result
