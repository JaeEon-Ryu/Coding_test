'''
Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.
'''

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxheap, result = [], None

        for num in nums:
            heapq.heappush(maxheap, -num)

        for _ in range(k):
            result = -heapq.heappop(maxheap)

        return result
