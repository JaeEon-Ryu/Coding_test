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


'''
Time complexity : O(nlogn) 추가 
reference : leetcode
내가 쓴 is_overlap 으로 값을 하나하나 비교하지 않고
정렬된 리스트를 참고하여 intervals의 end값만 비교

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort(key=lambda x: x[0])

        merged = []
        for interval in intervals:
            # if the list of merged intervals is empty or if the current
            # interval does not overlap with the previous, simply append it.
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
            # otherwise, there is overlap, so we merge the current and previous
            # intervals.
                merged[-1][1] = max(merged[-1][1], interval[1])

        return merged
'''