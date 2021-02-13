class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        nums_merged = nums1 + nums2
        nums_merged.sort()

        nums_len = len(nums_merged)
        if nums_len % 2 == 1:
            return nums_merged[nums_len // 2]
        else:
            return (nums_merged[nums_len // 2 - 1] + nums_merged[nums_len // 2]) / 2
