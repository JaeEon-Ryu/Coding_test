'''
Given an integer array nums and two integers k and t,
return true if there are two distinct indices i and j in the array such that abs(nums[i] - nums[j]) <= t and abs(i - j) <= k.
'''

class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        # reference : MichalBrzozowski91

        # O(N) solution
        if k <= 0 or t < 0:
            return False

        from collections import deque
        bucket_cache = deque([], k)
        bucket_dict = dict()

        for i in range(len(nums)):
            # 버킷 nums[i]의 버킷 인덱스 계산
            remainder = nums[i] % (t + 1)
            bucket = (nums[i] - remainder) / (t + 1)

            # 겹치는 것 캐시 계산
            if bucket in bucket_dict:  # 같은 버킷에서 두개의 값
                return True
            if bucket - 1 in bucket_dict and abs(nums[i] - bucket_dict[bucket - 1]) <= t:  # 인접한 버킷과 가까운 값에서 두개의 값
                return True
            if bucket + 1 in bucket_dict and abs(nums[i] - bucket_dict[bucket + 1]) <= t:  # 인접한 버킷과 가까운 값에서 두개의 값
                return True

                # 캐시에 새 버킷 추가
            if i >= k:  # 최대 캐시 크기 = k
                bucket_to_remove = bucket_cache.popleft()
                del bucket_dict[bucket_to_remove]
            bucket_cache.append(bucket)
            bucket_dict[bucket] = nums[i]

        return False

        '''시간초과
        num_dict = dict()
        for i, num in enumerate(nums):
            if len(num_dict) > 2*t:
                for j in range(num-t,num+t+1):
                    if j in num_dict and i-num_dict[j] <= k:
                        return True
            else:
                for j in num_dict:
                    if t >= abs(num-j) and i-num_dict[j] <= k:
                        return True
            num_dict[num] = i
        return False
        '''

