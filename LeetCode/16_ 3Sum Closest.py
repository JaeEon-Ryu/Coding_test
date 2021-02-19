class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:

        result = sum(nums[:3])
        nums.sort()

        for i, n in enumerate(nums):
            # 맨 끝 인덱스에 대해서는 진행x
            if i > 0 and n == nums[i - 1]:
                continue

            # 이진탐색
            l, r = i + 1, len(nums) - 1
            while l < r:
                sum_3 = n + nums[l] + nums[r]

                if abs(target - sum_3) < abs(target - result):
                    result = sum_3

                if sum_3 > target:
                    r -= 1
                elif sum_3 <= target:
                    l += 1

        return result