'''
Given an array of non-negative integers nums, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

You can assume that you can always reach the last index.
'''

class Solution:
    def jump(self, nums: List[int]) -> int:

        # reference : JustForWanShua

        result, edge, maxEdge = 0, 0, 0

        for i in range(len(nums)):
            if i > edge:  # 점프 개수가 증가되는 조건  ( 최대 범위보다 현재 인덱스 i가 더 높다면 )
                edge = maxEdge  # 다음 인덱스 위치 결정
                result += 1  # 최대 거리 점프로 인해 점프 개수 증가

            maxEdge = max(maxEdge, i + nums[i])  # 임시 인덱스 위치 갱신

        return result


'''
# 시간제한 초과가 걸린 코드 ( 재귀 )

class Solution:
    def jump(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return 0

        global min_count, is_crossed
        min_count = len(nums)
        is_crossed = False

        def cross(idx, cnt):
            global min_count, is_crossed

            for i in range(idx + 1, idx + nums[idx] + 1):

                if i >= len(nums) - 1:
                    min_count = min(min_count, cnt)
                    is_crossed = True
                    break
                else:
                    cross(i, cnt + 1)

        cross(0, 1)
        return min_count if is_crossed else 0

'''