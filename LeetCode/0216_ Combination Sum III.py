'''
Find all valid combinations of k numbers that sum up to n such that the following conditions are true:

Only numbers 1 through 9 are used.
Each number is used at most once.
Return a list of all possible valid combinations.
The list must not contain the same combination twice, and the combinations may be returned in any order.
'''

class Solution:

    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        self.result = []
        self.k, self.n = k, n
        self.dfs([])
        return self.result

    def dfs(self, candidate: List[int]):
        if candidate:
            if sum(candidate) > self.n:
                return
            if sum(candidate) == self.n and self.k == len(candidate):
                self.result.append(candidate)
                return

        '''
        1부터 시작해서 k개에 해당하는 숫자들을 뽑아낸다
        숫자는 1부터 시작하며 다음 숫자는 이전의 숫자보다 1 이상 커야한다
        '''
        if not candidate:
            start_num = 1
        else:
            start_num = candidate[-1] + 1

        for num in range(start_num, 10):
            self.dfs(candidate + [num])


