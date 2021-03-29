'''
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

The number of elements initialized in nums1 and nums2 are m and n respectively.
You may assume that nums1 has a size equal to m + n such that it has enough space to hold additional elements from nums2.
'''

import collections

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        m, n, idx = m - 1, n - 1, len(nums1) - 1

        while n >= 0:
            if m >= 0 and nums1[m] > nums2[n]:
                nums1[idx] = nums1[m]
                m -= 1
            else:
                nums1[idx] = nums2[n]
                n -= 1

            idx -= 1
