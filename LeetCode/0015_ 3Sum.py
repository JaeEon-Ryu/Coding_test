# solution 참고

class Solution:
    # solution 참고

    def threeSum(self, nums: List[int]) -> List[List[int]]:

        result = []
        nums.sort()

        for i, n in enumerate(nums):
            # 맨 끝 인덱스에 대해서는 진행x
            if i > 0 and n == nums[i - 1]:
                continue

            # 이진탐색
            l, r = i + 1, len(nums) - 1
            while l < r:
                sum_3 = n + nums[l] + nums[r]
                if sum_3 > 0:
                    r -= 1
                elif sum_3 < 0:
                    l += 1
                else:
                    result.append([n, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:  # 같은 숫자 중복 방지
                        l += 1

        return result

'''
# 시간초과가 났던 코드
from itertools import combinations

def threeSum(self, nums: List[int]) -> List[List[int]]:

    if len(nums) < 3:
        return []

    three_nums = list(combinations(nums,3))
    cleaned_set = set()

    # sorting list and removing duplicate values
    for num_list in three_nums:
        if sum(num_list) == 0:
            num_list = tuple(sorted(list(num_list)))
            cleaned_set.add(num_list)

    result = []
    # tuple to list
    for num_list in cleaned_set:
        result.append(list(num_list))

    return result
'''


