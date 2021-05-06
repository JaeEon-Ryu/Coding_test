'''
Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane, return the maximum number of points that lie on the same straight line.
'''

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        '''
        reference : y5yeyey
        '''
        res = 0
        for i in range(len(points) - 1):
            current = 0
            lines = {}
            # y = a x + b
            for j in range(i + 1, len(points)):
                dx = points[i][0] - points[j][0]  # distance between x1 and x2
                dy = points[i][1] - points[j][1]  # distance between y1 and y2

                if dx == 0:
                    key = None
                else:
                    key = 10.0 * dy / dx
                lines[key] = lines.get(key, 0) + 1
                current = max(current, lines[key])

            res = max(res, current)

        return res + 1