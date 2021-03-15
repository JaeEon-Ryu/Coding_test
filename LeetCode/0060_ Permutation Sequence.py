'''
The set [1, 2, 3, ..., n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order, we get the following sequence for n = 3:

"123"
"132"
"213"
"231"
"312"
"321"
Given n and k, return the kth permutation sequence.
'''


class Solution:
    def getPermutation(self, n: int, k: int) -> str:

        # 리스트에서 필요한 부분의 숫자를 빼서 다시 넣는 방식으로 linear한 풀이법
        # reference : darkTianTian

        import math

        result = ''
        nums = list(map(str, range(1, n + 1)))
        fact = math.factorial(n - 1)
        k -= 1

        while k:
            i, k = divmod(k, fact)  # 몫, 나머지
            result += nums.pop(i)
            fact //= len(nums)

        result += ''.join(nums)
        return result

        '''
            시간초과
            global cnt,result
            nums,cnt,result = [],1,False


            def permutation():
                global cnt,result

                if result:
                    return

                if n == len(nums):
                    if n == len(set(nums)):
                        if cnt == k:
                            result = ''.join([str(_) for _ in nums])
                        cnt += 1
                        return
                    return

                for num in range(1,n+1):
                    nums.append(num)
                    permutation()
                    nums.pop()

            permutation()
            return result
            '''

