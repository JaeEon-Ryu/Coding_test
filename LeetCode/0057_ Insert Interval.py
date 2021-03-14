'''
Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their start times.
'''


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        intervals.sort()
        modified_intervals, result, is_not_used = [], [], True
        s, e = newInterval[0], newInterval[1]  # start,end

        # 1차 가공 ( newInterval 삽입 후 변경 )
        for interval in intervals:
            if interval[0] <= s and e <= interval[1]:
                is_not_used = False

            if s <= interval[0] <= e or s <= interval[1] <= e:
                is_not_used = False
                modified_intervals.append([min(s, interval[0]), max(e, interval[1])])
            else:
                modified_intervals.append(interval)

        if is_not_used:  # newInterval이 쓰이지 않았다면
            modified_intervals.append(newInterval)
            modified_intervals.sort()

        # 2차 가공 ( newInterval이 삽입된 환경에서 겹치는 부분 병합 )
        for interval in modified_intervals:
            if not result:
                result.append(interval)
            else:
                if interval[0] <= result[-1][1] <= interval[1]:
                    result[-1][1] = interval[1]
                else:
                    result.append(interval)

        return result


'''
다른 사람의 풀이 ( reference : StefanPochmann )
깊은 list comprehension 을 통한 풀이

리스트를 합칠 떄 복합연산자 ( ex : += )를 이용했다는 점 생각

class Solution:
def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
    s, e = newInterval[0], newInterval[1]
    left, right = [], []
    for i in intervals:
        if i[1] < s:
            left += i,
        elif i[0] > e:
            right += i,
        else:
            s = min(s, i[0])
            e = max(e, i[1])
    return left + [[s, e]] + right
'''
