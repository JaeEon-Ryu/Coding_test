class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        def dfs(remain, stack):
            if remain == 0 and sorted(stack) not in result:
                result.append(sorted(stack))
                return

            for item in candidates:
                if item > remain:  # candidates의 합이 target보다 큰 경우
                    break
                dfs(remain - item, stack + [item])

        result = []
        candidates = sorted(candidates)
        dfs(target, [])

        return result


'''시간초과
    def find_combination():

        sum_p = sum(combination)
        if sum_p >= target:
            if sum_p == target and sorted(combination) not in result:
                result.append(sorted(combination))
            return

        for i in range(len(candidates_2)):
            combination.append(candidates_2[i])
            find_combination()
            combination.pop()

    result = []
    candidates_2 = []
    for candidate in candidates:
        for _ in range(target // candidate):
            candidates_2.append(candidate)

    combination = []
    find_combination()

    return result

'''