'''
Given a collection of numbers, nums, that might contain duplicates,
return all possible unique permutations in any order.
'''

from collections import Counter
# Counter : dict자료형으로 리스트 안에 담겨있는 각 숫자의 개수를 세어줌

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:

        # reference : edtsoi430
        result = []

        def shuffle(counter, path):
            if len(path) == len(nums):
                result.append(path)
                return

            for num in counter:
                if counter[num]:
                    counter[num] -= 1
                    shuffle(counter, path + [num])
                    counter[num] += 1

        shuffle(Counter(nums), [])

        return result

        '''
        시간초과가 났던 코드
        result_nums = []
        idx_list = []

        def shuffle():
            if len(nums) == len(idx_list):
                if len(nums) == len(set(idx_list)):  # 중복 제거
                    p = [nums[idx] for idx in idx_list] # possible_permutation
                    if p not in result_nums:
                        result_nums.append(p)
                return

            for idx in range(len(nums)):
                idx_list.append(idx)
                shuffle()
                idx_list.pop()

        shuffle()

        return result_nums
        '''

print(permute())