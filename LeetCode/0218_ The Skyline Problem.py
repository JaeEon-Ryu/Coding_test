'''
A city's skyline is the outer contour of the silhouette formed by all the buildings in that city when viewed from a distance.
Given the locations and heights of all the buildings, return the skyline formed by these buildings collectively.

The geometric information of each building is given in the array buildings where buildings[i] = [lefti, righti, heighti]:

lefti is the x coordinate of the left edge of the ith building.
righti is the x coordinate of the right edge of the ith building.
heighti is the height of the ith building.
You may assume all buildings are perfect rectangles grounded on an absolutely flat surface at height 0.

The skyline should be represented as a list of "key points" sorted by their x-coordinate in the form [[x1,y1],[x2,y2],...].
Each key point is the left endpoint of some horizontal segment in the skyline except the last point in the list, which always has a y-coordinate 0 and is used to mark the skyline's termination where the rightmost building ends.
Any ground between the leftmost and rightmost buildings should be part of the skyline's contour.

Note: There must be no consecutive horizontal lines of equal height in the output skyline.
For instance, [...,[2 3],[4 5],[7 5],[11 5],[12 7],...] is not acceptable; the three lines of height 5 should be merged into one in the final output as such: [...,[2 3],[4 5],[12 7],...]
'''

class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        # reference : oscartsai

        def addsky(pos, hei):
            if sky[-1][1] != hei:
                sky.append([pos, hei])

        sky = [[-1,0]]

        # 모서리 부분이 될 수 있는 모든 부분
        position = set([b[0] for b in buildings] + [b[1] for b in buildings])
        live = []
        i = 0

        for t in sorted(position):

            # 위치 t보다 더 왼쪽에 있는 곳에 building add
            while i < len(buildings) and buildings[i][0] <= t:
                heappush(live, (-buildings[i][2], buildings[i][1]))
                i += 1

            # t보다 왼쪽에있는 오른쪽면을 제거
            while live and live[0][1] <= t:
                heappop(live)

            # 현재 라인에서 가장 높은 지점 고르기
            h = -live[0][0] if live else 0
            addsky(t, h)

        return sky[1:]