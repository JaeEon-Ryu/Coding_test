'''
You are given a sorted unique integer array nums.

Return the smallest sorted list of ranges that cover all the numbers in the array exactly.
That is, each element of nums is covered by exactly one of the ranges, and there is no integer x such that x is in one of the ranges but not in nums.

Each range [a,b] in the list should be output as:

"a->b" if a != b
"a" if a == b
'''

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:

        nums.append(float('inf'))
        result = []
        num_range = []  # 숫자 범위를 다루기 위함 ( 시작값, 종료값)

        for num in nums:
            if num_range:
                if num_range[-1] == num - 1:
                    num_range.append(num)
                else:  # 연속적인 숫자가 아닌 경우
                    if len(num_range) > 1:  # 범위가 있음
                        result.append(str(num_range[0]) + '->' + str(num_range[-1]))
                    else:  # 범위가 없음
                        result.append(str(num_range[-1]))
                    num_range = [num]
            else:
                num_range.append(num)

        return result