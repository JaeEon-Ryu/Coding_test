'''
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals,
and return an array of the non-overlapping intervals that cover all the intervals in the input.
'''

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort()

        def is_overlap(l1, l2):
            for num in range(l1[0], l1[1] + 1):
                if l2[0] <= num <= l2[1]:
                    return True
            return False

        i = 0
        while intervals and i < len(intervals) - 1:
            if is_overlap(intervals[i], intervals[i + 1]): # 겹친다면 병합
                intervals[i] = [min(intervals[i][0], intervals[i + 1][0]),
                                max(intervals[i][1], intervals[i + 1][1])]
                del intervals[i + 1]
            else: # 겹치지 않는다면 다음 인덱스로 이동
                i += 1

        return intervals