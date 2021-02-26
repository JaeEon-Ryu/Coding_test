class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        if not nums or target < nums[0] or target > nums[-1]:
            return [-1, -1]

        # solution - binary search
        l, r = 0, len(nums)
        target_idx = -1

        while l <= r:
            mid = (l + r) // 2
            if nums[mid] > target:
                r = mid - 1
            elif nums[mid] < target:
                l = mid + 1
            else:
                target_idx = mid
                break

        result = []
        # nums의 원소중에 target과 맞는 원소를 찾았다면
        # 좌, 우로 인덱스를 늘려가면서 target과 맞는 원소가 또 있는지 검색
        if target_idx > -1:
            l, r = target_idx, target_idx
            result = [l, r]
            while l >= 0 or r < len(nums):

                if l >= 0 and nums[l] == target:
                    result[0] = l
                    l -= 1
                else:
                    l = -1

                if r < len(nums) and nums[r] == target:
                    result[1] = r
                    r += 1
                else:
                    r = len(nums)
            return result
        else:
            return [-1, -1]



'''
위처럼 이진탐색을 이용하여 문제를 풀었지만 코드를 너무 난잡하게 쓴 것 같아서
다 풀고 leetcode solution에서는 어떻게 해결하였는지 보았다

class Solution:
    # returns leftmost (or rightmost) index at which `target` should be inserted in sorted
    # array `nums` via binary search.
    def extreme_insertion_index(self, nums, target, left):
        lo = 0
        hi = len(nums)

        # target과 맞는 원소가 나오면 루프를 중단시키지 않고 끝까지 하도록 되어 있음
        # left를 참으로 두느냐 거짓으로 두느냐에 따라서 
        # target값에 해당하는 맨 왼쪽 인덱스 혹은 맨 오른쪽 인덱스를 얻을 수 있다.
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] > target or (left and target == nums[mid]):
                hi = mid
            else:
                lo = mid+1

        return lo


    def searchRange(self, nums, target):
        left_idx = self.extreme_insertion_index(nums, target, True)

        # assert that `left_idx` is within the array bounds and that `target`
        # is actually in `nums`.
        if left_idx == len(nums) or nums[left_idx] != target:
            return [-1, -1]

        return [left_idx, self.extreme_insertion_index(nums, target, False)-1]

'''