class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:

        result = 1
        nums.sort()

        for num in nums:
            if num < 1:
                continue

            if num == result:
                result += 1
            elif num < result:
                continue
            else:
                break

        return result

'''
정렬을 하지 않고 문제를 풀어본다면?
reference - asones

def firstMissingPositive(self, nums):
    """
    :type nums: List[int]
    :rtype: int
     Basic idea:
    1. for any array whose length is l, the first missing positive must be in range [1,...,l+1], 
        so we only have to care about those elements in this range and remove the rest.
    2. we can use the array index as the hash to restore the frequency of each number within 
         the range [1,...,l+1] 
    """
    nums.append(0)
    n = len(nums)
    for i in range(len(nums)): # 불필요한 요소 제거
        if nums[i]<0 or nums[i]>=n:
            nums[i]=0
    for i in range(len(nums)): # 인덱스를 해시로 사용하여 각 숫자의 빈도를 기록
        nums[nums[i]%n]+=n
    for i in range(1,len(nums)):
        if nums[i]/n==0:
            return i
    return n
'''