'''
Given a list of non-negative integers nums, arrange them such that they form the largest number.

Note: The result may be very large, so you need to return a string instead of an integer.
'''

'''
버블정렬 + 비교 함수 활용
'''

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if self.right_is_bigger(nums[i], nums[j]):
                    nums[i], nums[j] = nums[j], nums[i]
        return str(int(''.join(list(map(str, nums)))))

    def right_is_bigger(self, n1: int, n2: int):
        n1, n2 = str(n1), str(n2)

        if n1 + n2 < n2 + n1:
            return True
        else:
            return False

'''
다른 사람이 쓴 코드 - 101leetcode

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        ## RC ##
        ## APPROACH : CUSTOM SORTING WITH COMPARATOR ##
        ## MAIN IDEA : It's all about comparison . We define a func that compares two strings a ,b. we consider a bigger than b if a+b > b+a . then we sort the numbers and concatenate them .
        ## a-> 3, b-> 30 => 330 > 303
        ## Things to note : Your comparator is supposed to return negative/zero/positive, not a boolean. ##
        
        ## ALSO : We can use any type of sort, while sorting instead of comparing two numbers directly, we can use the current comparator logic to compare and swap elements accordingly.
        
        ## Edge case : o/p -> "00" expected:"0"
        
		## TIME COMPLEXITY : O(NlogN) ##
		## SPACE COMPLEXITY : O(N) ##

        import functools
        def comparator(s1, s2):
            if int(s1+s2) < int(s2+s1):
                return -1
            if int(s1+s2) > int(s2+s1):
                return 1
            return 0
        
        nums = [str(num) for num in nums]
        nums = sorted(nums, key = functools.cmp_to_key(comparator),  reverse = True)
        ans = '0' if nums[0] == '0' else ''.join(nums)      # if the biggest number after sorting is 0 in first position, then rest all will also be 0's so return 0
        return ans
        
'''

'''
주목할점
1. 처음부터 모든 숫자를 문자로 치환함
2. sorted() 내장 함수에서 key값을 functools.cmp_to_key(comparator)로 씀 ( functools 이라는 함수와 cmp_to_key, 그리고 인자값을 따로 함수로 만들어주어야 함 )
3. 인자값인 comparaotr를 직접 만듦
'''