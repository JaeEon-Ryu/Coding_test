class Solution:
    from collections import deque
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        temp = deque()
        result = []
        for idx, num in enumerate(nums):
            while temp and nums[temp[-1]] <= num:  # 비교 후 값이 작은 건 바로 삭제
                temp.pop()

            temp.append(idx)

            if temp[0] == idx - k:  # window에서 벗어나게 된 값 -> 지우기
                temp.popleft()

            if idx + 2 > k:  # window에서 벗어나게 될 값 , 아직 남아있다면 추가
                result.append(nums[temp[0]])

        return result

        '''
        # Time Limit Exceeded
        result = []
        len_nums = len(nums)
        if len_nums == 1:
            return nums
        else:
            temp = deque()
            for i in range(k):
                temp.appendleft(nums[i])
            result.append(max(temp))

            for i in range(k,len_nums):
                temp.pop()
                temp.appendleft(nums[i])
                result.append(max(temp))

        return result
        '''